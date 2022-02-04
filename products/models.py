from django.db import models


class Product(models.Model):

    PRODUCT_CHOICES = (
        ('fishes', 'fishes'),
        ('fist tanks', 'fish tanks'),
        ('fish foods', 'fish foods'),
        ('decoratives', 'decoratives'),
        ('heaters', 'heaters'),
        ('filters', 'filters'),
        ('lightings', 'lightings'),
        ('plants', 'plants'),
    )

    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    additional_info = models.CharField(blank=True, max_length=20)   # for product volume, weight, etc
    description = models.TextField()
    product_type = models.CharField(choices=PRODUCT_CHOICES, max_length=100)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return f"{self.name} : {self.product_type}"

    @property
    def inStock(self):
        if self.quantity > 0:
            return "In stock"
        return "Not in stock"
