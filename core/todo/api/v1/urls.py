from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', views.TodoViewSet, basename="tasks")




urlpatterns = [
    
    path('users/', views.UsersGenericApiView.as_view()),
    
    ]

urlpatterns += router.urls
