Este código es una aplicación simple para gestionar las ventas de tres departamentos a lo largo de un año. Permite al usuario agregar, buscar y eliminar ventas, todo organizado en una tabla

      Class Ventas
Este código define una clase que ayuda a crear objetos con ciertas caracteristicas y funcionamientos

         def __init__(self):
  
        self.departamentos = [[0] * 12 for _ in range(3)]
        self.nombres_departamentos = ["ropa", "deportes", "jugueteria"]
Este es el constructor de la clase, que se ejecuta cuando se crea un objeto de la clase.
self.departamentos: es una lista que tiene 3 sublistas una para cada departamento, y cada sublista tiene 12 valores inicializados en 0. Esto significa que para cada departamento tenemos los valores de venta de los 12 meses 
self.nombres_departamentos: es una lista con los nombres de los 3 departamentos ropa, deportes y juguetería
 
         def obtener_indice_departamento(self, nombre)
          if nombre in self.nombres_departamentos
            return self.nombres_departamentos.index(nombre)
        return None
Este método convierte el nombre de un departamento en un índice numérico para poder acceder fácilmente a las ventas de ese departamento en la lista departamentos. Si el nombre no está en la lista de departamentos, devuelve None.

         insertar_venta(self, departamento, mes, monto)
        def insertar_venta(self, departamento, mes, monto):
         indice = self.obtener_indice_departamento(departamento)
         if indice is not None and 1 <= mes <= 12:
         self.departamentos[indice][mes - 1] = monto
         else:
        print("Error: Departamento o mes inválido.")
Este método permite ingresar una venta en un departamento y mes específicos y es el metodo que permite insertar elementos enn el arreglo.Primero usa el método obtener_indice_departamento para conseguir el índice del departamento. Luego, se asegura de que el mes esté entre 1 y 12.
Si todo está bien, asigna el valor monto a la venta correspondiente en departamentos. Si el departamento o el mes no son válidos, imprime un mensaje de error.

       buscar_venta(self, departamento, mes)
      def buscar_venta(self, departamento, mes):
      indice = self.obtener_indice_departamento(departamento)
     if indice is not None and 1 <= mes <= 12:
        return self.departamentos[indice][mes - 1]
     print("Error: Departamento o mes inválido.")
    return None
Este método busca y devuelve la venta de un departamento en un mes específico y usa el método obtener_indice_departamento para obtener el índice del departamento, Verifica que el mes esté entre 1 y 12. Si todo es válido, devuelve el monto de la venta; si no, muestra un mensaje de error.
       eliminar_venta(self, departamento, mes)

      def eliminar_venta(self, departamento, mes):
     indice = self.obtener_indice_departamento(departamento)
      if indice is not None and 1 <= mes <= 12:
        self.departamentos[indice][mes - 1] = 0
    else:
        print("Error: Departamento o mes inválido.")
Este método elimina una venta, lo que significa poner el monto de la venta en 0 para un departamento y mes específicos y verifica que el departamento y mes sean válidos y luego cambia el valor a 0.

      mostrar_ventas(self)
     def mostrar_ventas(self):
    print("\nTabla de Ventas Mensuales")
    print("Mes        Ropa    Deportes    Jugueteria")
    print("----------------------------------------")
    for mes in range(12):
        print(f"{mes+1: <10}{self.departamentos[0][mes]: <8}{self.departamentos[1][mes]: <12}{self.departamentos[2][mes]}")
Este método muestra todas las ventas de forma organizada, como si fuera una tabla con los meses y los valores de cada departamento Uza un bucle para recorrer los 12 meses y mostrar los valores correspondientes.

       ingresar_datos_usuario(self)
      def ingresar_datos_usuario(self):
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
Este método permite al usuario ingresar ventas manualmente, pidiendo el nombre del departamento, el mes y el monto de la venta,si el usuario ingresa "salir", termina el ciclo. Si no, se asegura de que los valores del mes y el monto sean números válidos y luego llama al método insertar_venta para guardar los datos.
        buscar_venta_usuario(self)
       def buscar_venta_usuario(self):
       departamento = input("Ingrese el departamento a buscar (ropa, deportes, jugueteria): ").lower()
        mes = input("Ingrese el mes (1-12): ")
    
     if mes.isdigit():
        mes = int(mes)
        venta = self.buscar_venta(departamento, mes)
        if venta is not None:
            print(f"La venta en {departamento} en el mes {mes} fue: {venta}")
    else:
        print("Error: Ingrese un número de mes válido.")
Este método permite al usuario buscar una venta en un departamento y mes específicos Si el mes es válido, llama al método buscar_venta y muestra el resultado.
eliminar_venta_usuario(self)
def eliminar_venta_usuario(self):
    departamento = input("Ingrese el departamento a eliminar (ropa, deportes, jugueteria): ").lower()
    mes = input("Ingrese el mes (1-12): ")
    
    if mes.isdigit():
        mes = int(mes)
        self.eliminar_venta(departamento, mes)
        print(f"Venta eliminada en {departamento} en el mes {mes}.")
    else:
        print("Error: Ingrese un número de mes válido.")
Este método permite al usuario eliminar una venta de un departamento y mes específicos,Si el mes es válido, llama al método eliminar_venta y confirma que la venta fue eliminada.
