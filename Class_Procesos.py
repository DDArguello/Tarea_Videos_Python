
class VideosPyton:
    def __init__(self, titulo):
        self.mensaje=titulo
    
    def ejercicio1(self):
        N=input("Tu nombre: ")
        print("Ahora estas en la matrix, ", N)
    def ejercicio2(self):
        costo=float(input("Costo de la cena: $"))
        servicio=costo*0.062
        prop=costo*0.1
        total=costo+servicio+prop
        print(f"Costo total de la comida: ${total:.2f}")
    def ejercicio3(self):
        fecha=input("Fecha en Formato DDMMAA: ")
        dia=fecha[:2]
        mes=fecha[2:4]
        ano=fecha[4:]
        print(f"{dia} / {mes} / {ano}")
    def ejercicio4(self):
        capacidad=float(input("Capacidad del tanque: "))
        Rendmoto=float(input("Rendimiento (Km por Litro): "))
        recorr=float(input("Km totales a recorrer: "))
        kmtanque=recorr/(capacidad*Rendmoto)

        print(f"Se necesitarian {kmtanque:.2f} tanques.")
    def ejercicio5(self):
        Capacidadm2=4
        PorcenGrada=0.2
        PorcenEspe=0.3
        PorcenComun=0.7
        dimensiones=float(input("Dimenciones del estadio (en m2): "))
        Persogradas=int(input("Cantidad de personas que caben en las gradas: "))
        Porcentescen=int(input("Porcentaje que ocupa el escenario: "))
        m2gradas=dimensiones*PorcenGrada
        m2escen=dimensiones*(Porcentescen/100)
        m2dispo=dimensiones-m2gradas-m2escen
        persotot=(m2dispo*4)+Persogradas
        print(f"Caben {persotot} personas")
        precioee=float(input("Precio entrada especial: "))
        precioec=float(input("Precio entrada comun: "))
        print(f"ingreso total de ventas: ${(persotot*PorcenEspe)*precioee+(persotot*PorcenComun)*precioec}")
    def ejercicio6(self):
        num=int(input("Ingrese un numero: "))
        if num<0:
            numero=num*-1
            print(f"El valor absoluto de {num} es {numero}")
        else:
            print(f"El valor absoluto de {num} es {num}")
    def ejercicio7(self):
        nom1=input("Ingrese nombre: ")
        nom2=input("Ingrese otro nombre: ")
        if nom1[0]==nom2[0] or nom1[-1]==nom2[-1]:
            print("Hay coincidencia")
        else:
            print("No hay coincidencia")
    def ejercicio8(self):
        candidato=input("Elija la lista de su candidato [A-B-C]: ").upper()
        if candidato=="A":
            print("Usted voto por el partido rojo")
        elif candidato=="B":
            print("Usted voto por el partido azul")
        elif candidato=="C":
            print("Usted voto por el partido verde")
        else:
            print("Opcion incorrecta!")
    def ejercicio9(self):
        letra=input("Ingrese una letra: ").lower()
        if len(letra)!=1:
            print("Debe ingresar solo una letra!")
        else:
            if letra in "aeiou":
                print("Es una vocal")
            else:
                print("No es una vocal")
    def ejercicio10(self):
        year=int(input("Ingrese un año: "))
        if year%4 != 0:
            print(f"El año {year} no es bisiesto")
        else:
            if year%100 != 0 or year%400 == 0:
                print(f"El año {year} es bisiesto")
            else:
                print(f"EL año {year} no es bisiesto")
    def ejercicio11(self):
        fecha=input("Fecha [Formato 'dia, DD/MM']: ").lower()
        diasem=fecha[0:fecha.find(',')]
        dianum=int(fecha[fecha.find(' ')+1:fecha.find('/')])
        mesnum=int(fecha[fecha.find('/')+1:])
        if dianum>31 or mesnum>12:
            print("Fecha incorrecta!")
        else:
            if diasem in "lunes,martes,miercoles":
                resp=input("¿Se tomaron exámenes? S/N: ").lower()
                if resp=="s":
                    aprob=int(input("Ingrese la cantidad de aprobados: "))
                    repro=int(input("Ingrese la cantidad de rreprobados: "))
                    print(f"Porcentaje de aprobados: {(aprob*100)/(aprob+repro):.2f}%")
            elif diasem=="jueves":
                asis=int(input("Ingrese el porcentaje de asistencia:"))
                if asis>50:
                    print("Asistieron la mayoria")
                else:
                    print("No asistió la mayoria")
            elif diasem=="viernes":
                if dianum==1 and (mesnum==1 or mesnum==7):
                    print("Inicio del nuevo ciclo")
                    alum=int(input("Ingrese la cantidad de alumnos: "))
                    arancel=float(input("Ingrese el arancel: $"))
                    print(f"ingreso total: ${alum*arancel}")
            else:
                print("Fecha incorrecta!")
        print("FIN DEL PROGRAMA...")
    def ejercicio12(self):
        total=0
        for i in range(101):
            total+=i
        print(f"La sumatoria es: {total}")
    def ejercicio13(self):
        total=0
        for i in range(101):
            if i%3==0:   
                total+=i
        print(f"La sumatoria es: {total}")
    def ejercicio14(self):
        num=int(input("Ingrese numero: "))
        fact=1
        if num!=0:
            for i in range (1,num+1):
                fact=fact*i
        print(f"El factorial es: {fact}")
    def ejercicio15(self):
        n1=0
        n2=1
        print(n1),print(n2)
        for i in range(8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
    def ejercicio16(self):
        sumnega=0
        sumposi=0
        cantposi=0
        for i in range(6):
            num=int(input("Ingrese numero: "))
            if num>=0:
                cantposi+=1
                sumposi+=num
            else:
                sumnega+=num
        print(f"La suma de negativos es: {sumnega}")
        if cantposi!=0:
            print(f"El promedio de positivos es: {sumposi/cantposi:.2f}")
        else:
            print("No se ingreso numeros positivos")
    def ejercicio17(self):
        corri=int(input("Ingrese Corrimiento: "))
        alfa="abcdefghijklmnñopqrstuvwxyz"
        for i in range(5):
            msj=input("Ingrese mensaje a encriptar: ")
            encrip=""
            for caracter in msj:
                if caracter.lower() in alfa:
                    indice=alfa.find(caracter.lower())
                    indice=(indice+corri)%27
                    encrip+=alfa[indice]
                else:
                    encrip+=caracter
            print(f"Mensaje encriptado: {encrip}")
    def ejercicio18(self):
        tot=0
        monto=1
        while monto!=0:
            if monto<0:
                print("El monto es incorrecto!")
                monto=1
            else:
                monto=float(input("Ingrese el monto de la venta: "))
                tot+=monto
        if tot>1000:
            tot-=tot*0.1
        print(f"El monto total a pagar es: ${tot}")
    def ejercicio19(self):
        totpar=0
        totimpar=0
        num=int(input("Ingrese numero: "))
        while num!=0:
            par=0
            impar=0
            while num!=0:
                verificar=num%10
                if verificar%2==0:
                    par+=1
                    totpar+=1
                else:
                    impar+=1
                    totimpar+=1
                num=num//10
            print(f"El numero ingresado tiene {par} digitos pares y {impar} digitos impares")
            num=int(input("Ingrese numero: "))
        print(f"El total de digitos pares es: {totpar}")
        print(f"El total de digitos impares es: {totimpar}")
    def ejercicio20(self):
        digEnLaLinea=0
        cant_lineas=0
        tit=input("Titulo del libro: ")
        while tit!="*":
            if tit=="/":
                cant_lineas+=1
                print(f"Linea completa. Aparecen {digEnLaLinea} digitos")
                digEnLaLinea=0
            else:
                for caracter in tit:
                    if caracter in "0123456789":
                        digEnLaLinea+=1
            tit=input("Titulo del libro: ")
        print(f"Fin. Se leyeron {cant_lineas} lineas")
    def ejercicio21(self):
        cant=0
        num=int(input("Ingrese numero: "))
        while num!=0:
            primo=True
            for i in range(2,num):
                if num%i==0:
                    primo=False
                    break
            if primo:
                cant+=1
            num=int(input("Ingrese numero: "))
        print(f"Hay {cant} numeros primos")
    def ejercicio22(self):
        yearini=int(input("Ingrese el año inicial: "))
        yearfin=int(input("Ingrese el año final: "))
        for year in range(yearini,yearfin+1):
            if not year%10==0:
                continue
            if not year%4==0:
                continue
            if year%100!=0 or year%400==0:
                print(year)
    #Desde aqui comienzan ejercicios sobre Funciones! <3
    def ejercicio23_ValidarDNI(self,dni):
        dni=str(dni)
        if len(dni)>6 and len(dni)<9:
            return True
        else:
            return False
    def ejercicio24_ContarUltimaPalabra(self,cadena):
        lon=len(cadena)
        if lon==0:
            return 0
        cant=0
        for i in range(lon):
            if cadena[i]!=" ":
                cant+=1
            else:
                if cadena[i]==" " and i<(lon-1) and cadena[i+1]!=" ":
                    cant=0
        return cant
#-------------------------------Forma parte de un solo ejercicio Video 29
    def ejercicio25_Identificador(self,nombre,dni):
        nombre=nombre.strip()
        i=nombre[0:nombre.find(" ")]
        i=i+str(VideosPyton(None).ejercicio24_ContarUltimaPalabra(nombre))
        i=i+str(VideosPyton(None).ejercicio25_TresDIgitosPrimeros(dni))
        return i
    def ejercicio25_TresDIgitosPrimeros(self,numero):
        while numero>=1000:
            numero=numero/10
        return int(numero)
#-----------------------------------------------
#---------Forma parte de un solo ejercicio video 32 
    def ejercicio26_Suma(self,lista):
        suma=0
        for n in lista:
            suma+=n
        return suma
    def ejercicio26_NumMenores(self,lista,lim):
        new=[]
        for n in lista:
            if n<lim:
                new.append(n)
        return new
    def ejercicio26_Frecuencia(self,lista):
        new=[]
        for n in lista:
            if (n, lista.count(n)) not in new:
                new.append((n, lista.count(n)))
        return new
#------------------------------------------------
#--------Forma parte de un ejercicio video 33
    def ejercicio27_AgregarPasajeros(self,pasajeros):
        nombre=input("Nombre -x para cortar: ")
        while nombre!="x":
            dni=int(input("DNI: "))
            destino=input("Ciudad destino: ")
            pasajeros.append((nombre,dni,destino))
            nombre=input("Nombre -x para cortar: ")
        return pasajeros
    def ejercicio27_AgregarCiudades(self,ciudades):
        ciudad=input("Ciudad -x para cortar: ")
        while ciudad!="x":
            pais=input("País: ")
            ciudades.append((ciudad,pais))
            ciudad=input("Ciudad -x para cortar: ")
        return ciudades
    def ejercicio27_BuscarCiudad(self,pasajeros, dni):
        for viaje in pasajeros:
            if viaje[1]==dni:
                return viaje[2]
        return ""
    def ejercicio27_CantidadPasajerosCiudad(self,pasajeros, ciudad):
        cantidad=0
        for viaje in pasajeros:
            if viaje[2]==ciudad:
                cantidad+=1
        return cantidad
    def ejercicio27_BuscarPaisDestino(self,pasajeros, ciudades, dni):
        buscada=VideosPyton(None).ejercicio27_BuscarCiudad(pasajeros, dni)
        for ciudad in ciudades:
            if ciudad[0]==buscada:
                return ciudad[1]
        return ""
    def cantidadPasajerosPais(self,pasajeros, ciudades, pais):
        cantidad=0
        for viaje in pasajeros:
            if pais==VideosPyton(None).ejercicio27_BuscarPaisDestino(pasajeros, ciudades, viaje[1]):
                cantidad+=1
        return cantidad
#-----------------------------------------
#-------------------------Ejercicios Conjuntos
    def ejercicio28_CargarNombres(self,alumnos):
        nombre=input("Nombre: ")
        while nombre!="x":
            alumnos.add(nombre)
            nombre=input("Nombre: ")
        return alumnos
    def ejercicio29_Direcciones(self,ventas):
        domicilios=set()
        for venta in ventas:
            domicilios.add(venta[3])
        return domicilios
#-----------------------------------------
#-------------------------Ejercicios Diccionarios
    def ejercicio30_Dicc1(self,cant):
        contadores={}
        for i in range(cant):
            cadena=input("Cadena de caracteres: ")
        for caracter in cadena:
            if caracter not in contadores:
                contadores[caracter]=1
            else:
                contadores[caracter]+=1
        print("Frecuencia de cada carácter")
        for caracter, cantidad in contadores.items():
            print(caracter, ": ", cantidad)
    def ejercicio31_Dicc2(self,cant):
        contadores={}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto+alfabeto.upper():
            contadores[letra]=0
        for i in range(cant):
            cadena=input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]+=1
        print("Frecuencia de cada letra")
        for caracter, cantidad in contadores.items():
            print(caracter, ": ", cantidad)
