import openai
import requests
import json
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
URL = "https://api.openai.com/v1/chat/completions"

def generateProductDescription(prompt):
    productdesc = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Generate Product Description on: {prompt}. \n \n Don't generate desciption if it is not a product."}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = productdesc)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateBusinessPitch(prompt):
    businesspitch = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Generate Business Pitch on : {prompt}. \n \n like how to pitch ,so that it is help to gow our business"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = businesspitch)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateColdEmail(prompt):
    coldemail = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Cold Email Generator on: {prompt}. \n \n,Try to generate it in more professional manners"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = coldemail)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateJobDescription(prompt):
    jobdesc = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Job Description Generator: {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = jobdesc)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateSocialMedia(prompt):
    socialmedia = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"You are social media advert ideas Generator: {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = socialmedia)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateTweetIdeas(prompt):
    tweetideas = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Genrate tweet ideas with hashtags on : {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = tweetideas)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateVideoDescription(prompt):
    videodesc = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Youtube Video Description Generator: {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = videodesc)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateVideoIdeas(prompt):
    videoideas = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Youtube Video Ideas Generator: {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = videoideas)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

