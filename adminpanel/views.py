from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from tasks.models import Task, Submission
from .models import App
from .serializers import AppSerializer
import json
from django.shortcuts import get_object_or_404, redirect

# API View for listing and creating apps
class AppListCreateView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

# Check if user is an admin
def is_admin(user):
    return user.is_superuser  # Only admin users can access

@user_passes_test(is_admin)
def admin_dashboard(request):
    users = UserProfile.objects.all()
    tasks = Task.objects.all()
    submissions = Submission.objects.all()
    
    return render(request, 'admin_dashboard.html', {
        'users': users,
        'tasks': tasks,
        'submissions': submissions
    })

# Function to add a task (Admin only)
@login_required
@csrf_exempt
def add_task(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task_name = data.get("name")
            task_points = data.get("points")

            # Validate fields
            if not task_name or task_points is None:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            # Ensure task_points is an integer
            try:
                task_points = int(task_points)
            except ValueError:
                return JsonResponse({"error": "Invalid points value"}, status=400)

            # Create the task
            task = Task.objects.create(name=task_name, points=task_points)
            return JsonResponse({"message": "Task added successfully", "task_id": task.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@login_required
@csrf_exempt
def edit_task(request, task_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task_name = data.get("name")
            task_points = data.get("points")

            if not task_name or task_points is None:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            try:
                task_points = int(task_points)
            except ValueError:
                return JsonResponse({"error": "Invalid points value"}, status=400)

            task = Task.objects.get(id=task_id)
            task.name = task_name
            task.points = task_points
            task.save()

            return JsonResponse({"message": "Task updated successfully"}, status=200)

        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'})

def approve_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    submission.is_approved = True  # Adjust field based on your model
    submission.save()
    return JsonResponse({'message': 'Submission approved successfully'})

def reject_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    submission.is_approved = False  # Adjust based on your model field
    submission.save()
    return JsonResponse({'message': 'Submission rejected successfully'})