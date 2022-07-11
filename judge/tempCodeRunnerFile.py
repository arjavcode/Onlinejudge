def registerPage(request):
    context = {}
    return render(request, 'judge/register.html' , context)

def loginPage(request):
    context = {}
    return render(request, 'judge/login.html' , context)
