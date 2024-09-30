import re

nombre1="Sandra López"

nombre2="Antonio Gómez"

nombre3="Maria López"

if re.match("andra",nombre2, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")