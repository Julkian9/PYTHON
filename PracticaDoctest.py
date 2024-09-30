def areaTriangulo(base,altura):
        """
        Calcula el area de un triangulo utilizando los parametros base y altura

        >>> areaTriangulo(3,6)
        'El area del triangulo es: 9.0'

        >>> areaTriangulo(4,5)
        'El area del triangulo es: 10.0'

        >>> areaTriangulo(9,3)
        'El area del triangulo es: 13.5'

        """
        return "El area del triangulo es: " + str((base*altura)/2)

#print(areaTriangulo(2,4))


def compruebaMail(mailUsuario):
        """
        La funcion compruebaMail evalua un mail recibido
        en busca de la @.  Si tiene un @ es correcto, si
        tiene mas de una @ es incorrecto si la @ esta al 
        final es incorrecto

        >>> compruebaMail('jjmafla@emcali.com.co')
        True

        >>> compruebaMail('jjmaflaemcali.com.co@')
        False

        >>> compruebaMail('jjmaflaemcali.com.co')
        False

        >>> compruebaMail('jjmafla@emcali@com.co')
        False

        """

        arroba=mailUsuario.count('@')

        if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
                return False
        else:
                return True


import doctest
doctest.testmod()