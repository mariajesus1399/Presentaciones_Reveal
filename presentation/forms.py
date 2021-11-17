from django import forms
from presentation.models import SeleccionUnica

class SeleccionUnicaForm(forms.ModelForm):
    
    class Meta:
        model = SeleccionUnica

        fields = [
            'user',
            'color',
            'vol',
        ]
        labels = {
            'user': 'Usuario',
            'color': 'Color',
            'vol': 'Volumen',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'vol': forms.TextInput(attrs={'class':'form-control'}),
        }