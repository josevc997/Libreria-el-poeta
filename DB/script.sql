CREATE DATABASE libreria;

USE libreria;

CREATE TABLE autor (
    id_autor INTEGER NOT NULL AUTO_INCREMENT,
    nombres_autor VARCHAR(30),
    apellidos_autor VARCHAR(30),
    correo_autor VARCHAR(30),
    nacionalidad_autor VARCHAR(30),
    pseudonimo_autor VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_autor)
);

CREATE TABLE genero (
    id_genero INTEGER NOT NULL AUTO_INCREMENT,
    nombre_genero VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_genero)
);

CREATE TABLE editorial (
    id_editorial INTEGER NOT NULL AUTO_INCREMENT,
    nombre_editorial VARCHAR(30) NOT NULL,
    correo_editorial VARCHAR(30),
    telefono_editorial VARCHAR(30),
    direccion_editorial VARCHAR(30),
    PRIMARY KEY (id_editorial)
);

CREATE TABLE publicacion (
    id_publicacion INTEGER NOT NULL AUTO_INCREMENT,
    id_editorial INTEGER NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    resumen Text,
    tipo_producto VARCHAR(30) NOT NULL,
    edicion VARCHAR(30),
    fecha_publicacion VARCHAR(30),
    isbn VARCHAR(30),
    numero_serie INTEGER,
    precio INTEGER,
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
    nombre_bodega VARCHAR(30),
    direccion VARCHAR(30),
    comuna VARCHAR(30),
    telefono_bodega VARCHAR(30),
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
    nombres VARCHAR(30) NOT NULL,
    apellidos VARCHAR(30),
    rut VARCHAR(30) NOT NULL,
    direccion VARCHAR(30),
    correo VARCHAR(30),
    telefono VARCHAR(30),
    PRIMARY KEY (id_persona)
);

CREATE TABLE perfil (
    id_perfil INTEGER NOT NULL AUTO_INCREMENT,
    id_persona INTEGER NOT NULL,
    id_bodega INTEGER NOT NULL,
    nombre_usuario VARCHAR(30) NOT NULL,
    clave VARCHAR(30),
    tipo_usuario VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_perfil),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
    FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega)
);

CREATE TABLE proveedor (
    id_proveedor INTEGER NOT NULL AUTO_INCREMENT,
    nombre_proveedor VARCHAR(30),
    direccion_proveedor VARCHAR(30),
    comuna_proveedor VARCHAR(30),
    correo_proveedor VARCHAR(30),
    telefono_proveedor VARCHAR(30),
    PRIMARY KEY (id_proveedor)
);

CREATE TABLE pedido (
    id_pedido INTEGER NOT NULL AUTO_INCREMENT,
    id_perfil INTEGER NOT NULL,
    id_bodega INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    fecha_pedido VARCHAR(30),
    total_pedido VARCHAR(30),
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_perfil) REFERENCES perfil(id_perfil),
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
    metodo_pago VARCHAR(30),
    fecha_compra VARCHAR(30),
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
    id_perfil INTEGER NOT NULL,
    id_bodega_origen INTEGER NOT NULL,
    id_bodega_destino INTEGER NOT NULL,
    fecha_solicitud VARCHAR(30),
    estado VARCHAR(30),
    fecha_realizado VARCHAR(30),
    PRIMARY KEY (id_movimiento),
    FOREIGN KEY (id_perfil) REFERENCES perfil(id_perfil),
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