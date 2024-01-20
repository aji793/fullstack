from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Todo
# Create your views here.
def index(req):
  todos=Todo.objects.all()
  print(todos)
  return render(req,"todos/base.html",{"todo":todos})
def createTodo(req):
  if req.method=="GET":
   return render(req,"todos/form.html")
  if req.method=="post":
    todo=req.POST['todo']
    print(todo)
    return redirect("/")