from events.models import Article
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news_listing(request):
    event_list = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(event_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)

    return render_to_response('center/base_center_news.html',
                              {'events':events},
                              context_instance=RequestContext(request))

#make generic view
def showArticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('center/base_center_news_article.html',
                              {'article':article},
                              context_instance=RequestContext(request))
