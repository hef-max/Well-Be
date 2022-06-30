from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	context = {
		"page_title":"blog"
	}
	return render(request, 'blog/index.html', context)