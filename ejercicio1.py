from datetime import date, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None or mes is None or año is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
        self.fecha = date(self.año, self.mes, self.dia)

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("El argumento debe ser una instancia de la clase Fecha")
        return abs((self.fecha - otra_fecha.fecha).days)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    def __add__(self, days):
        if not isinstance(days, int):
            raise TypeError("El argumento debe ser un número entero")
        nueva_fecha = self.fecha + timedelta(days=days)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("El argumento debe ser una instancia de la clase Fecha")
        return self.fecha == otra_fecha.fecha
