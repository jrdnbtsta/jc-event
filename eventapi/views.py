import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from eventapi.models import *

# Create your views here.

class AnnouncementApi(View):

    def get(self, request, announcement_id=None):
        try:
            if announcement_id:
                query = Announcement.objects.filter(id=announcement_id).first()
                formatted = {
                    "id": query.id,
                    "created": query.created,
                    "due_date": query.due_date,
                    "content": query.content,
                    "url": query.url
                }

            else:
                query = Announcement.objects.all()
                formatted = []
                for a in query:
                    formatted.append({
                        "id": a.id,
                        "created": a.created,
                        "due_date": a.due_date,
                        "content": a.content,
                        "url": a.url
                    })

            content = {
                "content": formatted,
                "message": "Received Announcements",
                "status": 200
            }
            status = 200

        except Exception as e:
            print('error getting annoucements')
            status = 400
            content = e

        return HttpResponse(content=json.dumps(content, default=str), status=status, content_type='application/json')
