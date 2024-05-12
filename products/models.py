from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Products(models.Model):
    fx_id = models.IntegerField(unique=True)
    code = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    img_link = models.CharField(max_length=255)
    export_on_eshop = models.BooleanField(default=False)

    def __str__(self):
        return self.name
>>>>>>> origin/products_services
