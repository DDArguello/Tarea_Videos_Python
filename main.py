from Class_Procesos import VideosPyton
from os import system

c=0       
while c==0:
    opc=int(input("Ingrese el número del ejercicio a realizar, entre [1-32]: "))
    if opc==1:
        tarea=VideosPyton("ejercicio 1")
        print(tarea.mensaje)
        tarea.ejercicio1()
        c=1
    elif opc==2:
        tarea=VideosPyton("ejercicio 2")
        print(tarea.mensaje)
        tarea.ejercicio2()
    elif opc==3:
        tarea=VideosPyton("ejercicio 3")
        print(tarea.mensaje)
        tarea.ejercicio3()
    elif opc==4:
        tarea=VideosPyton("ejercicio 4")
        print(tarea.mensaje)
        tarea.ejercicio4()
    elif opc==5:
        tarea=VideosPyton("ejercicio 5")
        print(tarea.mensaje)
        tarea.ejercicio5()
    elif opc==6:
        tarea=VideosPyton("ejercicio 6")
        print(tarea.mensaje)
        tarea.ejercicio6()
    elif opc==7:
        tarea=VideosPyton("ejercicio 7")
        print(tarea.mensaje)
        tarea.ejercicio7()
    elif opc==8:
        tarea=VideosPyton("ejercicio 8")
        print(tarea.mensaje)
        tarea.ejercicio8()
    elif opc==9:
        tarea=VideosPyton("ejercicio 9")
        print(tarea.mensaje)
        tarea.ejercicio9()
    elif opc==10:
        tarea=VideosPyton("ejercicio 10")
        print(tarea.mensaje)
        tarea.ejercicio10()
    elif opc==11:
        tarea=VideosPyton("ejercicio 11")
        print(tarea.mensaje)
        tarea.ejercicio11()
    elif opc==12:
        tarea=VideosPyton("ejercicio 12")
        print(tarea.mensaje)
        tarea.ejercicio12()
    elif opc==13:
        tarea=VideosPyton("ejercicio 13")
        print(tarea.mensaje)
        tarea.ejercicio13()
    elif opc==14:
        tarea=VideosPyton("ejercicio 14")
        print(tarea.mensaje)
        tarea.ejercicio14()
    elif opc==15:
        tarea=VideosPyton("ejercicio 15")
        print(tarea.mensaje)
        tarea.ejercicio15()
    elif opc==16:
        tarea=VideosPyton("ejercicio 16")
        print(tarea.mensaje)
        tarea.ejercicio16()
    elif opc==17:
        tarea=VideosPyton("ejercicio 17")
        print(tarea.mensaje)
        tarea.ejercicio17()
    elif opc==18:
        tarea=VideosPyton("ejercicio 18")
        print(tarea.mensaje)
        tarea.ejercicio18()
    elif opc==19:
        tarea=VideosPyton("ejercicio 19")
        print(tarea.mensaje)
        tarea.ejercicio19()
    elif opc==20:
        tarea=VideosPyton("ejercicio 20")
        print(tarea.mensaje)
        tarea.ejercicio20()
    elif opc==21:
        tarea=VideosPyton("ejercicio 21")
        print(tarea.mensaje)
        tarea.ejercicio21()
    elif opc==22:
        tarea=VideosPyton("ejercicio 22")
        print(tarea.mensaje)
        tarea.ejercicio22()
