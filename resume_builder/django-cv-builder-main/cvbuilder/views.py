from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .mixins import LoginRequiredMixin
from .models import (Education, Resume, Experience,
                     Skill, Language, Achievement, Publication)
from .forms import ResumeForm, ExperienceForm
from django.contrib import messages
from django.urls import reverse
from .mixins import (OwnerResumeUpdateView, OwnerResumeCreateView,
                     OwnerResumeDeleteView, SaveModelOrderMixin)
from wkhtmltopdf.views import PDFTemplateView


# ---- DOWNLOAD AS PDF ---- #

class PDFView(PDFTemplateView):
    cmd_options = {
        'margin-top': 0,
        'margin-left': 0,
        'margin-right': 0,
        'margin-bottom': 3,
    }

    def get_filename(self):
        resume = Resume.objects.get(user=self.request.user)
        return resume.name.replace(" ", "_") + '_Resume.pdf'

    def get_template_names(self):
        return self.get_template_name_color()['template_name']

    def get_context_data(self, **kwargs):
        context = super(PDFView, self).get_context_data(**kwargs)
        resume = Resume.objects.get(user=self.request.user)
        context = {
            'resume': resume,
            'experiences': resume.experiences.all().order_by('order'),
            'skills': resume.skills.all().order_by('order'),
            'educations': resume.educations.all().order_by('order'),
            'languages': resume.languages.all().order_by('order'),
            'achievements': resume.achievements.all().order_by('order'),
            'publications': resume.publications.all().order_by('order'),
            'color': self.get_template_name_color()['color'],
        }
        return context

    def get_template_name_color(self):
        template_name = 'cvbuilder/resumes/default.html'
        resume = Resume.objects.get(user=self.request.user)
        color = 'blue'
        template = resume.template
        if not template is None:
            if not template.name == "":
                template_name = 'cvbuilder/resumes/' + template.name.split(" ")[0].lower() + '.html'
                color = template.name.split(" ")[1].lower()
        return {
            'template_name': template_name,
            'color': color
        }


# ---- MAIN PAGE - EDIT OF DETAILS ---- #

