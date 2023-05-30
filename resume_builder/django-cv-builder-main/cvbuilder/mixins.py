from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resume
from django.http import HttpResponse
from django.db import transaction
from django.views import View


class OwnerResumeCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        object = form.save(commit=False)
        resume = Resume.objects.get(user=self.request.user)
        object.resume = resume
        object.save()
        return super(OwnerResumeCreateView, self).form_valid(form)


class OwnerResumeUpdateView(UpdateView):
    def get_queryset(self):
        qs = super(OwnerResumeUpdateView, self).get_queryset()
        resume = Resume.objects.get(user=self.request.user)
        return qs.filter(resume=resume)


class OwnerResumeDeleteView(DeleteView):
    def get_queryset(self):
        qs = super(OwnerResumeDeleteView, self).get_queryset()
        resume = Resume.objects.get(user=self.request.user)
        return qs.filter(resume=resume)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SaveModelOrderMixin(View):
    model = None

    def post(self, request):
        ordered_ids = request.POST.get('ordering')
        if len(ordered_ids) > 0:
            ordered_ids = ordered_ids.split(',')
            with transaction.atomic():
                current_order = 1
                for lookup_id in ordered_ids:
                    object = self.model.objects.get(id=lookup_id)
                    if not object.resume.user == self.request.user: return HttpResponse(status=400)
                    object.order = current_order
                    object.save()
                    current_order += 1
        return HttpResponse(status=204)