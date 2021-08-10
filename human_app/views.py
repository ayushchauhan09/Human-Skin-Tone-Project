from .skintone import imageskintone
from django.shortcuts import render
from .forms import ImageForm
#importing models
from .models import Image
#importing skintone ML file
from . import skintone
from . import models

# Create your views here.
def index(request):
    visit = "disabled"
    return render(request,"index.html",{"visit1":visit})

#skintone(upload image) page view
def skintone(request):
    visit = "skintone"
    return render(request,"skintone.html",{"visit2":visit})

#about page view
def about(request):
    visit = "about"
    return render(request,"about.html",{"visit3":visit})

        

#logic to save image in database and finding its database
def SaveImage(request):
    visit = "skintone"
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            if obj :            
                imag =  obj.image
                url = "http://127.0.0.1:8000/media/" + str(imag)
                #calling method imageskintone from skintone ML to find skintone 
                skin_tones = imageskintone(url)
                form = ImageForm()
                
                return render(request,"skintone.html",{"obj":obj,"skinto":skin_tones,"visit2":visit})

    else:
        return render(request,"skintone.html",{"visit2":visit})

    


