from django.shortcuts import render
from .serializers import Productdata
from rest_framework.views import APIView
from .models import Product as p
from django.http import  HttpResponse,JsonResponse
from rest_framework import status
from django.db import IntegrityError
# Create your views here.
class Product(APIView):
    # permission_classes = (IsAuthenticated,)

    serializer_class = Productdata
    # <-- And here
    def get(self, request):
          snippets = p.objects.all()
          serializer = Productdata(snippets, many=True)
          content = {'status': '200', 'Message': 'Details fetch  successfully',
                     'data': serializer.data}
          return JsonResponse(content, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        content1 = {'status': '404','Message': 'Something went Wrong'}

        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():

             serializer.save()
             content = {'status': '200', 'Message': 'Product Add  successfully',
                       'data': serializer.data}
             return JsonResponse(content, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return JsonResponse(content1, status=status.HTTP_200_OK)
    #delete product
    def delete(self, request, format=None):

        content1 = {'status': '404', 'Message': 'Something went wrong'}
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id = serializer.data['id']
                content = {'status': '200', 'Message': 'Product  Delete successfully'}
                p.objects.filter(id=id).delete()
                if serializer.is_valid():
                    return JsonResponse(content, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return JsonResponse(content1, status=status.HTTP_200_OK)
    
    def put(self, request, format=None):

        content1 = {'status': '404', 'Message': 'Something went wrong'}
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id = serializer.data['id']
                pname=serializer.data['pname']
                pdesc=serializer.data['pdesc']

                content = {'status': '200', 'Message': 'Product Update successfully',
                               'data': serializer.data}
                p.objects.filter(id=id).update(pname=pname,pdesc=pdesc)
                if serializer.is_valid():
                    return JsonResponse(content, status=status.HTTP_200_OK)
        except IntegrityError as e:
                      return JsonResponse(content1, status=status.HTTP_200_OK)
