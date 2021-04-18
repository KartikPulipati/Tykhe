from django.shortcuts import render, redirect, get_object_or_404
from .models import ZoomMtg
from .forms import ZForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginuser')
def createZoom(request):
    if request.method == 'GET':
        return render(request, 'zoom/createZoom.html', {'form': ZForm()})
    else:
        form = ZForm(request.POST)
        new = form.save(commit=False)
        new.user = request.user
        new.save()
        return redirect('listZoom')


@login_required(login_url='loginuser')
def listZoom(request):
    z = ZoomMtg.objects.filter(user=request.user).order_by('time')
    return render(request, 'zoom/listZoom.html', {'zoom': z})


@login_required(login_url='loginuser')
def deleteZoom(request, zoom_pk):
    todo = get_object_or_404(ZoomMtg, pk=zoom_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('listZoom')

