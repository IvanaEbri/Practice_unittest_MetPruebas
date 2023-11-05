import unittest
from App_db import AreaEmergencia, TipoEmergencia, RegistroEmergencias, sqlite_db
from App_tablas_ref import App_emergencia

class TestAppEmergenciaConexion(unittest.TestCase):
    def setUp(self):
        self.app = App_emergencia()
        self.app._conectar_db()

    def tearDown(self):
        self.app._cerrar_db()
        sqlite_db.close()

    def test_conectar_db(self):
        """Verificar que la conexión a la base de datos se realiza correctamente"""
        self.assertTrue(sqlite_db.connect, "La conexion no se realizó") 

class TestAppEmergenciaCierre(unittest.TestCase):
    def setUp(self):
        self.app = App_emergencia()
        self.app._cerrar_db()
        self.app._conectar_db()

    def test_cerrar_conexion(self):
        """Verificar que la conexión a la base de datos se cierra correctamente"""
        self.app._cerrar_db()
        self.assertTrue(sqlite_db.is_closed(), "La conexion no se encuentra cerrada")

class TestAppEmergenciaMethods(unittest.TestCase):
    def setUp(self):
        self.app = App_emergencia()

    def test_ultimas_emergencias(self):
        """Verificar si se devuelven las últimas 2 emergencias correctamente"""
        emergencias=self.app._ultimas_emergencias(2)
        cant_registros = len(emergencias)
        self.assertEqual(cant_registros, 2)

    def test_ciudad_cercana(self):
        """Verificar si la función ciudad_cercana devuelve la ubicación esperada"""
        berazategui = self.app.ciudad_cercana(-34.763704,-58.208684)
        river= self.app.ciudad_cercana(-34.544762,-58.450766)
        self.assertEqual(berazategui.address,"Diagonal Lisandro de la Torre, Berazategui, Partido de Berazategui, Buenos Aires, B1880BFG, Argentina")
        self.assertEqual(river.address, "21642, Conector Interciclovías, Barrio River, Belgrano, Buenos Aires, Comuna 13, Ciudad Autónoma de Buenos Aires, C1424BCL, Argentina")
       
    def test_mapear_orm(self):
        """Verificar que la función _mapear_orm crea las tablas correctamente"""
        self.app._mapear_orm()
        #verifico si existen todas
        self.assertTrue(AreaEmergencia.table_exists())
        self.assertTrue(TipoEmergencia.table_exists())
        self.assertTrue(RegistroEmergencias.table_exists())

    def test_datos_desplegables(self):
        """Verificar que las tablas de Área y Tipo de emergencia no se envcuentran vacias"""
        areas_count = AreaEmergencia.select().count()
        tipos_count = TipoEmergencia.select().count()
        # Realizar las aserciones
        self.assertNotEqual(areas_count, 0) 
        self.assertEqual(areas_count, 7)
        self.assertNotEqual(tipos_count, 0) 
        self.assertEqual(tipos_count, 5)




if __name__ == '__main__':
    unittest.main(verbosity=2)