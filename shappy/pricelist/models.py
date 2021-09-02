from django.db import models

class Product(models.Model):
    store = models.CharField(max_length=50, default='Aldi')
    isle = models.IntegerField(null=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    pack_size = models.IntegerField(default=1)
    price = models.CharField(max_length=200)
    def __str__(self):
        template = '{0.store} {0.isle} {0.code} {0.description} {0.pack_size} {0.price}'
        return template.format(self)

