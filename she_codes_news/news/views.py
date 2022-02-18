import datetime
from urllib import parse
from zoneinfo import ZoneInfo

from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic

from .forms import StoryForm
from .models import NewsStory


def get_tz_name(request):
    if request.COOKIES.get('timezone'):
        return parse.unquote(request.COOKIES.get('timezone'))
    return settings.TIME_ZONE 


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        tz_name = get_tz_name(self.request)
        initial['pub_date'] = datetime.datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%dT%H:%M")
        return initial
