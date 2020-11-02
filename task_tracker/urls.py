from django.urls import path, re_path

from .views import TaskView, BoardView, SingleTaskView, FilteredTasks


app_name = "task_manager"


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view()),
    path('boards/', BoardView.as_view()),
    path('boards/<int:pk>', BoardView.as_view()),
    path('task/<int:pk>', SingleTaskView.as_view()),
    re_path('tasks/board_id=(?P<id>.+)', FilteredTasks.as_view())
]
