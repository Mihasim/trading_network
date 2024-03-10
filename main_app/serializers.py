from rest_framework import serializers

from main_app.models import TheLinkOfTheNetwork, Product


class TheLinkOfTheNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheLinkOfTheNetwork
        fields = '__all__'

        # закрыл обновления через API поля «Задолженность перед поставщиком»
        read_only_fields = ('debit_to_the_provider',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
