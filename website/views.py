from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import BadHeaderError, send_mail
import smtplib
from django.contrib import messages
# Create your views here.
from django.core.mail import EmailMessage


def error_404_view(request, exception):
    return render(request, '404.html')


def home(request):
    test = Test.objects.all()
    sliders = Slider.objects.all()
    logos = LogoEquipment.objects.all()
    contacts = Homecontact.objects.all()
    links = Socialiconlink.objects.all()

    context = {'sliders': sliders,  'test': test,
               'logos': logos, 'contacts': contacts, 'links': links}
    return render(request, "index.html", context)


def about(request):
    posts = About.objects.all()
    banners = AboutBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'posts': posts, 'banners': banners,
               'test': test, 'links': links}
    return render(request, "about.html", context)


def services(request):
    banners = ServiceBanner.objects.all()
    services = Service.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'services':  services,
               'banners': banners, 'test': test, 'links': links}
    return render(request, "services.html", context)


def liftingproduct(request):
    lifting = Lifting.objects.all()
    liftbanner = LiftBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'lifting':  lifting,
               'liftbanner': liftbanner, 'test': test, 'links': links}
    return render(request, "lifting.html", context)


def equipments(request):

    equipments = Equipment.objects.all()
    ebanner = EquipBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'equipments':  equipments,
               'ebanner': ebanner, 'test': test, 'links': links}
    return render(request, "equipments.html", context)


def construction(request):
    constructions = Construction.objects.all()
    constructionBanner = ConstructionBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'constructions':  constructions,
               'constructionBanner': constructionBanner, 'test': test, 'links': links}
    return render(request, "construction-equipment.html", context)


def onroadproducts(request):
    products = OnRoad.objects.all()
    onroadBanner = OnroadBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'products':  products,
               'onroadBanner': onroadBanner, 'test': test, 'links': links}
    return render(request, "onroad.html", context)


def transportproduct(request):
    transport = Transport.objects.all()
    tbanner = TransportBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'transport':  transport,
               'tbanner': tbanner, 'test': test, 'links': links}
    return render(request, "transport.html", context)


def test(request):
    test = Test.objects.all()
    #product = Homebody.objects.all()
    context = {'test': test}
    return render(request, "test.html", context)


def enquiry(request):
    banners = EnquiryBanner.objects.all()
    test = Test.objects.all()
    links = Socialiconlink.objects.all()
    context = {'banners': banners, 'test': test, 'links': links}
    if request.method == "POST":
        e_fullname = request.POST['e-fullname']
        e_companyname = request.POST['e-companyname']
        e_mobile = request.POST['e-mobile']
        e_landnumber = request.POST['e-landnumber']
        e_website = request.POST['e-website']
        email = request.POST['email']
        e_subject = request.POST['e-subject']
        e_mesage = request.POST['e-mesage']
        e_file = request.POST['e-file']

        appoint = "Full Name: " + e_fullname + " \n Company Name: " + e_companyname + \
            " \n Mobile: " + e_mobile + " \n Land Number: " + \
            e_landnumber + " \nWebsite" + e_website + "\nEmail: " + email + \
            "\nSubject: " + e_subject + "\nMessage: " + e_mesage + "\nFile: " + e_file
        # send email
        send_mail(
            'Appoinment Request',  # subject
            appoint,  # message

            'vavachan6kwt@gmail.com',
            ['vavachan6kwt@gmail.com'],  # from_email
            fail_silently=False,

        )

        return render(request, "inquiry.html", {'e_fullname': e_fullname, 'e_companyname': e_companyname, 'e_mobile': e_mobile, 'e_landnumber': e_landnumber, 'e_website': e_website, 'email': email, 'e_subject': e_subject, 'e_mesage': e_mesage, 'e_file': e_file})
    else:

        return render(request, "inquiry.html", context)


def contact(request):
    banners = ContactBanner.objects.all()
    test = Test.objects.all()
    contacts = Homecontact.objects.all()
    links = Socialiconlink.objects.all()
    context = {'banners': banners, 'test': test,
               'contacts': contacts, 'links': links}
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_mobile = request.POST['message-mobile']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        # file_field = request.POST['file-field']
        appoint = "Name :" + message_name + " \n Mobile :" + message_mobile + \
            " \n Subject :" + message_subject + " \n Message :" + message
        # send email
        send_mail(
            'Appoinment Request',  # subject
            appoint,  # message

            'vavachan6kwt@gmail.com',
            ['vavachan6kwt@gmail.com'],  # from_email
            fail_silently=False,

        )

        return render(request, "contact.html", {'message_name': message_name, 'message_email': message_email, 'message_mobile': message_mobile, 'message_subject': message_subject, })
    else:

        return render(request, "contact.html", context)
