from django.http import HttpResponseRedirect


def start_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/home/start/")
