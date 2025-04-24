from django.shortcuts import render
from .serializers import *
# Create your views here.
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data)
