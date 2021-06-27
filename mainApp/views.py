from django.shortcuts import render

def mainPage(request):
	data = {"name": "hello"}
	return render(request, "mainPage/index.html", context=data)