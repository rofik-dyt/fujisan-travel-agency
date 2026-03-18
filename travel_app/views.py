from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TravelPackage, BlogPost, Testimonial, ContactMessage

def home_view(request):
    packages = TravelPackage.objects.all()[:3]
    blogs = BlogPost.objects.all().order_by('-created_at')[:3]
    testimonials = Testimonial.objects.all()
    context = {
        'packages': packages,
        'blogs': blogs,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def packages_view(request):
    packages = TravelPackage.objects.all()
    context = {'packages': packages}
    return render(request, 'packages.html', context)

def blog_list_view(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def blog_detail_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill out all required fields.')
            
    return render(request, 'contact.html')

def login_view(request):
    return redirect('admin:login')
