from django.shortcuts import render

def home_view(request):
    """
    Renderiza a página principal que conterá o DataTables.
    """
    return render(request, 'home.html')
