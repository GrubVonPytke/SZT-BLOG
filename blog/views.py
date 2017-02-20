from django.shortcuts import render_to_response
# Create your views here.
def base(request):
    return render_to_response('base.html')

