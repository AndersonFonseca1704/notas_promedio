print("--------------------------------------------------------------------")
print("-----------------caso 1 centinela-----------------------------------")
print("---------------nota de estudiantes----------------------------------")
print("--------------------------------------------------------------------")

#entrada

cod = int(input("digite el codigo del estudiante:"))
nombre = input("digite el nombre del estudiante :")
if cod!=0:
    nota1= float (input("digite la nota delparcial no. 1:"))
    nota2= float (input("digite la nota delparcial no. 2:"))
    nota3= float (input("digite la nota delparcial no. 3:"))

else :
    print("fin de los datos de entrada")

# processing
reprobados =0
while cod !=0:
    nota_final =(nota1+nota2+nota3/3)
    print("el estudiante de codigo" + str (cod) + "cuyo nombre es" + nombre + "obtuvo una nota definitiva de" + str(nota_final))
    if nota_final <3:
        reprobados + 1

#entrada
cod =int(input("digite el codigo del estudiante :"))
nombre= input("digite el nombre del estudiante:")
if cod!=0:
    nota1= float (input("digite la nota delparcial no. 1:"))
    nota2= float (input("digite la nota delparcial no. 2:"))
    nota3= float (input("digite la nota delparcial no. 3:"))

else :
    print("fin de los datos de entrada")

#salida
print("fcantidad de estudiantes que reprobaron la materia:"+ str(reprobados))