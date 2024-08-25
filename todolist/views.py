from django.shortcuts import render, redirect
from .models import ToDoList

# Create your views here.

def index(request):
    # 取得 ToDoList 所有資料
    todoAll = ToDoList.objects.all()

    if request.method == "POST":
        text = request.POST.get("todo_text")
        # 新增待辦事項
        ToDoList.objects.create(todo_text=text)
        return redirect('todolist:index')

    return render(request, 'todolist/index.html', locals())

def todo_delete(request, id):
    todo = ToDoList.objects.get(todo_id=id)
    todo.delete()
    return redirect('todolist:index')

def todo_completed(request, id):
    todo = ToDoList.objects.get(todo_id=id)
    todo.todo_completed = not todo.todo_completed
    todo.save()
    return redirect('todolist:index')
