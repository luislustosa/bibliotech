from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views as api_views
from catalog import views as catalog_views

router = routers.DefaultRouter()
router.register(r'livros', api_views.LivroViewSet, basename='livro')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs da API
    path('api/', include(router.urls)), 
    
    # URL da Home (Front-end)
    path('', catalog_views.home_view, name='home'), 
]
