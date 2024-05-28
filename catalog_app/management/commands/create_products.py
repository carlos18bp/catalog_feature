from faker import Faker
from django.core.management.base import BaseCommand
from catalog_app.models import Product, ProductResource, get_category_choices
import random

class Command(BaseCommand):
    help = 'Create Product records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_products', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_products = options['number_of_products']
        fake = Faker()

        category_choices = [choice[0] for choice in get_category_choices()]

        for _ in range(number_of_products):
            new_product = Product.objects.create(
                title=fake.word(),
                description=fake.text(max_nb_chars=300),
                price=fake.random_int(min=100, max=190),
                category=random.choice(category_choices)
            )

            # Add all available ProductResource images
            new_product.images.add(*ProductResource.objects.all())

            self.stdout.write(self.style.SUCCESS(f'Product "{new_product}" created'))

        self.stdout.write(self.style.SUCCESS(f'"{Product.objects.count()}" Product records created'))
