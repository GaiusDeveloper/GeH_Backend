from rest_framework import serializers

from .models import Specification, Product

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields ='__all__'
        read_only_fields = ['id']

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields =['id', 'name']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # product_category = CategorySerializer(read_only =True)
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    # product_category = CategorySerializer(read_only = True)
    specification = SpecificationSerializer(read_only = True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductWriteSerializer(serializers.ModelSerializer):
    #accept category by id
    # product_category = CategorySerializer(read_only = True)
    specification = SpecificationSerializer(read_only = True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        specs_data = validated_data.pop('specification', [])
        product = Product.objects.create(**validated_data)
        for specs in specs_data:
            Specification.objects.create(product =product, **specs)
        return product

    def update(self, instance, validated_data):
        specs_data = validated_data.pop('specification', None)
        #update product field
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        #If specs pass, replace existing specs with new list
        if specs_data is not None:
            instance.specifications.all().delete()
            for specs in specs_data:
                Specification.objects.create(product=instance, **specs)
        return instance