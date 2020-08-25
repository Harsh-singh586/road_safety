from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from. models import data
from . serializers import DataSerializer 
import datetime
from django.contrib import messages
# Create your views here.

class alldata(APIView):

     def get(self, request, event, date_time):
          ''' param Event, Date_time
              Event is URL param
              Date_time is Date/time combination
              returns JSON response '''
           now = datetime.datetime.now()
           now_date = str(now.date())
           now_time = str(now.time())[:5]
           parse = date_time.split('+')
           parse_date = parse[0]
           parse_time = parse[1]
           #checking if date/time recieved is current
           if now_date == parse_date and now_time == parse_time:
                return Response(status = 204)
           else:
                p = parse_date + " "+parse_time
                d = data.objects.filter(url = event, date_time = p)
                if d.exists():
                    serialize = DataSerializer(d, many = True)
                    return Response(serialize.data)
                else:
                    return Response(status = 404)

class status_check(APIView):
      
     def get(self, request):
              ''' if server is alive Returns Ok status '''
              return Response({'status' : 'OK'})
           

def add(request):
       ''' used to add data to the Database '''
       if request.method == 'POST':
             url = request.POST['event']
             dt = request.POST['date']
             time = request.POST['time']
             date_time = dt+' '+time
             if data.objects.filter(url = url, date_time = date_time).exists():
                 messages.info(request,'Already Exists')
                 return redirect('/add')
             else:
                 item = data()
                 item.url = url
                 item.date_time = date_time
                 item.save() 
                 messages.info(request,'Added')
                 return redirect('/add')
       return render(request, "add.html")
def index(request):
     '''home page view'''
      return render(request, "index.html")       
