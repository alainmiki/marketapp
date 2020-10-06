from django.urls import path
from . import views
app_name="products"
urlpatterns = [
    path('',views.home,name='home'),
    path('product-detail/<int:id>/',views.product_details,name='product_details'),
    path('about',views.about_us,name='about'),
    path("services",views.our_services,name="services"),
    path("search",views.search,name="search"),
    path("contacts",views.contactView,name="contact"),
]
