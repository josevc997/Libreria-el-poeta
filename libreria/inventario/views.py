from re import template
from django.shortcuts import render, redirect
from .models import Compra, Genero, Movimiento, Pedido, Perfil, Persona, Editorial, Publicacion, Autor, Autor_Publicacion, Proveedor, Bodega, Publicacion_Bodega
from .seed import seedTables
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

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
    data['autores'] = Autor.objects.all()
    return render(request, template, data)

def detalleAutor(request, id_autor):
    template = "autores/detalle.html"
    
    data = dict()
    data['titulo'] = "Detalle Autor"
    data['autor'] = Autor.objects.get(id_autor=id_autor)

    return render(request, template, data)

def editarAutor(request, id_autor):
    template = "autores/editar.html"
    
    data = dict()
    data['titulo'] = "Editar Autor"
    autor = Autor.objects.get(id_autor=id_autor)
    data['autor'] = autor

    if request.method == 'POST':
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
        print(autor)
        autor.save()
        return redirect('detalleAutor', id_autor)

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

def detallePublicacion(request, id_publicacion):
    template = "productos/detalle.html"
    
    data = dict()
    data['titulo'] = "Detalle Publicacion"
    data['publicacion'] = Publicacion.objects.get(id_publicacion=id_publicacion)

    return render(request, template, data)

def editarPublicacion(request, id_publicacion):
    template = "productos/editar.html"
    
    data = dict()
    data['titulo'] = "Editar Publicacion"
    publicacion = Publicacion.objects.get(id_publicacion=id_publicacion)
    data['publicacion'] = publicacion 

    if(request.POST):
        if(request.POST['nombre'].strip(" ") != ''):
            publicacion.nombre = request.POST['nombre']
        if(request.POST['edicion'].strip(" ") != ''):
            publicacion.edicion = request.POST['edicion']
        if(request.POST['isbn'].strip(" ") != ''):
            publicacion.isbn = request.POST['isbn']
        if(request.POST['resumen'].strip(" ") != ''):
            publicacion.resumen = request.POST['resumen']
        if(request.POST['precio'].strip(" ") != ''):
            publicacion.precio = int(request.POST['precio'])
        publicacion.save()
        return redirect('detallePublicacion', publicacion.id_publicacion)

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

def generos(request): 
    template = "generos/lista.html"
    data = dict()
    data['titulo'] = "Generos Registrados"
    data['generos'] = Genero.objects.all()
    return render(request, template, data)

def registroGeneros(request):
    template = "generos/registro.html"
    data = dict()
    data['titulo'] = "Registro Generos"

    if request.method == 'POST':
        genero = Genero()
        if(request.POST['nombre'].strip(" ") != ''):
            genero.nombre_genero = request.POST['nombre']
            genero.save()
            return redirect('generos')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "genero no registrada, debe rellenar los campos obligatorios"
    return render(request, template, data)
    

def detalleGenero(request, id_genero):
    template = "generos/detalle.html"
    
    data = dict()
    data['titulo'] = "Detalle Genero"
    data['genero'] = Genero.objects.get(id_genero=id_genero)

    return render(request, template, data)

def editarGenero(request, id_genero):
    template = "generos/editar.html"
    data = dict()
    data['titulo'] = "Editar Generos"
    genero = Genero.objects.get(id_genero=id_genero)
    data['genero'] = genero

    if request.method == 'POST':
        if(request.POST['nombre'].strip(" ") != ''):
            genero.nombre_genero = request.POST['nombre']
            genero.save()
            return redirect('generos')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "genero no registrada, debe rellenar los campos obligatorios"
    return render(request, template, data)

def movimientos(request): 
    template = "movimientos/lista.html"
    data = dict()
    data['titulo'] = "Movimientos Registrados"
    data['movimientos'] = Movimiento.objects.all()
    return render(request, template, data)

