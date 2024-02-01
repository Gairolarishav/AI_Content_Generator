from django.urls import path
from AI_Content import views

urlpatterns = [
    path('',views.home,name='home'),
    path('business_pitch/',views.business,name='business'),
    path('cold_emails/',views.cold,name='cold'),
    path('job_discription/',views.job,name='job'),
    path('product_discription/',views.product,name='product'),
    path('social_media/',views.social,name='social'),
    path('tweet_ideas/',views.tweet,name='tweet'),
    path('video_description/',views.videodesc,name='videodesc'),
    path('video_ideas/',views.videoideas,name='videoideas'),
    path('language_translator/',views.LanguageTranslator,name='translator'),
]