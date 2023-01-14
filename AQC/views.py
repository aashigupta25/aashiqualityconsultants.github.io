from django.shortcuts import render
from AQC.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def client(request):
    return render(request, "client.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        desc = request.POST['desc']
        print(name, email, phone, service, desc)
        
        if len(name) <2 or len(email)< 2 or len(phone)<10: 
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name = name, email = email, phone = phone, service = service, desc = desc)
            print('we are using post request')
            contact.save()
            messages.success(request, "Your message has been sent!")
    return render(request, "contact.html")

def feedback(request):
    return render(request, "feedback.html")

def CompanyProfile(request):
    return render(request, "CompanyProfile.html")

# def Industry(request):
#     return render(request, "industry.html")

def Standard(request):
    return render(request, "standard.html")

def Consultancy(request):
    return render(request, "consultancy.html")

def Method(request):
    return render(request, "method.html")

def Inspection(request):
    return render(request, "inpection.html")

def PhotoGallery(request):
    return render(request, "PhotoGallery.html")

def Training(request):
    return render(request, "Training.html")

def Compliance(request):
    return render(request, 'Compliance.html')

def SupplyChainImprovement(request):
    return render(request, "SupplyChainImprovement.html")

def ISO90012015(request):
    return render(request, "ISO90012015.html" )

def ISO140012015(request):
    return render(request, "ISO140012015.html")

def IATF(request):
    return render(request, "IATF.html")

def IRIS(request):
    return render(request, "IRIS.html")

def SImplementation(request):
    return render(request, "5SImplementation.html")

def BRC(request):
    return render(request, "BRC.html")

def ISO450012018(request):
    return render(request, "ISO450012018.html")

def FSSC(request):
    return render(request, "FSSC.html")

def SA8000(request):
    return render(request, "SA8000.html")

def HACCP(request):
    return render(request, "HACCP.html")

def ISO27001(request):
    return render(request, "ISO27001.html")

def ISO150012018(request):
    return render(request, "ISO150012018.html")

def BIOS55001(request):
    return render(request, "BIOS55001.html")

def AS91012014(request):
    return render(request, "AS91012014.html")

def ISO180012017OHSAS(request):
    return render(request, "ISO180012017OHSAS.html")

def KAIZEN(request):
    return render(request, "KAIZEN.html")

def APQP(request):
    return render(request, "APQP.html")

def SIXSIGMA(request):
    return render(request, "SIXSIGMA.html")

def POKAYOKA(request):
    return render(request, "POKAYOKA.html")

def WK(request):
    return render(request, "WK.html")
