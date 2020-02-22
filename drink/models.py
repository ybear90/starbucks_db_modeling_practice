from django.db import models

# Create your models here.

class Drink(models.Model):
    category            = models.ForeignKey('Category', models.SET_NULL, blank=True, null=True)
    datail_category     = models.ForeignKey('DetailCategory', models.SET_NULL, blank=True, null=True)
    name                = models.CharField(max_length=45)
    name_eng            = models.CharField(max_length=45)
    introduction        = models.CharField(max_length=500)
    size                = models.ManyToManyField('Size')
    nutrition           = models.ForeignKey('Nutrition', models.SET_NULL, blank=True, null=True)
    allergic            = models.ManyToManyField('Allergic', through='DrinkAllergic')
    img_link            = models.URLField(max_length=500)
    desc                = models.CharField(max_length=500)

    class Meta:
        db_table = 'drink'

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'

class DetailCategory(models.Model):
    name        = models.CharField(max_length=50)
    category    = models.ForeignKey('Category', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'detail_category'

class Size(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'size'

class Nutrition(models.Model):
    kcal_per_one    = models.DecimalField(max_digits=5, decimal_places=1)
    sodium          = models.DecimalField(max_digits=5, decimal_places=1)
    saturated_fat   = models.DecimalField(max_digits=5, decimal_places=1)
    sugars          = models.DecimalField(max_digits=5, decimal_places=1)
    protein         = models.DecimalField(max_digits=5, decimal_places=1)
    caffein         = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        db_table = 'nutrition'

class DrinkAllergic(models.Model):
    drink    = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)
    allergic = models.ForeignKey('Allergic', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'drink_allergic'


class Allergic(models.Model):
    desc = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergic'
