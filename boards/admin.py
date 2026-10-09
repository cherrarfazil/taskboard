from django.contrib import admin
from .models import Board, BoardMember, BoardList, Card

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']

@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'board', 'role']

@admin.register(BoardList)
class BoardListAdmin(admin.ModelAdmin):
    list_display = ['title', 'board']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'board_list']