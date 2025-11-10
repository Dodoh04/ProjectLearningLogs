from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request, 'learning_logs/index.html')
def pg2(request):
      return render(request, 'learning_logs/pg2.html')
def pg3(request):
      return render(request, 'learning_logs/pg3.html')
def pg4(request):
      return render(request, 'learning_logs/pg4.html')