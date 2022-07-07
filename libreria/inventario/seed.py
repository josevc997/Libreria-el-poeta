from .models import *
from datetime import datetime

def seedTables():
    autor0 = Autor()
    autor0.nombres_autor = "Gabriel José"
    autor0.apellidos_autor = "García Márquez"
    autor0.correo_autor = "gabriel.marquez@gmail.com"
    autor0.nacionalidad_autor = "Colombia"
    autor0.pseudonimo_autor = "Gabriel García Márquez"
    autor0.save()

    editorial = Editorial()
    editorial.nombre_editorial = "Literatura Random House"
    editorial.correo_editorial = "literaturarandomhouse@gmail.com"
    editorial.telefono_editorial = "227828200"
    editorial.direccion_editorial = "Av. Andrés Bello 2299, Oficina 801, Providencia, Chile"
    editorial.save()

    genero = Genero()
    genero.nombre_genero = "Realismo mágico"
    genero.save()

    publicacion0 = Publicacion()
    publicacion0.id_editorial = editorial
    publicacion0.nombre = "Cien años de soledad"
    publicacion0.resumen = "En ocasión del 50 aniversario de la publicación de Cien años de soledad, llega una edición con ilustraciones inéditas de la artista chilena Luisa Rivera y con una tipografía creada por el hijo del autor, Gonzalo García Barcha. Una edición conmemorativa de una novela clave en la historia de la literatura, una obra que todos deberíamos tener en nuestras estanterías.   «Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.»   Con esta cita comienza una de las novelas más importantes del siglo XX y una de las aventuras literarias más fascinantes de todos los tiempos. Millones de ejemplares de Cien años de soledad leídos en todas las lenguas y el premio Nobel de Literatura coronando una obra que se había abierto paso «boca a boca» -como gustaba decir el escritor- son la más palpable demostración de que la aventura fabulosa de la familia Buendía-Iguarán, con sus milagros, fantasías, obsesiones, tragedias, incestos, adulterios, rebeldías, descubrimientos y condenas, representaba al mismo tiempo el mito y la historia, la tragedia y el amor del mundo entero.   El mejor homenaje a Gabo es leerlo.   Pablo Neruda dijo... «El Quijote de nuestro tiempo.»"
    publicacion0.tipo_producto = "Libro"
    publicacion0.edicion = "001"
    publicacion0.fecha_publicacion = "2017"
    publicacion0.isbn = "9788439732471"
    publicacion0.numero_serie = "9788439732471"
    publicacion0.precio = 36930
    publicacion0.save()
    
    publicacion0.autores.add(autor0)
    publicacion0.generos.add(genero)

    genero = Genero()
    genero.nombre_genero = "Saga familiar"
    genero.save()

    publicacion0.generos.add(genero)

    genero = Genero()
    genero.nombre_genero = "Ficción épica"
    genero.save()

    publicacion0.generos.add(genero)

    autor = Autor()
    autor.nombres_autor = "John Ronald"
    autor.apellidos_autor = "Reuel Tolkien"
    autor.correo_autor = "john.tolkien@gmail.com"
    autor.nacionalidad_autor = "Reino Unido"
    autor.pseudonimo_autor = "J. R. R. Tolkien"
    autor.save()

    autor1 = Autor()
    autor1.nombres_autor = "Bruno Jesus"
    autor1.apellidos_autor = "Pozo Donoso"
    autor1.correo_autor = "bruno.pozo@gmail.com"
    autor1.nacionalidad_autor = "España"
    autor1.pseudonimo_autor = "B. P. R. Donoso"
    autor1.save()

    autor2 = Autor()
    autor2.nombres_autor = "Jose Andres"
    autor2.apellidos_autor = "Valencia Cerda"
    autor2.correo_autor = "jose.valencia@gmail.com"
    autor2.nacionalidad_autor = "Chile"
    autor2.pseudonimo_autor = "J. A. V. Cerda"
    autor2.save()

    autor3 = Autor()
    autor3.nombres_autor = "Pablo Esteban"
    autor3.apellidos_autor = "Cea Carrasco"
    autor3.correo_autor = "pablo.cea@gmail.com"
    autor3.nacionalidad_autor = "Argentina"
    autor3.pseudonimo_autor = "P. E. C. Carrasco"
    autor3.save()

    editorial = Editorial()
    editorial.nombre_editorial = "Minotauro"
    editorial.correo_editorial = "infominotauro@planeta.es"
    editorial.telefono_editorial = "556677889"
    editorial.direccion_editorial = "Diagonal, 662-664 7ª planta 08034 Barcelona"
    editorial.save()

    genero = Genero()
    genero.nombre_genero = "Literatura fantástica"
    genero.save()

    publicacion1 = Publicacion()
    publicacion1.id_editorial = editorial
    publicacion1.nombre = "El Señor de los Anillos, 1. La Comunidad del Anillo"
    publicacion1.resumen = "En la adormecida e idílica Comarca, un joven hobbit recibe un encargo: custodiar el Anillo Único y emprender el viaje para su destrucción en las Grietas del Destino. Consciente de la importancia de su misión, Frodo abandona la Comarca e inicia el camino hacia Mordor con la compañía de inesperada de Sam, Pippin y Merry.  Pero sólo con la ayuda de Aragorn conseguirán vencer a los Jinetes Negros y alcanzar el refugio de la Casa de Elrond en Rivendel."
    publicacion1.tipo_producto = "Libro"
    publicacion1.edicion = "2002"
    publicacion1.fecha_publicacion = "2002"
    publicacion1.isbn = "8445073729"
    publicacion1.numero_serie = "9788445073728"
    publicacion1.precio = 24210
    publicacion1.save()

    publicacion1.autores.add(autor)
    publicacion1.generos.add(genero)

    genero = Genero()
    genero.nombre_genero = "Obra de referencia"
    genero.save()
    publicacion1.generos.add(genero)

    publicacion3 = Publicacion()
    publicacion3.id_editorial = editorial
    publicacion3.nombre = "El Precio por Tenerla"
    publicacion3.resumen = "Natasha Rivas, es una mujer, joven, hermosa, decidida y una buena esposa. Se caso con un hombre de su misma clase social, de buena familia y según muchos el marido perfecto."
    publicacion3.tipo_producto = "Libro"
    publicacion3.edicion = "2022"
    publicacion3.fecha_publicacion = "2022"
    publicacion3.isbn = "8666321245"
    publicacion3.numero_serie = "67801234223"
    publicacion3.precio = 28210
    publicacion3.save()

    publicacion3.autores.add(autor1, autor2, autor3)
    publicacion3.generos.add(genero)
    
    genero = Genero()
    genero.nombre_genero = "Novela Romantica"
    genero.save()

    publicacion3.generos.add(genero)

    publicacion2 = Publicacion()
    publicacion2.id_editorial = editorial
    publicacion2.nombre = "El Bebé del Millonario"
    publicacion2.resumen = "Fueron las últimas palabras que el magnate turco le escuchó decir a su mujer antes de que ella abordara un avión y lo dejara con el pequeño bebé de nueve meses en sus brazos."
    publicacion2.tipo_producto = "Libro"
    publicacion2.edicion = "2020"
    publicacion2.fecha_publicacion = "2020"
    publicacion2.isbn = "7654321890"
    publicacion2.numero_serie = "82134076612"
    publicacion2.precio = 30000
    publicacion2.save()

    publicacion2.autores.add(autor1, autor0)
    publicacion2.generos.add(genero)

    genero = Genero()
    genero.nombre_genero = "Humor"
    genero.save()

    publicacion2.generos.add(genero)

    bodega = Bodega()
    bodega.nombre_bodega =  "Sede Central"
    bodega.direccion = "Almirante Barroso 76"
    bodega.comuna = "Santiago Centro"
    bodega.telefono_bodega = "224723000"
    bodega.save()

    bodega.publicaciones.add(publicacion0, through_defaults={ 'cantidad': 100 })
    bodega.publicaciones.add(publicacion2, through_defaults={ 'cantidad': 100 })

    bodega1 = Bodega()
    bodega1.nombre_bodega =  "El Poeta"
    bodega1.direccion = "Aurelio Diaz Meza"
    bodega1.comuna = "Recoleta"
    bodega1.telefono_bodega = "223004488"
    bodega1.save()
    bodega1.publicaciones.add(publicacion1, through_defaults={ 'cantidad': 296 })
    bodega1.publicaciones.add(publicacion3, through_defaults={ 'cantidad': 296 })

    bodega2 = Bodega()
    bodega2.nombre_bodega =  "Librerillo"
    bodega2.direccion = "Av. Providencia 2296"
    bodega2.comuna = "Providencia"
    bodega2.telefono_bodega = "930880360"
    bodega2.save()

    bodega2.publicaciones.add(publicacion2, through_defaults={ 'cantidad': 406 })
    bodega2.publicaciones.add(publicacion3, through_defaults={ 'cantidad': 406 })

    persona = Persona()
    persona.nombres = "Administrador"
    persona.apellidos = "Maximo"
    persona.rut = "12312312-3"
    persona.direccion = "Calle falsa 123"
    persona.correo = "armin.brun@gmail.com"
    persona.telefono = "997403821"
    persona.save()

    perfil = Perfil()
    perfil.id_persona = persona
    perfil.id_bodega = bodega
    perfil.username = "Administrador"
    perfil.set_password("adminJBP123")
    perfil.is_superuser = 0
    perfil.first_name = "Administrador"
    perfil.last_name = "Maximo"
    perfil.email = "admin@gmail.com"
    perfil.is_staff = 1
    perfil.is_active = 1
    perfil.date_joined = datetime.now()
    perfil.tipo_usuario = "Administrador"
    perfil.save()

    persona1 = Persona()
    persona1.nombres = "bodeguero"
    persona1.apellidos = "de prueba"
    persona1.rut = "32132132-1"
    persona1.direccion = "Calle falsa 123"
    persona1.correo = "bodeguero@gmail.com"
    persona1.telefono = "432312541"
    persona1.save()

    perfil1 = Perfil()
    perfil1.id_persona = persona1
    perfil1.id_bodega = bodega
    perfil1.username = "Bodeguero"
    perfil1.set_password("bodeguero321")
    perfil1.is_superuser = 0
    perfil1.first_name = "bodeguero"
    perfil1.last_name = "de prueba"
    perfil1.email = "bodeguero@gmail.com"
    perfil1.is_staff = 1
    perfil1.is_active = 1
    perfil1.date_joined = datetime.now()
    perfil1.tipo_usuario = "Bodeguero"
    perfil1.save()

    persona2 = Persona()
    persona2.nombres = "Jefebodega"
    persona2.apellidos = "Superior"
    persona2.rut = "54353454-3"
    persona2.direccion = "Calle falsa 423"
    persona2.correo = "jefe.bodega@gmail.com"
    persona2.telefono = "1235234432"
    persona2.save()

    perfil2 = Perfil()
    perfil2.id_persona = persona2
    perfil2.id_bodega = bodega
    perfil2.username = "Jefebodega"
    perfil2.set_password("bodeguero321")
    perfil2.is_superuser = 0
    perfil2.first_name = "Jefebodega"
    perfil2.last_name = "Superior"
    perfil2.email = "jefe.bodega@gmail.com"
    perfil2.is_staff = 1
    perfil2.is_active = 1
    perfil2.date_joined = datetime.now()
    perfil2.tipo_usuario = "Jefe de bodega"
    perfil2.save()

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
    pedido.fecha_pedido = datetime.now()
    pedido.total_pedido = publicacion0.precio
    pedido.estado = "Pendiente"
    pedido.save()

    pedido.publicaciones.add(publicacion0, through_defaults={ 'cantidad': 5, 'precio_proveedor': 15000 })

    compra = Compra()
    compra.id_bodega = bodega
    compra.id_persona = persona
    compra.total = publicacion0.precio
    compra.metodo_pago = "Efectivo"
    compra.fecha_compra = datetime.now()
    compra.estado = "Pendiente"
    compra.save()

    compra.publicaciones.add(publicacion0, through_defaults = { 'cantidad': 3, 'precio': publicacion0.precio})

    movimiento = Movimiento()
    movimiento.id = perfil
    movimiento.id_bodega_origen = bodega
    movimiento.id_bodega_destino = bodega
    movimiento.fecha_solicitud = datetime.now()
    movimiento.estado = "Pendiente"
    movimiento.fecha_realizado = datetime.now()
    movimiento.save()

    movimiento.publicaciones.add(publicacion0, through_defaults = {"cantidad": 15})