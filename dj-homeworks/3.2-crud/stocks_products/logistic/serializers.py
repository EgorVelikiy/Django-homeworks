from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'stocks']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for item in positions:
            StockProduct.objects.create(stock=stock, product=item['product'], quantity=item['quantity'],
                                        price=item['price'])

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for item in positions:
            StockProduct.objects.update_or_create(stock=stock,
                                                  product=item.get('product'),
                                                  defaults={'price': item.get('price'),
                                                            'quantity': item.get('quantity')
                                                            }
                                                  )

        return stock
