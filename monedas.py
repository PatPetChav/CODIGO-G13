#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR SOLES A DOLARES
#INPUTS -ENTRADAS
montoOrigen=input("ingrese el monto: ")
#PROCESO
opcion = "0"
while(opcion == "0") :
    print(" opcion 1 - soles a dolares")
    print(" opcion 2 - dolares a soles")
    print(" opcion 3 - soles a euros")
    print(" opcion 4 - euros a soles")
    opcion = input("Elija una opción : ")
    if(opcion == "1") :
        montoDolares = float(montoOrigen) / 3.80
        montoDolaresFormato = "${:,.2f}".format(montoDolares)
        #OUTPUTS - SALIDAS
        print("El monto en dolares es:"  + str(montoDolaresFormato))
    elif(opcion == "2") :
        montoSoles = float(montoOrigen) * 3.80
        montoSolesFormato = "${:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en soles es:",montoSolesFormato)
    elif(opcion == "3") :
        montoEuros = float(montoOrigen) * 0.25
        montoEurosFormato = "${:,.2f}".format(montoEuros)
         #OUTPUTS - SALIDAS
        print("El monto en euros es:",montoEurosFormato)
    elif(opcion == "4") :
        montoSoles = float(montoOrigen) / 0.25
        montoSolesFormato = "${:,.2f}".format(montoSoles)
         #OUTPUTS - SALIDAS
        print("El monto en soles es:",montoSolesFormato)
    else:
        print("ALERTA!!!, debe seleccionar una opción válida")
        opcion = "0"