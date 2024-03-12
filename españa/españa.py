 def __init__(self):
        self.ventana1=tk.Tk()
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=0)
        self.scroll1.configure(command=self.listbox1.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')        
        self.listbox1.insert(0,"España")
        self.listbox1.insert(1,"Francia")
        self.listbox1.insert(2,"Alemania")
        self.listbox1.insert(3,"Inglaterra")
        self.listbox1.insert(4,"Holanda")
        self.listbox1.insert(5,"Italia")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1=Aplicacion()
