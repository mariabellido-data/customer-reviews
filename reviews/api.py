from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Review
from .serializers import ReviewSerializer

class ReviewListCreate(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
