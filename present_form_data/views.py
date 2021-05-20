from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        
        checklanguages = request.POST.getlist('checklangs[]')       # lines 6-9 put the list of checkbox items ('checklangs[]') from index.html and then iterate 
        checkdata = ''                                              # through the list to pull out the data into a string ('checkdata'), which is then matched into
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
        return render(request, 'result.html', context)
    return render(request, 'result.html')