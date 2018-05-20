from django import forms
from appAdminAplicacion.models import *

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = aeropuerto
        exclude = ()
        field = [
            '',
            '',
            '',
            '',
        ]
        widgets = {
            
        }