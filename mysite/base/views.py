from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, "base/index.html")


def reception1(request):
    return render(request, "base/intro/login.html")


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("intro01")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, "registration/signup.html", context={"form": form})


def intro01(request):
    return render(request, "base/intro/intro01.html")


def intro02(request):
    return render(request, "base/intro/intro02.html")


def intro03(request):
    return render(request, "base/intro/intro03.html")


def intro04(request):
    return render(request, "base/intro/intro04.html")


def intro05(request):
    return render(request, "base/intro/intro05.html")


def intro06(request):
    return render(request, "base/intro/intro06.html")


def intro07(request):
    return render(request, "base/intro/intro07.html")


def intro08(request):
    return render(request, "base/intro/intro08.html")


def intro09(request):
    return render(request, "base/intro/intro09.html")


def choosefamiliar(request):
    return render(request, "base/intro/choosefamiliar.html")


def hub(request):
    return render(request, "base/hub/hub.html")


def reception(request):
    return render(request, "base/hub/reception.html")


def room(request):
    return render(request, "base/hub/room.html")


def tannaspast01(request):
    return render(request, "base/tannas-past/01.html")


def tannaspast02(request):
    return render(request, "base/tannas-past/02.html")


def tannaspast03(request):
    return render(request, "base/tannas-past/03.html")


def tannaspast04(request):
    return render(request, "base/tannas-past/04.html")


def london01(request):
    return render(request, "base/london/01.html")


def london02(request):
    return render(request, "base/london/02.html")


def london03(request):
    return render(request, "base/london/03.html")


def london04(request):
    return render(request, "base/london/04.html")


def london05(request):
    return render(request, "base/london/05.html")


def london06(request):
    return render(request, "base/london/06.html")


def london07(request):
    return render(request, "base/london/07.html")


def london08(request):
    return render(request, "base/london/08.html")


def london09(request):
    return render(request, "base/london/09.html")


def london10(request):
    return render(request, "base/london/10.html")


def london11(request):
    return render(request, "base/london/11.html")


def london12(request):
    return render(request, "base/london/12.html")


def london13(request):
    return render(request, "base/london/13.html")


def london14(request):
    return render(request, "base/london/14.html")


def ghana01(request):
    return render(request, "base/ghana/01.html")


def ghana02(request):
    return render(request, "base/ghana/02.html")


def ghana03(request):
    return render(request, "base/ghana/03.html")


def ghana04(request):
    return render(request, "base/ghana/04.html")


def ghana05(request):
    return render(request, "base/ghana/05.html")


def ghana06(request):
    return render(request, "base/ghana/06.html")


def ghana07(request):
    return render(request, "base/ghana/07.html")


def capetown01(request):
    return render(request, "base/capetown/01.html")


def capetown02(request):
    return render(request, "base/capetown/02.html")


def capetown03(request):
    return render(request, "base/capetown/03.html")


def capetown04(request):
    return render(request, "base/capetown/04.html")


def capetown05(request):
    return render(request, "base/capetown/05.html")


def capetown06(request):
    return render(request, "base/capetown/06.html")


def numidia01(request):
    return render(request, "base/numidia/01.html")


def numidia02(request):
    return render(request, "base/numidia/02.html")


def numidia03(request):
    return render(request, "base/numidia/03.html")


def numidia04(request):
    return render(request, "base/numidia/04.html")


def numidia05(request):
    return render(request, "base/numidia/05.html")


def numidia06(request):
    return render(request, "base/numidia/06.html")


def numidia07(request):
    return render(request, "base/numidia/07.html")


def ethiopia01(request):
    return render(request, "base/ethiopia/01.html")


def ethiopia02(request):
    return render(request, "base/ethiopia/02.html")


def ethiopia03(request):
    return render(request, "base/ethiopia/03.html")


def ethiopia04(request):
    return render(request, "base/ethiopia/04.html")


def ethiopia05(request):
    return render(request, "base/ethiopia/05.html")


def ethiopia06(request):
    return render(request, "base/ethiopia/06.html")


def ethiopia07(request):
    return render(request, "base/ethiopia/07.html")


def ethiopia08(request):
    return render(request, "base/ethiopia/08.html")


def ethiopia09(request):
    return render(request, "base/ethiopia/09.html")


def ethiopia10(request):
    return render(request, "base/ethiopia/10.html")


def ethiopia11(request):
    return render(request, "base/ethiopia/11.html")


def ethiopia12(request):
    return render(request, "base/ethiopia/12.html")


def ethiopia13(request):
    return render(request, "base/ethiopia/13.html")


def ethiopia14(request):
    return render(request, "base/ethiopia/14.html")


def congo01(request):
    return render(request, "base/congo/01.html")


def congo02(request):
    return render(request, "base/congo/02.html")


def congo03(request):
    return render(request, "base/congo/03.html")


def congo04(request):
    return render(request, "base/congo/04.html")


def congo05(request):
    return render(request, "base/congo/05.html")


def congo06(request):
    return render(request, "base/congo/06.html")


def fishpeople01(request):
    return render(request, "base/fish-people/01.html")


def fishpeople02(request):
    return render(request, "base/fish-people/02.html")


def fishpeople03(request):
    return render(request, "base/fish-people/03.html")


def fishpeople04(request):
    return render(request, "base/fish-people/04.html")


def fishpeople05(request):
    return render(request, "base/fish-people/05.html")


def fishpeople06(request):
    return render(request, "base/fish-people/06.html")


def fishpeople07(request):
    return render(request, "base/fish-people/07.html")
