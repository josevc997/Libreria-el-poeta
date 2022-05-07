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
    data['productos'] = [{'nombre': "primer libro", 'tipo': "Revista", 'annio': 2015, 'edicion': 'Primera Edición', 'resumen': "Mejor libro de todos"}, {'nombre': "segundo libro", 'tipo': "libro", 'annio': 1997, 'edicion': 'Segunda Edición', 'resumen': "Segundo mejor libro de todos"}, {'nombre': "tercer libro", 'tipo': "enciclopedia", 'annio': 2022, 'edicion': 'Ultima Edición', 'resumen': "Peor libro de todos"}]
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

def bodegas(request): 
    template = "bodegas/lista.html"
    data = dict()
    data['titulo'] = "Bodegas Registrados"
    data['bodegas'] = [{'id': 1, 'nombre': 'Santiago','comuna': 'Santiago Centro','direccion': 'Almirante Barroso #333'},{'id': 2, 'nombre': 'Concepción','comuna': 'Concepción','direccion': 'Paseo Costero #1125'},{'id': 3, 'nombre': 'Valparaiso','comuna': 'Con Con','direccion': 'Ambrosio Ohiggins #2201'}]
    return render(request, template, data)

def detalleBodegas(request, bodega_id): 
    template = "bodegas/detalle.html"
    data = dict()
    data['titulo'] = "Bodega XXXXX"
    data['bodega'] = {'id': 3, 'nombre': 'Valparaiso','comuna': 'Con Con','direccion': 'Ambrosio Ohiggins #2201'}
    data['productos'] = [{'nombre': "primer libro", 'tipo': "Revista", 'annio': 2015, 'edicion': 'Primera Edición', 'resumen': "Mejor libro de todos", 'cantidad': 15}, {'nombre': "segundo libro", 'tipo': "libro", 'annio': 1997, 'edicion': 'Segunda Edición', 'resumen': "Segundo mejor libro de todos", 'cantidad': 23}, {'nombre': "tercer libro", 'tipo': "enciclopedia", 'annio': 2022, 'edicion': 'Ultima Edición', 'resumen': "Peor libro de todos", 'cantidad': 30}]
    return render(request, template, data)

def registroBodegas(request):
    template = "bodegas/registro.html"
    data = dict()
    data['titulo'] = "Registro bodegas"

    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['comuna']
        annio = request.POST['direccion']

    return render(request, template, data)

def editoriales(request): 
    template = "editoriales/lista.html"
    data = dict()
    data['titulo'] = "Editoriales Registrados"
    data['editoriales'] = [{'nombre': 'Zig-Zag', 'id': 1},{'nombre': 'Alfaguara', 'id': 2},{'nombre': 'Libros Premiere', 'id': 3}]
    return render(request, template, data)

def registroEditoriales(request):
    template = "editoriales/registro.html"
    data = dict()
    data['titulo'] = "Registro Editoriales"

    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['comuna']
        annio = request.POST['direccion']

    return render(request, template, data)