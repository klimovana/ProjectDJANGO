from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фамилия")
    email = models.EmailField(unique=True, max_length=255, verbose_name="Email")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    waist_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Обхват талии")
    chest_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Обхват груди")
    torso_length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Длина туловища")
    hip_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Обхват бёдер")
    leg_length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Длина ног")
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Длина рукава")

    def __str__(self):
        return f"Мерки пользователя {self.user.email}"