def registroMovimientos(request):
    template = "movimientos/registro.html"
    data = dict()
    data['titulo'] = "Registro Movimientos"
    data['bodegas'] = Bodega.objects.all()

    if request.method == 'POST':
        print(request.user.is_authenticated)
        movimiento = Movimiento()
        if(request.POST['bodega_origen'].strip(" ") != ''):
            movimiento.id_bodega_origen = Bodega.objects.get(id_bodega = int(request.POST['bodega_origen']))
        if(request.POST['bodega_destino'].strip(" ") != ''):
            movimiento.id_bodega_destino = Bodega.objects.get(id_bodega = int(request.POST['bodega_destino']))
        if(request.POST['bodega_origen'].strip(" ") == '' and request.POST['bodega_destino'].strip(" ") == ''):
            data['toast'] = "Error"
            data['mensaje'] = "Movimiento no registrada, debe rellenar los campos obligatorios"
        elif(movimiento.id_bodega_origen == movimiento.id_bodega_destino):
            data['toast'] = "Error"
            data['mensaje'] = "Movimiento no registrada, La bodega de origen debe ser distinta a la bodega de destino"
        if(not request.user.is_authenticated):
            data['toast'] = "Error"
            data['mensaje'] = "Movimiento no registrada, Debe iniciar sesión para registrar movimiento"
        else:
            movimiento.id = request.user
            movimiento.estado = "Solicitando"
            movimiento.fecha_solicitud = datetime.now()
            movimiento.save()
            return redirect('movimientos')
    return render(request, template, data)

def agregarPublicacionMovimiento(request, id_movimiento):
    template = "movimientos/agregar.html"
    data = dict()
    data['titulo'] = "Agregar publicacions a movimiento"
    movimiento = Movimiento.objects.get(id_movimiento = id_movimiento)

    if request.method == 'POST':
        print(request.POST['publicacion'])
        if(request.POST['publicacion'].strip(" ") != ''):
            publicacion = Publicacion.objects.get(id_publicacion=int(request.POST['publicacion']))
            publicacionEnBodega = Publicacion_Bodega.objects.get(id_publicacion=int(request.POST['publicacion']), id_bodega=movimiento.id_bodega_origen.id_bodega)
        if(request.POST['cantidad'].strip(" ") != ''):
            cantidad = int(request.POST['cantidad'])
        if(request.POST['publicacion'].strip(" ") == '' or request.POST['cantidad'].strip(" ") == ''):
            data['toast'] = "Error"
            data['mensaje'] = "Publicacion no registrada, Debe rellenar todos los campos"
        elif(publicacion in movimiento.publicaciones.all()):
            data['toast'] = "Error"
            data['mensaje'] = "Publicacion ya agregada al movimiento"
        elif (cantidad > publicacionEnBodega.cantidad):
            data['toast'] = "Error"
            data['mensaje'] = "No puede agregar más publicaciones de las que se encuentran en stock"
        else:
            movimiento.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad})
            publicacionEnBodega.cantidad -= cantidad
            publicacionEnBodega.save()

    data['movimiento'] = movimiento
    data['publicaciones'] = Publicacion_Bodega.objects.filter(id_bodega = request.user.id_bodega)

    return render(request, template, data)
    
def detalleMovimiento(request, id_movimiento):
    template = "movimientos/detalle.html"
    
    data = dict()
    data['titulo'] = "Detalle Movimiento"
    data['compra'] = Compra.objects.get(id_compra=1)
    data['movimiento'] = Movimiento.objects.get(id_movimiento=id_movimiento)

    return render(request, template, data)

