from django.http import HttpResponse,HttpRequest
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

# Create your views here.

@csrf_exempt
def login_teacher_form(request):
    "return login teacher template"
    return render_to_response('teachers/login.html', {})

def register_teacher(request):
    "return register teacher template"
    return render_to_response('teachers/register.html', {})
