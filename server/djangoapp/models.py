from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    """
    CarMake model represents the make of a car, including the name and a description.
    """
    name = models.CharField(max_length=100, verbose_name="Car Make")
    description = models.TextField(verbose_name="Description")
    
    # Optional: You can add other relevant fields if needed, like country_of_origin, etc.

    def __str__(self):
        """
        Return the name of the car make as its string representation.
        """
        return self.name


class CarModel(models.Model):
    """
    CarModel model represents the details of a car model, including its name, type, year,
    and a foreign key relationship to the CarMake model.
    """
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    WAGON = 'WAGON'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        # Add more car types as needed
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, verbose_name="Car Make")
    name = models.CharField(max_length=100, verbose_name="Car Model")
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default=SUV,
        verbose_name="Type of Car"
    )
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)],
        verbose_name="Manufacture Year"
    )
    
    # Optional: You can add additional fields like fuel_type, transmission, etc.

    def __str__(self):
        """
        Return a string representation of the car model, including its make, name, and year.
        """
        return f"{self.car_make.name} {self.name} ({self.year})"
