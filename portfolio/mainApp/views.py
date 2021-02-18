from .models import HomeData, AboutData, SkillData, ResumeData
from django.views.generic import(TemplateView)
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
import json

class Home(TemplateView):
    template_name = 'mainApp/home.html'
    model = HomeData

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homedata = HomeData.objects.first()
        context.update({
            'tab': 'Home',
            'homedata': homedata,
        })
        return context

class About(TemplateView):
    template_name = 'mainApp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutData = AboutData.objects.first()
        skills = SkillData.objects.filter(active = True)
        context.update({
            'tab': 'About',
            'aboutData': aboutData,
            'skills': skills
        })
        return context

class Resume(TemplateView):
    template_name = 'mainApp/resume.html'

    def convertToJson(self, querySetResume):
        """The objects have to be serialized"""
        resumes = []
        resume = {}

        for r in querySetResume:
            resume = {
                "name": r.name,
                "start": r.start.strftime("%d-%b-%Y"),
                "end": r.end.strftime("%d-%b-%Y"),
                "mainText": r.mainText,
                "location": r.location,
                "resume": r.resume,
                "language": r.language,
                "company": r.company,
                "details": [d.detail for d in r.getDetails()]
            }
            resumes.append(resume)
        return json.dumps(resumes)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        resume = ResumeData.getByLanguage(ResumeData, self.request.GET.get('language'))
        mainText = resume.filter(resume="M")
        self.education = resume.filter(resume="E")
        self.experience = resume.filter(resume="X")

        context.update({
            'tab':'Resume',
            'mainText':mainText[0],
            'education': self.education,
            'experience': self.experience
        })
        return context

    def get(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        if self.request.is_ajax() and self.request.method == "GET":
            self.educationJson = self.convertToJson(context["education"])
            self.experienceJson = self.convertToJson(context["experience"])

            if self.request.is_ajax():
                return JsonResponse({
                    "education": self.educationJson,
                    "experience": self.experienceJson
                    }, status= 200)
        else:
            return self.render_to_response(context)
            