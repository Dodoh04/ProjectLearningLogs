from django.shortcuts import render
from .models import Topic
from .models import Entry
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse 

# Create your views here.
def index(request):
      return render(request, 'learning_logs/index.html')

def pg2(request):
      return render(request, 'learning_logs/pg2.html')

def pg3(request):
      return render(request, 'learning_logs/pg3.html')

def pg4(request):
      return render(request, 'learning_logs/pg4.html')

def topics(request):
      topics = Topic.objects.order_by('date_added', 'text')
      context = {'topics' : topics}
      return render(request, 'learning_logs/topics.html',  context)

def topic(request, topic_id):
      topic = Topic.objects.get(id = topic_id)
      entries = topic.entry_set.order_by('-date_added')
      context = {'topic' : topic, 'entries': entries}
      return render(request, 'learning_logs/topic.html',  context)
            # mostra um unico assunto e suas entradas.

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        # Dados POST submetidos; processa os dados.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
