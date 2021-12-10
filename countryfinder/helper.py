import requests


def search_unogs(title):

    url = "https://unogsng.p.rapidapi.com/search"

    querystring = {"start_year":"1972","orderby":"rating","audiosubtitle_andor":"and","limit":"100","subtitle":"english","query":title,"audio":"english","country_andorunique":"or","offset":"0","end_year":"2021"}

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': "c43aec1f40msh3fb932bf0de2a5ep1abe40jsn922055654121"
        }

    r = requests.request("GET", url, headers=headers, params=querystring)

    response_unogs = r.json()

    return response_unogs