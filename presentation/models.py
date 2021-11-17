from django.db import models 


# Create your models here.
class SeleccionUnica(models.Model):
    user = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    vol = models.IntegerField(null=True)
    def __str__(self): #Devuelve etiqueta del objeto
        return '{}{}{}'.format(self.user, self.color, self.vol)