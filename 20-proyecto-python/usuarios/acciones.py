import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Cual es tu emai?: ")
        password = input("¿Cuales son tus contrtaseñas?: ")
        
        usuario = modelo.Usuario(nombre, apellidos,email,password)
        registro = usuario.registrar()
        
        if registro[0]>=1:
            print(f"Perfecto {registro[1].nombre} con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        print("\nIdentificate en el sistema ... ")
        #try:
        email = input("Email: ")
        password = input("Contraseña: ")
        
        usuario = modelo.Usuario('','', email, password)
        login = usuario.identificar()
        
        if email == login[3]:
            print(f"Bienvenido {login[1]}, te has registrado en el sistema, usuario desde {login[5]}")
            self.proximasAcciones(login)
    
        
        #except:
        print("Datos no validos")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles:
            - Crear nota (crear)
            - Mostar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)
        
        accion = input("¿Que deseas hacer ?: ")
        hazEl = notas.acciones.Acciones()
        if accion == "crear":
            print("Vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion =="mostrar":
            print("Vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminar":
            print("vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            exit()