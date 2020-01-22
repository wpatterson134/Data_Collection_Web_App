from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Media
from .forms import UserForm
from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import admin
from .models import Media, Profile
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import HttpResponse


def export_as_json(mediaadmin, request, queryset):
     if request.user.is_superuser:
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response


class MediaAdmin(admin.ModelAdmin):
    readonly_fields = ('video_tag',)
    actions = [export_as_json]


admin.site.register(Profile)
admin.site.register(Media, MediaAdmin)
