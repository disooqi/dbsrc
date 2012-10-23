from polls.models import Poll
from django.http import HttpResponse

def index(request):
    pass

def getCurrentPoll(request):
    output = 'no poll'
    l = Poll.objects.filter(isCurrent=True).order_by('-pub_date')[:1]
    if len(l) == 1:
        output = l[0].question
    return HttpResponse(output)

    
