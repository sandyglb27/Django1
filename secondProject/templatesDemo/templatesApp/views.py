from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={"name":"Sandeep"}
    return render(request,'templates/firstTemplates.html',context=myDict)

def renderEmployee(request):
    mydic={"id":123,"name":"Sandy","salary": 100000}
    return render(request,'templates/employeeTemplates.html',context=mydic)
