from rest_framework import serializers
from catalog.models import Autor, Editora, Livro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome']

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ['nome']

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    editora = EditoraSerializer(read_only=True)

    class Meta:
        model = Livro
        fields = [
            'id', 
            'titulo', 
            'autor', 
            'editora', 
            'isbn', 
            'genero', 
            'data_publicacao'
        ]
