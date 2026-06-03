from django.contrib import admin
from .models import Category, Goal, Task, Comment, Reminder

admin.site.register(Category)
admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Reminder)