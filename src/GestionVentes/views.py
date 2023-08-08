from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Materiel,Employee,Etablissement,Emplacement
from .forms import materielForm,employeForm,etablissementForm,emplacementForm
def homePage(request):
    return render(request,"home.html",{"navbar":'home'})


# Materiels
def materiel(request):
    all_materiel = Materiel.objects.all()
    return render(request,"materiels/index.html",{"materiels": all_materiel,"navbar":'materiel'})


def load_form_materiel(request):
    form = materielForm()
    return render(request, "materiels/add.html",{'form':form,"navbar":'materiel'})
def add_materiel(request):
    form = materielForm(request.POST)
    form.save()
    return redirect('materiel')
def edit_materiel(request, id):
    materiel = Materiel.objects.get(id=id)
    return render(request,'materiels/edit.html',{'materiel':materiel,"navbar":'materiel'})
def update_materiel(request, id):
    materiel = Materiel.objects.get(id=id)
    form = materielForm(request.POST, instance=materiel)
    form.save()
    return redirect('materiel')
def delete_materiel(request, id):
    materiel = Materiel.objects.get(id=id)
    materiel.delete()
    return redirect('materiel')




# Employees
def employe(request):
    all_employe= Employee.objects.all()
    return render(request,"employees/index.html",{"employes": all_employe,"navbar":'employe'})


def load_form_employe(request):
    form = employeForm()
    return render(request, "employees/add.html",{'form':form,"navbar":'employe'})
def add_employe(request):
    form = employeForm(request.POST)
    form.save()
    return redirect('employe')
def edit_employe(request, id):
    employe = Employee.objects.get(id=id)
    return render(request,'employees/edit.html',{'employe':employe,"navbar":'employe'})
def update_employe(request, id):
    employe = Employee.objects.get(id=id)
    form = employeForm(request.POST, instance=employe)
    form.save()
    return redirect('employe')
def delete_employe(request, id):
    employe = Employee.objects.get(id=id)
    employe.delete()
    return redirect('employe')


# Etablissement
def etablissement(request):
    all_etablissement= Etablissement.objects.all()
    return render(request,"etablissements/index.html",{"etablissements": all_etablissement,"navbar":'etablissement'})

def load_form_etablissement(request):
    form = etablissementForm()
    return render(request, "etablissements/add.html",{'form':form,"navbar":'etablissement'})
def add_etablissement(request):
    form = etablissementForm(request.POST)
    form.save()
    return redirect('etablissement')
def edit_etablissement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    return render(request,'etablissements/edit.html',{'etablissement':etablissement,"navbar":'etablissement'})
def update_etablissement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    form = etablissementForm(request.POST, instance=etablissement)
    form.save()
    return redirect('etablissement')
def delete_etablissement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    etablissement.delete()
    return redirect('etablissement')

# Etablissement
def emplacement(request):
    all_emplacement= Emplacement.objects.all()
    return render(request,"emplacements/index.html",{"emplacements": all_emplacement,"navbar":'emplacement'})

def load_form_emplacement(request):
    all_employe = Employee.objects.all()
    all_etablissement = Etablissement.objects.all()
    form = emplacementForm()
    return render(request, "emplacements/add.html",{'form':form,"navbar":'etablissement','employes':all_employe,'etablissements':all_etablissement})
def add_emplacement(request):
    form = emplacementForm(request.POST)
    form.save()
    return redirect('emplacement')
def edit_emplacement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    return render(request,'etablissements/edit.html',{'etablissement':etablissement,"navbar":'etablissement'})
def update_etablissement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    form = etablissementForm(request.POST, instance=etablissement)
    form.save()
    return redirect('etablissement')
def delete_etablissement(request, id):
    etablissement = Etablissement.objects.get(id=id)
    etablissement.delete()
    return redirect('etablissement')
