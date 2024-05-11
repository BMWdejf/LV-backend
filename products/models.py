from django.db import models

class Products(models.Model):
    code = models.CharField(max_length=150)
    name = models.CharField(max_length=255)
    img_link = models.CharField(max_length=255)
    exportNaEshop = models.BooleanField(default=False)

    def __str__(self):
        return self.name