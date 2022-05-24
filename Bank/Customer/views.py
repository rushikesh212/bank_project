from django.shortcuts import render
from .forms import Feedback
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data
from django.contrib.auth.decorators import login_required



# Create your views here.


def show(r):
    form = Feedback()
    my_dict = {'form': form}
    if r.method == 'POST':
        form = Feedback(r.POST, r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/message")
        else:
            print("Data Not Fetched")

    return render(r, 'add.html', context=my_dict)


@login_required(login_url='/accounts/login/')
def show1(r):
    form = Data.objects.all()
    my_dict = {'form': form}
    return render(r, 'display.html', context=my_dict)


def show2(r):
    return render(r, 'home.html')


def show3(r):
    return render(r, 'message.html')
