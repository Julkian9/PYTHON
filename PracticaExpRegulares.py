import re

cadena="Vamos a aprender a expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
#si esta devuelve objeto y si no esta devuelve none
print(re.search("aprenderrr",cadena))

textoBuscar="Python"

textoEncontrado=re.search(textoBuscar,cadena)


'''if re.search(textoBuscar, cadena) is not None:
        print("He encontrado el texto")
else:
        print("No he encontrado el texto")'''

#start() indica el punto inicia la palabra buscada
print(textoEncontrado.start())

#end() indica el caracter final 
print(textoEncontrado.end())

#span() indica el caracter inicial y final en una tupla 
print(textoEncontrado.span())

#findall encuentra todas las conincidencias dentro de una lista
print(re.findall(textoBuscar,cadena))
#findall con len indica la cantidad de veces que esta una palabra en una cadena
print(len(re.findall(textoBuscar,cadena)))


lista_nombres=['Ana Gomez',
               'Maria Martin',
               'Sandra Lopez',
               'Santiago Martin',
               'Sandra Martin']
#Busca todas las coninciencias dentro de una cadena que tenga al inicio '^X' y al final 'Y$' dentro de una lista
for elemento in lista_nombres:
    if re.findall('^Sandra',elemento) or re.findall('Martin$',elemento):
        print(elemento)

lista_url=['adsl.emcali.net.co',
            'ticket.emcali.net.co',
            'elias.emcali.net.co',
            'dominio.emcali.com.co',
            'nexoservicios.emcali.com.co']

for url in lista_url:
    if  re.findall('.com.co',url):
        print(url)

lista_cosas=['hombres',
             'mujeres',
             'mascotas',
             'niños',
             'niñas',
             'camión',
             'camion']
#Busca todas las coincidencias empezadas niñ que tengan una o a y termine en s
for personas in lista_cosas:
    if re.findall('niñ[oa]s',personas):
        print(personas)

for objetos in lista_cosas:
    if re.findall('cami[oó]n',objetos):
        print(objetos)

lista_trabajadores=['Carlos',
                    'Angelo',
                    'Alejandro',
                    'Marien',
                    'Walter',
                    'Vicky',
                    'Juan',
                    'Oscar']
for trabajadores in lista_trabajadores:
    if re.findall('[o-t]$',trabajadores):
        print(trabajadores)