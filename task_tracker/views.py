from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, Board
from .serializers import TaskSerializer, BoardSerializer


class TaskView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})

    def post(self, request):
        task = request.data.get('task')
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({"success": "Task '{}' created successfully".format(task_saved.title)})

    def put(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data.get('task')
        serializer = TaskSerializer(instance=saved_task, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            saved_task = serializer.save()

        return Response({"success": "Task '{}' updated successfully".format(saved_task.title)})

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({"message": "Task '{}' has been deleted".format(task.title)}, status=204)


class BoardView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response({"boards": serializer.data})

    def post(self, request):
        board = request.data.get('board')
        serializer = BoardSerializer(data=board)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
        return Response({"success": "Board '{}' created successfully".format(board_saved.name)})

    def put(self, request, pk):
        saved_board = get_object_or_404(Board.objects.all(), pk=pk)
        data = request.data.get('board')
        serializer = BoardSerializer(instance=saved_board, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            saved_board = serializer.save()

        return Response({"success": "Board '{}' updated successfully".format(saved_board.name)})

    def delete(self, request, pk):
        board = get_object_or_404(Board.objects.all(), pk=pk)
        board.delete()
        return Response({"message": "Board '{}' has been deleted".format(board.name)}, status=204)


class SingleTaskView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        serializer = TaskSerializer(task)
        return Response({"task": serializer.data})


class FilteredTasks(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        board_id = self.kwargs['id']
        return Task.objects.filter(board_id=board_id)

