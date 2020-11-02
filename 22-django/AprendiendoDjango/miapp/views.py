from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from miapp.forms import FormArticle

# Create your views here.
#MVC Modelo Vista Controlador
#MVT Modelo Vista Template

layout = """

"""
lenguajes = ["Java", "Python", "PHP"]
nombre =  "Ruben Beltran"

def index(request):
    
    """
    html = 
                        <h1> Inicio <h1>
                        <p> Años hasta 2050 </p>
                        <lu>
                        
    year = 2021
    while year <= 2050:
        if year%2 ==0 : 
            html += f"<li> {str(year)} </li>"
            
        year += 1
    html += "</lu>"
    """
    year = 2020
    hasta = range(year,2051)
    
    
    
    
    
    
    
    return render(request,"index.html",{
        'mi_variable' :' Soy un dato que esta en la vista',
        'title':'Esto es el titulo',
        'lenguajes':lenguajes,
        'years':hasta,
        'nombre': nombre
        
    })

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request,redirigir=0):
    
    if redirigir==1:
        return redirect('contacto',nombre="manolo", apellidos="El del bombo")
    
    return render(request,'pagina.html', {
        'texto':'Hola',
        'lista':['uno','dos','tres']
})


def contacto(request, nombre="a", apellidos=""):
    html = ""
    
    if nombre and apellidos:
        html += f"<h3> {nombre} {apellidos}</h3>"
    
    
    return HttpResponse(layout+f"<h2>Contacto</h2>" + html )

def crear_articulo(request, title, content, public):
    articulo =  Article(
        title= title,
        content = content,
        public = public
    )
    
    articulo.save()
    return HttpResponse(f"Articulo Creado: <strong>{articulo.title} </strong> - {articulo.content}")


def articulo(request,id):
    try:
        articulo =  Article.objects.get(id=id)
        reponse = f"Articulo <strong>{articulo.title} </strong> - {articulo.content}"
    except:
        reponse = "Articulo No Encontrado"
    return HttpResponse(reponse)

def editar_articulo(request, id):
    articulo =  Article.objects.get(pk=id)
    
    articulo.title = "Articulo Batman"
    articulo.content= "Pelicula 2017"
    
    articulo.save()
    
    return HttpResponse(f"Articulo Modificado <strong>{articulo.title} </strong> - {articulo.content}")

def articulos(request):
    articulos =  Article.objects.all()
    
    
    
    return render(request,'articulos.html',{
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo =  Article.objects.get(pk=id)
    articulo.delete()
    
    return redirect('articulos')

def articulo_consulta(request):
    articulos =  Article.objects.raw("SELECT * FROM miapp_article WHERE title='Segundo Articulo' AND public=1")
    
    return render(request,'articulos.html',{
        'articulos': articulos
    })
    
def save_article(request):
    
    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        
        articulo =  Article(
            title= title,
            content = content,
            public = public
        )
        
        articulo.save()
        return HttpResponse(f"Articulo Creado: <strong>{articulo.title} </strong> - {articulo.content}")
    
    
    else:
        return HttpResponse("No ha sido posible")
    
    
def create_article(request):
    return render(request, 'create_article.html')

def create_article_full(request):
    
    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title= data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            
            articulo =  Article(
            title= title,
            content = content,
            public = public
            )
        
            articulo.save()
            return HttpResponse("HOLA SOY RUBEN " + title + ' ' + content + '  ' + str(public))
    else:
        formulario = FormArticle()
    
    return render (request, 'create_full_article.html', {
        'form' : formulario
    })