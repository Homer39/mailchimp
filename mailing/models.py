import datetime
from django.conf import settings

from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )

    start_time = models.DateTimeField(verbose_name='Время старта', **NULLABLE,
                                      default=datetime.datetime.now(datetime.timezone.utc))
    end_time = models.DateTimeField(verbose_name='Время окончания', **NULLABLE,
                                    default=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7))
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='Период')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='Статус')

    message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'{self.start_time} / {self.period}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        # Отключение рассылок
        permissions = [
            ('set_status',
             'Can change status')
        ]


class MailingMessage(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'Тема: {self.letter_subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    try_status = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='Статус попытки')
    mailing_service_response = models.TextField(verbose_name='Ответ почтового сервера, если он был', **NULLABLE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')

    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='Рассылка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'{self.last_attempt} - {self.try_status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class MailingClient(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='клиент')
    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='рассылка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'{self.client} - {self.mailing}'

    class Meta:
        verbose_name = 'Список рассылки'
        verbose_name_plural = 'Списки рассылок'
