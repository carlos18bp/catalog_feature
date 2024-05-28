from rest_framework import serializers
from catalog_app.models import Product, ProductResource

class ProductResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductResource model.
    
    Serializes the image field to include the URL of the image.
    """
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductResource
        fields = ['image_url']

    def get_image_url(self, obj):
        """
        Retrieves the URL of the image associated with the ProductResource instance.
        
        :param obj: The ProductResource instance.
        :return: The absolute URL of the image.
        """
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    
    Serializes the related ProductResource instances.
    """
    images = ProductResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'images']
