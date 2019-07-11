from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
  
def prototype(request):
    return render(request, 'coloring/prototype.html')
  
def bars(request):
    return render(request, 'coloring/bars.html')