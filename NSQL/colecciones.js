// Para la base de datos MongoDB de Aguas Araucanía, se han creado las siguientes colecciones y documentos:
// encuestas, comentarios_redes, archivos_adjuntos

db.encuestas.insertMany([
  {
    "reclamo_id": 1012,
    "cliente_id": 45678,
    "fecha_respuesta": ISODate("2023-11-15T14:30:00Z"),
    "puntuacion": 4,
    "comentario": "El técnico resolvió la fuga rápidamente, pero llegó 1 hora tarde",
    "metrica_analisis": {
      "sentimiento": "positivo",
      "palabras_clave": ["técnico", "fuga", "rápido", "tarde"]
    }
  },
  {
    "reclamo_id": 1015,
    "cliente_id": 78901,
    "fecha_respuesta": ISODate("2023-11-16T09:15:00Z"),
    "puntuacion": 2,
    "comentario": "Sigo sin recibir la factura rectificada",
    "metrica_analisis": {
      "sentimiento": "negativo",
      "palabras_clave": ["factura", "rectificada", "demora"]
    }
  }
])

db.comentarios_redes.insertMany([
  {
    "plataforma": "Twitter",
    "usuario": "@usuario123",
    "fecha": ISODate("2023-11-10T18:45:00Z"),
    "contenido": "@AguasAraucania Hace 3 días reporté una fuga y nadie ha venido. ¡Pésimo servicio!",
    "cliente_id": 45678,
    "analisis_automatico": {
      "sentimiento": "negativo",
      "urgencia": "alta",
      "palabras_clave": ["fuga", "demora", "servicio"]
    }
  },
  {
    "plataforma": "Facebook",
    "usuario": "Juan Pérez",
    "fecha": ISODate("2023-11-12T10:20:00Z"),
    "contenido": "Gracias por resolver el problema de agua turbia en mi sector.",
    "cliente_id": null,
    "analisis_automatico": {
      "sentimiento": "positivo",
      "urgencia": "baja",
      "palabras_clave": ["agua turbia", "resolución"]
    }
  }
])

db.archivos_adjuntos.insertMany([
  {
    "reclamo_id": 1012,
    "tipo_archivo": "imagen",
    "nombre_archivo": "fuga_calle_principal.jpg",
    "ruta_almacenamiento": "/adjuntos/2023/11/fuga_1012.jpg",
    "fecha_subida": ISODate("2023-11-14T08:00:00Z"),
    "metadata": {
      "tamano_kb": 1200,
      "formato": "JPEG",
      "resolucion": "1920x1080"
    }
  },
  {
    "reclamo_id": 1015,
    "tipo_archivo": "pdf",
    "nombre_archivo": "factura_rectificada.pdf",
    "ruta_almacenamiento": "/adjuntos/2023/11/factura_1015.pdf",
    "fecha_subida": ISODate("2023-11-16T11:30:00Z"),
    "metadata": {
      "tamano_kb": 350,
      "paginas": 2,
      "protegido": true
    }
  }
])


db.createUser({
  user: "admin_aguas",
  pwd: "Aguas123",
  roles: [
    { role: "dbOwner", db: "aguas_araucania" },
    { role: "clusterMonitor", db: "admin" }
  ],
  mechanisms: ["SCRAM-SHA-256"]
});