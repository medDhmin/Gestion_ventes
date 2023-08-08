"""
URL configuration for GestionVentes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from . import views
urlpatterns = [
    # administration
    path('admin/', admin.site.urls),

    # tableau de borde
    path('home/', views.homePage, name="home"),

    # l'authentification
    path('', include("accounts.urls")),

    # Materiels
    path('materiel/', views.materiel, name="materiel"),
    path('add_materiel/', views.load_form_materiel,name="add_materiel"),
    path('get_add_materiel/', views.add_materiel),
    path('edit_materiel/<int:id>', views.edit_materiel,name="edit_materiel"),
    path('update_materiel/<int:id>', views.update_materiel,name="update_materiel"),
    path('delete_materiel/<int:id>', views.delete_materiel,name="delete_materiel"),

    # Employees
    path('employe/', views.employe, name="employe"),
    path('add_employe/', views.load_form_employe, name="add_employe"),
    path('get_add_employe/', views.add_employe),
    path('edit_employe/<int:id>', views.edit_employe, name="edit_employe"),
    path('update_employe/<int:id>', views.update_employe, name="update_employe"),
    path('delete_employe/<int:id>', views.delete_employe, name="delete_employe"),

    # etablissements
    path('etablissement/', views.etablissement, name="etablissement"),
    path('add_etablissement/', views.load_form_etablissement, name="add_etablissement"),
    path('get_add_etablissement/', views.add_etablissement),
    path('edit_etablissement/<int:id>', views.edit_etablissement, name="edit_etablissement"),
    path('update_etablissement/<int:id>', views.update_etablissement, name="update_etablissement"),
    path('delete_etablissement/<int:id>', views.delete_etablissement, name="delete_etablissement"),

    # emplacement
    path('emplacement/', views.emplacement, name="emplacement"),
    path('add_emplacement/', views.load_form_emplacement, name="add_emplacement"),
    path('get_add_emplacement/', views.add_emplacement),
    path('edit_etablissement/<int:id>', views.edit_etablissement, name="edit_etablissement"),
    path('update_etablissement/<int:id>', views.update_etablissement, name="update_etablissement"),
    path('delete_etablissement/<int:id>', views.delete_etablissement, name="delete_etablissement"),

]
