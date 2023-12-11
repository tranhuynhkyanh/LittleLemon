from django.urls import path
from restaurant.views import index
from restaurant.views import MenuItemsView,SingleMenuItemView
urlpatterns = [
    path("",index,name="index"),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
]
