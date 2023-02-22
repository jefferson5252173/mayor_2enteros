
#programa para verificar cual de dos números enteros es el mayor



#input
x= int(input("digite el valor de :x "))
y= int(input("digite el valor de :y "))

#prosessing
if x == y:
    #output
    print("los numeros son iguales...")
if x > y:
    mayor = x
else:
    mayor = y

#output
print ("el mayor entero entre " + str(x) + " y " + str(y) + "es" + str(mayor))
