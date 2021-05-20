from django.shortcuts import render

def index(request):
    return render(request, "index.html")            # initial index.html, then Form action gives new path, which routes back here to .process method below...

def process(request):
    if request.method == "POST":
        
        checklanguages = request.POST.getlist('checklangs[]')       # lines 6-9 take 'checklangs[]' from index.html POST request and then iterate through list
        checkdata = ''                                              # to pull out the data into a string ('checkdata'), which is then matched into
        for x in checklanguages:                                    # the "context" dictionary as value to key of "data"
            checkdata = checkdata + x + " "
        
        context = {
            "name": request.POST['name'],
            "dojo": request.POST['dojo_location'],
            "language": request.POST['fav_language'],
            "radiolanguage": request.POST['radiofav_language'],
            "data": checkdata,
            "comment": request.POST['comment'],
        }
        return render(request, 'result.html', context)              # after context dict built, render the results page with context sent in
    return render(request, 'result.html')