from django.db import models
from django.db.models import SET_NULL

from src.base.models import BaseModel


class ReviewModel(BaseModel):
    description = models.TextField(db_column='description')
    full_name = models.TextField(db_column='full_name')

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Review"
        db_table = "review"

    def __str__(self):
        return self.full_name


class UpdatesModel(models.Model):
    email = models.TextField(db_column='email')
    first_name = models.TextField(db_column='first_name')
    last_name = models.TextField(db_column='last_name')
    instagram = models.TextField(db_column='instagram')

    class Meta:
        verbose_name = "Updates"
        verbose_name_plural = "Updates"
        db_table = "updates"

    def __str__(self):
        return self.instagram


class ContactsModel(models.Model):
    full_name = models.TextField(db_column='full_name')
    email = models.TextField(db_column='email')
    whatsapp = models.TextField(db_column='whatsapp')
    message = models.TextField(db_column='message')

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"
        db_table = "contacts"

    def __str__(self):
        return self.messages


class CategoryModel(models.Model):
    title = models.CharField(max_length=256, db_column='title')
    image = models.ImageField(upload_to='images/', db_column='image')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        db_table = "category"

    def __str__(self):
        return self.title


class OrderModel(models.Model):
    full_name = models.CharField(max_length=128, db_column='full_name')
    country = models.CharField(max_length=64, db_column='country')
    city = models.CharField(max_length=64, db_column='city')
    address = models.TextField(db_column='address')
    post_code = models.CharField(max_length=256, db_column='post_code')
    email = models.CharField(max_length=64, db_column='email')
    payment_status = models.BooleanField(default=False, db_column="payment_status")
    cart_front = models.ImageField(upload_to='images/', db_column='cart_front')
    cart_back = models.ImageField(upload_to='images/', db_column='cart_back')
    cart_id = models.IntegerField(db_column='cart_id')
    color_id = models.IntegerField(db_column='color_id')
    border_id = models.IntegerField(db_column='border_id')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
        db_table = "order"

    def __str__(self):
        return self.full_name


##new
class BorderModel(models.Model):
    border = models.ImageField(upload_to='images/', db_column='border')
    price = models.IntegerField(db_column='price')

    class Meta:
        verbose_name = "Border"
        verbose_name_plural = "Border"
        db_table = "border"

    def __str__(self):
        return str(self.price)


class CartModel(models.Model):
    image_front = models.ImageField(upload_to='images/')
    image_back = models.ImageField(upload_to='images/')
    borders = models.ManyToManyField(BorderModel, related_name='carts', db_column='borders')

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Cart"
        db_table = "cart"

    def __str__(self):
        return list(self.borders)


class ColorModel(models.Model):
    cart = models.ForeignKey(CartModel, null=True, blank=True, on_delete=SET_NULL, db_column='cart')
    banner = models.ImageField(upload_to='images/', db_column='banner')
    image_front = models.ImageField(upload_to='images/', db_column='image_front')
    image_back = models.ImageField(upload_to='images/', db_column='image_back')
    price = models.IntegerField(db_column='price')

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Color"
        db_table = "color"

    def __str__(self):
        return str(self.price)