def editarMovimiento(request, id_movimiento):
    template = "movimientos/editar.html"
    data = dict()
    data['titulo'] = "Editar Movimientos"
    movimiento = Movimiento.objects.get(id_movimiento=id_movimiento)
    data['movimiento'] = movimiento

    # if request.method == 'POST':
    #     if(request.POST['nombre'].strip(" ") != ''):
    #         genero.nombre_genero = request.POST['nombre']
    #         genero.save()
    #         return redirect('generos')
    #     else:
    #         data['toast'] = "Error"
    #         data['mensaje'] = "genero no registrada, debe rellenar los campos obligatorios"
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
        if(request.POST['correo'].strip(" ") != ''):
            editorial.correo_editorial = request.POST['correo']
        if(request.POST['telefono'].strip(" ") != ''):
            editorial.telefono_editorial = request.POST['telefono']
        if(request.POST['direccion'].strip(" ") != ''):
            editorial.direccion_editorial = request.POST['direccion']
        if(request.POST['nombre'].strip(" ") != ''):
            editorial.nombre_editorial = request.POST['nombre']
            editorial.save()
            return redirect('editoriales')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Editorial no registrada, debe rellenar los campos obligatorios"
    return render(request, template, data)

def detalleEditorial(request, id_editorial):
    template = "editoriales/detalle.html"
    data = dict()
    data['titulo'] = "Detalle Editorial"

    editorial = Editorial.objects.get(id_editorial=id_editorial)
    data["editorial"] = editorial

    if request.method == 'POST':
        if(request.POST['correo'].strip(" ") != ''):
            editorial.correo_editorial = request.POST['correo']
        if(request.POST['telefono'].strip(" ") != ''):
            editorial.telefono_editorial = request.POST['telefono']
        if(request.POST['direccion'].strip(" ") != ''):
            editorial.direccion_editorial = request.POST['direccion']
        if(request.POST['nombre'].strip(" ") != ''):
            editorial.nombre_editorial = request.POST['nombre']
            editorial.save()
            return redirect('editoriales')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Editorial no modificada, debe rellenar los campos obligatorios"


    return render(request, template, data)

def editarEditorial(request, id_editorial):
    template = "editoriales/editar.html"
    data = dict()
    data['titulo'] = "Editar Editorial"

    editorial = Editorial.objects.get(id_editorial=id_editorial)
    data["editorial"] = editorial

    if request.method == 'POST':
        if(request.POST['correo'].strip(" ") != ''):
            editorial.correo_editorial = request.POST['correo']
        if(request.POST['telefono'].strip(" ") != ''):
            editorial.telefono_editorial = request.POST['telefono']
        if(request.POST['direccion'].strip(" ") != ''):
            editorial.direccion_editorial = request.POST['direccion']
        if(request.POST['nombre'].strip(" ") != ''):
            editorial.nombre_editorial = request.POST['nombre']
            editorial.save()
            return redirect('editoriales')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Editorial no modificada, debe rellenar los campos obligatorios"


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
    data['compras'] = Compra.objects.filter(id_persona=id_persona)
    # print(data['persona'].publicacion_compra_set.all())

    return render(request, template, data)

def editarPersonas(request, id_persona):
    template = "personas/editar.html"
    
    data = dict()
    data['titulo'] = "Editar Persona"
    persona = Persona.objects.get(id_persona=id_persona)
    data['persona'] = persona
    if request.method == 'POST':
        persona = Persona.objects.get(id_persona=id_persona)
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
    # print(data['persona'].publicacion_compra_set.all())

    return render(request, template, data)

def seed(request):
    seedTables()
    return redirect('index')

def loginPerfil(request):
    template = "perfil/login.html"

    data = dict()

    data['titulo'] = "Inicio de sesion"
    
    if(request.method == "POST"):
        nombre = request.POST['username']
        contraseña = request.POST['password']
        user = authenticate(username=nombre, password=contraseña)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('productos')
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Usuario o contraseña incorrectos"


    return render(request, template, data)    

def logoutPerfil(request):
    data = dict()

    data['titulo'] = "Cerrar sesion"
    
    if(request.user.is_authenticated):
        logout(request)
    return redirect('index')

def perfiles(request):
    template = "perfil/lista.html"

    data = dict()
    data['titulo'] = "Lista de perfiles"
    data['perfiles'] = Perfil.objects.all()

    return render(request, template, data)

