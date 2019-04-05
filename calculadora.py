def suma(a,b):
    print("La suma es:",a+b)

def resta(a,b):
    print("La resta es:",a-b)

def multiplicacion(a,b):
    print("La multiplicación es:",a*b)

def division(a,b):
    print("La división es:",a/b)

def exponencial(a,b):
    print("La exponencial es:",a**b)


dict={'1':suma,'2':resta,'3':multiplicacion,'4':division,'5':exponencial}


while True:
    #print("\n-----------MENU--------\n 1. Suma \n 2. Resta\n 3. Multiplicación\n 4. División\n 5. Exponencial\n q. Exit \n")
    print("-----------MENU--------")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplica")
    print("4.Divide")
    print("5.Exponente")
    print("6.Salir")
    try:
        variable = input("Escoge opción: ")
        if variable == '6':
            print("\nFin")
            break
        else:
           if (variable =='1' or variable =='2' or variable =='3' or variable =='4' or variable=='5'):
            a = float(input("Variable a: "))
            b = float(input("Variable b: "))
            #llamamos a la función
            dict[variable](a,b)

    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    except ValueError:
        print("Debe ingresar valores numéricos.")
    except:
        print("Error Genérico")