import requests
from bs4 import BeautifulSoup
from data import answers as data

# definitions
baseUrl = 'https://u.pizzahutsurvey.com/'

headers = {
    'Origin': 'https://u.pizzahutsurvey.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'https://u.pizzahutsurvey.com/Index.aspx?c=475405',
    'Connection': 'keep-alive',
}

# use user input to start the survey
def getUserInput():
    date = raw_input("Date of your visit YYMMDD:")
    time = raw_input("Time of your visit HH:MM:")
    restaurantNumber = raw_input("Restaurant Number:")
    receiptNumber = raw_input("Receipt Number:")

    data[0][2] = restaurantNumber
    data[0][8] = receiptNumber

    data[0][5] = date[:2]
    data[0][4] = date[2:4]
    data[0][3] = date[4:6]

    data[0][6] = time[:2]
    data[0][7] = time[2:4]

def getNextForm(responseData):
    parsedText = BeautifulSoup(responseData, "lxml")
    action = parsedText.find('form', id='surveyForm').get('action')
    return baseUrl + action

def postRequest(fullUrl, cookies, formData):
    r = requests.post(fullUrl, headers=headers, cookies=cookies, data=formData)
    return r.content

def getValCode(responseData):
    parsedText = BeautifulSoup(responseData, "lxml")
    action = parsedText.find('p', attrs={'class':'ValCode'})
    return action.text

def main():
    r = requests.Session()
    r = requests.get('http://www.phfeedbackswe.com/')
    soup = BeautifulSoup(r.content, "lxml")

    # fetch the survey entry form
    action = soup.find('form', id='surveyEntryForm').get('action')
    fullUrl = baseUrl + action

    # start the survey and iterate through all the forms
    for item in range(len(data)):
        print "Form Number: %d -- URL: %s" % (item, fullUrl) 
        response = postRequest(fullUrl, r.cookies, data[item])
        if (item == 15):
            # all done. fetch "ValCode" from the response
            print(getValCode(response))
        else:
            fullUrl = getNextForm(response)


if __name__ == "__main__":
     main()
