from rest_framework import viewsets, filters
from catalog.models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ReadOnlyModelViewSet):
    
    # API endpoint que permite visualizar os livros.
    
    queryset = Livro.objects.all().select_related('autor', 'editora')
    serializer_class = LivroSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'autor__nome', 'editora__nome', 'genero', 'isbn']
  
