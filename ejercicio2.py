from datetime import date, datetime

class Alumno:
    def _init_(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        if isinstance(fecha_ingreso, str):
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
        hoy = date.today()
        return (hoy - fecha_ingreso).days // 365

    def _str_(self):
        return f"Alumno({self.datos})"

    def _eq_(self, otro):
        if isinstance(otro, Alumno):
            return self.datos["DNI"] == otro.datos["DNI"]
        return False

