from django.shortcuts import render, HttpResponse
from django.contrib import messages
from myblog.models import Contact, Newsletter
from myblog.models import Post, Keypoints
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    home_post = Post.objects.filter(section='Home').order_by('-id')[0:10]
    upcoming_post = Post.objects.filter(section='frettir').order_by('-id')
    Recent_post = Post.objects.filter(section='featured', status=1).order_by('-id')[0:20]
    Popular_post = Post.objects.all()[0:10]

    context = {
        'upcoming_post': upcoming_post,
        'Recent_post': Recent_post,
        'Popular_post': Popular_post,

        'home_post': home_post,
    }
    return render(request, 'index.html', context)


def about(request):
    # Popular_post = Post.objects.all()[0:10]
    # context = {
    #        'Popular_post':Popular_post,}
    return render(request, 'about.html')


def radgjof(request):
    return render(request, 'radgjof.html')


def adild(request):
    return render(request, 'adild.html')

@login_required()
def contact(request):
    Popular_post = Post.objects.all()[0:10]
    context = {
           'Popular_post':Popular_post,}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        #file_pdf = request.POST['file_pdf']
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request, 'please fill the form correctly .')
        else:
            contact = Contact(name=name, email=email,message=message)
            contact.save()
            messages.success(request, 'your message has been sent.')
    return render(request,'contact.html',context )

# @login_required
# def skodun(request):
#     Popular_post = Post.objects.all()[0:10]
#     context = {
#            'Popular_post':Popular_post,}
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         if len(name)<2 or len(email)<3 or len(message)<4 :
#             messages.error(request, 'please fill the form correctly .')
#         else:
#             contact = Contact(name=name, email=email,message=message)
#             contact.save()
#             messages.success(request, 'your message has been sent.')
#     return render(request,'skodun.html',context )

# def shop(request):
#     Popular_post = Post.objects.all()[0:10]
#     context = {
#            'Popular_post':Popular_post,}
#     return render(request,'shop.html',context)


def blog(request):
    Popular_post = Post.objects.all()[0:10]

    context = {

        'Popular_post': Popular_post,

    }
    return render(request, 'blog.html', context)

#
# @login_required
# def frettir(request):
#     upcoming_post = Post.objects.filter(section='frettir').order_by('-id')
#     key_points = Keypoints.objects.all()
#     Popular_post = Post.objects.all()
#
#     context = {
#         'upcoming_post': upcoming_post,
#         'key_points': key_points,
#         'Popular_post': Popular_post,
#
#     }
#
#     return render(request, 'frettir.html', context)




#
# def News(request):
#     Popular_post = Post.objects.all()[0:10]
#     context = {
#         'Popular_post': Popular_post, }
#     if request.method == 'POST':
#         fullname = request.POST['fullname ']
#         email = request.POST['email']
#
#         if len(fullname) < 2 or len(email) < 3:
#             messages.error(request, 'plz fill the from correctly .')
#
#         else:
#             newsletter = Newsletter(fullname=fullname, email=email)
#             newsletter.save()
#             messages.success(request, 'your message has been send.')
#     return render(request, 'thankyou.html',context)


def SingleBlog(request, slug):
    post = Post.objects.filter(slug=slug).first()
    all_post = Post.objects.all()
    cat = Post.objects.all()
    tag = Post.objects.all()
    Popular_post = Post.objects.all()

    context = {
        'post': post,
        'all_post': all_post,
        'cat': cat,
        'tag': tag,
        'Popular_post': Popular_post,

    }
    return render(request, 'SingleBlog.html', context)