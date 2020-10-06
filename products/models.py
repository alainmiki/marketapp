from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=200)
    brand=models.CharField( max_length=50)
    image=models.URLField( max_length=200,null=True, blank=True)
    amazon_link=models.TextField(null=True, blank=True)
    text_link=models.URLField( max_length=300, null=True, blank=True)
    image_link1=models.TextField( null=True, blank=True)
    description=models.TextField()
    config=models.TextField( null=True, blank=True)
    price=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_price=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    other_image=models.URLField(max_length=300, null=True, blank=True)
    other_image1=models.URLField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title+' '+self.brand
    
    class Meta:
        ordering=['title','brand',]

class About_us(models.Model):
    title=models.CharField(max_length=200)
    image1=models.URLField( max_length=200 ,null=True,blank=True)
    image2=models.URLField( max_length=200 ,null=True,blank=True)
    image3=models.URLField( max_length=200 ,null=True,blank=True)
    image4=models.URLField( max_length=200 ,null=True,blank=True)
    image5=models.URLField( max_length=200 ,null=True,blank=True)
    facebook_page1=models.URLField( max_length=200 ,null=True,blank=True)
    facebook_page2=models.URLField( max_length=200 ,null=True,blank=True)
    youtube_channel=models.URLField( max_length=200 ,null=True,blank=True)
    instagram=models.URLField( max_length=200 ,null=True,blank=True)
    github=models.URLField( max_length=200 ,null=True,blank=True)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['title',]
        verbose_name_plural="About Us"

class Service(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['title',]
        verbose_name_plural="Services"

class Team(models.Model):
    name=models.CharField( max_length=200)
    image=models.URLField( max_length=500,null=True,blank=True)
    position=models.CharField(max_length=50)
    description=models.TextField(("description"),null=True,blank=True)
    email=models.EmailField(("email"), max_length=254)
    date_join=models.DateTimeField(("date join"),auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Team"
class Messages(models.Model):
    name=models.CharField(max_length=150)
    phone_number=models.IntegerField()
    email=models.EmailField(("email"), max_length=254)
    message=models.TextField(("message"))
    send_date=models.DateTimeField(("send date"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name',]
        verbose_name='Message'
        verbose_name_plural="Messages"

class Contact(models.Model):
   
    image=models.URLField(("image url"), max_length=200)
    phone_number=models.IntegerField()
    email=models.EmailField(("email"), max_length=254)
    country=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    town=models.CharField(max_length=50)
    street=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.country+' '+self.email
    
    class Meta:
        ordering=['country','phone_number',]
