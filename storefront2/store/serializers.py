from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection'
    )

    def calculate_tax(self, product:Product):
        return product.unit_price*Decimal(1.1)

    class Meta:
        model = Product
        fields = ['id','title', 'unit_price', 'price_with_tax', 'collection']
