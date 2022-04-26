import pysbd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from wikipediaapi import Wikipedia

from .models import Project, Sentence


class Home(TemplateView):
    def get(self, request):
        return render(request, 'home.html')


class Login(TemplateView):
    def get(self, request):
        return render(request, 'login.html')


class SignUp(TemplateView):
    def get(self, request):
        return render(request, 'signup.html')


class Translate(TemplateView):
    def get(self, request):
        target_lang = request.GET.get('target_lang')
        wiki_title = request.GET.get('wiki_title')
        if request.user.is_authenticated:
            project_object, created = Project.objects.prefetch_related("sentence_set").get_or_create(
                user=request.user, wiki_title=wiki_title, target_lang=target_lang)
            if created:
                page = Wikipedia().page(wiki_title)
                if page.exists():
                    intro = page.summary
                    sentences = [Sentence(user=request.user, project=project_object, target_lang=target_lang, original_sentence=sentence,
                                          translated_sentence="") for sentence in pysbd.Segmenter(language='en', clean=False).segment(intro)]
                    Sentence.objects.bulk_create(sentences)
                    context = {"intro_list": sentences,
                               "target_lang": target_lang}
                else:
                    context = {"intro_list": [Sentence(
                        original_sentence="Page Not Found.", translated_sentence="")], "target_lang": target_lang}
            else:
                context = {"intro_list": project_object.sentence_set.all(
                ), "target_lang": target_lang}
        else:
            page = Wikipedia().page(wiki_title)
            intro = page.summary if page.exists() else "Page not Found."
            sentences = pysbd.Segmenter(
                language='en', clean=False).segment(intro)
            context = {"intro_list": [Sentence(original_sentence=sentence, translated_sentence="")
                                      for sentence in sentences], "target_lang": target_lang}
        return render(request, 'translate.html', context=context)


class Projects(TemplateView):
    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        return render(request, 'projects.html', context={"projects": projects})


class SaveSentence(APIView):
    def post(self, request):
        translated_sentence = request.data.get('translated_sentence')
        sentence = Sentence.objects.get(user=request.user, id=request.data.get(
            "sentence_id"), target_lang=request.data.get("target_lang"))
        sentence.translated_sentence = translated_sentence
        sentence.save()
        return HttpResponse("Sentence Saved Successfully.")
