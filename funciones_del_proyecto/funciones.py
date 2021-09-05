
import data_2doparcial.consumos as dt

# Funcion para calcular los comsumos x tarifa al mes.

def total_consumo_por_mes(mes):
        return (dt.consumo_energia['Sopladora']["Loja"]["consumos"][mes] * dt.tarifa_planta['Sopladora']["Loja"]["tarifa"]) + (dt.consumo_energia['Sopladora']["Guayaquil"]["consumos"][mes] * dt.tarifa_planta['Sopladora']["Guayaquil"]["tarifa"]) + (dt.consumo_energia['Sopladora']["Quito"]["consumos"][mes] * dt.tarifa_planta['Sopladora']["Quito"]["tarifa"]) + (dt.consumo_energia['Coca Codo Sinclair']["Quito"]["consumos"][mes] * dt.tarifa_planta['Coca Codo Sinclair']["Quito"]["tarifa"]) + (dt.consumo_energia['Coca Codo Sinclair']["Guayaquil"]["consumos"][mes] * dt.tarifa_planta['Coca Codo Sinclair']["Guayaquil"]["tarifa"])  

#Funcion para calcular el consumo total en la region Sierra.

def total_region_sierra():
        return ((dt.total_consumo["Coca Codo Sinclair"]["Quito"]["consumos"] * dt.tarifa_planta['Coca Codo Sinclair']["Quito"]["tarifa"]) + (dt.total_consumo["Sopladora"]["Quito"]["consumos"] * dt.tarifa_planta['Sopladora']["Quito"]["tarifa"]) + (dt.total_consumo["Sopladora"]["Loja"]["consumos"] * dt.tarifa_planta['Sopladora']["Loja"]["tarifa"]))
       
#Funcion para calcular el consumo total en la region Costa.

def total_region_costa():
        return  ((dt.total_consumo["Coca Codo Sinclair"]["Guayaquil"]["consumos"] * dt.tarifa_planta["Coca Codo Sinclair"]["Guayaquil"]["tarifa"]) + (dt.total_consumo["Sopladora"]["Guayaquil"]["consumos"] * dt.tarifa_planta["Sopladora"]["Guayaquil"]["tarifa"]))
        
#Funcion para calcular el consumo total en la Ciudad Quito.

def total_ciudad_Quito():
        print("Su consumo total en la planta Coca Codo Sinclair es: ", dt.total_consumo["Coca Codo Sinclair"]["Quito"]["consumos"])
        print("Su consumo total en la planta Sopladora es: ", dt.total_consumo["Sopladora"]["Quito"]["consumos"])
        return (dt.total_consumo["Coca Codo Sinclair"]["Quito"]["consumos"] + dt.total_consumo["Sopladora"]["Quito"]["consumos"])
        

#Funcion para calcular el consumo total en la Ciudad Guayaquil.

def total_ciudad_Guayaquil():
        print("Su consumo total en la planta Coca Codo Sinclair es: ", dt.total_consumo["Coca Codo Sinclair"]["Guayaquil"]["consumos"])
        print("Su consumo total en la planta Sopladora es: ", dt.total_consumo["Sopladora"]["Guayaquil"]["consumos"])
        return (dt.total_consumo["Coca Codo Sinclair"]["Guayaquil"]["consumos"] + dt.total_consumo["Sopladora"]["Guayaquil"]["consumos"])
        

#Funcion para calcular el consumo total en la Ciudad Loja.

def total_ciudad_Loja():
        print("Su consumo total en la planta Sopladora es: ", dt.total_consumo["Sopladora"]["Loja"]["consumos"])
        return dt.total_consumo["Sopladora"]["Loja"]["consumos"]

#Funcion para calcular el consumo total en la de la panta "Sopladora" por cada ciudad.

def buscar_ciudad_sopladora(ciudad):
    if ciudad == "Guayaquil":
        return sum(dt.consumo_energia["Sopladora"]["Guayaquil"]["consumos"])
    if ciudad == "Quito":
        return sum(dt.consumo_energia["Sopladora"]["Quito"]["consumos"])
    if ciudad == "Loja":
        return sum(dt.consumo_energia["Sopladora"]["Loja"]["consumos"])

#Funcion para calcular el consumo total en la de la panta "Coca Codo Sinclair" por cada ciudad.

def buscar_ciudad_coca_codo_sinclair(ciudad):
    if ciudad == "Quito":  
        return sum(dt.consumo_energia["Coca Codo Sinclair"]["Quito"]["consumos"])
    if ciudad == "Guayaquil":
        return sum(dt.consumo_energia["Coca Codo Sinclair"]["Guayaquil"]["consumos"])






