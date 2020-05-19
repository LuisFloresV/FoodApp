from django.shortcuts import render
import requests



def home(request):
    context = {}
    if request.method == 'POST':
        query = request.POST['q']
        url = 'http://www.recipepuppy.com/api/?q={}'
        #This line do the request
        f = requests.get(url.format(query)).json()
        food_recipe = {
            'title' : f['results'][0]['title'],
            'ingredients' : f['results'][0]['ingredients'],
            'href' : f['results'][0]['href'],
        }
        context = {'food_recipe' : food_recipe}
        print (context)
    return render(request,'home.html',context)
   