#Desde aqui comienzan ejercicios sobre Funciones! <3
    elif opc==23:
        tarea=VideosPyton("ejercicio 23")
        print(tarea.mensaje)
        print(tarea.ejercicio23_ValidarDNI(1234567))
    elif opc==24:
        tarea=VideosPyton("ejercicio 24")
        print(tarea.mensaje)
        print(tarea.ejercicio24_ContarUltimaPalabra("Estructura de datos"))
    elif opc==25:
        tarea=VideosPyton("ejercicio 25")
        print(tarea.mensaje)
        nombre=input("Ingrese nombre del socio: ")
        while nombre!="":
            dni=int(input("Ingrese DNI del socio: "))
            while not (tarea.ejercicio23_ValidarDNI(dni)):
                print("Numero de DNI Invalido!")
                dni=int(input("Ingrese DNI del socio: "))
            identificador=tarea.ejercicio25_Identificador(nombre,dni)
            print(f"El identificador del socio es: {identificador}")
            nombre=input("Ingrese nombre del socio: ")
    elif opc==26:
        tarea=VideosPyton("ejercicio 26")
        print(tarea.mensaje)
        #1
        numeros=[]
        num=int(input("Ingrese numero: "))
        while num!=0:
            numeros.append(num)
            num=int(input("Ingrese numero: "))
        #2
        elim=int(input("Ingrese numero a eliminar: "))
        if elim in numeros:
            numeros.remove(elim)
        else:
            print("Ese numero no se encuentra entre los ingresados!")
        #3
        print(f"La sumatoria de los numeros es: {tarea.ejercicio26_Suma(numeros)}")
        #4
        limite=int(input("Filtrar numeros menores a: "))
        for n in tarea.ejercicio26_NumMenores(numeros,limite):
            print(n)
        #5
        print("Frecuencias: ")
        for tupla in tarea.ejercicio26_Frecuencia(numeros):
            print(f"{tupla[0]} aparece {tupla[1]} veces")
    elif opc==27:
        tarea=VideosPyton("ejercicio 27")
        print(tarea.mensaje)
        pasajeros=[]
        ciudades=[]
        while True:
            
            print("1. Agregar pasajeros")
            print("2. Agregar ciudades")
            print("3. Buscar ciudad destino mediante el DNI")
            print("4. Cantidad de pasajeros que viajan a una ciudad")
            print("5. Buscar país destino mediante DNI")
            print("6. Cantidad de pasajeros que viajan a un país")
            print("7. Salir del programa")
            opcion=int(input("Acción a ejecutar: "))
            if opcion==1:
                system("cls")
                print("AGREGAR PASAJEROS")
                pasajeros=tarea.ejercicio27_AgregarPasajeros(pasajeros)
            elif opcion==2:
                system("cls")
                print("AGREGAR CIUDADES")
                ciudades=tarea.ejercicio27_AgregarCiudades(ciudades)
            elif opcion==3:
                system("cls")
                dni=int(input("DNI: "))
                print(f"El pasajero viaja a {tarea.ejercicio27_BuscarCiudad(pasajeros, dni)}")
            elif opcion==4:
                system("cls")
                ciudad=input("Ciudad a buscar: ")
                print(f"Viajan {tarea.ejercicio27_CantidadPasajerosCiudad(pasajeros, ciudad)} pasajeros")
            elif opcion==5:
                system("cls")
                dni=int(input("DNI: "))
                print(f"Viaja a {tarea.ejercicio27_BuscarPaisDestino(pasajeros,ciudades,dni)}")
            elif opcion==6:
                system("cls")
                pais=input("País: ")
                print(f"Viajan {tarea.ejercicio27_CantidadPasajerosPais(pasajeros,ciudades,pais)} pasajeros")
            elif opcion==7:
                break
            else:
                print("Opción inválida")
    elif opc==28:
        tarea=VideosPyton("ejercicio 28")
        print(tarea.mensaje)
        primaria=set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria=tarea.ejercicio28_CargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria=tarea.ejercicio28_CargarNombres(secundaria)
        print("NOMBRES DE TODOS LOS ALUMNOS:")
        for nombre in primaria|secundaria:
            print(nombre)
        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)
        print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
        for nombre in primaria-secundaria:
            print(nombre)
    elif opc==29:
        tarea=VideosPyton("ejercicio 29")
        print(tarea.mensaje)
        domi=tarea.ejercicio29_Direcciones([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")])
        print(domi)
    elif opc==30:
        tarea=VideosPyton("ejercicio 30")
        print(tarea.mensaje)
        dic=tarea.ejercicio30_Dicc1(3)
        print(dic)
    elif opc==31:
        tarea=VideosPyton("ejercicio 31")
        print(tarea.mensaje)
        dic=tarea.ejercicio31_Dicc2(3)
        print(dic)
    elif opc==32:
        tarea=VideosPyton("ejercicio 31")
        print(tarea.mensaje)
        socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

        print("***Cargar socios")
        socios_activos=tarea.ejercicio32_CargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero=int(input("Número de socio: "))
        socios_activos[numero][2]=True

        print("***Modificando fecha de ingreso...")
        socios_activos=tarea.ejercicio32_ModificarFecha(socios_activos, "13032018", "14032018")

        print("***Eliminar socio")
        nombre=input("Nombre y apellido: ")
        numero=tarea.ejercicio32_NumeroSocio(socios_activos, nombre)
        if numero in socios_activos:
            del socios_activos[numero]
        tarea.ejercicio32_ImprimirListado(socios_activos)
    else:
        print("Opcion incorrecta! Vuelva a intentar: ")
    if True:
        opc=input("Desea acceder a otro ejercicio? [s/n]")
        if opc=='s':
            c=0
        else:
            c=1
            print("Gracias por revisar los ejercicios <3")