
import funciones_del_proyecto.funciones as fp

op = -1

while op != 0:

    print("-------------------------------------------------------------------------------------")
    print("#1 Mostrar el total de consumos de una ciudad en una planta.")
    print("#2 Mostrar nuevo diccionario con el total de MWh que ha dado a una ciudad.")
    print("#3 Mostar cuanto dinero ha recaudado una región comparado con la región Sierra.")
    print("#4 Mostar cuanto dinero se ha recaudado por mes en total.")
    print("-------------------------------------------------------------------------------------")

    op = int(input("Ingrese opcion: "))

    if op == 1:
        print("-------------------------------------------------")
        print("Las plantas son: ")
        print("-->", "Coca Codo Sinclair")
        print("-->", "Sopladora")
        print("-------------------------------------------------")
        
        planta = input("Ingrese el nombre de una Planta: ")
    
        if planta == "Coca Codo Sinclair":
            print("-------------------------------------------------")
            print("Las ciudades son: ")
            print("-->", "Quito")
            print("-->", "Guayaquil")
            print("-------------------------------------------------")
            ciudad = input("Ingrese el nombre de una Ciudad: ")
            print("-------------------------------------------------") 
            planta_ccs = fp.buscar_ciudad_coca_codo_sinclair(ciudad)
            print("Su consumo Total es: ", planta_ccs)

        if planta == "Sopladora":
            print("-------------------------------------------------")
            print("Las ciudades son: ")
            print("-->", "Guayaquil")
            print("-->", "Quito")
            print("-->", "Loja")
            print("-------------------------------------------------")
            ciudad = input("Ingrese el nombre de una Ciudad: ")
            print("-------------------------------------------------") 
            planta_sopladora = fp.buscar_ciudad_sopladora(ciudad)
            print("Su consumo Total es: ", planta_sopladora)

    elif op == 2:
        print("-------------------------------------------------")
        print("Todas las ciudades que estan en más que sea 1 planta son: ")
        print("-->", "Quito")
        print("-->", "Guayaquil")
        print("-->", "Loja")
        print("-------------------------------------------------")   

        ciudad = input("Ingrese el nombre de una Ciudad: ")
        
        if ciudad == "Quito":
            print("-------------------------------------------------") 
            ciudad_quito = fp.total_ciudad_Quito()
            print("Su consumo Total es: ", ciudad_quito)
            
        if ciudad == "Guayaquil":
            print("-------------------------------------------------") 
            ciudad_guayaquil = fp.total_ciudad_Guayaquil()
            print("Su consumo Total es: ", ciudad_guayaquil)


        if ciudad == "Loja":
            print("-------------------------------------------------") 
            ciudad_loja = fp.total_ciudad_Loja()
            print("Su consumo Total es: ", ciudad_loja)

    elif op == 3:
        print("-------------------------------------------------")
        print("Las regiones son: ")
        print("-->", "Costa con las ciudades: Guayaquil y Manta")
        print("-->", "Sierra con las ciudades: Quito, Ambato y Loja")
        print("-->", "Oriente con las ciudades: Tena y Nueva Loja")
        print("-------------------------------------------------") 

        region = input("Ingrese el nombre de una Región: ")

        if region == "Sierra":
            print("-------------------------------------------------") 
            sierra = fp.total_region_sierra()
            print("El dinero que ha recaudado la Región Sierra es: ", sierra)

        if region == "Costa":
            print("-------------------------------------------------") 
            costa = fp.total_region_costa()
            print("El dinero que ha recaudado la Región Costa es: ", costa)
            sierra = fp.total_region_sierra()
            print("El dinero que ha recaudado la Región Sierra es: ", sierra) 
            
        if region == "Oriente":
            print("-------------------------------------------------") 
            print("Información no disponible")
            print("Pero......") 
            sierra = fp.total_region_sierra()
            print("El dinero que ha recaudado la Región Sierra es: ", sierra)
    elif op == 4:
        print("----------------------------------------------------------------------")
        print("Enero = 1 , Febrero = 2, Marzo = 3,  Abril = 4, Mayo = 5, Junio = 6, Julio = 7")
        print("Agosto = 8, Septiembre = 9, Octubre = 10, Noviembre = 11, Diciembre = 12")
        print("----------------------------------------------------------------------")
        nom_mes = input("Ingrese el Nombre del mes: ")
        print("-------------------------------------------------")
        mes = int(input("Ingrese el Numero del mes: "))
        print("-------------------------------------------------")
        print("El mes de", nom_mes, "tiene un consumo de: ", end="")
        result = fp.total_consumo_por_mes(mes)
        print(result)






