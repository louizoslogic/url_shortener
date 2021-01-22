from django.urls import path
from . import views

app_name = 'directurl'
urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('<int:hashed>', views.send_to, name='send_to')
]