class MainPage(LoginRequiredMixin, View):
    template_name = 'cvbuilder/0_mainpage.html'

    def get(self, request):
        try:
            resume = Resume.objects.get(user=request.user)
        except Resume.DoesNotExist:
            resume = Resume(user=request.user, name=request.user.username)
            resume.save()

        ctx = {
            'resume': resume,
            'form': ResumeForm(instance=resume),
            'experiences': resume.experiences.all().order_by('order'),
            'skills': resume.skills.all().order_by('order'),
            'educations': resume.educations.all().order_by('order'),
            'languages': resume.languages.all().order_by('order'),
            'achievements': resume.achievements.all().order_by('order'),
            'publications': resume.publications.all().order_by('order'),
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        resume = Resume.objects.get(user=request.user)
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if not form.is_valid: return render(request, self.template_name, {'form': form})
        form.save()
        messages.info(request, 'Resume information saved')
        return redirect(reverse('cvbuilder:MainPage'))


# --- RESUME VIEW AS HTML ---- #

class ResumePreview(LoginRequiredMixin, View):
    def get(self, request):
        resume = Resume.objects.get(user=request.user)
        template = resume.template

        # Default Template Values
        template_name = 'cvbuilder/resumes/default.html'
        color = 'blue'

        if not template is None:
            if not template.name == "":
                template_name = 'cvbuilder/resumes/' + template.name.split(" ")[0].lower() + '.html'
                color = template.name.split(" ")[1]

        if not resume.user == request.user: return redirect(reverse('pages:NoAccess'))
        ctx = {
            'resume': resume,
            'experiences': resume.experiences.all().order_by('order'),
            'skills': resume.skills.all().order_by('order'),
            'educations': resume.educations.all().order_by('order'),
            'languages': resume.languages.all().order_by('order'),
            'achievements': resume.achievements.all().order_by('order'),
            'publications': resume.publications.all().order_by('order'),
            'color': color.lower(),
        }
        return render(request, template_name, ctx)


# --- SHARED RESUME VIEW AS HTML ---- #

class SharedResumePreview(View):
    def get(self, request, code):
        resume = Resume.objects.get(code=code)
        template = resume.template

        # Default Template Values
        template_name = 'cvbuilder/resumes/default.html'
        color = 'blue'

        if not template is None:
            if not template.name == "":
                template_name = 'cvbuilder/resumes/' + template.name.split(" ")[0].lower() + '.html'
                color = template.name.split(" ")[1]

        ctx = {
            'resume': resume,
            'experiences': resume.experiences.all().order_by('order'),
            'skills': resume.skills.all().order_by('order'),
            'educations': resume.educations.all().order_by('order'),
            'languages': resume.languages.all().order_by('order'),
            'achievements': resume.achievements.all().order_by('order'),
            'publications': resume.publications.all().order_by('order'),
            'shared_view': 1,
            'color': color.lower(),
        }

        return render(request, template_name, ctx)


#### --------------------- CRUD VIEWS --------------------- ####

# ---- Experience CRUD --- #

class SaveExperienceOrdering(SaveModelOrderMixin):
    model = Experience


class CreateExperience(OwnerResumeCreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'cvbuilder/crud_experience.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class UpdateExperience(OwnerResumeUpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'cvbuilder/crud_experience.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeleteExperience(OwnerResumeDeleteView):
    model = Experience
    success_url = reverse_lazy('cvbuilder:MainPage')


# ---- Skills CRUD --- #

class SaveSkillsOrder(SaveModelOrderMixin):
    model = Skill


class CreateSkill(OwnerResumeCreateView):
    model = Skill
    fields = ['title']
    template_name = 'cvbuilder/crud_skill.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeleteSkill(OwnerResumeDeleteView):
    model = Skill
    success_url = reverse_lazy('cvbuilder:MainPage')


# ---- Education CRUD --- #

class SaveEducationOrder(SaveModelOrderMixin):
    model = Education


class CreateEducation(OwnerResumeCreateView):
    model = Education
    fields = ['title', 'description', 'duration']
    template_name = 'cvbuilder/crud_education.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class UpdateEducation(OwnerResumeUpdateView):
    model = Education
    fields = ['title', 'description', 'duration']
    template_name = 'cvbuilder/crud_education.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeleteEducation(OwnerResumeDeleteView):
    model = Education
    success_url = reverse_lazy('cvbuilder:MainPage')


# ---- Language CRUD --- #

class SaveLanguageOrder(SaveModelOrderMixin):
    model = Language


class CreateLanguage(OwnerResumeCreateView):
    model = Language
    fields = ['title', 'level']
    template_name = 'cvbuilder/crud_language.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class UpdateLanguage(OwnerResumeUpdateView):
    model = Language
    fields = ['title', 'level']
    template_name = 'cvbuilder/crud_language.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeleteLanguage(OwnerResumeDeleteView):
    model = Language
    success_url = reverse_lazy('cvbuilder:MainPage')


# ---- Achievement CRUD --- #

class SaveAchievementOrder(SaveModelOrderMixin):
    model = Achievement


class CreateAchievement(OwnerResumeCreateView):
    model = Achievement
    fields = ['title', 'description']
    template_name = 'cvbuilder/crud_achievement.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class UpdateAchievement(OwnerResumeUpdateView):
    model = Achievement
    fields = ['title', 'description']
    template_name = 'cvbuilder/crud_achievement.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeleteAchievement(OwnerResumeDeleteView):
    model = Achievement
    success_url = reverse_lazy('cvbuilder:MainPage')


# ---- Publication CRUD --- #

class SavePublicationOrder(SaveModelOrderMixin):
    model = Publication


class CreatePublication(OwnerResumeCreateView):
    model = Publication
    fields = ['title', 'description']
    template_name = 'cvbuilder/crud_publication.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class UpdatePublication(OwnerResumeUpdateView):
    model = Publication
    fields = ['title', 'description']
    template_name = 'cvbuilder/crud_publication.html'
    success_url = reverse_lazy('cvbuilder:MainPage')


class DeletePublication(OwnerResumeDeleteView):
    model = Publication
    success_url = reverse_lazy('cvbuilder:MainPage')