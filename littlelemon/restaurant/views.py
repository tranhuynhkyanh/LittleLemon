from django.shortcuts import render
from django.http import response,HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from restaurant.serializers import MenuSerializer,BookingSerializer
from restaurant.models import Menu,Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
def index(request):
    return render(request,"index.html")

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 
