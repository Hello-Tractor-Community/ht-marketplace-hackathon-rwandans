from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view()
def product_list(request):
    products = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

def collection(request, id):
    queryset = Collection.objects.all()
    serializer = CollectionSerializer(queryset)
    return Response(serializer.data)

