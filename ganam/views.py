from django.views.generic import UpdateView, ListView 
from django.http import HttpResponse
from django.template.loader import render_to_string
from ganam.forms import *
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
#from ganam.models import user_playlist
from ganam.models import ganam_songs as songs
import json
import itertools
from django.core.context_processors import csrf
from django.shortcuts import render

""" items list """ 
"""
class ItemListView(ListView): 
	model = user_playlist 
	template_name = 'item_list.html' 
"""

@login_required
def article(request, article_id=1):
	songs.objects.filter(id=article_id).update(hit=F('hit')+1)
	name=songs.objects.get(id=article_id)
	return render_to_response('article.html',
				 {'article':songs.objects.get(id=article_id),
				   'select':songs.objects.filter(artist1=name.artist1).order_by("hit").reverse(),
				   'select2':songs.objects.filter(artist2=name.artist1).order_by("hit").reverse(),
				   'select3':songs.objects.filter(star=name.artist1).order_by("hit").reverse(),
				   'user': request.user,			  
})
@login_required
def genre(request, username):
	return render_to_response('genre.html',
				 {'select':songs.objects.filter(genre=username),
				  'sele':songs.objects.filter(genre=username).order_by("hit").reverse(),
				  'tu':username,
				  'user': request.user,
				  })
def vi(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response("view.html", {'top':songs.objects.all().order_by("id").reverse()[:15],})

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'forms': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )


def logout_page(request):
    logout(request)
    #return HttpResponseRedirect('/gaanam/logout/')
    return render_to_response('registration/logout.html')
 
@login_required
def home(request):
    return render_to_response('home.html',
	    { 'user': request.user,
	      'post':songs.objects.all().order_by("id")[:20], 
	      'top':songs.objects.all().order_by("hit").reverse()[:15], })


"""
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = songs.objects.filter(track=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return render(request, 'home.html', {'error': True})
"""
@login_required
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = songs.objects.filter(artist1__icontains=q)
	    books1 = songs.objects.filter(artist2__icontains=q)
	    books2 = songs.objects.filter(star__icontains=q)
	    books3 = songs.objects.filter(album__icontains=q)
            return render(request, 'search_results.html',{'books': books,'books1': books1,'books2': books2,'books3':books3, 'query': q ,})
    return render(request, 'search_results.html',
        {'error': error})

@login_required
def language(request, bhasha):
	return render_to_response('language.html',
				 {'sel':songs.objects.filter(language__icontains=bhasha),
				  'sele':songs.objects.filter(language__icontains=bhasha).order_by("hit").reverse(),
				  'vaani':bhasha,
				   'user': request.user,
	})
@login_required
def top_singer_chart(request):
	return render_to_response('top_singer_chart.html',
				 {'json_data':songs.objects.all().order_by("hit").reverse()[:10],
				  #'json_data':songs.objects.all().order_by().values('artist2').distinct()[:10],
				  'user': request.user, 
				  'name':"Singers",	})

@login_required
def top_language_chart(request,vaani):
	return render_to_response('top_language_chart.html',
				 {'json_data':songs.objects.filter(language__icontains=vaani).order_by("hit").reverse()[:10],
				  #'json_data':songs.objects.all().order_by().values('artist2').distinct()[:10],
				  'user': request.user, 
				  'name':vaani,	})

@login_required
def top_chart(request,music):
	return render_to_response('top_chart.html',
				 {'json_data':songs.objects.filter(genre__icontains=music).order_by("hit").reverse()[:10],
				  'user': request.user, 
				  'name':music,	})
@login_required
def manage(request):
	bn=request.user.username
	if (bn =="rajputs"):
		return render_to_response('manage.html',
				 {'user': request.user,
				  'permission':"you have permission",
				  'songs': songs.objects.all().order_by("id")
				  })
	else:
		return render_to_response('manage.html',
				 {'permission':"you don't have permission", 
				   'user': request.user, 
				  })
@login_required
def update(request, update_id=1):
	rat=songs.objects.get(id=update_id)
	return render_to_response('update.html',
				 {'name':rat.track.replace(" ",""),
				   'year':rat.release_year,
				   'artist1':rat.artist1.replace(" ",""),
				   'artist2':rat.artist2.replace(" ",""),
				   'genre':rat.genre.replace(" ",""),
				    'label':rat.release_label.replace(" ",""),
				    'star':rat.star.replace(" ",""),
				    'language':rat.language.replace(" ",""),
				    'id':update_id,
				    'user': request.user,			  
})
@csrf_protect
def done(request ,done_id=1):
  try:
	cat=songs.objects.get(id=done_id)
	if request.method == 'POST':
		cat.track=request.POST['update_track'],
		cat.release_year=request.POST['update_year'],
		cat.artist1=request.POST['update_artist1'],
		cat.artist2=request.POST['update_artist2'],
		cat.release_label=request.POST['update_label'],
		cat.star=request.POST['update_star'],
		cat.language=request.POST['update_language'],
		cat.genre=request.POST['update_genre'],
	return render_to_response('manage.html',
				 {'updated':"data updated", 
				   'user': request.user, 
				  })
  except:
	return render_to_response('manage.html',
				 {'updated':"data not updated", 
				   'user': request.user, 
				  })
@login_required				  			  
def comparehj(request,comp):
	ol=0
	op=0
	ok=0
	om=0
	mo=0
	hits=[]
	lang=[]
	lion=[]
	tiger={}
	if (comp=="language"):
		hindi=songs.objects.filter(language__icontains="hindi")
		english=songs.objects.filter(language__icontains="english")
		punjabi=songs.objects.filter(language__icontains="punjabi")
		for (u,v,w) in itertools.izip_longest(hindi,english,punjabi):
			try:				
				ol+=u.hit
				op+=v.hit
				ok+=w.hit
			except:
				pass
		hits.append(ol)
		hits.append(op)
		hits.append(ok)
		lang.append("hindi")
		lang.append("english")
		lang.append("punjabi")
		for (qs,bn)in itertools.izip_longest(hits,lang):
			tiger={"hits":qs,
			       "language":bn,
			       }
			lion.append(tiger)
		return render_to_response('compare.html', {'ol':lion, 'user': request.user, })
	if(comp=="genre"):
		pop=songs.objects.filter(genre__icontains="pop")
		jazz=songs.objects.filter(genre__icontains="jazz")
		indian=songs.objects.filter(genre__icontains="indian")
		Rap=songs.objects.filter(genre__icontains="Rap")
		Romance=songs.objects.filter(genre__icontains="Romance")
		for (u,v,w,x,y) in itertools.izip_longest(pop,jazz,indian,Rap,Romance):
			try:				
				ol+=u.hit
				op+=v.hit
				ok+=w.hit
				om+=x.hit
				mo+=y.hit		
			except:
				pass
		hits.append(ol)
		hits.append(op)
		hits.append(ok)
		hits.append(om)
		hits.append(mo)
		lang.append("Pop")
		lang.append("Jazz")
		lang.append("Indian")
		lang.append("Rap")
		lang.append("Romance")
		for (qs,bn)in itertools.izip_longest(hits,lang):
			tiger={"hits":qs,
			       "language":bn,
			       }
			lion.append(tiger)
		return render_to_response('compare.html',
					 {'ol':lion,
					  'user': request.user, 
					  })
@login_required			
def deleted(request,delete_id):
	songs.objects.filter(id=delete_id).delete()
	return render_to_response('manage.html',
				 {'user': request.user,
				  'permission':"you have permission",
				  'songs': songs.objects.all().order_by("id"),
				  'delete':"song deleted",
				  })
