from django.urls import path
from .views import index,PortFolioDetail

urlpatterns=[
    path('', index, name='index'),
    path('postfolio/<int:pk>/', PortFolioDetail.as_view(), name='portfolio-detail'),


]
