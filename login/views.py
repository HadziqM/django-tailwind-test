from django.shortcuts import render
from .models import Account
import bcrypt


class crypt():
    def __init__(self) -> None:
        pass

    def hash(password: str):
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt()).decode("utf-8")

    def match(password: str, crypt: str):
        return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(crypt, 'utf-8'))


class Fullpage():
    def __init__(self) -> None:
        pass

    def loginpage(request):
        return render(request, "index.html")

    def matchpw(request):
        username = request.POST['username']
        print(username)
        print(type(username))
        password = request.POST['password']
        try:
            user = Account.objects.filter(Username=username)[0]
        except:
            return render(request, "index.html", context={'logger': f"{request.POST['username']} not found"})
        if crypt.match(password, user.Password):
            return render(request, "landing_page.html",)
        else:
            return render(request, "index.html", context={'logger': "password invalid"})

    # def testpost(request):
    #     Account(Username=request.POST['username'], Password=crypt.hash(
    #         password=request.POST['password'])).save()
    #     print(request.method)
    #     print(request.POST)
    #     print(request.POST['username'])
    #     return render(request, "index.html", context={'logger': f"{request.POST['username']} saved to database"})