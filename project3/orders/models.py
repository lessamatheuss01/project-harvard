from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    SIZE_CHOICES = [("S", "Pequena"), ("L", "Grande")]
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_size_display()}) - R${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sub(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - R${self.price}"

    price = models.DecimalField(max_digits=5, decimal_places=2)

class Dinner(models.Model):
    SIZE_CHOICES = [("S", "Pequena"), ("L", "Grande")]
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_size_display()}) - R${self.price}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Pizza, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("Pendente", "Pendente"), ("Concluído", "Concluído")], default="Pendente")

    def __str__(self):
        return f"Pedido {self.id} - {self.user.username} - {self.status}"

# Create your models here.
