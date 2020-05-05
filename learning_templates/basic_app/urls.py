from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
# setting namespace whenever you're using template tagging
# Global variable where Django automatically look for it
app_name = 'basic_app'
# this statement will tell Django to look under the basic_app
# and find url that matches

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
