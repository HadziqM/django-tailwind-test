from django.shortcuts import render
from .models import Account
import bcrypt


class crypt():
    def __init__(self) -> None:
        pass

    def hash(password: str):
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    def match(password: str, crypt: str):
        return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(crypt, 'utf-8'))


class Fullpage():
    def __init__(self) -> None:
        pass

    def loginpage(request):
        return render(request, "index.html")

    def testpost(request):
        Account(Username=request.POST['username'], Password=crypt.hash(
            password=request.POST['password'])).save()
        print(request.method)
        print(request.POST)
        print(request.POST['username'])
        return render(request, "index.html")
