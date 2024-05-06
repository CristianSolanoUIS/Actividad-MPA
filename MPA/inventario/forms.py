from django import forms
from .models import Cambio_Stock


class ProductoForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Cambio_Stock

        fields = [
            'id_producto',
            'cantidad',
            'comentario'
        ]

        labels = {
            'id_producto':'Producto',
            'cantidad':'Cantidad',
            'comentario':'Comentario'
        }

        widgets = {
            'id_producto':forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
            'comentario':forms.TextInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['id_producto'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}