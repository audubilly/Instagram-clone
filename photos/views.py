from django.shortcuts import render, redirect

from photos.form import PhotoForm
from photos.models import PhotoModel


def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PhotoForm()
        photos = PhotoModel.objects.all()
        context = {
            'photos': photos,
            'form': form,
        }

    return render(request, 'photos/index.html', context)
