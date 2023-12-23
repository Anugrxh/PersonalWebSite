from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render

from Frontend.models import contactmedb




# Create your views here.
def index(request):
    file = contactmedb.objects.all()
    return render(request,"index.html",{'file':file})

def contactdata(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        ema = request.POST.get('email')
        msg = request.POST.get('message')
        obj = contactmedb(name=na,email=ema,message=msg)
        obj.save()
        return redirect(index)



from django.http import FileResponse


from django.http import FileResponse
from .models import Resume

def download(request):
    resume = Resume.objects.first()  # gets the first Resume object
    if resume is not None:
        response = FileResponse(resume.file)
        return response
    else:
        # Handle the case when there is no Resume object
        return HttpResponse("No file found.")



