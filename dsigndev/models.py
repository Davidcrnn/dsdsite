from django.db import models

# Create your models here.
CATEGORY_SITE = (
    ('Site vitrine', 'Site Vitrine'),
    ('Site Catalogue', 'Site Catalogue'),
    ('Blog', 'Site blog'),
    ('Site e-commerce', 'Site e-commerce'),
)

STATUS_CHOICES = {
    ('En développement', 'En développement'),
    ('Refonte du site', 'Refonte du site'),
    ('En ligne', 'En ligne'),
    ('Projet', 'Projet')
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
    url = models.CharField(null=True, blank=True, max_length=250)
    visible = models.BooleanField(default=True)
    year = models.IntegerField(default=2019)

    def __str__(self):
        return self.title
