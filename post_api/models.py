from django.db import models

# Create your models here.
# class Category(models.Model):
#     CATEGORY_OPTIONS = [
#     ('Phones', 'Phones'),
#     ('Laptops', 'Laptops'),
#     ('Consoles', 'Consoles'),
#     ('iPads', 'iPads'),
#     ('Accessories', 'Accessories'),
# ]
#     name =  models.CharField(max_length= 100, choices= CATEGORY_OPTIONS)

#     def __str__(self):
#         return self.name

class Specification(models.Model):
    CONDITION_OPTIONS = [
        ('New', 'New'),
        ('Used', 'Used'),
        ('Pre-owned', 'Pre-owned'),
    ]

    brand = models.CharField(max_length=50)
    model_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True, null=True)
    internal_storage = models.IntegerField(blank=True, null=True)
    RAM = models.IntegerField(blank=True, null=True)
    card_slot = models.CharField(max_length=50, blank=True, null=True)
    eSim = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=20, choices=CONDITION_OPTIONS)
    swap_allowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model_type}"


class Product(models.Model):
    STATUS_OPTIONS = [
        ('Available', 'Available'),
        ('Out of stock', 'Out of stock'),
    ]

    CATEGORY_OPTIONS = [
    ('Phones', 'Phones'),
    ('Laptops', 'Laptops'),
    ('Consoles', 'Consoles'),
    ('iPads', 'iPads'),
    ('Accessories', 'Accessories'),
]

    title = models.CharField(max_length=100)
    # product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_category = models.CharField(choices=CATEGORY_OPTIONS, )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='Available')
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, related_name='products', null=True, )
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    video = models.FileField(upload_to='products/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def calculate_discount_amount(self):
        if self.price and self.discount_percentage > 0:
            # Calculate the discount amount: price * percentage /100
            self.discount_price = self.price -(self.price * self.discount_percentage / 100)
            return self.discount_price
        return self.price




