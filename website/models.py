from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from django_google_maps import fields as map_fields
# Create your models here.


class Slider(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "HOME SLIDER "
        verbose_name_plural = "HOME SLIDER"


class Test(models.Model):

    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(blank=True, null=True, max_length=50)
    title1 = models.CharField(blank=True, null=True, max_length=50)
    title2 = models.CharField(blank=True, null=True, max_length=50)
    url = models.URLField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.caption

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "HOME BODY "
        verbose_name_plural = "HOME BODY"


class Homecontact(models.Model):

    phone = models.IntegerField(
        blank=True, null=True)
    contact = models.EmailField(blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = "HOME PAGE CONTACT"
        verbose_name_plural = "HOME PAGE CONTACT"


class LogoEquipment(models.Model):

    image = models.ImageField(null=True, blank=True)
    title = models.CharField(blank=True, null=True, max_length=50)
    link = models.URLField(None, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "LOGO EQUIPMENT "
        verbose_name_plural = "LOGO EQUIPMENT"


class EquipBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "EQUIPMENT BANNER "
        verbose_name_plural = "EQUIPMENT BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Equipment(models.Model):
    parent = models.ForeignKey(
        EquipBanner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(None, max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "EQUIPMENTS"
        verbose_name_plural = "EQUIPMENTS"


class ServiceBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "SERVICES BANNER "
        verbose_name_plural = "SERVICES BANNER"


class Service(models.Model):
    parent = models.ForeignKey(
        ServiceBanner, on_delete=models.CASCADE, null=True, blank=True)
    service_banner = models.ImageField(null=True, blank=True)
    page_heading = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.title) + ": $" + str(self.price)

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "SERVICES "
        verbose_name_plural = "SERVICES"


class LiftBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "LIFTING EQUIPMENT BANNER "
        verbose_name_plural = "LIFTING EQUIPMENT BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Lifting(models.Model):
    parent = models.ForeignKey(
        LiftBanner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "LIFTING EQUIPMENT"
        verbose_name_plural = "LIFTING EQUIPMENT"


class OnroadBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "ON ROAD EQUIPMENT Banner"
        verbose_name_plural = "ON ROAD EQUIPMENT Banner"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class OnRoad(models.Model):

    parent = models.ForeignKey(
        OnroadBanner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "ON ROAD EQUIPMENT"
        verbose_name_plural = "ON ROAD EQUIPMENT"


class ConstructionBanner(models.Model):

    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "CONSTRUCTION BANNER"
        verbose_name_plural = "CONSTRUCTION BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Construction(models.Model):
    parent = models.ForeignKey(
        ConstructionBanner, on_delete=models.CASCADE, null=True, blank=True)
    page_heading = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "CONSTRUCTION EQUIPMENT"
        verbose_name_plural = "CONSTRUCTION EQUIPMENT"


class AboutBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "ABOUT US BANNER"
        verbose_name_plural = "ABOUT US BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class About(models.Model):
    parent = models.ForeignKey(
        'AboutBanner', on_delete=models.CASCADE, blank=True, null=True)
    banner = models.ImageField(null=True, blank=True)
    heading = models.TextField(max_length=100, null=True, blank=True)
    description = RichTextUploadingField(null=True)

    class Meta:
        verbose_name = "ABOUT US "
        verbose_name_plural = "ABOUT US"


class TransportBanner(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(max_length=100, null=True, blank=True)

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "TRANSPORT BANNER"
        verbose_name_plural = "TRANSPORT BANNER"


class Transport(models.Model):

    parent = models.ForeignKey(
        TransportBanner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_description = models.CharField(
        max_length=100, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "TRANSPORTATION"
        verbose_name_plural = "TRANSPORTATION"


class ContactBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)
    message_heading = models.CharField(
        null=True, blank=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=100)
    geolocation = models.URLField(null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = "CONTACT BANNER"
        verbose_name_plural = "CONTACT BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class EnquiryBanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "ENQUIRY BANNERY BANNER"
        verbose_name_plural = "ENQUIRY BANNERY BANNER"

    @ property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Socialiconlink(models.Model):
    fb = models.URLField(null=True, blank=True, max_length=100)
    insta = models.URLField(null=True, blank=True, max_length=100)
    link = models.URLField(null=True, blank=True, max_length=100)
