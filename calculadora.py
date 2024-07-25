from tkinter import *
import math
import statistics

global datos
datos=[]

def envia_boton(valor):
   anterior = pantalla.get()
   pantalla.delete(0, END)
   pantalla.insert(0, str(anterior) + str(valor))

def suma():
   global num1
   global operacion
   num1 = pantalla.get()
   num1 = float(num1)
   pantalla.delete(0,END)
   operacion = "+"

def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "-"

def multiplicacion():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "*"

def division():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "/"

def potencia():
    global num1
    global num2
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "^"
    num2 = pantalla.get()
    num2 = float(num2)

def raiz():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "√"

def seno():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "sin"

def coseno():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "cos"

def tangente():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "tan"

def cargar_datos():
    global datos
    global operacion
    global num1
    while True:
        num1 = pantalla.get()
        if num1.isdigit():
            num1 = float(num1)
            datos.append(num1)
            pantalla.delete(0,END)
        elif num1 != "=":
            break
        else: num1=="M+"
    print(datos)
    operacion = "CargarDatos"
    return datos
    
def borrar_Datos():
    global datos
    global operacion
    datos.clear()    
    operacion = "M-"
    return datos

def media():
   global operacion
   global datos
   pantalla.delete(0,END)
   operacion = "X"

def mediana():
   global operacion
   global datos
   pantalla.delete(0,END)
   operacion = "Me"

def moda():
   global operacion
   global datos
   pantalla.delete(0,END)
   operacion = "Mo"

def varianza():
   global operacion
   global datos
   pantalla.delete(0,END)
   operacion = "σ2"

def desviacion_estandar():
   global operacion
   global datos
   pantalla.delete(0,END)
   operacion = "σ"

def borrar():
    pantalla.delete(0, END)

def borrar_uno():
    largo = len(pantalla.get())
    pantalla.delete(largo-1, END)

def igual():
    global num1
    global num2
    num2 = pantalla.get()
    pantalla.delete(0, END)

    if operacion == "+":
        pantalla.insert(0, num1 + float(num2))    
    
    elif operacion == "-":
        pantalla.insert(0, num1 - float(num2))
    
    elif operacion == "*":
        pantalla.insert(0, num1 * float(num2))
    
    elif operacion == "/":
        try:
            pantalla.insert(0, num1 / float(num2))
        except:
            pantalla.insert(0,"ERROR")
    
    elif operacion == "^":
        i=1
        num1=float(num1)
        resultado=float(num1)
        num2=float(num2)
        while (i<num2):
            resultado= resultado * num1
            i=i+1
        pantalla.insert(0, resultado )

    elif operacion == "√":
        num1=float(num1)
        resultado=math.sqrt(num1)
        pantalla.insert(0, resultado)
    
    elif operacion == "sin":
        res=math.sin(num1)
        pantalla.insert(0, res)
    
    elif operacion == "cos":
        res=math.cos(num1)
        pantalla.insert(0, res)
    
    elif operacion == "tan":
        res=math.tan(num1)
        pantalla.insert(0, res)
    
    elif operacion == "σ2":
        if len(datos)>0:
            print("la varianza es: ", statistics.variance(datos))   
            pantalla.insert(0, statistics.variance(datos))
        else:
            pantalla.insert(0, "ERROR NO HAY DATOS CARGADOS")
    
    elif operacion == "σ":
        if len(datos)>0: 
            print("la desviacion estandar es: ", statistics.stdev(datos))  
            pantalla.insert(0, statistics.stdev(datos))
        else:
            pantalla.insert(0, "ERROR NO HAY DATOS CARGADOS")
    
    elif operacion == "X":
        if len(datos)>0:   
            pantalla.insert(0, statistics.mean(datos))
        else:
            pantalla.insert(0, "ERROR NO HAY DATOS CARGADOS")
    
    elif operacion == "Mo":
        if len(datos)>0:
            #devuelve la mediana
            print("la moda es: ", statistics.mode(datos))
            pantalla.insert(0, statistics.mode(datos))
        else:
            pantalla.insert(0, "ERROR NO HAY DATOS CARGADOS")
    
    elif operacion == "Me":
        if len(datos)>0:
            #devuelve la mediana
            print("la mediana es: ", statistics.median(datos))
            pantalla.insert(0, statistics.median(datos))
        else:
            pantalla.insert(0, "ERROR NO HAY DATOS CARGADOS")
    
    elif operacion == "M-":    
        if len(datos)==0:
            pantalla.insert(0, "DATOS BORRADOS")
    
    elif operacion == "CargarDatos":    
        if len(datos)>0:
            pantalla.insert(0, datos)
    
    else:
        pantalla.insert(0, "Presione Botones")



