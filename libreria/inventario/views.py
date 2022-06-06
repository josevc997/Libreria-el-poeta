from django.shortcuts import render
from .models import Persona, Editorial, Publicacion, Autor, Autor_Publicacion, Proveedor

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
    data['autores'] = Autor.objects.all()
    return render(request, template, data)

def registroAutores(request):
    template = "autores/registro.html"
    data = dict()
    data['titulo'] = "Registro Autores"

    if request.method == 'POST':
        autor = Autor()
        if(request.POST['nombre'].strip(" ") != ''):
            autor.nombres_autor = request.POST['nombre']
        if(request.POST['apellido'].strip(" ") != ''):
            autor.apellidos_autor = request.POST['apellido']
        if(request.POST['correo'].strip(" ") != ''):
            autor.correo_autor = request.POST['correo']
        if(request.POST['nacionalidad'].strip(" ") != ''):
            autor.nacionalidad_autor = request.POST['nacionalidad']
        if(request.POST['pseudonimo'].strip(" ") != ''):
            autor.pseudonimo_autor = request.POST['pseudonimo']
        autor.save()

    return render(request, template, data)

def productos(request): 
    template = "productos/lista.html"
    data = dict()
    data['titulo'] = "productos Registrados"
    data['productos'] = Publicacion.objects.all()
    return render(request, template, data)

def registroProductos(request):
    template = "productos/registro.html"
    data = dict()
    data['titulo'] = "Registro Productos"
    # data['autores'] = [{'nombre': 'Neftali Reyes', 'id': 1},{'nombre': 'Violeta Parra', 'id': 2},{'nombre': 'Nicanor Parra', 'id': 3}]
    data['editoriales'] = Editorial.objects.all()
    data['autores'] = Autor.objects.all()

    if request.method == 'POST':
        publicacion = Publicacion()
        if(request.POST['nombre'].strip(" ") != ''):
            publicacion.nombre = request.POST['nombre']
        if(request.POST['autor'].strip(" ") != ''):
            autor = Autor.objects.get(id_autor = request.POST['autor'])
        if(request.POST['tipo'].strip(" ") != ''):
            publicacion.tipo_producto = request.POST['tipo']
        if(request.POST['editorial'].strip(" ") != ''):
            editorial = Editorial.objects.get(id_editorial = int(request.POST['editorial']))
            publicacion.id_editorial = editorial
        if(request.POST['edicion'].strip(" ") != ''):
            publicacion.edicion = request.POST['edicion']
        if(request.POST['fecha'].strip(" ") != ''):
            publicacion.fecha_publicacion = request.POST['fecha']
        if(request.POST['isbn'].strip(" ") != ''):
            publicacion.isbn = request.POST['isbn']
        if(request.POST['serie'].strip(" ") != ''):
            publicacion.numero_serie = int(request.POST['serie'])
        if(request.POST['resumen'].strip(" ") != ''):
            publicacion.resumen = request.POST['resumen']
        if(request.POST['precio'].strip(" ") != ''):
            publicacion.precio = int(request.POST['precio'])
        publicacion.save()
        publicacion.autores.add(autor)

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
    data['editoriales'] = Editorial.objects.all()
    return render(request, template, data)

def registroEditoriales(request):
    template = "editoriales/registro.html"
    data = dict()
    data['titulo'] = "Registro Editoriales"

    if request.method == 'POST':
        editorial = Editorial()
        if(request.POST['nombre'].strip(" ") != ''):
            editorial.nombre_editorial = request.POST['nombre']
        if(request.POST['correo'].strip(" ") != ''):
            editorial.correo_editorial = request.POST['correo']
        if(request.POST['telefono'].strip(" ") != ''):
            editorial.telefono_editorial = request.POST['telefono']
        editorial.save()


    return render(request, template, data)

def registroPersonas(request):
    template = "personas/registro.html"
    data = dict()
    data['titulo'] = "Registro Personas"

    if request.method == 'POST':
        persona = Persona()
        if(request.POST['nombre'].strip(" ") != ''):
            persona.nombres = request.POST['nombre']
        if(request.POST['rut'].strip(" ") != ''):
            persona.rut = request.POST['rut']
        if(request.POST['apellidos'].strip(" ") != ''):
            persona.apellidos = request.POST['apellidos']
        if(request.POST['direccion'].strip(" ") != ''):
            persona.direccion = request.POST['direccion']
        if(request.POST['correo'].strip(" ") != ''):
            persona.correo = request.POST['correo']
        if(request.POST['telefono'].strip(" ") != ''):
            persona.telefono = request.POST['telefono']
        if(persona.nombres != '' and persona.rut != ''):
            persona.save()
            data['toast'] = "Exito"
            data['mensaje'] = "Persona registrada correctamente"
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Persona no registrada, debe rellenar los campos obligatorios"

    return render(request, template, data)

def listaPersonas(request):
    template = "personas/lista.html"
    
    data = dict()
    data['titulo'] = "Lista Personas"
    data['personas'] = Persona.objects.all()

    return render(request, template, data)

def detallePersonas(request, id_persona):
    template = "personas/detalle.html"
    
    data = dict()
    data['titulo'] = "Detalle Personas"
    data['persona'] = Persona.objects.get(id_persona=id_persona)

    return render(request, template, data)

def registroProveedores(request):
    template = "proveedores/registro.html"

    data = dict()

    data['titulo'] = "Registro Proveedores"

    return render(request, template, data)