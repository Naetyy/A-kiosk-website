from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(max_length=1000)
    category = models.CharField(default="Uncategorized", max_length=50)
    image = models.ImageField(upload_to="for_all_app/static/img", null=True)
    
    def __str__(self):
        return self.title

class Temp(models.Model):
    title = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    current_total = models.IntegerField()
    order_num = models.IntegerField(null=True)
