from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
import os
from .models import Question
import logging

# Setup logger
logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'firstapp/home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class crud:  # Ensure this is lower case 'c'
    @staticmethod
    def savedata(request):
        sv = Question(name=request.POST['name'], question_text=request.POST['questiontext'], file=request.FILES['file'], image=request.FILES['image'], pub_date=timezone.now())
        sv.save()
        return HttpResponseRedirect(reverse('firstapp:index'))

    @staticmethod
    def editdata(request, data_id):
        data = get_object_or_404(Question, pk=data_id)
        alldata = Question.objects.order_by('-pub_date')
        return render(request, 'firstapp/home.html', {'data': data, 'qid': data_id, 'getdata': alldata})

    @staticmethod
    def updatedata(request):
        ed = Question.objects.get(id=request.POST['qid'])
        imagePath = os.path.join(settings.MEDIA_ROOT, ed.image.name)
        filePath = os.path.join(settings.MEDIA_ROOT, ed.file.name)

        if 'image' in request.FILES:
            ed.image = request.FILES['image']
            if os.path.isfile(imagePath):
                os.remove(imagePath)

        if 'file' in request.FILES:
            ed.file = request.FILES['file']
            if os.path.isfile(filePath):
                os.remove(filePath)

        ed.name = request.POST['name']
        ed.question_text = request.POST['questiontext']
        ed.save()

        return HttpResponseRedirect(reverse('firstapp:index'))

    @staticmethod
    def deletedata(request, data_id):
        dl = get_object_or_404(Question, id=data_id)
        imagePath = os.path.join(settings.MEDIA_ROOT, dl.image.name)
        filePath = os.path.join(settings.MEDIA_ROOT, dl.file.name)

        if os.path.isfile(imagePath):
            os.remove(imagePath)
            logger.info(f"Deleted image file at: {imagePath}")

        if os.path.isfile(filePath):
            os.remove(filePath)
            logger.info(f"Deleted file at: {filePath}")

        dl.delete()
        logger.info(f"Deleted Question object with id: {data_id}")

        return HttpResponseRedirect(reverse('firstapp:index'))