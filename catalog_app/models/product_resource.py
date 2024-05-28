from django.db import models

class ProductResource(models.Model):
    """
    Model representing a product resource.
    
    Attributes:
        image (ImageField): The image associated with the product.
    """
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    