from django.shortcuts import render, redirect

def index(request):
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
        return showform(request, context)                 ## 1) works, but doesn't redirect to "localhost:8000/result.html", just shows "localhost:8000"
        # return redirect(showform(request, context))     ## 2) throws error 
        # return redirect("/result")                      ## 2a) throws error
        # return render(request, "result.html", context)  ## 3) works, but same problem as above on #1

    return render(request, "index.html")


def showform(request, context): 
    return render(request, "result.html", context) 

# Create your views here.
