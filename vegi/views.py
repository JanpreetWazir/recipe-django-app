from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def receipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # Create a new recipe entry
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

    # Fetch all recipes
    receipe = Receipe.objects.all()

    # Filter recipes based on search query
    search_query = request.GET.get('search')
    if search_query:
        receipe = receipe.filter(receipe_name__icontains=search_query)

    return render(request, 'receipe.html', {'receipe': receipe})

def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('receipe')

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    if request.method == 'POST':
        receipe.receipe_name = request.POST.get('receipe_name')
        receipe.receipe_description = request.POST.get('receipe_description')
        if request.FILES.get('receipe_image'):
            receipe.receipe_image = request.FILES.get('receipe_image')
        receipe.save()
        return redirect('receipe')

    return render(request, 'update_receipe.html', {'receipe': receipe})
