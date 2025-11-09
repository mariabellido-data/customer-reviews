from django.urls import path
from .views import review_list
from .api import ReviewListCreate, ReviewDetail

urlpatterns = [
    path('reviews/', review_list, name='review_list'),
    path('api/reviews/', ReviewListCreate.as_view(), name='api_reviews'),
    path('api/reviews/<int:pk>/', ReviewDetail.as_view(), name='api_review_detail'),
]
