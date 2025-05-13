from rest_framework import viewsets
from .models import Car, Review
from .serializers import CarSerializer, CarCreateSerializer, ReviewSerializer
from dj_rql.drf import RQLFilterBackend
from .filters import CarFilterClass, ReviewFilterClass


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CarCreateSerializer
        return CarSerializer

    filter_backends = [RQLFilterBackend]
    qrl_filter_class = CarFilterClass


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [RQLFilterBackend]
    qrl_filter_class = ReviewFilterClass
