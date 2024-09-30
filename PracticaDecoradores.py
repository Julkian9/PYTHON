def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        # Acciones adicionales que decoran 
        print("Hemos terminado el calculo")

    return funcion_interior

# *arg puede usar un numero indeterminado de argumentos dentro de la funciona
# **kwargs puede recibir argumentos clave valor


@funcion_decoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(7,5,8)
resta(12,10)
potencia(base=5,exponente=3)