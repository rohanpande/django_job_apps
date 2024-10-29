from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFileForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            saved_object = form.instance
            context = {'form': form, 'saved_object': saved_object}
            return render(request, 'uploadapp/add_image.html', context)
    else:
        form = UploadForm()
        context = {'form': form}
    return render(request, 'uploadapp/add_image.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            saved_object = form.instance
            context = {'form': form, 'saved_object': saved_object}
            return render(request, 'uploadapp/add_file.html', context)
    else:
        form = UploadFileForm()
        context = {'form': form}
    return render(request, 'uploadapp/add_file.html', context)