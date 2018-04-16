from django.shortcuts import render

# NEW 16/04/2018
def post_list(request):
    return render(request, 'blog/post_list.html', {})
