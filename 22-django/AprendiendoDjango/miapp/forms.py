from django import forms
from django.core import validators

class FormArticle(forms.Form):
    
    
    title =  forms.CharField(
        label = "Titulo",
        max_length=20,
        required=True,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Mete el titulo',
                'class' : ' titulo_form_article'
            }
        ),
        validators =[
            validators.MinLengthValidator(4, 'El titulo es demasiado Corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )
    
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        required=False
    )
    
    
    public_options=[
        (1, 'Si'),
        (0, 'No')
    ]
    
    public = forms.TypedChoiceField(
        label = "¿Publicooooooo?",
        choices = public_options       
    )