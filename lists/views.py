from django.shortcuts import render
from django.http import HttpResponse


# home_page=None
def home_page(request):
	# if request.method =='POST':
	# 	return HttpResponse(request.POST['item_text'])
	return render(request,'home.html',{'new_item_text':request.POST['item_text']})



# Create your views here.
