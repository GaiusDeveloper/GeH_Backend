from rest_framework import serializers
from .models import Product
from cloudinary.utils import cloudinary_url
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# =================== Custom Login Response ===================
class CustomLoginResponseSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    access = serializers.CharField()
    refresh = serializers.CharField()  # fixed typo from "refersh"
    
    def get_user(self, obj):
        request = self.context.get("request")
        user = request.user
        return {
            "id": user.id,
            "username": user.username
        }

# =================== Product List Serializer ===================
class ProductListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image_small = serializers.SerializerMethodField()
    image_large = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", 
            "title",
            "product_category",
            "product_status",
            "price",
            "discount_percentage",
            "discount_price",
            "image_url",
            "image_small",
            "image_large",
            "video_url",
            "brand",
            "model_type",
            "color",
            "condition",
            "internal_storage",
            "ram",
            "card_slot",
            "eSim",
            "swap_allowed",
            "description",
            "created_at"
        ]

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None

    def get_image_small(self, obj):
        if obj.image:
            # Cloudinary transformations via URL params
            return f"{obj.image.url}?w=200&h=200&c=fill&q=auto&f=auto"
        return None

    def get_image_large(self, obj):
        if obj.image:
            return f"{obj.image.url}?w=800&h=800&c=fill&q=auto&f=auto"
        return None

    def get_video_url(self, obj):
        return obj.video.url if obj.video else None

# =================== Product Detail Serializer ===================
class ProductDetailSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image_small = serializers.SerializerMethodField()
    image_large = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_image_small(self, obj):
        if obj.image:
            return f"{obj.image.url}?w=200&h=200&c=fill&q=auto&f=auto"
        return None

    def get_image_large(self, obj):
        if obj.image:
            return f"{obj.image.url}?w=800&h=800&c=fill&q=auto&f=auto"
        return None

    def get_video_url(self, obj):
        return obj.video.url if obj.video else None

# =================== Product Write Serializer ===================
class ProductWriteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # accepts uploaded image
    video = serializers.FileField(required=False)   # accepts uploaded video

    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    discount_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False,
        required=False, allow_null=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        # Auto-calculate discount price if discount_percentage present
        discount_percentage = validated_data.get("discount_percentage")
        price = validated_data.get("price")

        if price and discount_percentage not in (None, "", 0):
            validated_data["discount_price"] = price - (
                price * discount_percentage / 100
            )

        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update fields normally
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Recalculate discount if needed
        price = validated_data.get("price", instance.price)
        discount_percentage = validated_data.get("discount_percentage", instance.discount_percentage)

        if price and discount_percentage not in (None, "", 0):
            instance.discount_price = price - (price * discount_percentage / 100)
        else:
            instance.discount_price = None

        instance.save()
        return instance



# from rest_framework import serializers
# from .models import Product
# from cloudinary.utils import cloudinary_url
# from dj_rest_auth.serializers import LoginSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomLoginResponseSerializer(serializers.Serializer):
#     user = serializers.SerializerMethodField()
#     access = serializers.CharField()
#     refersh = serializers.CharField()
    
#     def get_user(self, obj):
#         request = self.context.get("request")
#         user = request.user
        
#         return{
#             "id": user.id,
#             "username": user.username
#         }

# from rest_framework import serializers
# from .models import Product

# class ProductListSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
#     image_small = serializers.SerializerMethodField()
#     image_large = serializers.SerializerMethodField()
#     video_url = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = [
#             "id", 
#             "title",
#             "product_category",
#             "product_status",
#             "price",
#             "discount_percentage",
#             "discount_price",
#             "image_url",
#             "image_small",
#             "image_large",
#             "video_url",
#             "brand",
#             "model_type",
#             "color",
#             "condition",
#             "internal_storage",
#             "ram",
#             "card_slot",
#             "eSim",
#             "swap_allowed",
#             "description",
#             "created_at"
#         ]

#     def get_image_url(self, obj):
#         return obj.image.url if obj.image else None

#     def get_image_small(self, obj):
#         if obj.image:
#             # Use URL parameters for resizing via Cloudinary
#             return f"{obj.image.url}?w=200&h=200&c=fill&q=auto&f=auto"
#         return None

#     def get_image_large(self, obj):
#         if obj.image:
#             return f"{obj.image.url}?w=800&h=800&c=fill&q=auto&f=auto"
#         return None

#     def get_video_url(self, obj):
#         return obj.video.url if obj.video else None

# class ProductDetailSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_image_url(self, obj):
#         request = self.context.get('request')
#         if obj.image and hasattr(obj.image, 'url'):
#             return request.build_absolute_uri(obj.image.url)
#         return None
    
#     def get_image_small(self, obj):
#         if obj.image:
#             url, _ = cloudinary_url(obj.image.public_id, width=200, height=200, crop='fill', gravity='auto', fetch_format='auto', quality='auto')
#             return url
#         return None

#     def get_image_large(self, obj):
#         if obj.image:
#             url, _ = cloudinary_url(obj.image.public_id, width=800, height=800, crop='fill', gravity='auto', fetch_format='auto', quality='auto')
#             return url
#         return None

# class ProductWriteSerializer(serializers.ModelSerializer):
#     #accept category by id
    
    
#     price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
#     discount_price = serializers.DecimalField(
#         max_digits=10, decimal_places=2, coerce_to_string=False,
#         required=False, allow_null=True
#     )

#     class Meta:
#         model = Product
#         fields = '__all__'
#         read_only_fields = ['id', 'created_at']


#     def create(self, validated_data):
#         # Auto-calculate discount price if discount_percentage present
#         discount_percentage = validated_data.get("discount_percentage")
#         price = validated_data.get("price")

#         if price and discount_percentage not in (None, "", 0):
#             validated_data["discount_price"] = price - (
#                 price * discount_percentage / 100
#             )

#         product = Product.objects.create(**validated_data)
#         return product

#     def update(self, instance, validated_data):
#         # Update fields normally
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)

#         # Recalculate discount if needed
#         if (
#             "discount_percentage" in validated_data
#             or "price" in validated_data
#         ):
#             price = validated_data.get("price", instance.price)
#             discount_percentage = validated_data.get(
#                 "discount_percentage", instance.discount_percentage
#             )

#             if price and discount_percentage not in (None, "", 0):
#                 instance.discount_price = price - (
#                     price * discount_percentage / 100
#                 )
#             else:
#                 instance.discount_price = None

#         instance.save()
#         return instance