from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#MVC Modelo Vista Controlador
#MVT Modelo Vista Template

layout = """

"""
lenguajes = ["Java", "Python", "PHP"]
def prueba(request):
        return HttpResponse("""
                            <h1> Esto es una prueba </h1>
                            """)
def index(request):
    html = """
                        <h1> Inicio <h1>
                        <p> Años hasta 2050 </p>
                        <lu>
                        """
    year = 2021
    while year <= 2050:
        if year%2 ==0 : 
            html += f"<li> {str(year)} </li>"
            
        year += 1
    html += "</lu>"
    return render(request,"index.html",{
        'mi_variable' :' Soy un dato que esta en la vista',
        'title':'Esto es el titulo',
        'lenguajes':lenguajes
        
    })

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request,redirigir=0):
    
    if redirigir==1:
        return redirect('contacto',nombre="manolo", apellidos="El del bombo")
    
    return render(request,'pagina.html')


def contacto(request, nombre="", apellidos=""):
    html = ""
    
    if nombre and apellidos:
        html += f"<h3> {nombre} {apellidos}</h3>"
    
    
    return HttpResponse(layout+f"<h2>Contacto</h2>" + html )