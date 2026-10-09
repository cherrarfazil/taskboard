from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_boards')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BoardMember', related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class BoardMember(models.Model):
    class Role(models.TextChoices):
        OWNER = 'owner', 'Owner'
        MEMBER = 'member', 'Member'
        VIEWER = 'viewer', 'Viewer'
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['board', 'user'], name='unique_board_member')
        ]
        def __str__(self):
            return f"{self.user} - {self.board} ({self.role})"

class BoardList(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    title = models.CharField(max_length=100)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.title} ({self.board})"

class Card(models.Model):
    board_list = models.ForeignKey(BoardList, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    position = models.PositiveIntegerField(default=0)
    due_date = models.DateField(null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_cards')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.title} ({self.board_list})"

# Create your models here.
