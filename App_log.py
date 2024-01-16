from peewee import *
from abc import ABCMeta
from datetime import *
from App_db import *
from geopy.geocoders import Nominatim


class App_emergencia (metaclass = ABCMeta):

    def _conectar_db(self):
        """sentencias necesarias para realizar la conexión a la base de datos emergencias.db """
        try:
            """Intento de conexion a la base de datos"""
            sqlite_db.connect()
            return True
        except OperationalError as e:
            print("Error al conectar con la BD.", e)
            exit()
            return False

    def _cerrar_db(self):
        """cerrar la conexion a la base de datos"""
        sqlite_db.close()

    def _mapear_orm(self):
        """sentencias necesarias para realizar la creación de la
        estructura de la base de datos (tablas y relaciones) utilizando el método de instancia
        “create_tables(list)” del módulo peewee"""
        #self.conectar_db()
        try:
            sqlite_db.create_tables([AreaEmergencia, TipoEmergencia, RegistroEmergencias])
        except Exception as e:
            print("Error al crear las tablas.", e)
            exit()
        
        self._cerrar_db()

    def _cargar_datos(self):
        """sentencias necesarias para persistir los datos de las tablas de referencis en la base de datos relacional SQLite. 
        Para ello se debe utilizar el método de clase Model create() en cada una 
        de las clase del modelo ORM definido"""
        self.mapear_orm()
        #Carga de datos en la tabla 'area_emergencia'
        areas_referencia = ["Urbana", "Rural", "Carretera/ Ruta", "Bosque", "Rio", "Mar", "Montaña"]
        for elem in areas_referencia:
            try:
                AreaEmergencia.create(area = elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Areas de emergencia.", e)
        #Carga de datos en la tabla 'tipo_emergencia'
        tipos_referencia = ["Incendio", "Choque automovilistico", "Emergencia medica", "Personas en riesgo", "Inundacion"]
        for elem in tipos_referencia:
            try:
                TipoEmergencia.create(tipo = elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Tipos de emergencia.", e)

        self._cerrar_db()

    def nueva_emergencia(self):
        """Registrar una emergencia nueva (estos datos serian solicitados por el fron mediante un formulario y persistidos mediante este metodo)"""
        fecha_de_carga = datetime.now()
        latitud = 0
        longitud = 0
        area = 0
        tipo= 0
        riesgo = 0

        while True:
            print("Se le solicitará la latitud y longitud, recuerde los caracteres permitidos son '-', números y como separador de decimales '.'")
            lat_no = input("Ingrese la latitud de la emergencia ")
            lng_no = input("Ingrese la longitud de la emergencia ")
            try:
                latitud= float(lat_no)
                longitud= float(lng_no)
                if latitud >= -90 and latitud <= 90 and longitud >= -180 and longitud <= 180:
                   break
                else:
                    raise ValueError()
            except ValueError as e:
                print("Debe intoducir valores validos de latitud y longitud", e)
            except:
                print("Debe cumplir con los caracteres permitidos")

        while True:
            max_id = AreaEmergencia.select(fn.Max(AreaEmergencia.id_area)).scalar()
            query= AreaEmergencia.select()
            for area in query:
                print(f"   -{area.id_area}_{area.area}")
            try:
                area_no = int(input("Ingrese el número correspondiente al área donde se desarrolla la emergencia "))
                if area_no >= 0 and area_no<= max_id:
                    area = AreaEmergencia.select().where(AreaEmergencia.id_area==area_no)
                    break
                else:
                    print("Debe ingresar un número valido")
            except:
                print("Debe ingresar el número que corresponda a la opción elegida")
        referencia = input("Ingrese alguna referencia del sitio de emergencia si correspondiera ")

        while True:
            max_id = TipoEmergencia.select(fn.Max(TipoEmergencia.id_tipo)).scalar()
            query= TipoEmergencia.select()
            for tipo in query:
                print(f"   -{tipo.id_tipo}_{tipo.tipo}")
            try:
                tipo_no = int(input("Ingrese el número correspondiente al área donde se desarrolla la emergencia "))
                if tipo_no >= 0 and tipo_no<= max_id:
                    tipo = TipoEmergencia.select().where(TipoEmergencia.id_tipo==tipo_no)
                    break
                else:
                    print("Debe ingresar un número valido")
            except:
                print("Debe ingresar el número que corresponda a la opción elegida")
        
        foto = input("Ingrese el URL de la fotografia de la emergencia ")
        comentario = input("Ingrese un comentario si correspondiera ")

        while True:
            validacion = input("Si hay personas en riesgo ingrese 'S', caso contrario ingrese 'N' ")
            if validacion == 'S' or validacion =='s':
                riesgo = True
                break
            elif validacion == 'n' or validacion == 'N':
                riesgo = False
                break
            else:
                print("Debe ingresar uno de lo9s caracteres indicados")

        nueva_emergencia = RegistroEmergencias.create(fecha_registro= fecha_de_carga , latitud= latitud ,longitud= longitud, area_emergencia= area, ref_ubicacion= referencia, tipo_emergencia= tipo, foto = foto, coment_emergencia= comentario,riesgo_vida= riesgo)
        try:
            nueva_emergencia.save()
            print("Se ha cargado de manera correcta la emergencia.")
            return nueva_emergencia
        except Exception as e:
            print("Ha fallado el guardado de la emergencia",e)

        self._cerrar_db()

    def _ultimas_emergencias(self, n_emergencias):
        cantidad = n_emergencias
        
        try:
            ultimas_emergencias = RegistroEmergencias.select().order_by(RegistroEmergencias.fecha_registro.desc()).limit(cantidad)
        except:
            print("Ocurrio un error en la obtencion de datos")

        '''for emergencia in ultimas_emergencias:
            print(emergencia.__str__)'''
        
        return ultimas_emergencias

    def envio_avisos(self):
        cantidad = 0
        while True:
            try:
                cantidad = int(input("Ingrese cuantas emergencias desea mostrar "))
                if cantidad <=0:
                    raise ValueError()
                else:
                    break
            except ValueError as e:
                print("Debe ingresar un número valido", e)
        listado = self._ultimas_emergencias(cantidad)

        if listado:
            for emergencia in listado:
                direccion_emerg = self.ciudad_cercana(emergencia.latitud, emergencia.longitud)
                if emergencia.riesgo_vida:
                    riesgo= "CON"
                else:
                    riesgo= "SIN"
                print(f"""Emergencia #{emergencia.id_emergencia}:
                {emergencia.tipo_emergencia.tipo} {riesgo} de vida, en área {emergencia.area_emergencia.area}
                Direccion: {direccion_emerg}
                Latitud: {emergencia.latitud}, longitud: {emergencia.longitud}
                
                """)
        else:
            print("No se hayaron registros")

        self._cerrar_db()

    def ciudad_cercana(self,latitud, longitud):
        geolocalizador = Nominatim(user_agent="my-emergency-app")
        direccion_emerg = geolocalizador.reverse(f"{latitud}, {longitud}", exactly_one=True)
        return direccion_emerg


