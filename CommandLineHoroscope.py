import requests
import json
import random
import sys

signs = ["aquarius", "pisces", "aries", "taurus", "gemini", "cancer",
         "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"]

url = "http://ohmanda.com/api/horoscope/"

print("Welcome to my Command Line Horoscope app!\nType 'exit' to end the fun!\n")


def getInput():
    print("Enter your birth sign:")
    checkInput(input())


def checkInput(sign):
    if sign.lower() == "exit":
        print(":(")
        sys.exit()
    elif sign.lower() not in signs:
        print("Could not find your sign, try again\n")
    else:
        print("\nWow, I would have guessed you were a " +
              random.choice(signs) + "!\n")
        getHoroscope()
    getInput()


def getHoroscope():
    response = requests.get(url + random.choice(signs))
    data = json.loads(response.content)
    print("Your horoscope for " + data["date"] + " is:\n")
    print("" + data["horoscope"] + "\n")


getInput()
