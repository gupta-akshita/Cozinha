from django.db import models

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Shop(models.Model):
    sname = models.CharField(max_length=50)
    sdesp = models.CharField(max_length=255)
    saddress = models.CharField(max_length=255)
    savgtime = models.IntegerField()
    scategory = models.ManyToManyField(Categories)
    #savgprice = models.IntegerField()
    simage = models.ImageField(upload_to='img/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname

