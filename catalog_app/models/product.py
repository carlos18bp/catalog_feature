from django.db import models
from catalog_app.models import ProductResource

# List of product categories
CATEGORY_LIST = [
    'Bracelets',
    'Necklaces',
    'Earrings',
    'Rings',
    'Watches',
    'Brooches',
    'Anklets',
    'Hair Jewelry',
    'Cufflinks',
    'Pendants',
    'Charms',
    'Body Jewelry',
]

def get_category_choices():
    """
    Returns a list of tuples containing categories for the Product model.
    
    :return: List of tuples (category, category)
    """
    return [(category, category) for category in CATEGORY_LIST]

class Product(models.Model):
    """
    Model representing a product.
    
    Attributes:
        title (str): The title of the product.
        description (str): A detailed description of the product.
        price (int): The price of the product.
        category (str): The category of the product, chosen from a predefined list.
        images (ManyToManyField): A many-to-many relationship to the ProductResource model.
    """
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20, choices=get_category_choices())

    images = models.ManyToManyField(ProductResource)

    def __str__(self):
        return self.title
