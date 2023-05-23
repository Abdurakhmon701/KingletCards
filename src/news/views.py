from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReviewSerializers, UpdatesSerializers, ContactsSerializers, CategorySerializers, \
    CartSerializers, ColorSerializers
from .models import ReviewModel, CategoryModel, CartModel, ColorModel


class ReviewsAPI(APIView):
    serializer_class = ReviewSerializers
    queryset = ReviewModel.objects.all()

    def get(self, request):
        review_data = ReviewSerializers(self.queryset.all(), many=True)
        return Response(review_data.data)


class UpdatesAPI(APIView):
    def post(self, request, format=None):
        serializer = UpdatesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactsAPI(APIView):
    def post(self, request, format=None):
        serializer = ContactsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPI(APIView):
    serializer_class = CategorySerializers
    queryset = CategoryModel.objects.all()

    def get(self, request):
        review_data = CategorySerializers(self.queryset.all(), many=True)
        return Response(review_data.data)


# Dorabotka qilish kere ikkita birxil get bop qoldi
class CartAPI(APIView):
    serializer_class = CartSerializers
    queryset = CartModel.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)


class CartGetBorderAPI(APIView):
    def get(self, request, pk):
        border = get_object_or_404(CartModel, id=pk)
        serializer = CartSerializers(border)
        return Response(serializer.data)


class ColorAPI(APIView):
    def get(self, request, pk):
        color = get_object_or_404(ColorModel, id=pk)
        serializer = ColorSerializers(color)
        return Response(serializer.data)
