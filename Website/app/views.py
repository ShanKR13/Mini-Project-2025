from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os

# Create your views here.
def home(req):
    return render(req,'home.html')

def store(request):
    if request.method == 'POST':
        # If using a form class
        # form = FileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('success_url')
        if 'myfile' not in request.FILES or not request.FILES['myfile']:
            # Render the same page with an error message if no file is uploaded
            return redirect('/')
        # Without a form class
        file = request.FILES['myfile']
        filename = file.name
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filepath, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return render(request, 'display.html')
    else:
        return render(request, 'home.html')
