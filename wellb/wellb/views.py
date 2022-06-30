from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	context = {
		"page_title": "Home",
	}
	return render(request, 'index.html', context)