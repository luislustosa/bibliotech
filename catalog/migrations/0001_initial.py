from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('isbn', models.CharField(help_text='13 caracteres', max_length=13)),
                ('genero', models.CharField(max_length=50)),
                ('data_publicacao', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='catalog.autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='catalog.editora')),
            ],
        ),
    ]
