# user_activity/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserActivity

@login_required
def user_activity_dashboard(request):
    user_activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')[:10]
    return render(request, 'user_activity/dashboard.html', {'user_activities': user_activities})


# Create your views here.
