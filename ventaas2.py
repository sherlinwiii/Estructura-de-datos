class Ventas:
    def __init__(self):
  
        self.departamentos = [[0] * 12 for _ in range(3)]
        self.nombres_departamentos = ["ropa", "deportes", "jugueteria"]
    
    def obtener_indice_departamento(self, nombre):
        """Convierte el nombre del departamento en un índice de la lista."""
        if nombre in self.nombres_departamentos:
            return self.nombres_departamentos.index(nombre)
        return None
    
    def insertar_venta(self, departamento, mes, monto):
        """Inserta una venta en el departamento y mes especificado."""
        indice = self.obtener_indice_departamento(departamento)
        if indice is not None and 1 <= mes <= 12:
            self.departamentos[indice][mes - 1] = monto
        else:
            print("Error: Departamento o mes inválido.")
    
    def buscar_venta(self, departamento, mes):
        """Busca la venta de un departamento en un mes específico."""
        indice = self.obtener_indice_departamento(departamento)
        if indice is not None and 1 <= mes <= 12:
            return self.departamentos[indice][mes - 1]
        print("Error: Departamento o mes inválido.")
        return None
    
    def eliminar_venta(self, departamento, mes):
        """Elimina (pone en 0) la venta de un departamento en un mes específico."""
        indice = self.obtener_indice_departamento(departamento)
        if indice is not None and 1 <= mes <= 12:
            self.departamentos[indice][mes - 1] = 0
        else:
            print("Error: Departamento o mes inválido.")
    
    def mostrar_ventas(self):
        """Muestra todas las ventas organizadas en una tabla."""
        print("\nTabla de Ventas Mensuales")
        print("Mes        Ropa    Deportes    Jugueteria")
        print("----------------------------------------")
        for mes in range(12):
            print(f"{mes+1: <10}{self.departamentos[0][mes]: <8}{self.departamentos[1][mes]: <12}{self.departamentos[2][mes]}")
    
    def ingresar_datos_usuario(self):
        """Permite al usuario ingresar ventas manualmente."""
        while True:
            print("\nIngrese los datos de la venta (o escriba 'salir' para terminar):")
            departamento = input("Departamento (ropa, deportes, jugueteria): ").lower()
            if departamento == "salir":
                break
            mes = input("Mes (1-12): ")
            monto = input("Monto de la venta: ")
            
            if mes.isdigit() and monto.isdigit():
                mes = int(mes)
                monto = int(monto)
                self.insertar_venta(departamento, mes, monto)
            else:
                print("Error: Ingrese valores numéricos válidos para el mes y monto.")
    
    def buscar_venta_usuario(self):
        """Permite al usuario buscar una venta manualmente."""
        departamento = input("Ingrese el departamento a buscar (ropa, deportes, jugueteria): ").lower()
        mes = input("Ingrese el mes (1-12): ")
        
        if mes.isdigit():
            mes = int(mes)
            venta = self.buscar_venta(departamento, mes)
            if venta is not None:
                print(f"La venta en {departamento} en el mes {mes} fue: {venta}")
        else:
            print("Error: Ingrese un número de mes válido.")
    
    def eliminar_venta_usuario(self):
        """Permite al usuario eliminar una venta manualmente."""
        departamento = input("Ingrese el departamento a eliminar (ropa, deportes, jugueteria): ").lower()
        mes = input("Ingrese el mes (1-12): ")
        
        if mes.isdigit():
            mes = int(mes)
            self.eliminar_venta(departamento, mes)
            print(f"Venta eliminada en {departamento} en el mes {mes}.")
        else:
            print("Error: Ingrese un número de mes válido.")

ventas = Ventas()
ventas.ingresar_datos_usuario()
ventas.mostrar_ventas()
ventas.buscar_venta_usuario()
ventas.eliminar_venta_usuario()
ventas.mostrar_ventas()
