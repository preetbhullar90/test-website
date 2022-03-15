""" All import from django """
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Meals(models.Model):
    """ Food information model """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    people = models.IntegerField()
    price = models.DecimalField(max_length=5, decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='blogs/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            super(Meals, self).save(*args, **kwargs)

    class Meta:
        """ verbose name in model """
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


class Category(models.Model):

    """ Food catagory model """
    name = models.CharField(max_length=30)

    class Meta:
        """ Category verbose for model """

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

