"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AQC import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'Home'),
    path('client/', views.client, name='Client'),
    path('services/', views.services, name='Services'),
    path('contact/', views.contact, name='Contact'), 
    path('feedback/', views.feedback, name= 'Feedback'),
    path('CompanyProfile/', views.CompanyProfile, name= 'CompanyProfile'),
    # path('industry/', views.Industry, name = 'Industry' ),
    
    path('standard/', views.Standard, name = 'Standard' ),
    path('consultancy/', views.Consultancy, name= 'Consultancy'),
    path('method/', views.Method, name= 'Method'),
    path('Inspection/', views.Inspection, name= 'Inspection'),
    path('PhotoGallery/', views.PhotoGallery, name='PhotoGallery'),
    path('Training/', views.Training, name = 'Training'),
    path('Compliance/', views.Compliance, name= 'Compliance'),
    path('SupplyChainImprovement/', views.SupplyChainImprovement, name='SupplyChainImprovement'),
    
    path('ISO90012015/', views.ISO90012015, name='ISO90012015'),
    path('ISO140012015/', views.ISO140012015, name= 'ISO140012015'),
    path('IATF/', views.IATF, name= 'IATF'),
    path('IRIS/', views.IRIS, name= 'IRIS'),
    path('5SImplementation/', views.SImplementation, name= '5SImplementation'),
    path('BRC/', views.BRC, name= 'BRC'),
    path('ISO450012018/', views.ISO450012018, name= 'ISO450012018'),
    path('FSSC/', views.FSSC, name= 'FSSC'),
    path('SA8000/', views.SA8000, name= 'SA8000'),
    path('HACCP/', views.HACCP, name= 'HACCP'),
    path('ISO27001/', views.ISO27001, name= 'ISO27001'),
    path('ISO150012018/', views.ISO150012018, name= 'ISO150012018'),
    path('BIOS55001', views.BIOS55001, name= 'BIOS55001'),
    path('AS91012014/', views.AS91012014, name= 'AS91012014'),
    path('ISO180012017OHSAS/', views.ISO180012017OHSAS, name = 'ISO180012017OHSAS'),
    
    path('KAIZEN/', views.KAIZEN, name = 'KAIZEN'),
    path('APQP/', views.APQP, name = 'APQP'),
    path('SIXSIGMA/', views.SIXSIGMA, name = 'SIXSIGMA'),
    path('POKAYOKA/', views.POKAYOKA, name = 'POKAYOKA'),
    path('WK/', views.WK, name = 'WK'),
    
]
