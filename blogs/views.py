from django.shortcuts import render

def index(request):
#ユーザーのリクエスト情報をもとに、blogs/index.htmlを返す
    return render(request, 'blogs/index.html')