
from django.db import models
from accounts.models import User


class Service(models.Model):

    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=100
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    price = models.IntegerField()

    city = models.CharField(
        max_length=100
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=15
    )

    whatsapp = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Booking(models.Model):

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

