from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Board, BoardMember, BoardList, Card

@login_required
def dashboard(request):
    boards = Board.objects.filter(members=request.user)
    return render(request, 'boards/dashboard.html', {'boards': boards})
# Create your views here.
