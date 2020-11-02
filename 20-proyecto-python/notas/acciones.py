import notas.nota as modelo


class Acciones:
    
    def crear(self, usuario):
        print(f"ok! {usuario[1]}!! Vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de la nota : ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1 :
            print(f"\n Has guardado la nota {nota.titulo}")
        else:
            print(f"\n No se ha guardardo la nota {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n*****************")
            print("Titulo :", nota[2])
            print("Descripcion :", nota[3])
            
    def borrar(self, usuario):
        print(f"\n OKEy {usuario[1]}!!! Vamos a borrar la nota")
        
        titulo = input("Introduce la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("NO se ha borrado la nota")