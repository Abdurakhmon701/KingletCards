from rest_framework import serializers

from .models import ReviewModel, UpdatesModel, ContactsModel, CategoryModel, CartModel, ColorModel, BorderModel


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['description', 'full_name']


class UpdatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UpdatesModel
        fields = ['email', 'first_name', 'last_name', 'instagram']


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = ['full_name', 'email', 'whatsapp', 'message']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title', 'image']


class BorderSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorderModel
        fields = ['id', 'border', 'price']


class CartSerializers(serializers.ModelSerializer):
    borders = BorderSerializers(many=True)
    class Meta:
        model = CartModel
        fields = ['id', 'image_front', 'image_back', 'borders']


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ['id', 'cart', 'banner', 'image_front', 'image_back', 'price']
