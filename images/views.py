from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
# Create your views here.

@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image Is Add')

            return redirect(new_item.get_absolute_url())
        
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html' ,{'form':form})
