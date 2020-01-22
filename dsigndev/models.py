from django.db import models

# Create your models here.
CATEGORY_SITE = (
    ('Vitrine', 'Site Vitrine'),
    ('Catalogue', 'Site Catalogue'),
    ('Blog', 'Site blog'),
    ('Ecommerce', 'Site e-commerce'),
)

STATUS_CHOICES = {
    ('developpement', 'En développement'),
    ('refonte', 'Refonte du site'),
    ('production', 'En ligne'),
    ('projet', 'Projet')
}


class Projet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='images/')
    image1 = models.FileField(upload_to='images/', null=True, blank=True)
    image2 = models.FileField(upload_to='images/', null=True, blank=True)
    image3 = models.FileField(upload_to='images/', null=True, blank=True)
    category = models.CharField(choices=CATEGORY_SITE, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    url = models.URLField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    year = models.IntegerField(default=2019)

    def __str__(self):
        return self.title


class Message(models.Model):
    nom = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=True, blank=True)
    message = models.TextField()
    Objet = models.CharField(max_length=200)
    email = models.EmailField()
