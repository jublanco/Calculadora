from tkinter import *

boton=""
    #hacemos las 3 funciones que va a hacer nuestra calculadora

def digito(num):#con esta funcion hacemos que nos guarde toda la expreison matematica, lo guardara y despues lo mostrara en el campo de datos
    global boton #con estohacemos que sea para todos los que tienen nombre boton

    boton=boton+str(num)
    calculo.set(boton)
def igual():#esta funcion procesa todo con la funcion eval y nos muestra el resultado
    try:
        global boton

        cero=re.search("/0",boton)
        if cero:
            calculo.set("No se puede dividir por 0")
        else:
            total=str(eval(boton))
            calculo.set(total)
            boton=""
    except:
        calculo.set("error")
def limpiar():#es igual que digito pero en ves de mostrar el calculo nos devuelve un campo vacio
    calculo.set("")

def teclado(event):#esta funcion hara que se tomen los digitos tambien del teclado y no solo con el mouse
    digito(event.char)# a su vez esta función hace una llamada a la función digito(), y dentro de esta función enviamos los datos contenidos en event.char, char es el método que sirve para indicar que lo que queremos enviar es el carácter del objeto event.

if __name__ == "__main__":
    
    ventana = Tk() #con esto creamos la ventana
#agregamos varios metodos a la ventana
    ventana.configure(background="black") #aca lo que le puse es un color al background
    ventana.title("calculadora")#con esto le ponemos un titulo a la ventana
    ventana.geometry("195x245")#con esto le decimos el tamañano que tendra la ventana
    
    #agregamos 3 metodos mas pero del tipo entry es decir donde podemos escribir
    calculo = StringVar() #creamos una variable llamada calculo que lo convierte en cadena
    datos = Entry(ventana, textvariable=calculo, bg="black", fg="green") #crea el campo donde veremos los numeros y los calculos
    datos.grid(columnspan=10, ipadx=50, ipady=10)#con esto usamos el metodo grid para darle una ubicacion a ese campo


    #Hacemos los botones con la funciona Button

    boton1 = Button(ventana, text="1", fg="black", bg="white", #con esto creamos el boton en la ventana,le damos el texto como es el boton 1 va a ser 1, con fg le damos color a ese texto, y bg es el color del background
    command=lambda: digito(1), height=2, width=5) #comando le ponemos lambda porque esto nos permitos pasar distintos parametros para una sola funcion y despues le damos en px lel ancho y el alto

    boton1.grid(row=2, column=0)

    boton2 = Button(ventana, text="2", fg="black", bg="white",
    command=lambda: digito(2), height=2, width=5)

    boton2.grid(row=2, column=1)

    boton3 = Button(ventana, text="3", fg="black", bg="white",
    command=lambda: digito(3), height=2, width=5)

    boton3.grid(row=2, column=2)

    
    boton4 = Button(ventana, text="4", fg="black", bg="white",
    command=lambda: digito(4), height=2, width=5)

    boton4.grid(row=3, column=0)

    boton5 = Button(ventana, text="5", fg="black", bg="white",
    command=lambda: digito(5), height=2, width=5)

    boton5.grid(row=3, column=1)
    
    boton6 = Button(ventana, text="6", fg="black", bg="white",
    command=lambda: digito(6), height=2, width=5)

    boton6.grid(row=3, column=2)
    
    boton7 = Button(ventana, text="7", fg="black", bg="white",
    command=lambda: digito(7), height=2, width=5)

    boton7.grid(row=4, column=0)
    
    boton8 = Button(ventana, text="8", fg="black", bg="white",
    command=lambda: digito(8), height=2, width=5)

    boton8.grid(row=4, column=1)

    boton9 = Button(ventana, text="9", fg="black", bg="white",
    command=lambda: digito(9), height=2, width=5)

    boton9.grid(row=4, column=2)

    boton0 = Button(ventana, text="0", fg="black", bg="white",
    command=lambda: digito(0), height=2, width=5)

    boton0.grid(row=5, column=0)
    
    suma = Button(ventana, text="+", fg="black", bg="white",
    command=lambda: digito("+"), height=2, width=5)

    suma.grid(row=2, column=3)
    
    resta = Button(ventana, text="-", fg="black", bg="white",
    command=lambda: digito("-"), height=2, width=5)

    resta.grid(row=3, column=3)

    multiplica = Button(ventana, text="*", fg="black", bg="white",
    command=lambda: digito("*"), height=2, width=5)

    multiplica.grid(row=4, column=3)
    
    divide = Button(ventana, text='/', fg='black', bg='white',
    command=lambda: digito("/"), height=2, width=5)

    divide.grid(row=5, column=3)

    resultado = Button(ventana, text=' = ', fg='black', bg='white',
    command=igual, height=2, width=5) #en este caso el comando que le damos es el igual para que de el resultado del calculo

    resultado.grid(column=2, columnspan=2, ipadx=24)

    limpiar = Button(ventana, text='Limpiar', fg='black', bg='white',
    command=limpiar, height=2, width=5) #en este caso el comando es que limpie todo el resultado

    limpiar.grid(row=5, column=1)

    punto = Button(ventana, text='.', fg='black', bg='white',
    command=lambda: digito("."), height=2, width=5)

    punto.grid(row=5, column=2)

    parentesis1 = Button(ventana, text='(', fg='black', bg='white',
    command=lambda: digito("("), height=2, width=5)

    parentesis1 .grid(row=6, column=0)

    parentesis2 = Button(ventana, text=')', fg='black', bg='white',
    command=lambda: digito(")"), height=2, width=5)

    parentesis2 .grid(row=6, column=1)

    ventana.bind("<Return>", lambda event: igual())#con esto hacemos que la tecla enter haga la funcion igual

    ventana.bind("<Key>", teclado)#bind es el objeto al cual le decimos que capture "<Key>" es decir cualquier key(tecla), y que cuando lo haga añada una llamada a la función que creamos anteriormente llamada "teclado"

    ventana.mainloop()#si no lo agregamos este metodo la ventana se cerraria ni bien arranca, asi que creamos un loop, es decir un bucle