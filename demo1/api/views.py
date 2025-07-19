from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TodoForm
# Create your views here.
class TodoListCreateAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer_obj = TodoSerializer(todos, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        serializer_obj = TodoSerializer(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        return Response(serializer_obj.data, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer_obj = TodoSerializer(todo)
        return Response(data = serializer_obj.data)
    

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

class TodoUpdateAPIView(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer_obj = TodoSerializer(todo, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer_obj = TodoSerializer(todo, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj, status=status.HTTP_400_BAD_REQUEST)


class TodoDeleteAPIView(APIView):
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo-list-html') 

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo-list-html')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list-html')