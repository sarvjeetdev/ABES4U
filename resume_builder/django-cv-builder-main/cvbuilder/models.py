from django.db import models
from django.conf import settings
import random
import string


class Template(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Resume(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='cv_images', null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, verbose_name='Name-Surname')
    description = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    career_summary = models.TextField(blank=True, verbose_name='Career Summary')
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=8, default="", blank=True, unique=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.description)

    def save(self, *args, **kwargs):
        if self.code == "": self.code = self.get_resume_code()
        super().save(*args, **kwargs)

    def get_resume_code(self):
        length = 8
        while True:
            code = ''.join(random.choices(string.ascii_uppercase, k=length))
            if Resume.objects.filter(code=code).count() == 0:
                break
        return code

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    tech = models.TextField(blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    order = models.IntegerField(blank=False, default=100_000)

    def tech_as_list(self):
        tech_list = ""
        if not self.tech == "":
            tech_list = self.tech.replace(", ", ",").split(',')
            tech_list = [x[0].upper() + x[1:] for x in tech_list]
        return tech_list

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class Skill(models.Model):
    title = models.CharField(max_length=38)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, verbose_name='Department')
    duration = models.CharField(max_length=255)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='achievements')
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


class Language(models.Model):
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='publications')
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'