root=Tk()
root.resizable(0,0)
root.config(bg="black")
root.title("Calculadora")

# MARCO o FRAME
marco=Frame(root,bg="violet",width="650",height="350")
marco.pack(fill="none",expand="True")

pantalla=Entry(marco)
pantalla.grid(row=0,columnspan=5,sticky=W+E,pady=5,padx=3)
pantalla.config(bg="lightblue",fg="black",width=30,font=("Arial",18,'bold'),borderwidth=2,relief="solid",
               justify=RIGHT)

#BUTTONS NUMEROS

boton_1=Button(marco,text="1",command=lambda:envia_boton(1))
boton_1.grid(row=6,column=0,sticky=W+E,pady=1,padx=1)
boton_1.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_2=Button(marco,text="2",command=lambda:envia_boton(2))
boton_2.grid(row=6,column=1,sticky=W+E,pady=1,padx=1)
boton_2.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_3=Button(marco,text="3",command=lambda:envia_boton(3))
boton_3.grid(row=6,column=2,sticky=W+E,pady=1,padx=1)
boton_3.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_4=Button(marco,text="4",command=lambda:envia_boton(4))
boton_4.grid(row=5,column=0,sticky=W+E,pady=1,padx=1)
boton_4.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_5=Button(marco,text="5",command=lambda:envia_boton(5))
boton_5.grid(row=5,column=1,sticky=W+E,pady=1,padx=1)
boton_5.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_6=Button(marco,text="6",command=lambda:envia_boton(6))
boton_6.grid(row=5,column=2,sticky=W+E,pady=1,padx=1)
boton_6.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_7=Button(marco,text="7",command=lambda:envia_boton(7))
boton_7.grid(row=4,column=0,sticky=W+E,pady=1,padx=1)
boton_7.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_8=Button(marco,text="8",command=lambda:envia_boton(8))
boton_8.grid(row=4,column=1,sticky=W+E,pady=1,padx=1)
boton_8.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_9=Button(marco,text="9",command=lambda:envia_boton(9))
boton_9.grid(row=4,column=2,sticky=W+E,pady=1,padx=1)
boton_9.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_0=Button(marco,text="0",command=lambda:envia_boton(0))
boton_0.grid(row=7,column=1,columnspan=2,sticky=W+E,pady=1,padx=1)
boton_0.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#BUTTONS OPERACIONES

