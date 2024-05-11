from django.db import models

<<<<<<< HEAD
class Products(models.Model):
    code = models.CharField(max_length=150)
    name = models.CharField(max_length=255)
    img_link = models.CharField(max_length=255)
    export_on_eshop = models.BooleanField(default=False)

    def __str__(self):
        return self.name
=======
# Create your models here.
>>>>>>> 328f7f1 (Install clean Django app "Products")
