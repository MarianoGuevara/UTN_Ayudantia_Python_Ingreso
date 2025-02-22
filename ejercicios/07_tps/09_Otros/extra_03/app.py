import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
from os import system 
system("cls")

'''
Enunciado:

Una importante empresa dediada a la produccion de alfajores nos solicita una aplicacion que les 
permita controlar la produccion, dicha aplicacion contara con dos botones 

    - ALFAJOR ACEPTADO
    - ALFAJOR DESCARTADO

Mediante los cuales se registrara la cantidad total de alfajores producidos. 

Por tratarse de una produccion artesanal, cada alfajor puede variar su peso, por lo cual es importante
poder registrar el mismo al momento ACEPTARLO o DESCARTARLO. Los pesos deberan ser numeros flotantes 
positivos.

Receta en gramos:
Harina 000	         -   20
Almidón de Maíz	     -   5
Manteca	             -   10
Azúcar		         -   10
Cacao Amargo	     -   0.75
Polvo de hornear     -   0.5
Miel	             -   1
Extracto de Vainilla - 	 0.25
Huevo (gr)	         -   5
Dulce de Leche       -	 25


Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Cantidad total de alfajores fabricados
	B - Cantidad total de alfajores aceptados
	C - Cantidad total de alfajores rechazados
	D - Peso promedio de los alfajores aceptados
	E - Peso promedio de los alfajores rechazados
    F - Materia prima total utilizada * -> acumulador de peso en gramos
    E - Materia prima total desperdiciada * -> acumulador de peso en gramos 

    *(Tener en cuenta que la cocion produce una merma de 15% del peso)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, 
                                                placeholder_text="Peso Alfajor")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.btn_aceptar = customtkinter.CTkButton(master=self, text="ACEPTAR", 
                                            command=self.btn_aceptar_o_reject)
        self.btn_aceptar.grid(row=2, pady=10, columnspan=2, sticky="news")

        self.btn_rechazar = customtkinter.CTkButton(master=self, 
                                    text="RECHAZAR", command=self.btn_aceptar_o_reject)
        self.btn_rechazar.grid(row=3, pady=10, columnspan=2, sticky="news")

        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, 
                                                text="Generar Informe de Notas",
                                                command=self.btn_generar_informe_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")

        self.lista_pesos_rechazados = []
        self.lista_pesos_aceptados = []


    def btn_aceptar_o_reject(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()    