from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from news_stories.models import Story


# Create your views here.
def index(request):
    lastest_story_list = Story.objects.order_by('-date')
    template = loader.get_template('news_stories/index.html')
    context = {
        'latest_story_list': lastest_story_list
    }
    return HttpResponse(template.render(context, request))