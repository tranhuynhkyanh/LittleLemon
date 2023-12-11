from django.db import models
import uuid
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    def get_item(self): 
        return f'{self.title} : {str(self.price)}'