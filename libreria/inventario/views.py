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

def registroAutores(request):
    template = "autores/registro.html"
    data = dict()
    data['titulo'] = "Registro Autores"
    print("saludos")

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']

    return render(request, template, data)

def productos(request): 
    template = "productos/lista.html"
    data = dict()
    data['titulo'] = "productos Registrados"
    info = dict()
    productos = []
    productos.append({'nombre': "primer libro", 'tipo': "Revista", 'annio': 2015, 'edicion': 'Primera Edición', 'resumen': "Mejor libro de todos"})
    productos.append({'nombre': "segundo libro", 'tipo': "libro", 'annio': 1997, 'edicion': 'Segunda Edición', 'resumen': "Segundo mejor libro de todos"})
    productos.append({'nombre': "tercer libro", 'tipo': "enciclopedia", 'annio': 2022, 'edicion': 'Ultima Edición', 'resumen': "Peor libro de todos"})
    data['productos'] = productos
    return render(request, template, data)

def registroProductos(request):
    template = "productos/registro.html"
    data = dict()
    data['titulo'] = "Registro Productos"
    data['autores'] = [{'nombre': 'Neftali Reyes', 'id': 1},{'nombre': 'Violeta Parra', 'id': 2},{'nombre': 'Nicanor Parra', 'id': 3}]
    data['editoriales'] = [{'nombre': 'Zig-Zag', 'id': 1},{'nombre': 'Alfaguara', 'id': 2},{'nombre': 'Libros Premiere', 'id': 3}]

    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        annio = request.POST['annio']
        edicion = request.POST['edicion']
        resumen = request.POST['resumen']
        autor = request.POST['autor']

        print(autor)

    return render(request, template, data)