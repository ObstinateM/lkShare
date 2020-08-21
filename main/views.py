from django.shortcuts import render, redirect
from . import forms
from main.models import lk

# Create your views here.

def lkPage(request, urlid=None):
    if urlid == None:
        form = forms.lkEmptyForm()
        if request.method == 'POST':
            form = forms.lkEmptyForm(request.POST)
            if lk.objects.filter(url=urlid).exists():
                instance = form.save(commit=False)
                viewUrl = instance.url
                return redirect('lkFill', urlid=viewUrl)
            else:
                instance = form.save(commit=False)
                viewUrl = instance.url
                instance.save()
                return redirect('lkFill', urlid=viewUrl)
        context = {'form': form}
        return render(request, 'main/index.html', context)
    else:
        instance, created = lk.objects.get_or_create(
            url=urlid
        )
        form = forms.lkForm(instance=instance)
        if request.method == 'POST':
            form = forms.lkForm(request.POST, instance=instance)
            form.save()
        context = {'form': form}
        return render(request, 'main/lk.html', context)
