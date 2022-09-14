from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ProfileType(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.category)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], unique=True)
    category = models.ForeignKey(
        ProfileType, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.mobile}' + ' ' + f'{self.category}')
