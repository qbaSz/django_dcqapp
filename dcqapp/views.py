from django.shortcuts import render
from django.http import HttpResponse
from .models import DCEntry
import urllib.request
import urllib.parse
import subprocess
import sys
import json

# Create your views here.
def index(request):
    dc_entry_list = DCEntry.objects.all()
    context = { 'dc_entry_list' : dc_entry_list }
    return render(request, 'dcqapp/index.html', context)

def detail(request, commit_id):
    return HttpResponse("Details of %s." % commit_id)

def gerrit(request):
    HOST = 'ejakszu@gerrit.ericsson.se'
    PARAMS = "gerrit query --format=JSON owner:ejakszu status:open"
    '''    
    params = urllib.parse.urlencode({'owner':'ejakszu'})
    url = "https://gerrit.ericsson.se/#/q/owner:ejakszu"
    with urllib.request.urlopen(url) as u:
        print(url)
        return HttpResponse(u.read().decode("UTF-8"))
    '''
    ssh = subprocess.Popen(['ssh', "-p 29418", "%s" % HOST, PARAMS], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print("ERROR: %s" % error)
        return HttpResponse(error)
    else:
        #jResult = json.loads(result)
        #print(result)
        contextR = []
        for j in result[:-1]:
            contextR.append(json.loads(j))
            print(json.loads(j)['subject'])
        context = {'json_result' : contextR}
        return render(request, 'dcqapp/gerrit.html', context)
