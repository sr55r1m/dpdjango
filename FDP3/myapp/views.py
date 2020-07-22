from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
	return HttpResponse("<h1 style='color:blue'>Hello good morning to all</h1>")

def te(req,name):
	return HttpResponse("hello "+name)

def stu(request,na,roll):
	# for normal order of parameters in printing {} {}
	# to change parameter sequence in printing {1} {0}
	# to change type use type casting str(roll) or int(roll)
	# http://localhost:8000/user/bond/707/
	return HttpResponse("{1} assigned number {0}".format(roll,na))

def hy(request,us):
	# 'APP_DIRS': True, predefined paths templatesDIR holding userappDIR with html files
	return render(request,'myapp/sample.html',{'r':us})


