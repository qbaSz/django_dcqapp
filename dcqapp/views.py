from django.shortcuts import render
from django.http import HttpResponse
from .models import DCEntry

# Create your views here.
def index(request):
    dc_entry_list = DCEntry.objects.all()
    context = { 'dc_entry_list' : dc_entry_list }
    return render(request, 'dcqapp/index.html', context)

def detail(request, commit_id):
    return HttpResponse("Details of %s." % commit_id)