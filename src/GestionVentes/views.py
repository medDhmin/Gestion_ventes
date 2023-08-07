from django.shortcuts import render

def homePage(request):
    return render(request,"home.html")

def matriel(request):
    return render(request,"matriel.html")
def etablisement(request):
    return  render(request,"etablisement.html")

def employes(request):
    return  render(request,"employes.html")

def emplacement(request):
    return render(request,"emplacement.html")