from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request,'newshow.html')


def allShows(request):
	context = {
		'AllShows' : Shows.objects.all()
	}
	return render(request,'allshows.html', context)


def AddShow(request):
	print("****************")
	print(request.POST)
	print("****************")

	errorsFromValidator = Shows.objects.Add_validator(request.POST)

	print('PRINTING ERRORS HERE', errorsFromValidator)
	if len(errorsFromValidator) > 0:
		for key, value in errorsFromValidator.items():
			messages.error(request, value)
		return redirect('/shows/new')


	newShow = Shows.objects.create(Title = request.POST['title'], Network = request.POST['network'], Release_Date = request.POST['reldate'], Description = request.POST['desc'] )
	return redirect(f"/shows/info/{newShow.id}")

def ShowPage(request, showId):
	context = {
		'AShow' : Shows.objects.get(id=showId)
	}
	return render(request, "showinfo.html", context)


def EditPage(request, showId):
	context = {
		'AShow' : Shows.objects.get(id=showId)
	}
	errorsValidator = Shows.objects.Add_validator(request.POST)

	print('PRINTING ERRORS HERE', errorsValidator)
	if len(errorsValidator) > 0:
		for key, value in errorsValidator.items():
			messages.error(request, value)
		return redirect(f'/shows/edit/{showId}')
	
	return render(request, 'editshow.html', context)

def EditShow(request, showId):

	showUpdate = Shows.objects.get(id=showId)
	showUpdate.Title = request.POST['title']
	showUpdate.Network = request.POST['network']
	showUpdate.Release_Date = request.POST['reldate']
	showUpdate.Description = request.POST['desc']
	showUpdate.save()
	messages.success(request, 'Show successfully updated')
	return redirect('/shows')


def DeleteShow(request, showId):
	print('***************')
	showDeleted = Shows.objects.get(id=showId)
	print('bye',showDeleted.Title,'!')
	print('***************') 
	showDeleted.delete()
	return redirect('/shows')

