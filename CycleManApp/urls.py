from django.urls import path
from . import views

urlpatterns = [
    path('cycles', views.AllCycleView.as_view()),
    path('cycles/<int:pk>', views.SingleCycleView.as_view())
]
