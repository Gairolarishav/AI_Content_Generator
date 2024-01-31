from django.shortcuts import render,redirect
# from django.http import HttpResponse
from AI_Content import ai_genrator
# from . import tweet
# import requests,json

# Create your views here.
def home(request):
     return render(request,'home.html')

def page_not_found(request):
  return render(request,'404.html')

def business(request):
     if request.method == 'POST':
        prompt = request.POST.get('businessPitch', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateBusinessPitch(prompt)
            openAIAnswer = openAIAnswer.replace('\n','<br>')
            return render(request, 'business_pitch.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'business_pitch.html', {'prompt': error_message})
     return render(request,'business_pitch.html')

def cold(request):
     if request.method == 'POST':
        prompt = request.POST.get('coldEmails', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateColdEmail(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'cold_emails.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'cold_emails.html', {'prompt': error_message})
     return render(request,'cold_emails.html')

def job(request):
     if request.method == 'POST':
        prompt = request.POST.get('jobDescription', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateJobDescription(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'job_discription.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'job_discription.html', {'prompt': error_message})
     return render(request,'job_discription.html')

def product(request):
      if request.method == 'POST':
        prompt = request.POST.get('productDescription', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateProductDescription(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'product_discription.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the product title."
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'product_discription.html', {'prompt': error_message})
      return render(request,'product_discription.html')

def social(request):
     if request.method == 'POST':
        prompt = request.POST.get('socialMedia', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateSocialMedia(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'social_media.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'social_media.html', {'prompt': error_message})
     return render(request,'social_media.html')

def tweet(request):
     if request.method == 'POST':
        prompt = request.POST.get('tweetIdeas', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateTweetIdeas(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'tweet_ideas.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'tweet_ideas.html', {'prompt': error_message})
     return render(request,'tweet_ideas.html')

def videodesc(request):
     if request.method == 'POST':
        prompt = request.POST.get('videoDescription', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateVideoDescription(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'video_description.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'video_description.html', {'prompt': error_message})
     return render(request,'video_description.html')

def videoideas(request):
     if request.method == 'POST':
        prompt = request.POST.get('videoIdeas', '').strip()

        if prompt:
            openAIAnswer = ai_genrator.generateVideoIdeas(prompt)
            openAIAnswer = openAIAnswer.replace('\n', '<br>')
            return render(request, 'video_ideas.html', {'openAIAnswer': openAIAnswer, 'prompt': prompt})
        else:
            # Handle the case when the product title is empty
            error_message = "Please add something in the input section"
            return render(request, 'video_ideas.html', {'prompt': error_message})
     return render(request,'video_ideas.html')


