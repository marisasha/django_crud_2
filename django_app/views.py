from django.shortcuts import redirect, render
from django.urls import reverse
from django_app import models



def form(request):
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
    obj = models.Report.objects.all().filter()
    return render(
                    request=request,
                    template_name="statements.html",
                    context={"obj":obj}
                )

def statement(request,pk: str):
    obj = models.Report.objects.get(id=int(pk))
    return render(
                    request=request,
                    template_name="statement.html",
                    context={"obj":obj}
                )

def statement_delete(request,pk: str):
    obj = models.Report.objects.get(id=int(pk)).delete()

    return redirect(reverse("statements"))