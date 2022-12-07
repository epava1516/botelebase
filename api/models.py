from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

rateValues = [MinValueValidator(0), MaxValueValidator(5)]
ageValues = [MinValueValidator(18)]

class genreChoices(models.TextChoices):
    HOMBRE = 'H', _('Hombre')
    MUJER = 'M', _('Mujer')
    TRANS = 'T', _('Trans')

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=150, null=True)
    lastName = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=150)
    galeryPath = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    age = models.IntegerField(validators=ageValues, null=True)
    genre = models.CharField(max_length=30, choices=genreChoices.choices)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    phone_prefix = models.IntegerField(null=True)
    phone = models.IntegerField(unique=True)
    show_phone = models.BooleanField(default=False)
    # email = models.EmailField(unique=True)
    email = models.EmailField(unique=False, null=True)
    show_email = models.BooleanField(default=False)
    dni = models.CharField(max_length=30, null=True, unique=True)
    dniPhoto = models.CharField(max_length=30, null=True, unique=True)
    coordinates = models.JSONField(null=True)
    addressCity = models.CharField(max_length=30)
    addressCountry = models.CharField(max_length=30)
    addressPostalcode = models.CharField(max_length=30, null=True)
    addressState = models.CharField(max_length=30)
    addressMuni = models.CharField(max_length=30)
    addressZone = models.CharField(max_length=1000, null=True)
    addressStreet = models.CharField(max_length=30, null=True)
    services = models.JSONField(null=True)
    isWorker = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class UserComment(models.Model):
    userId = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    rate = models.IntegerField(validators=rateValues)
    description = models.TextField(max_length=30, null=True)
    createdBy = models.OneToOneField(User, related_name='Usuario', on_delete=models.CASCADE, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    coordinates = models.JSONField(null=True)
    addressCity = models.CharField(max_length=30)
    addressCountry = models.CharField(max_length=30)
    addressPostalcode = models.CharField(max_length=30, null=True)
    addressState = models.CharField(max_length=30)
    addressStreet = models.CharField(max_length=30, null=True)
    services = models.JSONField(null=True)
    isDeleted = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class GroupComment(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=rateValues)
    description = models.TextField(max_length=30, null=True)
    createdBy = models.OneToOneField(User, related_name='Grupo', on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class UserGallery(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.JSONField(default=list)
    video = models.JSONField(default=list)
    checksum = models.CharField(max_length=50, unique=True)
    verified = models.BooleanField(default=False)

class GroupGallery(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    photo = models.CharField(max_length=50)
    checksum = models.CharField(max_length=50, unique=True)
    verified = models.BooleanField(default=False)

class UserGroupRelation(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    isAdmin = models.BooleanField(default=False)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
