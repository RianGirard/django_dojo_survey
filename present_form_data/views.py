from django.shortcuts import redirect, render

def index(request):
    return render(request, "index.html")            # initial GET request for index.html

# def process(request):
#     if request.method == "POST":
        
#         checklanguages = request.POST.getlist('checklangs[]')       # lines 6-9 take 'checklangs[]' from index.html POST request and then iterate through list
#         checkdata = ''                                              # to pull out the data into a string ('checkdata'), which is then matched into
#         for x in checklanguages:                                    # the "context" dictionary as value to key of "data"
#             checkdata = checkdata + x + " "
        
#         context = {
#             "name": request.POST['name'],
#             "dojo": request.POST['dojo_location'],
#             "language": request.POST['fav_language'],
#             "radiolanguage": request.POST['radiofav_language'],
#             "data": checkdata,
#             "comment": request.POST['comment'],
#         }
#         return render(request, 'result.html', context)              # after context dict built, render the results page with context sent in
#     return render(request, 'result.html')

def process(request):                               # POST request triggered by the Form action on index.html
    if request.method == "POST":
        
        checklanguages = request.POST.getlist('checklangs[]')       # lines 28-31 take 'checklangs[]' from index.html POST request and then iterate through list
        checkdata = ''                                              # to pull out the data into a string ('checkdata'), which is then matched into
        for x in checklanguages:                                    # the "context" dictionary as value to key of "data"
            checkdata = checkdata + x + " "

        request.session['name'] = request.POST['name']              # request.session is the new dict, so no longer need "context"
        request.session['dojo'] = request.POST['dojo_location']     # leave comma separators out between these lines or you will get ['brackets'] around the 
        request.session['language'] = request.POST['fav_language']  # text values of the session variables
        request.session['radiolanguage'] = request.POST['radiofav_language']
        request.session['data'] = checkdata
        request.session['comment'] = request.POST['comment']

        return redirect('/result')

def result(request):                                # GET request triggered by redirect from .process (above)
    return render(request, 'result.html')