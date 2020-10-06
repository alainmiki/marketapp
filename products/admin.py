from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','brand','price','discount_price']

@admin.register(About_us)
class About_usAdmin(admin.ModelAdmin):
    list_display=['title','facebook_page1','facebook_page2','youtube_channel','instagram']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=['title',]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=["name","position","email"]

    list_display_links=["name","position","email"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["country","region","town","email"]

    list_display_links=["country","region","town","email"]

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display=["name","phone_number","email"]

    list_display_links=["name","phone_number","email"]
    

    

    

    

    

    
