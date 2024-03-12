  def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Nombre")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,with=20, textvariable.self=self.dato)
        self.entry1.grid(column=1,row=0)
        self.label1.=tkk.Label(self.ventana1,text="Seleccione un pais")
        self.label1.grind(column=1,row=1)
        self.opcion=tk.StringVar()
        paises=("España","Alemania","Italia","Grecia","Holanda","Dinamarca","Francia")
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=10, 
                                  textvariable=self.opcion, 
                                  values=diassemana)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text="Visualizar", command=self.recuperar)
        self.boton1.grid(column=0, row=3)
        self.label2=ttk.Label(self.ventana1, text="Valores")
        self.label2.grid(column=0, row=4)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text='Valores'+ self.dato1.get()+':'+self.opcion.get())

aplicacion1=Aplicacion()
