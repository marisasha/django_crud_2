import json
import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.cache import caches
from django_app import models

RamCache = caches["default"]


def home(request):
    return render(
        request,
        "form.html",
        context={}
        )

def save_form(request):
    name = request.POST["name"]
    report = request.POST["report_text"]
    models.Report.objects.create(name=name,report_text=report)

    print(name)
    return render(
                    request=request,
                    template_name="form.html",
                    context={}
                )

def statements(request):
    key = "_users"
    _users = RamCache.get(key)
    if _users is None:
        objs = models.Report.objects.all()
        _users = []
        for obj in objs:
            _users.append({ "id":obj.id_  ,"name": obj.name, "report_text": obj.report_text})
        RamCache.set(key, _users, timeout=5)
    return render(
                    request=request,
                    template_name="statements.html",
                    context={"obj":_users}
                )

def statement(request,pk: str):
    obj = models.Report.objects.get(id=int(pk))
    return render(
                    request=request,
                    template_name="statement.html",
                    context={"obj":obj}
                )

def statement_delete(request,pk: str):
    models.Report.objects.get(id=int(pk)).delete()

    return redirect(reverse("statements"))


def new_users():
    for i in range(1,1000):
        models.Report.objects.create(name=f'Александр{random.randint(1,99999)}',report_text=f'erorr number {i}')


