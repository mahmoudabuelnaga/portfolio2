from django.shortcuts import render,redirect
from .models import MyData,About,Portfolio
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from django.views.generic import DetailView
# Create your views here.
def index(request):
    data             = MyData.objects.get()
    about            = About.objects.get()
    portfolio        = Portfolio.objects.all()
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
        'form'             : form,
    }
    return render(request,'index.html',context)

class PortFolioDetail(DetailView):
    model = Portfolio
    context_object_name = 'portfolio_detail'
    template_name = 'postfolio_detail.html'    