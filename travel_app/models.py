from django.db import models

class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=100) # e.g. "5 Days / 4 Nights"
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    rating = models.IntegerField(default=5) # e.g. 1 to 5
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.customer_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
