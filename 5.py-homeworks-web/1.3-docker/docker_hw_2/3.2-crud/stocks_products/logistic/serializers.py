from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройка сериализатора для продукта
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройка сериализатора для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройка сериализатора для склада

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # заполняем связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for same in positions:
            StockProduct.objects.create(stock=stock, **same)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # обнавляем связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for same in positions:
            same_obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=same['product'],
                defaults={'stock': stock, 'product': same['product'], 'quantity': same['quantity'],
                          'price': same['price']
                          }
            )

        return stock
