import uuid

from django.db import models
from django.utils import timezone


class Contact(models.Model):
    ct_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    published_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Provinces(models.Model):
    u_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    story = models.CharField(max_length=500, null=True, blank=True)
    geography = models.CharField(max_length=500, null=True, blank=True)
    culture_and_traditions = models.CharField(max_length=500, null=True, blank=True)
    economy = models.CharField(max_length=500, null=True, blank=True)
    nature = models.CharField(max_length=500, null=True, blank=True)
    population = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Carusel(models.Model):
    cl_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    provinces = models.ForeignKey(Provinces, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=250, null=True, blank=True)
    image_file = models.ImageField(upload_to='Provinces/images', null=True, blank=True)
    published_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.provinces.name

    objects = models.Manager()  # defoult
