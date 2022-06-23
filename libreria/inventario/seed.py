from .models import *
from datetime import datetime

def seedTables():
    autor = Autor()
    autor.nombres_autor = "Gabriel José"
    autor.apellidos_autor = "García Márquez"
    autor.correo_autor = "gabriel.marquez@gmail.com"
    autor.nacionalidad_autor = "Colombia"
    autor.pseudonimo_autor = "Gabriel García Márquez"
    autor.save()

    editorial = Editorial()
    editorial.nombre_editorial = "Literatura Random House"
    editorial.correo_editorial = "literaturarandomhouse@gmail.com"
    editorial.telefono_editorial = "227828200"
    editorial.direccion_editorial = "Av. Andrés Bello 2299, Oficina 801, Providencia, Chile"
    editorial.save()

    genero = Genero()
    genero.nombre_genero = "Realismo mágico"
    genero.save()


    publicacion = Publicacion()
    publicacion.id_editorial = editorial
    publicacion.nombre = "Cien años de soledad"
    publicacion.resumen = "En ocasión del 50 aniversario de la publicación de Cien años de soledad, llega una edición con ilustraciones inéditas de la artista chilena Luisa Rivera y con una tipografía creada por el hijo del autor, Gonzalo García Barcha. Una edición conmemorativa de una novela clave en la historia de la literatura, una obra que todos deberíamos tener en nuestras estanterías.   «Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.»   Con esta cita comienza una de las novelas más importantes del siglo XX y una de las aventuras literarias más fascinantes de todos los tiempos. Millones de ejemplares de Cien años de soledad leídos en todas las lenguas y el premio Nobel de Literatura coronando una obra que se había abierto paso «boca a boca» -como gustaba decir el escritor- son la más palpable demostración de que la aventura fabulosa de la familia Buendía-Iguarán, con sus milagros, fantasías, obsesiones, tragedias, incestos, adulterios, rebeldías, descubrimientos y condenas, representaba al mismo tiempo el mito y la historia, la tragedia y el amor del mundo entero.   El mejor homenaje a Gabo es leerlo.   Pablo Neruda dijo... «El Quijote de nuestro tiempo.»"
    publicacion.tipo_producto = "Libro"
    publicacion.edicion = "001"
    publicacion.fecha_publicacion = "2017"
    publicacion.isbn = "9788439732471"
    publicacion.numero_serie = "9788439732471"
    publicacion.precio = 36930
    publicacion.save()
    publicacion.autores.add(autor)
    publicacion.generos.add(genero)
    genero = Genero()
    genero.nombre_genero = "Saga familiar"
    genero.save()
    publicacion.generos.add(genero)
    genero = Genero()
    genero.nombre_genero = "Ficción épica"
    genero.save()
    publicacion.generos.add(genero)

    autor = Autor()
    autor.nombres_autor = "John Ronald"
    autor.apellidos_autor = "Reuel Tolkien"
    autor.correo_autor = "john.tolkien@gmail.com"
    autor.nacionalidad_autor = "Reino Unido"
    autor.pseudonimo_autor = "J. R. R. Tolkien"
    autor.save()

    editorial = Editorial()
    editorial.nombre_editorial = "Minotauro"
    editorial.correo_editorial = "infominotauro@planeta.es"
    editorial.telefono_editorial = "556677889"
    editorial.direccion_editorial = "Diagonal, 662-664 7ª planta 08034 Barcelona"
    editorial.save()

    genero = Genero()
    genero.nombre_genero = "Literatura fantástica"
    genero.save()

    publicacion = Publicacion()
    publicacion.id_editorial = editorial
    publicacion.nombre = "El Señor de los Anillos, 1. La Comunidad del Anillo"
    publicacion.resumen = "En la adormecida e idílica Comarca, un joven hobbit recibe un encargo: custodiar el Anillo Único y emprender el viaje para su destrucción en las Grietas del Destino. Consciente de la importancia de su misión, Frodo abandona la Comarca e inicia el camino hacia Mordor con la compañía de inesperada de Sam, Pippin y Merry.  Pero sólo con la ayuda de Aragorn conseguirán vencer a los Jinetes Negros y alcanzar el refugio de la Casa de Elrond en Rivendel."
    publicacion.tipo_producto = "Libro"
    publicacion.edicion = "2002"
    publicacion.fecha_publicacion = "2002"
    publicacion.isbn = "8445073729"
    publicacion.numero_serie = "9788445073728"
    publicacion.precio = 24210
    publicacion.save()
    publicacion.autores.add(autor)
    publicacion.generos.add(genero)
    genero = Genero()
    genero.nombre_genero = "Obra de referencia"
    genero.save()
    publicacion.generos.add(genero)


    bodega = Bodega()
    bodega.nombre_bodega =  "Sede Central"
    bodega.direccion = "Almirante Barroso 76"
    bodega.comuna = "Santiago Centro"
    bodega.telefono_bodega = "224723000"
    bodega.save()
    bodega.publicaciones.add(publicacion, through_defaults={ 'cantidad': 10 })

    persona = Persona()
    persona.nombres = "Armin"
    persona.apellidos = "Brün Rüth"
    persona.rut = "12312312-3"
    persona.direccion = "Calle falsa 123"
    persona.correo = "armin.brun@gmail.com"
    persona.telefono = "997403821"
    persona.save()

    perfil = Perfil()
    perfil.id_persona = persona
    perfil.id_bodega = bodega
    perfil.nombre_usuario = "brun12"
    perfil.set_password("clave123")
    perfil.is_superuser = 0
    perfil.first_name = "Armin"
    perfil.last_name = "Brün"
    perfil.email = "armin.brun@gmail.com"
    perfil.is_staff = 1
    perfil.is_active = 1
    perfil.date_joined = datetime.now()
    perfil.tipo_usuario = "Administrador"
    perfil.save()

    proveedor = Proveedor()
    proveedor.nombre_proveedor = "Proveedor Maximus"
    proveedor.direccion_proveedor = "Calle falsa 345"
    proveedor.comuna_proveedor = "Santiago Centro"
    proveedor.correo_proveedor = "maximus@gmail.com"
    proveedor.telefono_proveedor = "226489197"
    proveedor.save()

    pedido = Pedido()
    pedido.id = perfil
    pedido.id_bodega = bodega
    pedido.id_proveedor = proveedor
    pedido.fecha_pedido = "09/06/2022"
    pedido.total_pedido = publicacion.precio
    pedido.save()
    pedido.publicaciones.add(publicacion, through_defaults={ 'cantidad': 1, 'precio_proveedor': 15000 })

    compra = Compra()
    compra.id_bodega = bodega
    compra.id_persona = persona
    compra.total = publicacion.precio
    compra.metodo_pago = "Efectivo"
    compra.fecha_compra = "10/06/2022"
    compra.save()
    compra.publicaciones.add(publicacion, through_defaults = { 'cantidad': 1, 'precio': publicacion.precio})

    movimiento = Movimiento()
    movimiento.id = perfil
    movimiento.id_bodega_origen = bodega
    movimiento.id_bodega_destino = bodega
    movimiento.fecha_solicitud = "10/06/2022"
    movimiento.estado = "Pendiente"
    movimiento.fecha_realizado = "10/06/2022"
    movimiento.save()
    movimiento.publicaciones.add(publicacion, through_defaults = {"cantidad": 1})