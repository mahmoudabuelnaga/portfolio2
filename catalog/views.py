from django.shortcuts import render,redirect
from .models import MyData,About,Portfolio
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
# Create your views here.
def index(request):
    data             = MyData.objects.get()
    about            = About.objects.get()
    portfolio        = Portfolio.objects.all()
    portfolio_detail = Portfolio.objects.get()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject    = form.cleaned_data['subject']
            email      = form.cleaned_data['email']
            message    = form.cleaned_data['message']
            try:
                send_mail(subject+" - "+email,message,email,['worldofbooks1751998@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    else:
        form = ContactForm()


    context = {
        'data'             : data,
        'about'            : about,
        'portfolio'        : portfolio,
        'portfolio_detail' : portfolio_detail,
        'form'             : form,
    }
    return render(request,'index.html',context)

# def emailView(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST or None)
#         if form.is_valid():
#             subject    = form.cleaned_data['subject']
#             email      = form.cleaned_data['email']
#             message    = form.cleaned_data['message']
#             try:
#                 send_mail(subject+" - "+email,message,email,['worldofbooks1751998@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('index')
#     else:
#         form = ContactForm()
#     return render(request, "contact.html", {'form': form})
