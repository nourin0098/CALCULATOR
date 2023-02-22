from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'calulator1.html')
def calc(request):
    if 'add' in request.POST:
        if request.method=="POST":
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            a = int(num1)+int(num2)
            return render(request,'result.html',{'object':num1,'object1':num2,'result':a})
    elif 'sub' in request.POST:
        if request.method=="POST":
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            a = int(num1)-int(num2)
            return render(request,'result.html',{'object':num1,'object1':num2,'result':a})
    elif 'mul' in request.POST:
        if request.method=="POST":
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            a = int(num1)*int(num2)
            return render(request,'result.html',{'object':num1,'object1':num2,'result':a})
    elif 'div' in request.POST:
        if request.method=="POST":
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            a = int(num1)/int(num2)
            return render(request,'result.html',{'object':num1,'object1':num2,'result':a})
    return render(request,'calculator1.html')

    
    # num3 = int(num2)+int(num1)
