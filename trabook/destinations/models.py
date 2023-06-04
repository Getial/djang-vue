from django.db import models

# Modelo de destinos
class Destination(models.Model):
    place = models.CharField(max_length=100, verbose_name="lugar")
    country = models.CharField(max_length=20, verbose_name="pais")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to='destinations', default='default.png', verbose_name='Imagen')
    score = models.FloatField(verbose_name="puntuacion")
    price = models.IntegerField(verbose_name="precio")
    isOnDiscount = models.BooleanField(default=False, verbose_name="descuento")
    priceWithDiscount = models.IntegerField(null=True, blank=True, verbose_name="precioConDescuento")

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'
        ordering = ['place']

    def __str__(self):
        return self.place


class VacationPlan(models.Model):
    place = models.CharField(max_length=100, verbose_name="lugar")
    country = models.CharField(max_length=20, verbose_name="pais", null=True)
    duration = models.CharField(max_length=20, verbose_name="duracion")
    description = models.TextField(verbose_name="descripcion")
    image = models.ImageField(upload_to='vacationplans', default='default.png', verbose_name='Imagen')
    score = models.FloatField(verbose_name="puntuacion")
    price = models.FloatField(verbose_name="precio")

    class Meta:
        verbose_name = 'VacationPlan'
        verbose_name_plural = 'VacationPlans'
        ordering = ['place']

    def __str__(self):
        return self.place


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="titulo")
    image = models.ImageField(upload_to='blogs', default='default.png', verbose_name='Imagen')
    pub_date = models.DateField(verbose_name="fechaDePublicacion")
    content = models.TextField(verbose_name="contenido")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['title']

    def __str__(self):
        return self.title