from django.urls import path
from Basic_App import views

app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_url_temp, name = 'relative'),
    path('other/',views.other, name = 'other')
]