def detallePerfiles(request, perfil_id):
    template = "perfil/detalle.html"

    data = dict()
    data['titulo'] = "detalle perfil"
    data['perfil'] = Perfil.objects.get(id=perfil_id)
    data['movimientos'] = Movimiento.objects.filter(id=perfil_id)
    data['pedidos'] = Pedido.objects.filter(id=perfil_id)

    return render(request, template, data)

def editarPerfil(request, id_perfil):
    template = "perfil/editar.html"

    data = dict()
    data['titulo'] = "Editar perfil"
    perfil = Perfil.objects.get(id=id_perfil)
    data['bodegas'] = Bodega.objects.all()
    if request.method == "POST":
        if(request.POST['username'].strip(" ") != '' and perfil.username != request.POST['username']):
            perfil.username = request.POST['username']
        if('activo' in request.POST):
            perfil.is_active = 1
        else:
            perfil.is_active = 0
        if(request.POST['tipo'].strip(" ") != '' and perfil.tipo_usuario != request.POST['tipo']):
            perfil.tipo_usuario = request.POST['tipo']
        if(request.POST['bodega'].strip(" ") != '' and perfil.id_bodega.id_bodega != int(request.POST['bodega'])):
            perfil.id_bodega = Bodega.objects.get(id_bodega=int(request.POST['bodega']))
        perfil.save()
    data['perfil'] = perfil

    return render(request, template, data)

def registroPerfil(request):
    template = "perfil/registro.html"

    data = dict()
    data['bodegas'] = Bodega.objects.all()
    data['titulo'] = "Registro perfil"
    if(request.method == "GET"):
        if(request.GET["rut"] != ""):
            rut = request.GET["rut"]
            # personaPerfil = Persona.objects.get(rut=rut)
            personaPerfil = Persona.objects.get_or_create(rut=request.GET['rut'])
            data['persona'] = personaPerfil[0]
    if(request.method == "POST"):
        if(request.POST["rut"] != ""):
            rut = request.POST["rut"]
            personaPerfil = Persona.objects.get(rut=rut)
        if(request.POST["nombres"] != ""):
            personaPerfil.nombres = request.POST["nombres"]
        if(request.POST["apellidos"] != ""):
            personaPerfil.apellidos = request.POST["apellidos"]
        if(request.POST["direccion"] != ""):
            personaPerfil.direccion = request.POST["direccion"]
        if(request.POST["correo"] != ""):
            personaPerfil.correo = request.POST["correo"]
        if(request.POST["telefono"] != ""):
            personaPerfil.telefono = request.POST["telefono"]
        personaPerfil.save()
        perfil = Perfil()
        if(request.POST["username"].strip(" ") != ""):
            perfil.username = request.POST["username"]
        if(request.POST["pass1"].strip(" ") != "" and request.POST["pass2"].strip(" ") != "" and request.POST["pass1"] == request.POST["pass2"]):
            perfil.set_password(request.POST["pass1"])
        if("activo" in request.POST):
            perfil.is_active = 1
        else:
            perfil.is_active = 0
        if(request.POST["tipo"].strip(" ") != ""):
            perfil.tipo_usuario = request.POST["tipo"]
        if(request.POST["bodega"].strip(" ") != ""):
            perfil.id_bodega = Bodega.objects.get(id_bodega=int(request.POST["bodega"]))
        perfil.id_persona = personaPerfil
        perfil.is_superuser = 0
        perfil.first_name = personaPerfil.nombres
        perfil.last_name = personaPerfil.apellidos
        perfil.email = personaPerfil.correo
        perfil.is_staff = 0
        perfil.is_active = 1
        perfil.date_joined = datetime.now()
        perfil.save()
        
    return render(request, template, data)

def preregistroPerfil(request):
    template = "perfil/preregistro.html"

    data = dict()
    data['titulo'] = "Registro perfil"
        
    return render(request, template, data)

def cambiarEstadoPerfil(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)
    if(perfil.is_active == 0):
        perfil.is_active = 1
    elif(perfil.is_active == 1):
        perfil.is_active = 0
    print(perfil.is_active)
    perfil.save()
    return redirect('perfiles')



