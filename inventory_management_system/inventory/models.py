from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Marks(models.Model):

    RollNo = models.CharField(max_length=10)
    MidSem = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    EndSem = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(75)])
    Attendance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    Others = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(35)])

    Grade = models.CharField(max_length=2)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.ID)

class DAA(Marks):
    pass

class DBMS(Marks):
    pass

class DS(Marks):
    pass