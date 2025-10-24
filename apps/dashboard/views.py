from django.shortcuts import render

def index_view(request):
    return render(request, "dashboard/index.html", {"active": "index"})

def usuarios_view(request):
    return render(request, "dashboard/index.html", {"active": "usuarios"})

def medidores_view(request):
    return render(request, "dashboard/index.html", {"active": "medidores"})

def consumos_view(request):
    return render(request, "dashboard/index.html", {"active": "consumos"})

def boletas_view(request):
    return render(request, "dashboard/index.html", {"active": "boletas"})

def reportes_view(request):
    return render(request, "dashboard/index.html", {"active": "reportes"})
