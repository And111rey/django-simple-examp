from django.shortcuts import render
# from django.template.response import TemplateResponse

def index(request):
    header = "Pesronal Data"
    langs = ["Python", "JavaScript", "TypeScript", "CSS", "HTML"]
    user = {"name": "Andrew", "age":"29"}
    addres = ("Ukraine", "Khm",)
    data={
        "header": header,
        "langs": langs,
        "user": user,
        "addr": addres
    }
    return render(request, "index.html", context=data)

def about(request):
    return render(request, "firstapp/about.html")

def contacts(request):
    tel = "097-xx-xx-xxx"
    mail = "exampl@mail.com"
    data = {
        "tel": tel,
        "mail": mail
    }
    return render(request, "firstapp/contacts.html", context=data)