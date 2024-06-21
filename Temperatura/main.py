from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk

"""
.isdigit() comprobamos que sea un valor numerico

input.get() tomamos el valor del input

.current() tomamos la poscion de la lista

messagebox.showerror()
"""


def conversorTemperatura():
    #if not input_var.get().isdigit():
    #    messagebox.showerror("Error", "Debe ingresar solo Números Enteros")
    #    return   # isdigit(), no me permite ingresar numeros negativos ni decimales 
    # valor_temp = float(valorEntrada.get())
    
    try:
        valor_temp = float(valorEntrada.get())
    except ValueError:
        messagebox.showerror("Error ", "Debe ingresar solo Números")
        return

    variableDe = var_celsius.get()
    variableA = var_fahrenheit.get()

    if variableDe == variableA:  #    para comprobar si el usuario selecciona opciones iguales el resultado sea igual al valor ingresado
        resultado = valor_temp
    elif variableDe == "Celsius" and variableA == "Fahrenheit":
        resultado = (valor_temp * 9/5) + 32
    elif variableDe == "Fahrenheit" and variableA == "Celsius":
        resultado = (valor_temp - 32) * 5/9

    label_resultado.config(text=f"resultado: {resultado:.2f} {variableA}") #actualiza el texto mostrado en una etiqueta (label_resultado)
    

#ventana principal
ventana = Tk()
ventana.title("Convertidor Temperatura V0.1")
ventana.config(background="#4169e1")


titulo_label = Label(ventana, text="CONVERTIDOR TEMPERATURA", fg='white', bg='#4067dc', font=("Arial", 14, "bold"))
titulo_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)


# creando la variable de entrada
valorEntrada = StringVar()
valorEntrada = ttk.Entry(ventana, textvariable=valorEntrada) #ttk en tkinter proporciona widgets con aspecto mejorados.
valorEntrada.grid(column=1, row=1, padx=10, pady=10)

input_label = Label(ventana, text="Ingrese el valor de temperatura:", bg="#d9d9d9")
input_label.grid(column=0, row=1, padx=10, pady=10)

# Variables para poder usarlas en los combobox
var_celsius = StringVar(value="Celsius")
var_fahrenheit = StringVar(value="Fahrenheit")


# Listas desplegables para seleccionar la conversión
label_menu1 = ttk.Combobox(ventana, textvariable=var_celsius, values=["Celsius", "Fahrenheit"])
label_menu1.grid(column=1, row=2, padx=10, pady=10)

label_menu2 = ttk.Combobox(ventana, textvariable=var_fahrenheit, values=["Celsius", "Fahrenheit"])
label_menu2.grid(column=1, row=3, padx=10, pady=10)

label_De = Label(ventana, text="De:", bg="#d9d9d9")
label_De.grid(column=0, row=2, padx=10, pady=10)

label_A = Label(ventana, text="A:", bg="#d9d9d9")
label_A.grid(column=0, row=3, padx=10, pady=10)

# Botón para realizar la conversión
btn_convert = ttk.Button(ventana, text="Convertir", command=conversorTemperatura)
btn_convert.grid(column=1, row=4, padx=10, pady=10)

# Label para mostrar el reaultado
label_resultado = Label(ventana, text="resultado:")
label_resultado.grid(column=1, row=5, padx=10, pady=10)

# Centrar ventana
ventana.eval('tk::PlaceWindow . center')





ventana.mainloop()
