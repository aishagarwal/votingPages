from django.shortcuts import render_to_response, render
from mainSite.models import *
import json
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .databaseManager import getCandidateDetail

# Create your views here.
def logged(request):
	return render(request, 'main_page.html')

def view_candidate(request):
	candidate_i = New_Candidate.objects.all()
	candidate_data = {
		"candidate_detail" : candidate_i
	}
	return render_to_response('view_candidates.html', candidate_data, context_instance=RequestContext(request))

def candidateView(request,candidateName):
	b = New_Candidate.objects.get(name=candidateName)
	data = {
		"detail" : b
	}
	#candidateDetails = getCandidateDetail(candidateName)
	#contextObj = Context({'candidateName':candidateName,'candidateDetails':candidateDetails})
	return render_to_response('test.html',data,context_instance=RequestContext(request))

def register(request):
	return render(request, 'registration_form.html')

def add_candidate(request):
	if request.GET:
		new_candidate = New_Candidate(name=request.GET['name'],post=request.GET['optionsRadios'],  roll=request.GET['roll'], department=request.GET['dept'], cpi=request.GET['cpi'], sem=request.GET['sem'], backlogs=request.GET['back'], email=request.GET['email'], contact=request.GET['contact'], hostel=request.GET['hostel'], room=request.GET['room'], agenda=request.GET['agenda'])
    	new_candidate.save()
	return HttpResponseRedirect('/main')

#get candidates for the required post
def candidateDetails(request, candidatePost):

	candidate_i = New_Candidate.objects.filter(post=candidatePost)
	#for candidate in candidate_i:

	candidate_data ={
		"candidate_detail" : candidate_i
	}

	tmp = 'vote' + candidatePost + '.html'
	return render_to_response(tmp, candidate_data, context_instance=RequestContext(request))
