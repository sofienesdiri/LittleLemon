from django.shortcuts import render
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request,'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializers_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializers_class = BookingSerializer