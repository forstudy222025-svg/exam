from django.urls import path
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
