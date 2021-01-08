
import re#libreria de expresiones regulares

path = "patrones.txt"

try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""
 
for linea in archivo:
	texto += linea


print "\nSentencia de asignación"
patron = r"([a-z0-9]+\s*=\s*[a-z0-9+]+)"
resultado = re.findall(patron,texto)
print "Resultado de Busqueda\n", resultado

print "\nOperaciones aritmeticas"
patronA = r"([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)"
resultadoA = re.findall(patronA,texto)
print "Resultado de Busqueda\n", resultadoA


print "\nOperaciones booleanas"
patronB = r"([A-Za-z0-9|a-z0-9]+\s*[=|<|>|!|<=|>=]+\s*[A-Za-z0-9|a-z0-9]+)"
resultadoB = re.findall(patronB, texto)
print "Resultado de Busqueda\n", resultadoB

print "\nOperaciones de encabezado FOR,WHILE,IF,TRY"
patron1= r"(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)"
patron2 = r"(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)"
patron3 = r"(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)"
patron4 = r"(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)"
resultado1 = re.findall(patron1, texto)
resultado2 = re.findall(patron2,texto)
resultado3 = re.findall(patron3,texto)
resultado4 = re.findall(patron4,texto)
print "Resultado de Busqueda\n", resultado1
print "Resultado de Busqueda\n", resultado2
print "Resultado de Busqueda\n", resultado3
print "Resultado de Busqueda\n", resultado4

print "\nFormulas complejas"
patron= r"([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])"
resultado = re.findall(patron,texto)
print "Resultado de Busqueda\n", resultado