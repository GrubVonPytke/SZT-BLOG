from django.shortcuts import render_to_response
from articles.models import News


def news(request):
	return render_to_response('news.html',{'news' : News.objects.all()})
