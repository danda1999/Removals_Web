from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
   
from django.conf import settings
from django.core.mail import send_mail

@csrf_exempt
def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

@csrf_exempt
def Contacts(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Contacts'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
        
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render())

@csrf_exempt
def AutoLocksmith(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        car_registration = request.POST.get('car_registration')
        phone = request.POST.get('phone')
        car_model = request.POST.get('car_model')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nCar registration: {}\nPhone: {}\nCar model: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, car_registration, phone, car_model, select, text
        )
        
        subject = 'Autolocksmith'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
 
    template = loader.get_template('AutoLocksmith.html')
    return HttpResponse(template.render())

@csrf_exempt
def Removals_and_Storage(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Removals&Storage'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Removals.html')
    return HttpResponse(template.render())

@csrf_exempt
def Cleaning(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        carpert_number = request.POST.get('carpet')
        staircase = request.POST.get('staircase')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nCarpet number: {}\nStaircase: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, carpert_number, staircase, select, text
        )
        
        subject = 'Carpet Cleaning'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Cleaning.html')
    return HttpResponse(template.render())

@csrf_exempt
def Plumbing(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Plumbing'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Plumbing.html')
    return HttpResponse(template.render())

@csrf_exempt
def Waste_Removals(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Waste Removals'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Waste_Removal.html')
    return HttpResponse(template.render())

@csrf_exempt
def Gardening(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Gardening'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Gardening.html')
    return HttpResponse(template.render())

@csrf_exempt
def Electrical(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nCarpet number: {}\nStaircase: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Electrical Services'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
        
    template = loader.get_template('ElectricalServices.html')
    return HttpResponse(template.render())

@csrf_exempt
def Landscaping(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Landscaping'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Landscaping.html')
    return HttpResponse(template.render())

@csrf_exempt
def Refurbishment(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Refurbishment'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('Refurbishment.html')
    return HttpResponse(template.render())

@csrf_exempt
def LCE(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Loft conversion and Extension'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('LCE.html')
    return HttpResponse(template.render())

@csrf_exempt
def WEB(request):
    
    if request.method == "POST":
        
        name = request.POST.get('name')
        psc = request.POST.get('PSC')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select = request.POST.get('select')
        text = request.POST.get('text')
        
        mail_body = "Name: {}\nAdress: {}\nEmail: {}\nPhone: {}\nSelect service: {}\nMessage: {}\n".format(
            name, psc, email, phone, select, text
        )
        
        subject = 'Webpage Developing'
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[settings.RECIPIENT_ADDRESS]
        send_mail( subject, mail_body, email_from, recipient_list)
    
    template = loader.get_template('LCE.html')
    return HttpResponse(template.render())

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Sitemap: https://zillionaire-group.uk/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
