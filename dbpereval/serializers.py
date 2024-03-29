from .models import *
from rest_framework import serializers

from datetime import datetime


class PerevalSerializer(serializers.Serializer):
    """
    Класс-сериализатор. Преобразует принятый JSON в модель dbPereval.
    Для каждого параметра JSON предусмотрено отдельное поле. Параметры, не входящие в данный список - игнорируются
    """
    pereval_id = serializers.IntegerField()
    beautyTitle = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField(allow_blank=True)
    add_time = serializers.DateTimeField(allow_null=True, required=False)
    user = serializers.JSONField()
    coords = serializers.JSONField()
    type = serializers.CharField()
    level = serializers.JSONField()
    images = serializers.JSONField()

    def to_representation(self, instance):
        """
        Возврат данных по запрошенному объекту
        :param instance: объект dbPereval
        :return: JSON со следующим содержанием: поле raw_data с добавлением поля images
        """
        raw_data = instance.raw_data
        raw_data['images'] = instance.images
        return raw_data

    def create(self, validated_data):
        """
        Создание объекта dbPereval. Условия создания:
        1) все параметры кроме images записываются в raw_data
        2) если в JSON имеется дата создания запроса, она записывается в поле date_added, в противном случае записывается текущая дата и время
        3) параметр images записывается в поле images
        :param validated_data: JSON, поступающий от клиентского приложения
        :return: объект Pereval
        """
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'user', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        pereval = dbPereval(date_added=validated_data.pop('add_time', datetime.now()), raw_data=raw_data,
                          images=validated_data.pop('images'))
        pereval.save()
        return pereval

    def update(self, instance, validated_data):
        """
        Редактирование объекта dbPereval по следующему правилу:
        в поле raw_data могут обновляться все параметры JSON кроме параметра user (данные о пользователе)
        :param instance: объект dbPereval
        :param validated_data: обновленные данные
        :return: обновленный объект dbPereval
        """
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        # оставляем данные о пользователе неизменными
        raw_data['user'] = instance.raw_data.pop('user', '{}')

        # Обновление путем создания новой записи dbPereval с ключом instance.id, тк возникла проблема обновления raw_data:
        # при вызове instance.raw_data = raw_data
        # вместо нового словаря почему то в бд сохранялся список из словаря и пустого поля
        pereval = dbPereval(id=instance.id, date_added=validated_data.pop('add_time', instance.date_added), raw_data=raw_data,
                          images=validated_data.pop('images'))
        pereval.save()
        return instance
