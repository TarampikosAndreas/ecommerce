from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='static/products', blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    session_id = models.CharField(max_length=250, blank=True)
    date_set = models.DateField(auto_now_add=True)


class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
    email = models.CharField(max_length=120)
    date_set = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

