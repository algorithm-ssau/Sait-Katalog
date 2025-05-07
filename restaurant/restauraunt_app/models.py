from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Для хранения хэша пароля

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.login


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dishes/')  # <--- Важно!

    def __str__(self):
        return self.name

class FavoriteDish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_dishes')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'dish')  # Предотвращает дублирование записей

    def __str__(self):
        return f"{self.user.login} - {self.dish.name}"