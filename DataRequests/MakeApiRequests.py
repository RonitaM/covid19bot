import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):

        url = "https://covid-193.p.rapidapi.com/countries"
        querystring={"country":country_name}

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "ae0ce7b55fmshb8889405b46bf4fp1b0e59jsn292e281c1c09"
        }

        response = requests.request("GET", url, headers=headers,params=querystring)

        # print(response.text)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self):
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {
            'x-rapidapi-host': "covid19-data.p.rapidapi.com",
            'x-rapidapi-key': "ae0ce7b55fmshb8889405b46bf4fp1b0e59jsn292e281c1c09"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
            "x-rapidapi-key": "ae0ce7b55fmshb8889405b46bf4fp1b0e59jsn292e281c1c09"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result

