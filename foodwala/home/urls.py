from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homep'),
    path('about', aboutpage, name='abnoutp'),
    path('login', loginpage, name='loginp'),
    path('register', registerpage, name='registerp'),
    path('logout', logoutpage, name='logoutpage'),
    path('feedback', feedbackpage, name='feedbackp'),
    path('category', categorypage, name='categoryp'),
    path('food', foodpage, name='foodp'),

    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('my-cart', view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('user-profile', userprofilepage, name='userp'),
    path('updtuser', updatedprofilepage, name='updateusrp'),
    path('update-item/<id>/', update_item, name='update_item'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
