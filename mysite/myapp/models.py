from django.db import models
    
class OfficeChairs(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description1 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/officeChairs/preview/')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url
    
class GameChairs(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description1 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/gameChairs/preview/')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url
    
class OrtChairs(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description1 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/ortChairs/preview/')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url