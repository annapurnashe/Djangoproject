from django.shortcuts import render

# Create your views here.

def view1(request):
    rollno = 1
    name = 'naresh'
    course = 'python'
    stud = {'rollno': rollno, 'name': name, 'course': course}
    response = render(request, 'dtl1.html', context={'stud': stud})
    return response

def view2(request):
    a = 20
    b = 100
    response = render(request, "dtl2.html", context={'a': a, 'b': b})
    return response

def view3(request):
    name = 'naresh'
    avg = 40
    res = render(request, "dtl3.html", context={'name': name, 'avg': avg})
    return res

def view4(request):
    email_list = ['anu@gmail.com', 'rajesh@gmail.com', 'ankita@gmail.com']
    res = render(request, "dtl4.html", context={'email_list': email_list})
    return res

def view5(request):
    marks = {
        'naresh': [12, 50, 90],
        'ankita': [90, 50, 50],
        'rajesh': [60, 70, 70]
    }
    res = render(request, "dtl5.html", context={'marks': marks})
    return res

def view6(request):
    A = [10, 20, 30, 40, 50]
    B = {'x': 10, 'y': 20, 'z': 30}
    res = render(request, "dtl6.html", context={'A': A, 'B': B})
    return res
