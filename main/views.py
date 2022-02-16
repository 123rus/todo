from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from main.models import Todo
# Create your views here.

# Получение данных из БД
def main(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos':todos})

# Создание данных в БД
def create(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()

    return HttpResponseRedirect('/')


def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except Todo.DoesNotExist:
        # return HttpResponseNotFound('<h2> Задачка не найдена :( </h2>')
        return HttpResponseNotFound('<img src="404p.png" >')


# def test(request,id):
    # todos2 = Todo.objects.all()
    # todo = Todo.objects.get(id=id)
    # return render(request, 'index.html', {'todos2':todos2, 'hello':'hello', 'id':id})



def test(request,id):
    todo = Todo.objects.get(id=id)
    print(todo)
    return render(request, 'index.html', {'todo':todo})



def edit(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.description = request.POST.get('description')
            todo.save()
            return HttpResponseRedirect('/')
        return render(request, 'edit.html', {'todo':todo})
    except Todo.DoesNotExist:
        return HttpResponseNotFound('<h2> Задачка не найдена :( </h2>')


def tasks(request):
    todos = Todo.objects.all()
    return render(request, 'tasks.html', {'todos':todos})