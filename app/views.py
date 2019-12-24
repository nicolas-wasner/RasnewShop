from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from app.models import Example, SignUpForm


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Example

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Titre page'
        result['Example'] = Example.objects.all()  # all() = "SELECT * FROM Cocktail"

        # result['ingredient'] = CocktailIngredientUnit.objects.all()

        return result


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})