from django.db import models

class dbPereval(models.Model):
    """
    Модель,  для загрузки данных в таблицу БД dbpereval_added
    Поля:
    date_added - дата добавления записи (берется из полученного JSON, если поле отсутствует или пустое - добавляется текущая дата)
    raw_data - сохраняется JSON без параметра images
    images - сохраняется параметр images
    status - статус записи. Значение берется из перечисления STATUS. По умолчанию принимает значение new
    """

    STATUS = [
        ('new', 'Новый'),
        ('pending', 'В обработке'),
        ('resolved', 'Завершен'),
        ('accepted', 'Принят'),
        ('rejected', 'Отменен'),
    ]

    date_added = models.DateTimeField(blank=True, null=True)
    raw_data = models.JSONField(blank=True)
    images = models.JSONField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='new')

    class Meta:
        db_table = 'pereval_added'
