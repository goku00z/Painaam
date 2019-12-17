from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')

def display_DBMS(request):
    items = DBMS.objects.all()
    context = {
        'items': items,
        'header': 'DBMS',
    }
    return render(request, 'inv/index.html', context)


def display_DAA(request):
    items = DAA.objects.all()
    context = {
        'items': items,
        'header': 'DAA',
    }
    return render(request, 'inv/index.html', context)


def display_DS(request):
    items = DS.objects.all()
    context = {
        'items': items,
        'header': 'DS',
    }
    return render(request, 'inv/index.html', context)

def add_student(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_DBMS(request):
    return add_student(request, DBMSForm)


def add_DAA(request):
    return add_student(request, DAAForm)


def add_DS(request):
    return add_student(request, DSForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_dbms(request, pk):
    return edit_item(request, pk, DBMS, DBMSForm)


def edit_daa(request, pk):
    return edit_item(request, pk, DAA, DAAForm)


def edit_ds(request, pk):
    return edit_item(request, pk, DS, DSForm)


def delete_dbms(request, pk):

    template = 'inv/index.html'
    DBMS.objects.filter(id=pk).delete()

    items = DBMS.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_daa(request, pk):

    template = 'inv/index.html'
    DAA.objects.filter(id=pk).delete()

    items = DAA.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_ds(request, pk):

    template = 'inv/index.html'
    DS.objects.filter(id=pk).delete()

    items = DS.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
