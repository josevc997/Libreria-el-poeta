CREATE DATABASE libreria;

USE libreria;

CREATE TABLE autor (
    id_autor INTEGER NOT NULL AUTO_INCREMENT,
    nombres_autor VARCHAR(150),
    apellidos_autor VARCHAR(150),
    correo_autor VARCHAR(150),
    nacionalidad_autor VARCHAR(150),
    pseudonimo_autor VARCHAR(150) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_autor)
);

CREATE TABLE genero (
    id_genero INTEGER NOT NULL AUTO_INCREMENT,
    nombre_genero VARCHAR(150) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_genero)
);

CREATE TABLE editorial (
    id_editorial INTEGER NOT NULL AUTO_INCREMENT,
    nombre_editorial VARCHAR(150) NOT NULL,
    correo_editorial VARCHAR(150),
    telefono_editorial VARCHAR(150),
    direccion_editorial VARCHAR(150),
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_editorial)
);

CREATE TABLE publicacion (
    id_publicacion INTEGER NOT NULL AUTO_INCREMENT,
    id_editorial INTEGER NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    resumen Text,
    tipo_producto VARCHAR(150) NOT NULL,
    edicion VARCHAR(150),
    fecha_publicacion VARCHAR(150),
    isbn VARCHAR(150),
    numero_serie INTEGER,
    precio INTEGER,
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_publicacion),
    FOREIGN KEY (id_editorial) REFERENCES editorial(id_editorial)
);

CREATE TABLE genero_publicacion (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_publicacion INTEGER NOT NULL,
    id_genero INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion)
);

CREATE TABLE autor_publicacion (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_autor INTEGER NOT NULL,
    id_publicacion INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_autor) REFERENCES autor(id_autor),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion)
);

CREATE TABLE bodega (
    id_bodega INTEGER NOT NULL AUTO_INCREMENT,
    nombre_bodega VARCHAR(150),
    direccion VARCHAR(150),
    comuna VARCHAR(150),
    telefono_bodega VARCHAR(150),
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_bodega)
);

CREATE TABLE publicacion_bodega (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_bodega INTEGER NOT NULL,
    id_publicacion INTEGER NOT NULL,
    cantidad INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion),
    FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega)
);

CREATE TABLE persona (
    id_persona INTEGER NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(150) NOT NULL,
    apellidos VARCHAR(150),
    rut VARCHAR(150) NOT NULL,
    direccion VARCHAR(150),
    correo VARCHAR(150),
    telefono VARCHAR(150),
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_persona)
);

CREATE TABLE perfil (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_persona INTEGER NOT NULL,
    id_bodega INTEGER NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    `password` varchar(150) NOT NULL,
    last_login datetime(6) DEFAULT NULL,
    is_superuser tinyint(1) NOT NULL,
    first_name varchar(150) NOT NULL,
    last_name varchar(150) NOT NULL,
    email varchar(150) NOT NULL,
    is_staff tinyint(1) NOT NULL,
    is_active tinyint(1) NOT NULL DEFAULT 1,
    date_joined datetime(6) NOT NULL,
    tipo_usuario VARCHAR(150) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
    FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega)
);

CREATE TABLE proveedor (
    id_proveedor INTEGER NOT NULL AUTO_INCREMENT,
    nombre_proveedor VARCHAR(150),
    direccion_proveedor VARCHAR(150),
    comuna_proveedor VARCHAR(150),
    correo_proveedor VARCHAR(150),
    telefono_proveedor VARCHAR(150),
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_proveedor)
);

CREATE TABLE pedido (
    id_pedido INTEGER NOT NULL AUTO_INCREMENT,
    id INTEGER NOT NULL,
    id_bodega INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    fecha_pedido VARCHAR(150),
    total_pedido VARCHAR(150),
    estado VARCHAR(150),
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id) REFERENCES perfil(id),
    FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);

CREATE TABLE publicacion_pedido (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_publicacion INTEGER NOT NULL,
    id_pedido INTEGER NOT NULL,
    cantidad INTEGER,
    precio_proveedor INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion)
);

CREATE TABLE compra (
    id_compra INTEGER AUTO_INCREMENT NOT NULL,
    id_bodega INTEGER NOT NULL,
    id_persona INTEGER NOT NULL,
    total INTEGER,
    metodo_pago VARCHAR(150),
    fecha_compra VARCHAR(150),
    estado VARCHAR(150),
    PRIMARY KEY (id_compra),
    FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE publicacion_compra (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_publicacion INTEGER NOT NULL,
    id_compra INTEGER NOT NULL,
    cantidad INTEGER,
    precio INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (id_compra) REFERENCES compra(id_compra),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion)
);

CREATE TABLE movimiento (
    id_movimiento INTEGER NOT NULL AUTO_INCREMENT,
    id INTEGER NOT NULL,
    id_bodega_origen INTEGER NOT NULL,
    id_bodega_destino INTEGER NOT NULL,
    fecha_solicitud VARCHAR(150),
    estado VARCHAR(150),
    fecha_realizado VARCHAR(150),
    PRIMARY KEY (id_movimiento),
    FOREIGN KEY (id) REFERENCES perfil(id),
    FOREIGN KEY (id_bodega_origen) REFERENCES bodega(id_bodega),
    FOREIGN KEY (id_bodega_destino) REFERENCES bodega(id_bodega)
);

CREATE TABLE publicacion_movimiento (
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_movimiento INTEGER NOT NULL,
    id_publicacion INTEGER NOT NULL,
    cantidad INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion),
    FOREIGN KEY (id_movimiento) REFERENCES movimiento(id_movimiento)
);