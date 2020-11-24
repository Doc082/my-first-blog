from django.shortcuts import render


def post_list(request):
    return render(request, 'sblog/post_list.html', {})