#Boton borrar
boton_AC=Button(marco,text="AC",command=borrar)
boton_AC.grid(row=4,column=4,sticky=W+E,pady=1,padx=1)
boton_AC.config(width=5,height=2, bg="red",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton M+
boton_M=Button(marco,text="M+",command=cargar_datos)
boton_M.grid(row=5,column=4,sticky=W+E,pady=1,padx=1)
boton_M.config(width=5,height=2, bg="red",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton M-
boton_B=Button(marco,text="M-",command=borrar_Datos)
boton_B.grid(row=5,column=3,sticky=W+E,pady=1,padx=1)
boton_B.config(width=5,height=2, bg="black",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton suma
boton_Suma=Button(marco,text="+",command=suma)
boton_Suma.grid(row=6,column=3,sticky=W+E,pady=1,padx=1)
boton_Suma.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton resta
boton_Resta=Button(marco,text="-",command=resta)
boton_Resta.grid(row=6,column=4,sticky=W+E,pady=1,padx=1)
boton_Resta.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton multiplicacion
boton_Mult=Button(marco,text="*",command=multiplicacion)
boton_Mult.grid(row=7,column=3,sticky=W+E,pady=1,padx=1)
boton_Mult.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton division
boton_Div=Button(marco,text="/",command=division)
boton_Div.grid(row=7,column=4,sticky=W+E,pady=1,padx=1)
boton_Div.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton flecha
boton_Borrar=Button(marco,text="←",command=borrar_uno)
boton_Borrar.grid(row=4,column=3,sticky=W+E,pady=1,padx=1)
boton_Borrar.config(width=5,height=2, bg="red",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton varianza
boton_Varianza=Button(marco,text="σ2",command=varianza)
boton_Varianza.grid(row=2,column=3,sticky=W+E,pady=1,padx=1)
boton_Varianza.config(width=5,height=2, bg="orange",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton desviacion estandar
boton_Desviacion=Button(marco,text="σ",command=desviacion_estandar)
boton_Desviacion.grid(row=2,column=4,sticky=W+E,pady=1,padx=1)
boton_Desviacion.config(width=5,height=2, bg="orange",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton media
boton_Media=Button(marco,text="X",command=media)
boton_Media.grid(row=2,column=0,sticky=W+E,pady=1,padx=1)
boton_Media.config(width=5,height=2, bg="orange",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton moda
boton_Moda=Button(marco,text="Mo",command=moda)
boton_Moda.grid(row=2,column=2,sticky=W+E,pady=1,padx=1)
boton_Moda.config(width=5,height=2, bg="orange",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton mediana
boton_Media=Button(marco,text="Me",command=mediana)
boton_Media.grid(row=2,column=1,sticky=W+E,pady=1,padx=1)
boton_Media.config(width=5,height=2, bg="orange",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton sin
boton_seno=Button(marco,text="sin",command=seno)
boton_seno.grid(row=3,column=2,sticky=W+E,pady=1,padx=1)
boton_seno.config(width=5,height=2, bg="green",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton cos
boton_coseno=Button(marco,text="cos",command=coseno)
boton_coseno.grid(row=3,column=3,sticky=W+E,pady=1,padx=1)
boton_coseno.config(width=5,height=2, bg="green",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton tangente
boton_tangente=Button(marco,text="tan",command=tangente)
boton_tangente.grid(row=3,column=4,sticky=W+E,pady=1,padx=1)
boton_tangente.config(width=5,height=2, bg="green",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton potencia
boton_Pot=Button(marco,text="^",command=potencia)
boton_Pot.grid(row=3,column=0,sticky=W+E,pady=1,padx=1)
boton_Pot.config(width=5,height=2, bg="green",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton raiz
boton_raiz=Button(marco,text="√",command=raiz)
boton_raiz.grid(row=3,column=1,sticky=W+E,pady=1,padx=1)
boton_raiz.config(width=5,height=2, bg="green",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton punto 
boton_Punto=Button(marco,text=".",command=lambda:envia_boton())
boton_Punto.grid(row=7,column=0,sticky=W+E,pady=1,padx=1)
boton_Punto.config(width=5,height=2, bg="blue",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton igual
boton_igual=Button(marco,text="=",command=igual)
boton_igual.grid(row=8,column=0,columnspan=3,sticky=W+E,pady=1,padx=1)
boton_igual.config(width=5,height=2, bg="black",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton carga datos
boton_datos=Button(marco,text="CargarDatos",command=lambda:cargar_datos())
boton_datos.grid(row=8,column=3,columnspan=3,sticky=W+E,pady=1,padx=1)
boton_datos.config(width=5,height=2, bg="gold2",fg="black",font=("Arial",10),cursor="hand2",borderwidth=3, relief="ridge")

root.mainloop()