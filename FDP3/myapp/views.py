from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Usregister
from myapp.forms import UsForm

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

def hy2(request,us,rl,ag):
	pms = {'user':us,'roll':rl,'age':ag}
	return render(request,'myapp/hy2-3para.html',{'g':pms})

def register(request):
	if request.method == 'POST':
		uname = request.POST['uname']
		upwd = request.POST['upwd']
		uage = request.POST['uage']
		data ={'uname':uname,'upwd':upwd, 'uage':uage}
		return render(request,'myapp/display.html',data)

	return render(request,'myapp/register.html',{})


def extcss(request):
	return render(request,'myapp/extcss.html',{})

def jsac(request):
	return render(request,'myapp/javasc.html')

def jsac2(request):
	return render(request,'myapp/jsac2.html')

def bot(request):
	return render(request,'myapp/bootext.html')

def botint(request):
	return render(request,'myapp/bootint.html')

def usrrg(request):
	if request.method== 'POST':
		uname = request.POST['uname']
		pwd = request.POST['pwd']
		age = request.POST['age']
		print(uname)

	return render(request,'myapp/usrreg.html')

def usreg(request):
	if request.method == "POST":
		e =UsForm(request.POST)
		if e.is_valid():
			e.save()
			# return HttpResponse("Record saved")
			return redirect('/sha')

	e = UsForm()
	return render(request, 'myapp/regis.html',{'t':e})

def showall(request):
	r = Usregister.objects.all()
	return render(request, 'myapp/showall.html',{'d':r})



