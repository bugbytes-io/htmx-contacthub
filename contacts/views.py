from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    contacts = request.user.contacts.all().order_by('-created_at')
    context = {'contacts': contacts}
    return render(request, 'contacts.html', context)