from django.http import JsonResponse
# Create your views here.
import requests
import json

from werkzeug.wrappers import response
import selenium
import time
from selenium import webdriver
#OPTIONAL PACKAGE, BUY MAYBE NEEDED
from webdriver_manager.chrome import ChromeDriverManager

def test(request):
	return JsonResponse({"message":"please provide username in url"})
def start_scrape(request,username):

    #THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
    # CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    # driver = webdriver.Chrome("./chromedriver",options=options)

    #THIS PRETTY MUCH TELLS THE WEB BROWSER WHICH WEBSITE TO GO TO
    driver.get(f'https://tokcounter.com/?user={username}')

    time.sleep(5)
    try:
        FOLLOWERS = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[4]/div[1]/div').text
        LIKES = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[4]/div[2]/div[1]/div/div/div').text
        FOLLOWING = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[4]/div[2]/div[2]/div/div/div/span/span[2]/span/span/span').text
        UPLOADS = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[4]/div[2]/div[3]/div/div/div').text
    
        #PRINTS OUT THE DATA PULLED FROM ABOVE
        followers=FOLLOWERS.split('\n')
        followers="".join(followers)
        
        likes = LIKES.split('\n')
        likes="".join(likes)

        following = FOLLOWING.split('\n')
        following="".join(following)

        uploads = UPLOADS.split('\n')
        uploads="".join(uploads)

        details = {
            "Username": username,
            "Live Followers": followers,
            "Likes":likes,
            "Following":following,
            "Uploads": uploads,
            # "Followers Rank": followers_rank
        }

        return JsonResponse(details)
    except:
        details = {
            "Message":"Something went wrong, please try again!"
        }
        return JsonResponse(details)


