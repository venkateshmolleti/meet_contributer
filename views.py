from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from .form import UserRegisterForm
from django.urls import reverse
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	CreateView,
)
from django.contrib.auth import login



class PersonsListView(ListView):
	model = Person
	template_name = 'index.html'
	context_object_name = 'persons'




class PersonCreateView( CreateView):
	model = Person
	fields = ['orpfield','quality','quantity','noofcloths','address','phoneno','pincode']
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	def get_success_url(self):
		return reverse('index')
	# 	return redirect('index')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('create')
	else:
		form = UserRegisterForm()
	return render(request, 'login.html', {'form': form })
