from re import template
from django.shortcuts import render, redirect
from .models import Compra, Genero, Movimiento, Pedido, Perfil, Persona, Editorial, Publicacion, Autor, Autor_Publicacion, Proveedor, Bodega, Publicacion_Bodega, Publicacion_Compra, Publicacion_Pedido
from .seed import seedTables
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    template = 'inventario/index.html'
    data = dict()
    data['titulo'] = "Inventario El Poeta"
    return render(request, template, data)

@login_required(login_url='/login')
def autores(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "autores/lista.html"
        data = dict()
        data['titulo'] = "Autores Registrados"
        data['autores'] = Autor.objects.all()
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoAutor(request, id_autor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        autor = Autor.objects.get(id_autor=id_autor)
        if(autor.is_active == 0):
            autor.is_active = 1
        elif(autor.is_active == 1):
            autor.is_active = 0
        print(autor.is_active)
        autor.save()
    else:
        return redirect('accesoDenegado')
    return redirect('autores')

@login_required(login_url='/login')
def detalleAutor(request, id_autor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "autores/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Autor"
        data['autor'] = Autor.objects.get(id_autor=id_autor)
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarAutor(request, id_autor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
            if('activo' in request.POST):
                autor.is_active = 1
            else:
                autor.is_active = 0
            autor.save()
            return redirect('detalleAutor', id_autor)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def registroAutores(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def productos(request): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "productos/lista.html"
        data = dict()
        data['titulo'] = "productos Registrados"
        data['productos'] = Publicacion.objects.all()
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoPublicacion(request, id_publicacion):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        publicacion = Publicacion.objects.get(id_publicacion=id_publicacion)
        if(publicacion.is_active == 0):
            publicacion.is_active = 1
        elif(publicacion.is_active == 1):
            publicacion.is_active = 0
        publicacion.save()
    else:
        return redirect('accesoDenegado')
    return redirect('productos')

@login_required(login_url='/login')
def detallePublicacion(request, id_publicacion):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "productos/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Publicacion"
        data['publicacion'] = Publicacion.objects.get(id_publicacion=id_publicacion)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarPublicacion(request, id_publicacion):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
            if('activo' in request.POST):
                publicacion.is_active = 1
            else:
                publicacion.is_active = 0
            publicacion.save()
            return redirect('detallePublicacion', publicacion.id_publicacion)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def registroProductos(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def generos(request): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "generos/lista.html"
        data = dict()
        data['titulo'] = "Generos Registrados"
        data['generos'] = Genero.objects.all()
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoGenero(request, id_genero):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        genero = Genero.objects.get(id_genero=id_genero)
        if(genero.is_active == 0):
            genero.is_active = 1
        elif(genero.is_active == 1):
            genero.is_active = 0
        genero.save()
    else:
        return redirect('accesoDenegado')
    return redirect('generos')

@login_required(login_url='/login')
def registroGeneros(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)
    

@login_required(login_url='/login')
def detalleGenero(request, id_genero):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "generos/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Genero"
        data['genero'] = Genero.objects.get(id_genero=id_genero)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarGenero(request, id_genero):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "generos/editar.html"
        data = dict()
        data['titulo'] = "Editar Generos"
        genero = Genero.objects.get(id_genero=id_genero)
        data['genero'] = genero

        if request.method == 'POST':
            if('activo' in request.POST):
                genero.is_active = 1
            else:
                genero.is_active = 0
            if(request.POST['nombre'].strip(" ") != ''):
                genero.nombre_genero = request.POST['nombre']
                genero.save()
                return redirect('generos')
            else:
                data['toast'] = "Error"
                data['mensaje'] = "genero no registrada, debe rellenar los campos obligatorios"
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def movimientos(request): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "movimientos/lista.html"
        data = dict()
        data['titulo'] = "Movimientos Registrados"
        data['movimientos'] = Movimiento.objects.all()
        if(request.method == "POST"):
            if(request.POST['tipo'] == 'Filtrar'):
                if(request.POST['fecha_inicio'].strip(" ") != ''):
                    fecha_inicio = request.POST['fecha_inicio']
                if(request.POST['fecha_fin'].strip(" ") != ''):
                    fecha_fin = request.POST['fecha_fin']
                if(request.POST['fecha_fin'].strip(" ") != '' and request.POST['fecha_inicio'].strip(" ") != ''):
                    data['movimientos'] = Movimiento.objects.filter(fecha_solicitud__range=[fecha_inicio, fecha_fin])
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def registroMovimientos(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
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
            elif(not request.user.is_authenticated):
                data['toast'] = "Error"
                data['mensaje'] = "Movimiento no registrada, Debe iniciar sesi??n para registrar movimiento"
            else:
                movimiento.id = request.user
                movimiento.estado = "Solicitando"
                movimiento.fecha_solicitud = datetime.now()
                movimiento.save()
                return redirect('movimientos')

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def agregarPublicacionMovimiento(request, id_movimiento):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "movimientos/agregar.html"
        data = dict()
        data['titulo'] = "Agregar publicacions a movimiento"
        movimiento = Movimiento.objects.get(id_movimiento = id_movimiento)

        if request.method == 'POST':
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
                data['mensaje'] = "No puede agregar m??s publicaciones de las que se encuentran en stock"
            else:
                movimiento.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad})
                publicacionEnBodega.cantidad -= cantidad
                publicacionEnBodega.save()

        data['movimiento'] = movimiento
        data['publicaciones'] = Publicacion_Bodega.objects.filter(id_bodega = request.user.id_bodega)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)
    
@login_required(login_url='/login')
def detalleMovimiento(request, id_movimiento):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "movimientos/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Movimiento"
        data['movimiento'] = Movimiento.objects.get(id_movimiento=id_movimiento)
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarMovimiento(request, id_movimiento):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "movimientos/editar.html"
        data = dict()
        data['titulo'] = "Editar Movimiento"
        movimiento = Movimiento.objects.get(id_movimiento = id_movimiento)

        if request.method == 'POST':
            if(movimiento.estado == "Solicitando"):
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
                    data['mensaje'] = "No puede agregar m??s publicaciones de las que se encuentran en stock"
                else:
                    movimiento.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad})
                    publicacionEnBodega.cantidad -= cantidad
                    publicacionEnBodega.save()

        data['movimiento'] = movimiento
        data['publicaciones'] = Publicacion_Bodega.objects.filter(id_bodega = request.user.id_bodega)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarEstadoMovimiento(request, id_movimiento):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        movimiento = Movimiento.objects.get(id_movimiento = id_movimiento)
        print(len(movimiento.publicacion_movimiento_set.all()))
        bodega = movimiento.id_bodega_destino
        if(movimiento.estado=="Solicitando" and len(movimiento.publicacion_movimiento_set.all()) > 0):
            movimiento.estado = "Pendiente"
        elif(movimiento.estado=="Pendiente"):
            movimiento.estado = "Enviado"
        elif(movimiento.estado=="Enviado"):
            movimiento.estado = "Entregado"
            movimiento.fecha_realizado = datetime.now()
            for publicacion in movimiento.publicacion_movimiento_set.all():
                try:
                    publicacionBodega = Publicacion_Bodega.objects.get(id_bodega=bodega, id_publicacion=publicacion.id_publicacion)
                    publicacionBodega.cantidad += publicacion.cantidad
                    publicacionBodega.save()
                except:
                    publicacionBodega = Publicacion_Bodega(id_bodega=bodega, id_publicacion=publicacion.id_publicacion, cantidad=publicacion.cantidad)
                    publicacionBodega.save()
        movimiento.save()

    else:
        return redirect('accesoDenegado')

    return redirect('detalleMovimiento', id_movimiento)

@login_required(login_url='/login')
def informeMovimiento(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        print(request.POST)
    else:
        return redirect('accesoDenegado')
    return redirect('movimientos')

@login_required(login_url='/login')
def editoriales(request): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "editoriales/lista.html"
        data = dict()
        data['titulo'] = "Editoriales Registrados"
        data['editoriales'] = Editorial.objects.all()
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoEditorial(request, id_editorial):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        editorial = Editorial.objects.get(id_editorial=id_editorial)
        if(editorial.is_active == 0):
            editorial.is_active = 1
        elif(editorial.is_active == 1):
            editorial.is_active = 0
        editorial.save()
    else:
        return redirect('accesoDenegado')
    return redirect('editoriales')

@login_required(login_url='/login')
def registroEditoriales(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def detalleEditorial(request, id_editorial):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
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

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarEditorial(request, id_editorial):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
            if('activo' in request.POST):
                editorial.is_active = 1
            else:
                editorial.is_active = 0
            if(request.POST['nombre'].strip(" ") != ''):
                editorial.nombre_editorial = request.POST['nombre']
                editorial.save()
                return redirect('editoriales')
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Editorial no modificada, debe rellenar los campos obligatorios"

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def registroPersonas(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "personas/registro.html"
        data = dict()
        data['titulo'] = "Registro Personas"
        if(request.GET.get('next') is not None and request.GET.get('rut') is not None):
            redirect_to = request.GET.get('next')
            data['redirect_to'] = redirect_to
        else:
            redirect_to = '/personas'

        if(request.GET.get('rut') is not None):
            rut = request.GET.get('rut')
            redirect_to=redirect_to+"?rut="+rut
            data['rut'] = rut
        
        print(redirect_to)

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
                return redirect(redirect_to)
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Persona no registrada, debe rellenar los campos obligatorios"
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def listaPersonas(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "personas/lista.html"
        
        data = dict()
        data['titulo'] = "Lista Personas"
        data['personas'] = Persona.objects.all()

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoPersona(request, id_persona):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        persona = Persona.objects.get(id_persona=id_persona)
        if(persona.is_active == 0):
            persona.is_active = 1
        elif(persona.is_active == 1):
            persona.is_active = 0
        persona.save()
    else:
        return redirect('accesoDenegado')
    return redirect('listaPersonas')

@login_required(login_url='/login')
def detallePersonas(request, id_persona):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "personas/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Personas"
        data['persona'] = Persona.objects.get(id_persona=id_persona)
        data['compras'] = Compra.objects.filter(id_persona=id_persona)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarPersonas(request, id_persona):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
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
            if('activo' in request.POST):
                persona.is_active = 1
            else:
                persona.is_active = 0
            if(persona.nombres != '' and persona.rut != ''):
                persona.save()
                return redirect('listaPersonas')
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Persona no registrada, debe rellenar los campos obligatorios"

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

def seed(request):
    seedTables()
    return redirect('index')

def loginPerfil(request):
    template = "perfil/login.html"

    data = dict()

    data['titulo'] = "Inicio de sesion"

    if(request.GET.get('next') is not None):
        redirect_to = request.GET.get('next')
    else:
        redirect_to = '/productos'

    # if(request.user):
    #     return redirect('/productos')
    
    data['redirect_to'] = redirect_to

    if(request.method == "POST"):
        nombre = request.POST['username']
        contrase??a = request.POST['password']
        user = authenticate(username=nombre, password=contrase??a)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect(redirect_to)
        else:
            data['toast'] = "Error"
            data['mensaje'] = "Usuario o contrase??a incorrectos"


    return render(request, template, data)    

@login_required(login_url='/login')
def logoutPerfil(request):
    data = dict()

    data['titulo'] = "Cerrar sesion"
    
    if(request.user.is_authenticated):
        logout(request)
    return redirect('index')

def accesoDenegado(request):
    template = "perfil/accesoDenegado.html"
    data = dict()

    data['titulo'] = "Acceso Denegado"
    
    return render(request, template, data)

@login_required(login_url='/login')
def perfiles(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "perfil/lista.html"

        data = dict()
        data['titulo'] = "Lista de perfiles"
        data['perfiles'] = Perfil.objects.all()
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def detallePerfiles(request, perfil_id):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "perfil/detalle.html"

        data = dict()
        data['titulo'] = "detalle perfil"
        data['perfil'] = Perfil.objects.get(id=perfil_id)
        data['movimientos'] = Movimiento.objects.filter(id=perfil_id)
        data['pedidos'] = Pedido.objects.filter(id=perfil_id)
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarPerfil(request, id_perfil):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def registroPerfil(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
            
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def preregistroPerfil(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "perfil/preregistro.html"

        data = dict()
        data['titulo'] = "Registro perfil"

    else:
        return redirect('accesoDenegado')
        
    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoPerfil(request, id_perfil):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        perfil = Perfil.objects.get(id=id_perfil)
        if(perfil.is_active == 0):
            perfil.is_active = 1
        elif(perfil.is_active == 1):
            perfil.is_active = 0
        print(perfil.is_active)
        perfil.save()
    else:
        return redirect('accesoDenegado')
    return redirect('perfiles')



@login_required(login_url='/login')
def bodegas(request): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "bodegas/lista.html"
        data = dict()
        data['titulo'] = "Bodegas Registrados"
        data['bodegas'] = Bodega.objects.all()
        return render(request, template, data)

    else:
        return redirect('accesoDenegado')

@login_required(login_url='/login')
def cambiarEstadoBodega(request, id_bodega):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        bodega = Bodega.objects.get(id_bodega=id_bodega)
        if(bodega.is_active == 0):
            bodega.is_active = 1
        elif(bodega.is_active == 1):
            bodega.is_active = 0
        bodega.save()
    else:
        return redirect('accesoDenegado')
    return redirect('bodegas')

@login_required(login_url='/login')
def detalleBodegas(request, id_bodega): 
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "bodegas/detalle.html"
        data = dict()
        data['titulo'] = "Detalle Bodegas"
        data['bodega'] = Bodega.objects.get(id_bodega=id_bodega)
        data['productos'] = Bodega.objects.filter(id_bodega=id_bodega)
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def registroBodegas(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "bodegas/registro.html"
        data = dict()
        data['titulo'] = "Registro bodegas"

        if request.method == "POST":
            bodega = Bodega()
            if(request.POST['nombre'].strip(" ") != ''):
                bodega.nombre_bodega = request.POST['nombre']
            if(request.POST['direccion'].strip(" ") != ''):
                bodega.direccion = request.POST['direccion']
            if(request.POST['comuna'].strip(" ") != ''):
                bodega.comuna = request.POST['comuna']
            if(request.POST['telefono'].strip(" ") != ''):
                bodega.telefono_bodega = request.POST['telefono']
            if(request.POST['direccion'].strip(" ") != '' and request.POST['comuna'].strip(" ") != '' and request.POST['telefono'].strip(" ") != '' and request.POST['nombre'].strip(" ") != ''):
                bodega.save()
                return redirect('detalleBodegas', bodega.id_bodega)
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Bodega no registrada, Debe rellenar los campos obligatorios"
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarBodegas(request, id_bodega):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
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
            if("activo" in request.POST):
                bodega.is_active = 1
            else:
                bodega.is_active = 0
            if(request.POST['direccion'].strip(" ") != '' and request.POST['comuna'].strip(" ") != '' and request.POST['telefono'].strip(" ") != '' and request.POST['nombre'].strip(" ") != ''):
                bodega.save()
                return redirect('detalleBodegas', id_bodega)
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Bodega no actualizada, Debe rellenar los campos obligatorios"
    else:
        return redirect('accesoDenegado')
            

    return render(request, template, data)

@login_required(login_url='/login')
def listaCompras(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "compras/lista.html"
        data = dict()
        data['titulo'] = "Lista Compras"
        data['compras']= Compra.objects.all()
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarEstadoCompra(request, id_compra):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        compra = Compra.objects.get(id_compra = id_compra)
        bodega = compra.id_bodega
        if(compra.estado=="Pendiente" and len(compra.publicacion_compra_set.all()) > 0):
            compra.estado = "Finalizada"
            for publicacion in compra.publicacion_compra_set.all():
                publicacionBodega = Publicacion_Bodega.objects.get(id_bodega=bodega, id_publicacion=publicacion.id_publicacion)
                publicacionBodega.cantidad -= publicacion.cantidad
                publicacionBodega.save()
        compra.save()

    else:
        return redirect('accesoDenegado')

    return redirect('detalleCompras', id_compra)

@login_required(login_url='/login')
def registroCompras(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "compras/registro.html"
        data = dict()
        data['titulo'] = "Registro Compras"

        if(request.GET.get('rut') is not None):
            rut = request.GET.get('rut')
            data['rut'] = rut

        if request.method == 'POST':
            print(request.user.is_authenticated)
            compra = Compra()
            if(request.POST['rut_cliente'].strip(" ") != ''):
                try:
                    id_cliente = Persona.objects.get(rut=request.POST['rut_cliente'])
                    compra.id_persona = id_cliente
                except:
                    return redirect('/personas/registro?next='+request.path+'&rut='+request.POST['rut_cliente'])
            if(request.POST['metodo_pago'].strip(" ") != ''):
                compra.id_bodega = request.user.id_bodega
                compra.total = 0
                compra.fecha_compra = datetime.now()
                compra.estado = "Pendiente"
                compra.metodo_pago = request.POST['metodo_pago']
                # print(compra.metodo_pago)
                compra.save()
                return redirect('editarCompras', compra.id_compra)
            if(request.POST['metodo_pago'].strip(" ") == ''):
                data['toast'] = "Error"
                data['mensaje'] = "Movimiento no registrada, debe rellenar los campos obligatorios"
            # elif(movimiento.id_bodega_origen == movimiento.id_bodega_destino):
            #     data['toast'] = "Error"
            #     data['mensaje'] = "Movimiento no registrada, La bodega de origen debe ser distinta a la bodega de destino"
            # elif(not request.user.is_authenticated):
            #     data['toast'] = "Error"
            #     data['mensaje'] = "Movimiento no registrada, Debe iniciar sesi??n para registrar movimiento"
            # else:
            #     movimiento.id = request.user
            #     movimiento.estado = "Solicitando"
            #     movimiento.fecha_solicitud = datetime.now()
                # movimiento.save()
                # return redirect('compras')

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def detalleCompras(request, id_compra):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "compras/detalle.html"
        data = dict()
        data['titulo'] = "Detalle Compras"
        #data['Persona'] = Persona.objects.get(id_persona=id_persona)
        data['compra'] = Compra.objects.get(id_compra=id_compra)
        #data['Fecha Compra'] = Compra.objects.filter(id_compra=id_compra)
        #data['Metodo Pago'] = Compra.objects.get(id_compra=id_compra)
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarCompras(request, id_compra):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "compras/editar.html"
        data = dict()
        data['titulo'] = "Editar Compra"
        compra = Compra.objects.get(id_compra = id_compra)

        if request.method == 'POST':
            if(compra.estado == "Pendiente"):
                if(request.POST['publicacion'].strip(" ") != ''):
                    publicacion = Publicacion.objects.get(id_publicacion=int(request.POST['publicacion']))
                    publicacionEnBodega = Publicacion_Bodega.objects.get(id_publicacion=int(request.POST['publicacion']), id_bodega=compra.id_bodega.id_bodega)
                if(request.POST['cantidad'].strip(" ") != ''):
                    cantidad = int(request.POST['cantidad'])
                if(request.POST['publicacion'].strip(" ") == '' or request.POST['cantidad'].strip(" ") == ''):
                    data['toast'] = "Error"
                    data['mensaje'] = "Publicacion no registrada, Debe rellenar todos los campos"
                elif(publicacion in compra.publicaciones.all()):
                    data['toast'] = "Error"
                    data['mensaje'] = "Publicacion ya agregada a la compra"
                elif (cantidad > publicacionEnBodega.cantidad):
                    data['toast'] = "Error"
                    data['mensaje'] = "No puede agregar m??s publicaciones de las que se encuentran en stock"
                else:
                    compra.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad, "precio": publicacion.precio})
                    compra.total = publicacion.precio * cantidad
                    compra.save()
                    # publicacionEnBodega.cantidad -= cantidad
                    publicacionEnBodega.save()

        data['compra'] = compra
        data['publicaciones'] = Publicacion_Bodega.objects.filter(id_bodega = request.user.id_bodega)

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

# def editarCompras(request, id_compra):
#     template = "compras/editar.html"
#     data = dict()
#     data['titulo'] = "Editar publicaciones a compras"
#     compra = Compra.objects.get(id_compra = id_compra)

#     if request.method == 'POST':
#         print(request.POST['publicacion'])
#         if(request.POST['publicacion'].strip(" ") != ''):
#             publicacion = Publicacion.objects.get(id_publicacion=int(request.POST['publicacion']))
#             publicacionEnBodega = Publicacion_Bodega.objects.get(id_publicacion=int(request.POST['publicacion']), id_compra=compra.id_compra_origen.id_compra)
#         if(request.POST['cantidad'].strip(" ") != ''):
#             cantidad = int(request.POST['cantidad'])
#         if(request.POST['publicacion'].strip(" ") == '' or request.POST['cantidad'].strip(" ") == ''):
#             data['toast'] = "Error"
#             data['mensaje'] = "Publicacion no registrada, Debe rellenar todos los campos"
#         elif(publicacion in compra.publicaciones.all()):
#             data['toast'] = "Error"
#             data['mensaje'] = "Publicacion ya agregada al movimiento"
#         elif (cantidad > publicacionEnBodega.cantidad):
#             data['toast'] = "Error"
#             data['mensaje'] = "No puede agregar m??s publicaciones de las que se encuentran en stock"
#         else:
#             compra.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad})
#             publicacionEnBodega.cantidad -= cantidad
#             publicacionEnBodega.save()

#     data['compra'] = compra
#     data['publicaciones'] = Publicacion_Compra.objects.filter(id_compra=id_compra)

#     return render(request, template, data)

@login_required(login_url='/login')
def registroProveedores(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "proveedores/registro.html"

        data = dict()

        data['titulo'] = "Registro Proveedores"

        if request.method == 'POST':
            proveedor = Proveedor()
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.nombre_proveedor = request.POST['nombreP']
            if(request.POST['direccionP'].strip(" ") != ''):
                proveedor.direccion_proveedor = request.POST['direccionP']
            if(request.POST['comunaP'].strip(" ") != ''):
                proveedor.comuna_proveedor = request.POST['comunaP']
            if(request.POST['correoP'].strip(" ") != ''):
                proveedor.correo_proveedor = request.POST['correoP']
            if(request.POST['telefonoP'].strip(" ") != ''):
                proveedor.telefono_proveedor = request.POST['telefonoP']
            if(request.POST['nombreP'].strip(" ") != '' and request.POST['direccionP'].strip(" ") != '' and request.POST['comunaP'].strip(" ") != '' and request.POST['correoP'].strip(" ") != '' and request.POST['telefonoP'].strip(" ") != ''):
                proveedor.save()
                return redirect('detalleProveedores', proveedor.id_proveedor)
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Proveedor no registrado, Debe rellenar los campos obligatorios"
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def proveedores(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "proveedores/historial.html"
        data = dict()

        data['titulo'] = "Lista Proveedores"

        
        data['proveedores'] = Proveedor.objects.all()
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)

@login_required(login_url='/login')
def cambiarEstadoProveedor(request, id_proveedor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
        if(proveedor.is_active == 0):
            proveedor.is_active = 1
        elif(proveedor.is_active == 1):
            proveedor.is_active = 0
        proveedor.save()
    else:
        return redirect('accesoDenegado')
    return redirect('proveedores')

@login_required(login_url='/login')
def detalleProveedores(request,id_proveedor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "proveedores/detalle.html"
        data = dict()
        data['titulo'] = "Detalle Proveedor"
        data['proveedor'] = Proveedor.objects.get(id_proveedor=id_proveedor)
    else:
        return redirect('accesoDenegado')

    return render(request,template,data)

@login_required(login_url='/login')
def editarProveedor(request, id_proveedor):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega"):
        template = "proveedores/editar.html"
        
        data = dict()
        data['titulo'] = "Editar Proveedor"
        proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
        data['proveedor'] = proveedor

        if request.method == 'POST':
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.nombre_proveedor= request.POST['nombreP']
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.direccion_proveedor= request.POST['direccionP']
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.comuna_proveedor=    request.POST['comunaP']
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.correo_proveedor=    request.POST['correoP']
            if(request.POST['nombreP'].strip(" ") != ''):
                proveedor.telefono_proveedor=  request.POST['telefonoP']
            if("activo" in request.POST):
                proveedor.is_active = 1
            else:
                proveedor.is_active = 0
            if(request.POST['nombreP'].strip(" ") != '' and request.POST['direccionP'].strip(" ") != '' and request.POST['comunaP'].strip(" ") != '' and request.POST['correoP'].strip(" ") != '' and request.POST['telefonoP'].strip(" ") != ''):
                proveedor.save()
                return redirect('detalleProveedores', proveedor.id_proveedor)
            else:
                data['toast'] = "Error"
                data['mensaje'] = "Proveedor no registrado, Debe rellenar los campos obligatorios"
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def pedidos(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "pedidos/lista.html"
        data = dict()

        data['titulo'] = "Lista Pedidos"

        
        data['pedidos'] = Pedido.objects.all()
    else:
        return redirect('accesoDenegado')
    return render(request, template, data)
    
@login_required(login_url='/login')
def registroPedidos(request):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "pedidos/registro.html"
        data = dict()
        data['titulo'] = "Registro Pedidos"
        data['proveedores'] = Proveedor.objects.all()

        if request.method == 'POST':
            print(request.user.is_authenticated)
            pedido = Pedido()
            if(request.POST['id_proveedor'].strip(" ") != ''):
                pedido.id_proveedor = Proveedor.objects.get(id_proveedor = int(request.POST['id_proveedor']))
                pedido.id = request.user
                pedido.id_bodega = request.user.id_bodega
                pedido.fecha_pedido = datetime.now()
                pedido.total_pedido = 0
                pedido.estado = "Pendiente"
                pedido.save()
                return redirect('editarPedidos', pedido.id_pedido)
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def detallePedidos(request, id_pedido):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "pedidos/detalle.html"
        
        data = dict()
        data['titulo'] = "Detalle Pedidos"
        data['pedido'] = Pedido.objects.get(id_pedido=id_pedido)
    
    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarPedidos(request, id_pedido):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        template = "pedidos/editar.html"
        data = dict()
        data['titulo'] = "Editar Pedidos"
        pedido = Pedido.objects.get(id_pedido = id_pedido)

        if request.method == 'POST':
            if(pedido.estado == "Pendiente"):
                if(request.POST['publicacion'].strip(" ") != ''):
                    publicacion = Publicacion.objects.get(id_publicacion=int(request.POST['publicacion']))
                    publicacionEnBodega = Publicacion_Bodega.objects.get_or_create(id_publicacion=publicacion, id_bodega=pedido.id_bodega)
                    publicacionEnBodega = publicacionEnBodega[0]
                        
                if(request.POST['cantidad'].strip(" ") != ''):
                    cantidad = int(request.POST['cantidad'])
                if(request.POST['publicacion'].strip(" ") == '' or request.POST['cantidad'].strip(" ") == ''):
                    data['toast'] = "Error"
                    data['mensaje'] = "Publicacion no registrada, Debe rellenar todos los campos"
                elif(publicacion in pedido.publicaciones.all()):
                    data['toast'] = "Error"
                    data['mensaje'] = "Publicacion ya agregada al movimiento"
                else:
                    print(publicacionEnBodega)
                    pedido.publicaciones.add(publicacion, through_defaults = {"cantidad": cantidad})
                    publicacionEnBodega.cantidad += cantidad
                    publicacionEnBodega.save()

        data['pedido'] = pedido
        data['publicaciones'] = Publicacion.objects.all()

    else:
        return redirect('accesoDenegado')

    return render(request, template, data)

@login_required(login_url='/login')
def editarEstadoPedido(request, id_pedido):
    if(request.user.tipo_usuario == "Administrador" or request.user.tipo_usuario == "Jefe de bodega" or request.user.tipo_usuario == "Bodeguero"):
        pedido = Pedido.objects.get(id_pedido = id_pedido)
        bodega = pedido.id_bodega
        if(pedido.estado=="Pendiente" and len(pedido.publicacion_pedido_set.all()) > 0):
            pedido.estado = "Finalizado"
            for publicacion in pedido.publicacion_pedido_set.all():
                publicacionBodega = Publicacion_Bodega.objects.get(id_bodega=bodega, id_publicacion=publicacion.id_publicacion)
                publicacionBodega.cantidad -= publicacion.cantidad
                publicacionBodega.save()
        pedido.save()

    else:
        return redirect('accesoDenegado')

    return redirect('detallePedidos', id_pedido)