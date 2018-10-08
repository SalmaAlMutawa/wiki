from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
	items = Page.objects.all()
	context = {
		"page_list" : items,
	}
	return render(request, 'list.html', context)

def page_detail(request, page_id):
	specific = Page.objects.get(id=page_id)
	context = {
		"page_details": specific,
	}
	return render(request, 'detail.html', context)