# Codigo Bruno Pozo
def bodegas(request): 
    template = "bodegas/lista.html"
    data = dict()
    data['titulo'] = "Bodegas Registrados"
    data['bodegas'] = Bodega.objects.all()
    return render(request, template, data)

def detalleBodegas(request, id_bodega): 
    template = "bodegas/detalle.html"
    data = dict()
    data['titulo'] = "Detalle Bodegas"
    data['bodega'] = Bodega.objects.get(id_bodega=id_bodega)
    data['productos'] = Bodega.objects.filter(id_bodega=id_bodega)
    return render(request, template, data)

def registroBodegas(request):
    template = "bodegas/registro.html"
    data = dict()
    data['titulo'] = "Registro bodegas"

    if request.method == "POST":
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        comuna = request.POST['comuna']
        telefono = request.POST['telefono']
        bodega = Bodega()
        bodega.nombre_bodega = nombre
        bodega.direccion = direccion
        bodega.comuna = comuna
        bodega.telefono_bodega = telefono
        bodega.save()

    return render(request, template, data)

def editarBodegas(request, id_bodega):
    template = "bodegas/editar.html"

    data = dict()
    data['titulo'] = "Editar Bodega"
    bodega = Bodega.objects.get(id_bodega=id_bodega)
    data['bodega'] = bodega

    if request.method == 'POST':
        if(request.POST['nombre'].strip(" ") != ''):
            bodega.nombre_bodega = request.POST['nombre']
        if(request.POST['comuna'].strip(" ") != ''):
            bodega.comuna = request.POST['comuna']
        if(request.POST['direccion'].strip(" ") != ''):
            bodega.direccion = request.POST['direccion']
        if(request.POST['telefono'].strip(" ") != ''):
            bodega.telefono_bodega = request.POST['telefono']
        print(bodega)
        bodega.save()
        return redirect('detalleBodegas', id_bodega)

    return render(request, template, data)


def listaCompras(request):
    template = "compras/lista.html"
    data = dict()
    data['titulo'] = "Lista Compras"
    data['compras']= Compra.objects.all()

    return render(request, template, data)

def registroCompras(request):
    template = "compras/registro.html"
    data = dict()
    data['titulo'] = "Registro Compras"
    return render(request, template, data)

def detalleCompras(request, id_compra):
    template = "compras/detalle.html"
    data = dict()
    data['titulo'] = "Detalle Compras"
    #data['Persona'] = Persona.objects.get(id_persona=id_persona)
    data['compra'] = Compra.objects.get(id_compra=id_compra)
    #data['Fecha Compra'] = Compra.objects.filter(id_compra=id_compra)
    #data['Metodo Pago'] = Compra.objects.get(id_compra=id_compra)

    return render(request, template, data)

#def detalleCompras(request):




# Codigo Pablo Cea
def registroProveedores(request):
    template = "proveedores/registro.html"

    data = dict()

    data['titulo'] = "Registro Proveedores"

    if request.method == 'POST':
        nombre = request.POST['nombreP']
        direccion = request.POST['direccionP']
        comuna =    request.POST['comunaP']
        correo =    request.POST['correoP']
        telefono =  request.POST['telefonoP']
        proveedor = Proveedor()
        proveedor.nombre_proveedor = nombre
        proveedor.direccion_proveedor = direccion
        proveedor.comuna_proveedor = comuna
        proveedor.correo_proveedor = correo
        proveedor.telefono_proveedor = telefono
        proveedor.save()
    return render(request, template, data)

def proveedores(request):
    template = "proveedores/historial.html"
    data = dict()

    data['titulo'] = "Registro Proveedores"

    
    data['proveedores'] = Proveedor.objects.all()
    return render(request, template, data)

def detalleProveedores(request,id_proveedor):
    template = "proveedores/detalle.html"
    data = dict()
    data['titulo'] = "Detalle autor"
    data['proveedor'] = Proveedor.objects.get(id_proveedor=id_proveedor)

    return render(request,template,data)
    

# # #