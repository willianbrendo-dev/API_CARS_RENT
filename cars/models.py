from django.db import models


class Car(models.Model):
    TYPE_CHOICES = [
        ('Sport', 'Sport'),
        ('SUV', 'SUV'),
        ('MPV', 'MPV'),
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
    ]

    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    FUEL_CHOICES = [
        ('Gasoline', 'Gasoline'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Diesel', 'Diesel'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    capacity = models.PositiveIntegerField()  # Número de pessoas
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    fuel_capacity = models.PositiveIntegerField(help_text="Capacidade do tanque em litros")
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    original_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return self.name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        verbose_name = 'Imagem do Carro'
        verbose_name_plural = 'Imagens do Carro'
        ordering = ['id']


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    user_position = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    rating = models.PositiveIntegerField()  # De 1 a 5
    date = models.DateField()

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-date']

    def __str__(self):
        return f"Review by {self.user_name} on {self.date}"
