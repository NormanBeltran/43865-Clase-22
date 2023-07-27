from django import forms 

class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Curso", max_length=50, required=True)
    comision = forms.IntegerField(label="Comision", required=True)
    email = forms.EmailField(label="Email", required=False)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )
    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)
    becado = forms.BooleanField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email")
    profesion = forms.CharField(label="Profesion", max_length=50, required=True)