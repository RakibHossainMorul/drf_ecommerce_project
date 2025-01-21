from rest_framework.viewsets import ModelViewSet
from .models import Order, OrderItem
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
