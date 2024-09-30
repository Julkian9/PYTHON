from Modulos import Funciones_matematicas

class areas:
    """Esta clase calcula de las diferentes figuras geometricas"""
    def areaCuadrado(lado):
        """Calcula el area de un cuadrado elevando al cuadrado el lado pasado por parametro"""
        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base,altura):
        """Calcula el area de un triangulo utilizando los parametros base y altura"""
        return "El area del triangulo es: " + str((base*altura)/2)

#help(areas.areaCuadrado)
#print(areas.areaCuadrado(5) + " " + areas.areaCuadrado.__doc__)

#help(areas.areaTriangulo)
#print(areas.areaTriangulo(3,2) + " " + areas.areaTriangulo.__doc__ )

#help(areas)
help(Funciones_matematicas)

