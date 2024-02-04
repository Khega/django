from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='product_photos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - Photo {self.id}"
