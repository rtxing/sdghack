from django.shortcuts import render
import pyTigerGraph as tg
import json

# Create your views here.

#x = tg.getToken("l69n326p9eavr7asdhrq6ubike8lk53e", setToken=True, lifetime=None)




def home(request):
    context_dict = {}
    #context_dict['problems'] = #
    #graph = tg.TigerGraphConnection(host="https://rtprac1.i.tgcloud.io/", graphname="Goals")

    #authToken = graph.getToken("l69n326p9eavr7asdhrq6ubike8lk53e")

    #print(authToken)

    conn = tg.TigerGraphConnection(host="https://rtprac1.i.tgcloud.io/", graphname="Goals", username="tigergraph", password="tigergraph", apiToken="nthnehl40m4ftjmefsl8vc3uosfg4isc")

    
    #x = conn.getToken("l69n326p9eavr7asdhrq6ubike8lk53e", "1000000")
    
    params = {} 
    preInstalledResult = conn.runInstalledQuery("goals1", params) 


    #json_object = json.loads(preInstalledResult[0]['gs'][0])
    #for i in preInstalledResult[0]['gs']:
     #   print(i)
    #for i in preInstalledResult:
    #    print(i)
    #print(json.dumps(json_object, indent = 1))
    context_dict['goals'] = preInstalledResult[0]['gs']

    return render(request, 'home.html', context_dict)



def tni(request):
    context_dict = {}
    #context_dict['problems'] = #
    return render(request, 'home.html', context_dict)


def tracking(request):
    context_dict = {}
    #context_dict['problems'] = #
    return render(request, 'home.html', context_dict)


def matrix(request):
    context_dict = {}
    #context_dict['problems'] = #
    return render(request, 'home.html', context_dict)

