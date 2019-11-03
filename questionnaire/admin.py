from django.contrib import admin
from .models import *

admin.site.register(Quiz_Team)
admin.site.register(Team_member)
admin.site.register(Question)
admin.site.register(Ans_chosen)