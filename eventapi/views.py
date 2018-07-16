import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from eventapi.models import *

# Create your views here.

class AnnouncementApi(View):

    def get(self, request):
        try:
            query = Announcement.objects.all()
            formatted = []
            for a in query:
                formatted.append({
                    "created": a.created,
                    "due_date": a.due_date,
                    "content": a.content,
                    "url": a.url
                })

            content = {
                "announcements": formatted,
                "message": "Received Announcements",
                "status": 200
            }
            status = 200

        except Exception as e:
            print('error getting annoucements')
            status = 400
            content = e

        return HttpResponse(content=json.dumps(content, default=str), status=status)
