from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    picture = models.ImageField()

    def __str__(self):
        return self.name


class Design(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.IntegerField(unique=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.order_number)


class ProductOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    design = models.ForeignKey('Design', on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Customer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

