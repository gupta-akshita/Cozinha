from django.db import models
from shops.models import Shop
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from shops.models import Categories

def validate_rating(value):
    if value < 1 and value > 5:
        raise ValidationError(
            _('Rating shoud be in range 1 to 5'),
            params={'value': value},
        )

class Product(models.Model):
    CATEGORY = (
        ('veg','Veg'),
        ('Non-Veg','Non-Veg')
    )

    pshop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    # pdesp = models.CharField(max_length=255)
    pprice = models.IntegerField()
    prating = models.FloatField(validators=[validate_rating])
    pimage = models.ImageField(upload_to='img/')
    ptype = models.CharField(max_length=10, choices=CATEGORY)
    pcategory = models.ManyToManyField(Categories) #choices are meant to be enter
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pname
