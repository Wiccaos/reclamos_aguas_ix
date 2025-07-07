ALTER USER 'root'@'localhost' IDENTIFIED BY 'Inacap.2030';
FLUSH PRIVILEGES;

CREATE DATABASE aguas_araucania;

CREATE USER 'admin_aguas'@'localhost' IDENTIFIED BY 'Aguas123';
GRANT ALL ON aguas_araucania.* TO 'admin_aguas'@'localhost';

-- Clientes
CREATE TABLE aguas_araucania.clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    direccion VARCHAR(100) NOT NULL
);

INSERT INTO aguas_araucania.clientes (nombre, correo, direccion) VALUES
('Ana López', 'ana.lopez@email.com', 'Calle Falsa 123'),
('Pedro Martínez', 'pedro.martinez@email.com', 'Av. Siempre Viva 456'),
('Lucía Rojas','lucia.rojas@email.com', 'Calle Real 789');

-- Soporte
CREATE TABLE aguas_araucania.soporte(
    id_sup INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    direccion VARCHAR(100) NOT NULL
);

INSERT INTO aguas_araucania.soporte (nombre, correo, direccion) VALUES
('Juan Pérez', 'juan.perez@aguasaraucania.cl', 'Calle del Agua 100'),
('María González', 'maria.gonzalez@aguasaraucania.cl', 'Av. del Río 200'),
('Carlos Muñoz', 'carlos.munoz@aguasaraucania.cl', 'Calle del Sol 300');

-- Reclamos
CREATE TABLE aguas_araucania.reclamos(
    id_reclamo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES aguas_araucania.clientes(id_cliente)
);

INSERT INTO aguas_araucania.reclamos (id_cliente, titulo, descripcion) VALUES
(1, 'Fuga en calle principal', 'Hay una fuga de agua en Av. Principal frente al número 200'),
(2, 'Factura con monto incorrecto', 'La última factura viene con un monto 50% mayor al consumo real'),
(3, 'Agua con mal olor', 'El agua que llega a mi domicilio tiene un olor desagradable');

-- Respuestas
CREATE TABLE aguas_araucania.respuestas(
    id_resp INT AUTO_INCREMENT PRIMARY KEY,
    reclamo_id INT NOT NULL,
    soporte_id INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    contenido TEXT NOT NULL,
    FOREIGN KEY (reclamo_id) REFERENCES aguas_araucania.reclamos(id_reclamo),
    FOREIGN KEY (soporte_id) REFERENCES aguas_araucania.soporte(id_sup)
);

INSERT INTO aguas_araucania.respuestas (reclamo_id, soporte_id, contenido) VALUES
(1, 1, 'Hemos registrado su reclamo y lo hemos asignado a nuestro equipo técnico. Un especialista visitará el lugar en las próximas 48 horas.'),
(1, 1, 'Se ha programado visita técnica para el día 2023-06-20 entre 10:00 y 14:00 hrs.'),
(2, 2, 'Hemos verificado su factura y efectivamente existe un error. Se generará una factura rectificativa en los próximos días.');