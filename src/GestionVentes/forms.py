from django import forms
from accounts.models import Materiel,Employee,Etablissement,Emplacement,Affectation

# Materiel
class materielForm(forms.ModelForm):
    class Meta:
        model= Materiel
        fields = "__all__"

# Employees
class employeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = "__all__"

# Etablissement
class etablissementForm(forms.ModelForm):
    class Meta:
        model= Etablissement
        fields = "__all__"

class emplacementForm(forms.ModelForm):
    class Meta:
        model= Emplacement
        fields = "__all__"

class affectationForm(forms.ModelForm):
    class Meta:
        model= Affectation
        fields = "__all__"
