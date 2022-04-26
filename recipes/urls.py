from django.urls import path
from recipes.views import home
from . import views

# 
app_name = 'recipes'

urlpatterns = [
    path('', home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]