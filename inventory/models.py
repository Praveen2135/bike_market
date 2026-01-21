from django.db import models

class Bike(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'Like New'),
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'),
    ]

    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    kms_driven = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"

class BikeImage(models.Model):
    bike = models.ForeignKey(Bike, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bikes/')

class Enquiry(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

