from django.shortcuts import render
from .models import Event
from .forms import ApplicantForm
# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {
        'events':events
    }
    return render(request,'eventApp/index.html',context)

def eventdetail(request,pk):
    events = Event.objects.get(pk = pk)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant  = form.save(commit=False)
            applicant.event = events
            applicant.save()
    form  = ApplicantForm()
    context = {
        'event' : events,
        'form' : form
    }
    return render(request,'eventApp/details.html',context)