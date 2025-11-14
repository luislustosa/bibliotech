from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name='livros')
    isbn = models.CharField(max_length=13, help_text="13 caracteres")
    genero = models.CharField(max_length=50)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
