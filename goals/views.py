from django.shortcuts import render
import pyTigerGraph as tg
import json
import requests
import collections

# Create your views here.

#x = tg.getToken("l69n326p9eavr7asdhrq6ubike8lk53e", setToken=True, lifetime=None)




def home(request):
    context_dict = {}
    #context_dict['problems'] = #
    #graph = tg.TigerGraphConnection(host="https://rtprac1.i.tgcloud.io/", graphname="Goals")

    #authToken = graph.getToken("l69n326p9eavr7asdhrq6ubike8lk53e")

    #print(authToken)

    conn = tg.TigerGraphConnection(host="https://rtprac1.i.tgcloud.io/", graphname="Goals", username="tigergraph", password="tigergraph", apiToken="03sctnp182af43kooj0mdj4ul1c995dt")

    
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



def tni(request, goal_no):
    context_dict = {}
    #context_dict['problems'] = #
    print(goal_no)
    params = {'gid': goal_no} 
    conn = tg.TigerGraphConnection(host="https://rtprac1.i.tgcloud.io/", graphname="Goals", username="tigergraph", password="tigergraph", apiToken="03sctnp182af43kooj0mdj4ul1c995dt")

    preInstalledResult = conn.runInstalledQuery("getTnI", params) 


    #json_object = json.loads(preInstalledResult[0]['gs'][0])
    #for i in preInstalledResult[0]['gs']:
     #   print(i)
    #for i in preInstalledResult:
    #    print(i)
    #print(json.dumps(json_object, indent = 1))
    #print(preInstalledResult[1])
    context_dict['tgts'] = preInstalledResult[0]['L1']
    for i in context_dict['tgts']:
        print(i)
    print("--------------------------------")
    context_dict['inds'] = preInstalledResult[1]['L2']
    context_dict['goal_no'] = goal_no
    for j in context_dict['inds']:
        print(j)

    return render(request, 'tni.html', context_dict)


def tracking(request):
    context_dict = {}
    #context_dict['problems'] = #
    return render(request, 'home.html', context_dict)



def success(request):
    context_dict = {}
    #context_dict['problems'] = #
    return render(request, 'success.html', context_dict)

def goalsinter(request, goal_no):
    context_dict = {}
    context_dict['goal_no'] = goal_no
    #context_dict['problems'] = #
    return render(request, 'goalsinter.html', context_dict)


def partnerships(request, goal_no):
    context_dict = {}
    context_dict['goal_no'] = goal_no
    #context_dict['problems'] = #
    return render(request, 'partnerships.html', context_dict)


def value(request, goal_no):
    context_dict = {}
    context_dict['goal_no'] = goal_no
    #context_dict['problems'] = #
    return render(request, 'value.html', context_dict)


def kg(request, goal_no):
    context_dict = {}
    context_dict['goal_no'] = goal_no
    return render(request, 'kg.html', context_dict)



def matrix(request):
    context_dict = {}
    #context_dict['problems'] = #
    corrs_list = []
    for j in range(1,18):
        url = "https://rtprac1.i.tgcloud.io:9000/graph/Goals/edges/goal/" + str(j) + "/correlation"
        r=requests.get(url, headers={'Authorization':'Bearer 03sctnp182af43kooj0mdj4ul1c995dt'})
        #for i in :
        corrs_matrix = {}
        res = json.loads(r.text)
        for i in res["results"]:
            corrs_matrix[int(i['to_id'])] = i['attributes']['correlation_score']
        od = collections.OrderedDict(sorted(corrs_matrix.items()))
        corrs_list.append(od)
    print("c list :")
    for k in corrs_list:
        print(k)
    context_dict['corrs'] = corrs_list
    return render(request, 'matrix.html', context_dict)

