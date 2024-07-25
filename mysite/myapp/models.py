from django.db import models
    
class Chairs(models.Model):
    GROUPS={
        ('office','офисное'),
        ('ort','ортопедическое'),
        ('game','игровое')
    }
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description1 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=50)
    group = models.CharField(max_length=50, choices=GROUPS)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/officeChairs/preview/')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url
    
#class GameChairs(models.Model):
#    name = models.CharField(max_length=100)
#    price = models.CharField(max_length=100)
#    description1 = models.CharField(max_length=50)
#    description2 = models.CharField(max_length=50)
#    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/gameChairs/preview/')
#
#    def __str__(self):
#        return self.name
#
#    @property
#    def image_url(self):
#        if self.image and hasattr(self.image, 'url'):
#           return self.image.url
#    
#class OrtChairs(models.Model):
#    name = models.CharField(max_length=100)
#    price = models.CharField(max_length=100)
#    description1 = models.CharField(max_length=50)
#    description2 = models.CharField(max_length=50)
#    image = models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/ortChairs/preview/')
#
#    def __str__(self):
#        return self.name
#
#    @property
#    def image_url(self):
#        if self.image and hasattr(self.image, 'url'):
#           return self.image.url

class Main_OfficeChairs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/main/')
    image_left = models.ImageField(blank=True, null=True, upload_to='images/content/main/officeChairs/left')
    image_right = models.ImageField(blank=True, null=True, upload_to='images/content/main/officeChairs/right')
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url

class Main_GameChairs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/main/')
    image_left = models.ImageField(blank=True, null=True, upload_to='images/content/main/gameChairs/left')
    image_right = models.ImageField(blank=True, null=True, upload_to='images/content/main/gameChairs/right')
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url

class Main_OrtChairs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/main/')
    image_left = models.ImageField(blank=True, null=True, upload_to='images/content/main/ortChairs/left')
    image_right = models.ImageField(blank=True, null=True, upload_to='images/content/main/ortChairs/right')
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url

class Main_DirChairs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/content/main/')
    image_left = models.ImageField(blank=True, null=True, upload_to='images/content/main/dirChairs/left')
    image_right = models.ImageField(blank=True, null=True, upload_to='images/content/main/dirChairs/right')
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image.url