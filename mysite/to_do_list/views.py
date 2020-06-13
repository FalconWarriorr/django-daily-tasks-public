from django.http import HttpResponse, JsonResponse
#from django.views import generic
from django.shortcuts import render
from django.core import serializers

from .models import ToDo, Mod
from .forms import ToDoForm, ModForm
from django.utils import timezone

import json as jsonjson

def modView(request):
    form = ModForm()
    mods = Mod.objects.all()

    return render(request, "todo/mod_list.html", {"form": form, "mods": mods})

def indexView(request):
    current_time = timezone.now()
    form = ToDoForm(initial={'refresh_time': timezone.localtime(timezone.now()), 'refresh_days_field': 'MTWHFSU'})
    tasks = ToDo.objects.all()
    
    for task in tasks:
        task.refresh_task()

    return render(request, "todo/list.html", {"form": form, "tasks": tasks})

def postMod(request):
    #request should be ajax with method POST
    if request.is_ajax and request.method == "POST":
        #get forms data
        form = ModForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            #Some form error occured
            return JsonResponse({"error": form.errors}, status=400)

    #Some other error occured
    return JsonResponse({"error": ""}, status=400)
    

def postTask(request):
    #request should be ajax with method POST
    if request.is_ajax and request.method == "POST":
        #get forms data
        form = ToDoForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            #Some form error occured
            return JsonResponse({"error": form.errors}, status=400)

    #Some other error occured
    return JsonResponse({"error": ""}, status=400)

def updateModAdded(request):
    #request should be ajax with method POST
    if request.is_ajax and request.method == "POST":
        post = request.POST
        mod_pk = post["modId"][4:]
        mod_added = post["modAdded"]
        instance = Mod.objects.get(pk=int(mod_pk))
        if mod_added == "true":
            instance.mod_added = True
        else:
            instance.mod_added = False
        instance.save()

        return JsonResponse({"success": ""}, status=200)
    return JsonResponse({"error": ""}, status=400)

def updateTaskDone(request):
    #request should be ajax with method POST
    if request.is_ajax and request.method == "POST":
        post = request.POST
        task_pk = post["taskId"][5:]
        task_done = post["taskDone"]
        instance = ToDo.objects.get(pk=int(task_pk))
        if task_done == "true":
            instance.task_done = True
        else:
            instance.task_done = False
        instance.save()


        #f = open("/home/niall/Code/post.txt", "w")
        #f.write(jsonjson.dumps(request.POST))
        #f.write(task_pk)
        #f.write(task_done)
        #f.write(str(instance))
        #f.close()


        return JsonResponse({"success": ""}, status=200)
    return JsonResponse({"error": ""}, status=400)


#class IndexView(generic.ListView):
#    template_name = 'todo/list.html'
#    context_object_name = 'all_todos'
#
#    def get_queryset(self):
#        """ Return all todos """
#        todos = ToDo.objects.all()
#        for todo in todos:
#            todo.refresh_task()
#        return ToDo.objects.all()
