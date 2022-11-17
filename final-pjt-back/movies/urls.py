from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views



urlpatterns = [
    
    path('movies/', views.movie_list),
    # path('<int:movie_pk>/', views.detail),
    
    path('movives/<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
]
