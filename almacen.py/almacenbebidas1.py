listabebidas=[]
class almacen(object): #declaro mi clase que va contener objetos
    def __init__(self,_Id,_nombre,_precio,_clasificacion,_marca): #init nos permite asignar atributos
        self.Id = _Id
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        
    def DarAlta(self): #Metodo para dar de alta
        print("ID: {} -{} -{} -{} -{}".format(self.Id,self.nombre,self.precio,self.clasificacion,self.marca))
        
    def DarBaja(self,_Id): #Metodo para dar de baja
        self.Id = _Id
        print("bebida dada de baja")

    
    def Actualizar(self,_Id,_nombre,_precio,_clasificacion,_marca):
        self.Id = _Id
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        print("Informacion actualizada")

def mostrar():
    print("Mostrar informacion")
    for objbebida in listabebidas: #ciclo for recorre todos lo lugares dentro de la lista
        objbebida.DarBaja()
    
def PrecioPromedio():
    print("Calcular precio promedio de bebidas")
    resultado = str(_precio)
    print("Precio promedio de bebida".format(resultado))
    
def BebidasMarca():
    print("Cantidad de bebidas de una marca")
    
def Clasificacion():
    print("cantidad por clasificacion")