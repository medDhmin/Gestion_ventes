from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Materiel,Employee,Etablissement,Emplacement,Affectation
from .forms import materielForm,employeForm,etablissementForm,emplacementForm,affectationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homePage(request):
    return render(request,"home.html",{"navbar":'home'})
@login_required(login_url='login')


# Materiels
def materiel(request):
    materiels = Materiel.objects.all()
    for materiel in materiels:
        affectations = Affectation.objects.filter(id_materiel=materiel)
        emplacements = [affectation.id_emplacement.designation for affectation in affectations]
        materiel.emplacements = emplacements
    return render(request,"materiels/index.html",{"materiels": materiels,"navbar":'materiel'})
@login_required(login_url='login')


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


# Affectation
def affectation(request):
    all_affectation = Affectation.objects.all()
    return render(request,"affectations/index.html",{"affectations": all_affectation,"navbar":'affectation'})

def load_form_affectation(request):
    all_materiel = Materiel.objects.all()
    all_emplacement = Emplacement.objects.all()
    form = affectationForm()
    return render(request, "affectations/add.html",{'form':form,"navbar":'affectation','materiels':all_materiel,'emplacements':all_emplacement})
def add_affectation(request):
    form = affectationForm(request.POST)
    form.save()
    return redirect('affectation')
def edit_affectation(request, id):
    all_materiel = Materiel.objects.all()
    all_emplacement = Emplacement.objects.all()
    affectation = Affectation.objects.get(id=id)
    form = affectationForm()
    return render(request,'affectations/edit.html',{'form':form,'affectation':affectation,"navbar":'affectation','materiels':all_materiel,'emplacements':all_emplacement})
def update_affectation(request, id):
    affectation = Affectation.objects.get(id=id)
    form = affectationForm(request.POST, instance=affectation)
    form.save()
    return redirect('affectation')
def delete_affectation(request, id):
    affectation = Affectation.objects.get(id=id)
    affectation.delete()
    return redirect('affectation')




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

# Emplacement
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
    all_employe = Employee.objects.all()
    all_etablissement = Etablissement.objects.all()
    emplacement = Emplacement.objects.get(id=id)
    form = emplacementForm()
    return render(request,'emplacements/edit.html',{'form':form,'emplacement':emplacement,"navbar":'emplacement','employes':all_employe,'etablissements':all_etablissement})
def update_emplacement(request, id):
    emplacement = Emplacement.objects.get(id=id)
    form = emplacementForm(request.POST, instance=emplacement)
    form.save()
    return redirect('emplacement')
def delete_emplacement(request, id):
    emplacement = Emplacement.objects.get(id=id)
    emplacement.delete()
    return redirect('emplacement')
