from django.contrib import admin
from todo.models import TodoApp

@admin.register(TodoApp)
class TodoAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']


