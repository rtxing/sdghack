from django.shortcuts import render

# Create your views here.

from problems.models import Mapuser, Problem

def home(request):
    context_dict = {}
    problems = Problem.objects.all()
    context_dict['problems'] = problems
    return render(request, 'home.html', context_dict)


def tree1(request):
    context_dict = {}
    return render(request, 'tree1.html', context_dict)




def profile(request):
    context_dict = {}
    user = Mapuser.objects.get(username = request.user)
    print(user.tokens)
    return render(request, 'profile.html', context_dict)




def postproblem(request):
    context_dict = {}
    problem_statement = request.POST['problem']
    parent_id = request.POST['parentproblemid']
    #parent = Problem.objects.get(id = parent_id)
    user = Mapuser.objects.get(username = request.user)
    ps = Problem.objects.create(title = problem_statement, created_by = user, parent = parent_id)
     
    return render(request, 'problem_post_success.html', context_dict)




def postproblem2(request):
    context_dict = {}
    problem_statement = request.POST['problem']
    #parent_id = request.POST['parentproblemid']
    #parent = Problem.objects.get(id = parent_id)
    user = Mapuser.objects.get(username = request.user)
    ps = Problem.objects.create(title = problem_statement, created_by = user)
     
    return render(request, 'problem_post_success.html', context_dict)

