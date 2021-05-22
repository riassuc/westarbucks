from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=CASCADE)

    class Meta:
        db_table = 'products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 4, decimal_places = 1)
    sodium_mg = models.DecimalField(max_digits = 4, decimal_places = 1)
    saturated_fat_g = models.DecimalField(max_digits = 4, decimal_places = 1)
    sugars_g = models.DecimalField(max_digits = 4, decimal_places = 1)
    protein_g = models.DecimalField(max_digits = 4, decimal_places = 1)
    caffeine_mg = models.DecimalField(max_digits = 4, decimal_places = 1)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class AllergyProduct(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=CASCADE)
    product = models.ForeignKey('Product', on_delete=CASCADE)

    class Meta:
        db_table = 'allergy_products'