#----------------------------Forma parte de un solo ejercicio video 38
    def ejercicio32_CargarSocios(self,socios):
        numero=int(input("Número de socio (0 para cortar): "))
        while numero!=0:
           nombre=input("Nombre y apellido: ")
           fecha=input("Fecha de ingreso (DDMMAAAA): ")
           cuota=input("¿Cuota al día? s/n: ")
           socios[numero]=[nombre,fecha,cuota.lower()=="s"]
           numero=int(input("Número de socio (0 para cortar): "))
        return socios

    def ejercicio32_ModificarFecha(self,socios, fecha_anterior, fecha_nueva):
        for datos in socios.values():
            if datos[1]==fecha_anterior:
                datos[1]=fecha_nueva
        return socios

    def ejercicio32_NumeroSocio(self,socios, nombre):
        for numero,datos in socios.items():
            if datos[0].lower()==nombre.lower():
                return numero
        return 0

    def ejercicio32_FormatoFecha(self,fecha):
        return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

    def ejercicio32_ImprimirListado(self,socios):
        for numero,datos in socios.items():
            print("-Número:",numero)
            print("-Nombre:",datos[0])
            print(f"-Ingresó: {VideosPyton(None).ejercicio32_FormatoFecha(datos[1])}")
            if datos[2]:
                print("-Cuota al día")
            else:
                print("-En deuda")