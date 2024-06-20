from django.db import models

# Create your models here.
class MobilePhone(models.Model):
    BRAND_CHOICES = [
        ('S', 'Samsung'),
        ('N', 'Nokia'),
        ('A', 'Apple'),
        ('M', 'Microsoft'),
        ('V', 'Vivo'),
        ('O', 'Oppo')
    ]
    SUPPORTIVE_NETWORK_CHOICES = [
        ('5g', '5g/4g/3g/LTE'),
    ]
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=1, choices=BRAND_CHOICES, default=None)
    model_number = models.PositiveIntegerField(default=None)
    supportive_network = models.CharField(max_length=2, choices=SUPPORTIVE_NETWORK_CHOICES, default=None)
    primary_memory = models.CharField(max_length=100)
    secondary_memory = models.CharField(max_length=100)
    description = models.TextField()
    mrp = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    url = models.CharField(max_length=250)
    price = models.IntegerField(default = 0)
    in_stock =models.BooleanField(default=False)
    offers_avaliable = models.BooleanField(default=False)
    offer_description =models.CharField(max_length=350) 
    manufactured_date = models.DateField(default=None)
    image =models.ImageField(upload_to='media/mobilePhone/')

    def save(self, *args, **kwargs):
        self.price = self.mrp - self.discount
        super().save(*args, **kwargs)

class Television(models.Model):
    BRAND_CHOICES = [
        ('Sa', 'Samsung'),
        ('Lg', 'LG'),
        ('So', 'Sony'),
    ]
    SIZE_CHOICES = [
        ('28inch', '28inch'),
        ('32inch', '32inch'),
        ('40inch', '40inch'),
        ('48inch', '48inch'),
        ('64inch', '64inch'),
        ('80inch', '80inch'),
        ('96inch', '96inch')
    ]
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=2, choices=BRAND_CHOICES, default=None)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default=None)
    model_number =models.PositiveIntegerField(default=None)
    manufactured_date = models.DateField(default=None)
    description = models.TextField()
    mrp = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    url = models.CharField(max_length=250)
    offers_avaliable = models.BooleanField(default=False)
    offers_description = models.CharField(max_length=350, default=None)
    in_stock = models.BooleanField(default=False)
    image =models.ImageField(upload_to='media/mobilePhone/')

    def save(self, *args, **kwargs):
        self.price = self.mrp - self.discount
        super().save(*args, **kwargs)


class Refrigrator(models.Model):
    pass

