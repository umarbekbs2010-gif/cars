from django.db import models

# Create your models here.



from django.db import models


class Cars(models.Model):
  model = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=12, decimal_places=2)
  invented_year = models.IntegerField()

  def __str__(self):
    return f'{self.model} ({self.invented_year})'