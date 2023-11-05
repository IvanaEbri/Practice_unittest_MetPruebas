from peewee import *


sqlite_db = SqliteDatabase('./emergencias.db', pragmas={'journal_mode': 'wal'})
try:
    """Intento de conexion a la base de datos"""
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()

class BaseModel(Model):
    """Clase base para las entidades de la base"""
    class Meta:
        database = sqlite_db

class AreaEmergencia(BaseModel):
    """Entidad Areas de emergencia"""
    id_area = AutoField(primary_key = True)
    area = TextField(unique = True, null = False)
    
    def __str__(self):
        return self.area

    class Meta:
        db_table='area_emergencia'

class TipoEmergencia(BaseModel):
    """Entidad Tipos de emergencia"""
    id_tipo = AutoField(primary_key = True)
    tipo = TextField(unique = True, null = False)
    
    def __str__(self):
        return self.tipo

    class Meta:
        db_table='tipo_emergencia'

class RegistroEmergencias (BaseModel):
    """Entidad que recopila las emergencias notificadas"""
    id_emergencia = AutoField(primary_key = True)
    fecha_registro = DateTimeField(null=False)
    latitud = FloatField(null = False)
    longitud = FloatField(null = False)
    area_emergencia = ForeignKeyField(AreaEmergencia, backref= 'registro_emergencia')
    ref_ubicacion = TextField (null= True)
    tipo_emergencia =ForeignKeyField(TipoEmergencia, backref= 'registro_emergencia')
    foto = TextField (null=True)
    coment_emergencia = TextField(null= True)
    riesgo_vida = BooleanField(null=False)

    def riesgo_de_vida(self):
        if self.riesgo_vida == True:
            return "SI"
        else:
            return "NO"

    def __str__(self):
        return(f"""
        Emergencia #{self.id_emergencia}  {self.fecha_registro};
        Latitud y longitud: {self.latitud}, {self.longitud}; Riesgo de vida: {self.riesgo_de_vida()};
        Tipo: {self.tipo_emergencia.tipo}, Área: {self.area_emergencia.area} """)
    
    class Meta:
        db_table = 'registro_emergencia'