from django.contrib import admin
from .models import BaseModel, WorkFlow, State, Transition


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator', 'enabled', 'create_time', 'update_time')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'create_time')
    search_fields = ('name',)
    readonly_fields = ('creator',)
    ordering = ('-id',)

    # def save_model(self, request, obj, form, change):
    #     if not obj.creator:
    #         obj.creator = request.user.username
    #     obj.save()


class StateAdmin(BaseModelAdmin):
    list_display = ('id','name', 'workflow', 'type_id', 'owner', 'creator','enabled', 'create_time', 'update_time')
    list_filter = ('workflow', 'name', 'create_time')


class TransitionAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'last_state', 'next_state', 'workflow', 'timer', 'type_id')
    list_filter = ('workflow', 'name', 'create_time')



admin.site.register(WorkFlow)
admin.site.register(State, StateAdmin)
admin.site.register(Transition, TransitionAdmin)
