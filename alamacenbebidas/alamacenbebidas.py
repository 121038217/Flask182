listabebidas=[]
class almacen(object): #declaro mi clase que va contener objetos
    def __init__(self,_Id,_nombre,_precio,_clasificacion,_marca): #init nos permite asignar atributos
        self.Id = _Id
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        self.historial = []
    
    def entregarinformacion(self):
        print("ID: {} -{} {} -{} - {}".format(self.Id,self.nombre,self.precio,self.clasificacion,self.marca))
    
    def actualizarinformacion(self,_nombre,_precio,_clasificacion,_marca):
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        print("Informacion actualizada")
        
    def incluirEvento(self,_nombre,_precio,_clasificacion,_marca): #creamos metodo para poder mostrar un mensaje con la modificacion
        #return ejecuta la última instrucción del programa y el programa termina.
        return("Modificacion: nombre: {} - precio: {} - clasificcion: {} - marca: {} ".format(_nombre,_precio,_clasificacion,_marca))

def DarAlta():
    print("Dar de alta bebida")
    Id = int(input("Ingresar ID: "))
    nombre = str(input("Ingresar nombre de la bebida:"))
    precio = float(input("Ingresa el precio de la bebida: "))
    clasificacion = str(input("Ingresar la clasificacion: "))
    marca = str(input("Ingresa la marca: "))
    objbebida= almacen(Id,nombre,precio,clasificacion,marca)
    listabebidas.append(objbebida)
        
def DarBaja():
    print("Darde Baja bebida")
    Id = int(input("Ingresar ID: "))
    objbebida = almacen(Id)
    listabebidas.append(objbebida)
    
def mostrar():
    print("Lista de bebidas")
    for objbebida in listabebidas: #ciclo for recorre todos lo lugares dentro de la lista
        objbebida.entregarinformacion()
    
def actualizar():
    print("Modificacion de la bebida")
    Id = int(input("Ingrese el ID: "))
    for objbebida in listabebidas:
        if Id == objbebida.Id:
            nombre = str(input("Ingrese el nuevo nombre: "))
            precio = float(input("Ingrese el nuevo precio: "))
            clasificacion = str(input("Ingrese la nueva calificacion: "))
            marca = str(input("Ingrese la nueva marca: "))
            objbebida.actualizarinformacion(nombre,precio,clasificacion,marca)
            objbebida.entregarinformacion()
            recepcionmensaje=objbebida.incluirEvento(nombre,precio,clasificacion,marca)
            objbebida.historial.append(recepcionmensaje)

def PrecioPromedio():
    print("Calcular precio promedio de bebidas")
    resultado = sum(objbebida.precio/listabebidas)
    print("Precio promedio de bebida es: ".format(total))
    
def BebidasMarca():
    print("Cantidad de bebidas de una marca")
    
def Clasificacion():
    print("cantidad por clasificacion")

def salir():
    print("Salir del programa")
    exit()

def main():  #main es el metodo principal donde uniremos todos los metodos para que realice diferentes funciones
        while True:
            print("             MENU          ")
            print("1.- Dar de alta")
            print("2.- Dar de baja")
            print("3.- Actualizar")
            print("4.- Mostrar")
            print("5.- calcular precio promedio de bebidas")
            print("6.- cantidad de bebidas de una marca")
            print("7.- cantidad por clasificacion")
            print("8.- Salir del programa")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                DarAlta()
                print("Se ha guardado exitosamente")
            elif opcion == 2:
                DarBaja()
            elif opcion == 3:
                actualizar()
            elif opcion == 4:
                mostrar()
            elif opcion == 5:
                PrecioPromedio()
            elif opcion == 6:
                BebidasMarca()
            elif opcion == 7:
                Clasificacion()
            elif opcion == 8:
                salir()

if __name__=='__main__':
    main()