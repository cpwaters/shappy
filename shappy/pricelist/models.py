from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    def __str__(self):
        template = '{0.code} {0.description} {0.price}'
        return template.format(self)

