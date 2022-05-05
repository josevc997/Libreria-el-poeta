from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'inventario/index.html'
    data = dict()
    data['titulo'] = "Inventario El Poeta"
    return render(request, template, data)

def autores(request): 
    template = "autores/lista.html"
    data = dict()
    data['titulo'] = "Autores Registrados"
    info = dict()
    autores = []
    autores.append({'nombre': "Jose", 'apellido': "Valencia", 'correo': "jose.valencia@gmail.com"})
    autores.append({'nombre': "Juan", 'apellido': "Vasquez", 'correo': "juan.vasquez@gmail.com"})
    autores.append({'nombre': "Javiera", 'apellido': "Simpson", 'correo': "javiera.Simpson@gmail.com"})
    data['autores'] = autores
    return render(request, template, data)