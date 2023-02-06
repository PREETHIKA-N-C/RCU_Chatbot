import email
from typing import Type
from unittest import result
from flask import Flask, request, jsonify
import json
import requests
import datetime
from datetime import date
from requests.auth import HTTPBasicAuth
# from flask_ngrok import run_with_ngrok
# from datetime import datetime
# from flask_lt import run_with_lt
import sys
from zeep import Client
import os
import dateutil
# from sympy import li
import xmltodict, json
import pyjokes
#  Defining PORT no and Credentials
app = Flask(__name__)
# run_with_ngrok(app)
# port = "80"
# link= "https://c750-27-5-155-86.ngrok.io"
login_data = {
    "d": {
        "results": [
            {"Email": "kchandrasekar@kaartech.com", "Password": "chandru"},
            {"Email": "m.alsobhi@rcu.gov.sa", "Password": "alsobhi"},
             {"Email": "01419", "Password": "12345"},
        ]
    }
}


#Pending Approval
@app.route("/pending_Approvals", methods=["POST"])
def pending_Approvals():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    PR_value = data["conversation"]["memory"]["PR_No"]["scalar"]
    memory=data['conversation']['memory']
    PR_No = "PR" + str(PR_value)
    print(PR_No)

    response1 = requests.post("https://api.mn2.ariba.com/v2/oauth/token?grant_type=openapi_2lo",
    headers = {
        'Authorization': 'Basic MGE2ZWE1Y2YtZThhMy00ZmU3LWIxNTctYTBhNWE0MTUwMDlmOm1zeWNDbURhbG1rM21qOEp1eVVDdXhLcnJ5OGN3elhs'
      }
    )

    data1 = response1.json()
    a1 = data1["access_token"]
    print (a1)
    a = 'Bearer '+ a1

    response = requests.get("https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables?realm=RCU-1&$filter=approvableType eq 'requisitions'",
    headers = {
        'Authorization': a,
        'Content-Type' : 'application/json',
        'apiKey' : 'KQP7qFHbHBO41kEk9IrbRaw0i1tbei9S'
      }
    )

    data = response.json()

    # json_url = os.path.join("/", "/", "pa.json")
    # data = json.load(open(json_url))
    # data=pa.json
    # t=open(pa.json,r)
    # f = open("pa.json")
    # data = json.load(f)
    pr_no1 = ""
    type = ""
    Desc = ""
    Date = ""
    approver = ""
    email = ""

    for attrs in data["value"]:
        if attrs["approvableUniqueName"] == PR_No:
            pr_no1 = attrs["approvableUniqueName"]
            type = attrs["approvableType"]
            Desc = attrs["description"]
            Date = attrs["assignedDate"]
            approver = attrs["approver"]
            email = attrs["email"]
            break
        else:
            pr_no1 = "Not found"
            type = "Not found"
            Desc = "Not found"
            Date = "Not found"
            approver = "Not found"
            email = "Not found"
    memory["PR_Value"]= pr_no1,
    memory["Type"]= type
    memory["Description"]= Desc
    memory["Date"]= Date
    memory["Approver"]= approver
    memory["Approver_Mail"]= email
    memory["Auth_Status"]= "SUCCESS"

    # Date = str(Date)
    return jsonify(
        {
            "conversation": {
                "memory": memory
                
            }
        }
    )


def processinput(text):
    print(type(text))
    sw_nltk = [
        "i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours",
        "ourselves",
        "you",
        "you're",
        "you've",
        "you'll",
        "you'd",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "she's",
        "her",
        "hers",
        "herself",
        "it",
        "it's",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "that'll",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "don't",
        "should",
        "should've",
        "now",
        "d",
        "ll",
        "m",
        "o",
        "re",
        "ve",
        "y",
        "ain",
        "aren",
        "aren't",
        "couldn",
        "couldn't",
        "didn",
        "didn't",
        "doesn",
        "doesn't",
        "hadn",
        "hadn't",
        "hasn",
        "hasn't",
        "haven",
        "haven't",
        "isn",
        "isn't",
        "ma",
        "mightn",
        "mightn't",
        "mustn",
        "mustn't",
        "needn",
        "needn't",
        "shan",
        "shan't",
        "shouldn",
        "shouldn't",
        "wasn",
        "wasn't",
        "weren",
        "weren't",
        "won",
        "won't",
        "wouldn",
        "wouldn't",
    ]
    words = [word for word in text.split() if word.lower() not in sw_nltk]
    new_text = " ".join(words)
    return new_text


def solve(s0, s1):
    s0 = s0.lower()
    s1 = s1.lower()
    s0List = s0.split(" ")
    s1List = s1.split(" ")
    #print(s1List,s0List)
    return len(list(set(s0List) & set(s1List)))


@app.route("/pending_Approvals2", methods=["POST"])
def pending_Approvals2():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    PR_value = data["conversation"]["memory"]["selected_pr"]
    memory=data["conversation"]["memory"]
    x = PR_value.partition(" ")
    PR_No = x[0]
    print(PR_No)

    response1 = requests.post("https://api.mn2.ariba.com/v2/oauth/token?grant_type=openapi_2lo",
    headers = {
        'Authorization': 'Basic MGE2ZWE1Y2YtZThhMy00ZmU3LWIxNTctYTBhNWE0MTUwMDlmOm1zeWNDbURhbG1rM21qOEp1eVVDdXhLcnJ5OGN3elhs'
      }
    )

    data1 = response1.json()
    a1 = data1["access_token"]
    print (a1)
    a = 'Bearer '+ a1

    response = requests.get("https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables?realm=RCU-1&$filter=approvableType eq 'requisitions'",
    headers = {
        'Authorization': a,
        'Content-Type' : 'application/json',
        'apiKey' : 'KQP7qFHbHBO41kEk9IrbRaw0i1tbei9S'
      }
    )

    data = response.json()
    
    pr_no1 = ""
    type = ""
    Desc = ""
    Date = ""
    approver = ""
    email = ""

    for attrs in data["value"]:
        if attrs["approvableUniqueName"] == PR_No:
            pr_no1 = attrs["approvableUniqueName"]
            type = attrs["approvableType"]
            Desc = attrs["description"]
            Date = attrs["assignedDate"]
            approver = attrs["approver"]
            email = attrs["email"]
            break
        else:
            pr_no1 = "Not found"
            type = "Not found"
            Desc = "Not found"
            Date = "Not found"
            approver = "Not found"
            email = "Not found"
    memory["PR_Value"]=pr_no1
    memory["Description"]= Desc
    memory["Date"]= Date
    memory["Approver"]= approver
    memory["Approver_Mail"]= email
    print("PR Value")
    print(pr_no1, Desc)
    

    # Date = str(Date)
    return jsonify(
        {
            "conversation": {
                "memory": memory
            }
        }
    )




@app.route("/pending_Approval", methods=["POST"])
def pending_Approval():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    PR_value = data["conversation"]["memory"]["PR_No"]["scalar"]
    memory=data["conversation"]["memory"]
    PR_No = "PR" + str(PR_value)
    print(PR_No)

    response1 = requests.post("https://api.mn2.ariba.com/v2/oauth/token?grant_type=openapi_2lo",
    headers = {
        'Authorization': 'Basic MGE2ZWE1Y2YtZThhMy00ZmU3LWIxNTctYTBhNWE0MTUwMDlmOm1zeWNDbURhbG1rM21qOEp1eVVDdXhLcnJ5OGN3elhs'
      }
    )

    data1 = response1.json()
    a1 = data1["access_token"]
    print (a1)
    a = 'Bearer '+ a1

    response = requests.get("https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables?realm=RCU-1&$filter=approvableType eq 'requisitions'",
    headers = {
        'Authorization': a,
        'Content-Type' : 'application/json',
        'apiKey' : 'KQP7qFHbHBO41kEk9IrbRaw0i1tbei9S'
      }
    )

    data = response.json()

    # json_url = os.path.join("/", "/", "pa.json")
    # data = json.load(open(json_url))
    # data=pa.json
    # t=open(pa.json,r)
    # f = open("pa.json")
    # data = json.load(f)
    pr_no1 = ""
    type = ""
    Desc = ""
    Date = ""
    approver = ""
    email = ""

    for attrs in data["value"]:
        if attrs["approvableUniqueName"] == PR_No:
            pr_no1 = attrs["approvableUniqueName"]
            type = attrs["approvableType"]
            Desc = attrs["description"]
            Date = attrs["assignedDate"]
            approver = attrs["approver"]
            email = attrs["email"]
            break
        else:
            pr_no1 = "Not found"
            type = "Not found"
            Desc = "Not found"
            Date = "Not found"
            approver = "Not found"
            email = "Not found"
    memory['PR_Value']=pr_no1
    memory['Type']=type
    memory['Description']=Desc
    memory['Date']=Date
    memory['Approver']=approver
    memory['Approver_Mail']=email

    # Date = str(Date)
    return jsonify(
        {
            "conversation": {
                "memory": memory

            }
        }
    )


@app.route("/pending_Approvals_Description", methods=["POST"])
def pending_Approvals_Description():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    PR_value = data["conversation"]["memory"]["description"]
    memory=data["conversation"]["memory"]
    memory["pr_flag"]="True"

    PR_No = str(PR_value)  # user input string....

    processed_user_input = processinput(PR_No)
    print(processed_user_input)

    response1 = requests.post("https://api.mn2.ariba.com/v2/oauth/token?grant_type=openapi_2lo",
    headers = {
        'Authorization': 'Basic MGE2ZWE1Y2YtZThhMy00ZmU3LWIxNTctYTBhNWE0MTUwMDlmOm1zeWNDbURhbG1rM21qOEp1eVVDdXhLcnJ5OGN3elhs'
      }
    )

    data1 = response1.json()
    a1 = data1["access_token"]
    print (a1)
    a = 'Bearer '+ a1

    response = requests.get("https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables?realm=RCU-1&$filter=approvableType eq 'requisitions'",
    headers = {
        'Authorization': a,
        'Content-Type' : 'application/json',
        'apiKey' : 'KQP7qFHbHBO41kEk9IrbRaw0i1tbei9S'
      }
    )

    data = response.json()
    # print(data)
    output_list = []  # final ouptut array
    
    x = ""

    def solve(s0, s1):
        s0 = s0.lower()
        s1 = s1.lower()
        s0List = s0.split(" ")
        s1List = s1.split(" ")
        return len(list(set(s0List) & set(s1List)))
    
    for i in data["value"]:
        temp = {}

        s = i["description"] + " " + i["assignedDate"] + " " + i["approver"]+" "+i["approvableUniqueName"][2:]
        score = solve(s, processed_user_input)
        print(score)
        if score >= 0:
            # print(i["approvableUniqueName"]+" "+i['description'])
            output_list.append(i["approvableUniqueName"]+" "+i['description'])
            # print(output_list)
        
    type(output_list)
    
    print(output_list)
    # print(output_list)
    # count=len(output_list)
    # output_list=set(output_list)
    # output_list=list(output_list)
    count=len(output_list)
    if count<1:
        memory["pr_flag"]="False"
    print(output_list)
    # Date = str(Date)
    memory["pr_array"]=output_list
    memory["count"]=count
    # print(count)

    # print(memory)
    return jsonify({"conversation": {"memory": memory
    ,"merge":True}})
    # output_list = []


@app.route("/authentication", methods=["POST"])
def authentication():
    data = json.loads(request.get_data())
    Email = data["conversation"]["memory"]["Email"]
    Password = data["conversation"]["memory"]["Password"]

    for attrs in login_data["d"]["results"]:
        if attrs["Email"] == Email and attrs["Password"] == Password:
            authentication_status = "SUCCESS"
            break
        else:
            authentication_status = "Failed"
    print(authentication_status)
    return jsonify({"conversation": {"memory": {"Auth_Status": authentication_status,"link":link}}})

#ms to date
@app.route("/mstodate", methods=["POST"])
def mstodate():
    data = json.loads(request.get_data())
    ms = data["conversation"]["memory"]["ms"]
    memory=data["conversation"]["memory"]
    l1=len(ms)
    ms=ms[6:l1-2]
    ms = int(ms)
    # ms = 1554076800000
    # ms = 1115076800000
    date = datetime.datetime.fromtimestamp(ms/1000.0)
    memory['date']=date


    return jsonify({"conversation": {"memory": memory}})
#end of ms to date

#ms to date_of_joining
@app.route("/mstodate_of_joining", methods=["POST"])
def mstodate_of_joining():
    data = json.loads(request.get_data())
    ms = data["conversation"]["memory"]["ms"]
    memory=data["conversation"]["memory"]
    
    ms = int(ms)
    # ms = 1554076800000
    # ms = 1115076800000
    date = datetime.datetime.fromtimestamp(ms/1000.0)
    day = date.strftime("%A")
    month = date.strftime("%B")
    year = date.strftime("%Y")
    memory['day']=day
    memory['month']=month
    memory['year']=year

    return jsonify({"conversation": {"memory": memory}})
#end of ms to date_of_joining

#ms to age
@app.route("/mstoage", methods=["POST"])
def mstoage():
    data = json.loads(request.get_data())
    ms = data["conversation"]["memory"]["ms"]
    memory=data["conversation"]["memory"]
    print(ms)
    l1=len(ms)
    ms=ms[6:l1-2]
    print(ms)
    ms = int(ms)
    # ms = 1115076800000
    start_date = datetime.datetime.fromtimestamp(ms/1000.0)
    from datetime import date
    end_date = date.today()
    from dateutil.relativedelta import relativedelta
    difference_in_years = relativedelta(end_date, start_date).years
    memory['age']=difference_in_years


    return jsonify({"conversation": {"memory": memory}})
#end of ms to age


@app.route("/wiki", methods=["POST"])
def wiki():
    data = json.loads(request.get_data())
    text = data["conversation"]["memory"]["text"]
    memory=data["conversation"]["memory"]
    import wikipedia
    text_final = wikipedia.suggest(text)
    found = True
    try:
        result = wikipedia.summary(text_final, sentences = 2)
    except :
        result = wikipedia.search(text_final, results = 3)
        found = False

    memory['Data']=result
    memory['Status']=found
    

    
    
    return jsonify({"conversation": {"memory": memory}})


#distance
@app.route("/distance", methods=["POST"])
def distance():
    data = json.loads(request.get_data())
    point1 = data["conversation"]["memory"]["point1"]
    point2 = data["conversation"]["memory"]["point2"]
    memory=data["conversation"]["memory"]
    
    from geopy.geocoders import Nominatim
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(point1)
    print(getLoc)
    points_of_1 = (getLoc.latitude , getLoc.longitude)
    getLoc = loc.geocode(point2)
    points_of_2 = (getLoc.latitude , getLoc.longitude)

    from geopy.distance import geodesic
    distance = geodesic(points_of_1, points_of_2).km
    distance=int(distance)
    memory['distance']=distance
    memory['point1']=point1
    memory['point2']=point2
    
    return jsonify({"conversation": {"memory": memory}})




# wiki if cai failed  input:sentence  output:noun
@app.route("/fetch_nouns" , methods=["POST"])
def fetch_nouns():
    data = json.loads(request.get_data())
    point1 = data["conversation"]["memory"]["point1"]
    import nltk
    lines = 'givr me information about mohammed'
    lines = 'give me information about Riyadh'
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(point1)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    print (nouns)
    return str(nouns)

def fetch_nouns_local(inputu):
    import nltk
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(inputu)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    print (nouns)
    s = ""
    for i in nouns:
        s=s +" " + i + " "
    print(s)
    return s



@app.route("/services" , methods=["POST"])
def services():
    data = json.loads(request.get_data())
    user_input = data["conversation"]["memory"]["services"]
    memory=data["conversation"]["memory"]
    #user_input = fetch_nouns_local(user_input)
    black_list = ['services', 'service' , 'details', 'information'  ]
    user_input_list = user_input.split()
    user_input_list_processed = [word for word in user_input_list if word not in black_list]
    user_input = ' '.join(user_input_list_processed)
    print("processed sentence is --> ",user_input)
    my_dict = {}
    services_data = {'Ikmah':['Ikmah is a platform for RCU staff included all Learning and development activities for-instance: In-house and Talent development programs' , 'https://my.rcu.gov.sa/EN/Departments/HumanCapital/Questionnaire/Pages/default.aspx','https://www.experiencealula.com/EAPortal/media/Sit…l%20Ikmah/jabal-ikmah_Landscape-Hero-1280x559.jpg'],
                      'Overtime':['Overtime is paid based on the Saudi Labor Law','https://my.rcu.gov.sa/EN/Departments/HumanCapital/Questionnaire/Pages/default.aspx','https://scontent.fcjb3-3.fna.fbcdn.net/v/t1.6435-9/s526x296/34035323_1033588660126838_7994721080474337280_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=e3f864&_nc_ohc=FNALgIzRvj0AX-gNUz7&_nc_ht=scontent.fcjb3-3.fna&oh=00_AT-ZBioIuQoJSin5ZwU_VEb8NISaTiG2eGRMHhQZhmEAhw&oe=62024424'],}

    op = []
    for service in services_data:
        if solve(service , user_input)>0:
            op = services_data[service]
            break
    memory['service']=service
    memory['op']=op
    return jsonify({"conversation": {"memory": memory}})


@app.route("/countemp" , methods=["POST"])
def countemp():
    data = json.loads(request.get_data())
    user_input = data["conversation"]["memory"]["emp_desc"]
    memory=data["conversation"]["memory"]
    user_input = str(user_input) 
    user_input = fetch_nouns_local(user_input)
    response = requests.get('https://api23preview.sapsf.com/odata/v2/User?$format=json',
            auth = HTTPBasicAuth('Cbot_t@theroyalcoT1', 'Test@123'))
    res1 = response.json()
    res1 = res1['d']['results']
    oplist = []
    for i in res1:
        temp =i['department']+" "+str(i['title'])+" "+i['location']+" "+str(i['city'])
        score = solve(str(user_input), temp)
        print(score)
        if score >0 :
            oplist.append(i['userId'])
    oplist = set(oplist)
    memory['pr_array']=len(oplist)



    

    return jsonify({"conversation": {"memory": memory}})



def toint(st):
    if int(st[0])==0:
        return int(st)
    if int(st[1])==0:
        return int(st)
def mod60(i):
    if i >= 60 :
        return '00'
    return str(i)





@app.route("/find_title_count" , methods=["POST"])
def find_title_count():
    data = json.loads(request.get_data())
    user_input = data["conversation"]["memory"]["title"]
    memory=data["conversation"]["memory"]

    user_input = fetch_nouns_local(user_input)
    response = requests.get('https://api23preview.sapsf.com/odata/v2/User?$format=json',
            auth = HTTPBasicAuth('Cbot_t@theroyalcoT1', 'Test@123'))
    res1 = response.json()
    res1 = res1['d']['results']
    oplist = []
    my_dict = {}
    for i in res1:
        key =str(i['title'])
        my_dict[key] = my_dict.get(key, 0) + 1

    sol = {}
    user_input =user_input.rsplit(' ', 1)[0]
    count = 0
    for i in my_dict:
        if solve(i , user_input)>0:
            sol[i] = my_dict[i]
            count+= my_dict[i]
    opt = []
    for i in sol:
        opt.append(""+str(sol[i])+" " + str(i))
    memory['title_count']=opt
    memory['user_input']=user_input
    memory['count']=count
    return jsonify({"conversation": {"memory": memory}})



@app.route("/list_of_employees", methods=["POST"])
def list_of_employees():
    data = json.loads(request.get_data())
    user_input = data["conversation"]["memory"]["title_with_count"]
    memory=data["conversation"]["memory"]
    user_input = user_input.partition(' ')[2]
    response = requests.get('https://api23preview.sapsf.com/odata/v2/User?$format=json',
            auth = HTTPBasicAuth('Cbot_t@theroyalcoT1', 'Test@123'))
    res1 = response.json()
    res1 = res1['d']['results']
    oplist = []
    my_dict = {}
    for i in res1:
        temp = ""
        if str(i['title']) == user_input:
        #title =str(i['title'])
            id = str(i['userId'])
            name = str(i['defaultFullName'])
            temp = id + "pending_approvals  " + name
            oplist.append(temp)
    memory['user_title']=user_input
    memory['oplist']=oplist
    return jsonify({"conversation": {"memory": memory}})

    

#start for userdata
@app.route("/possibleusernumbers", methods=["POST"])
def possibleusernumbers():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    user_input = data["conversation"]["memory"]["emp_desc"]
    memory=data["conversation"]["memory"]
    user_input = str(user_input)  # user input string....
   # print(user_input)

    response = requests.get('https://api23preview.sapsf.com/odata/v2/User?$format=json',
            auth = HTTPBasicAuth('Cbot_t@theroyalcoT1', 'Test@123'))
    res1 = response.json()
    res1 = res1['d']['results']
    oplist = []
    for i in res1:
        temp = i['userId']+" "+i['timeZone']+" "+i['department']+" "+i['defaultFullName']+" "+i['location']
        # if i['email'] != 'None':
        #     temp = temp+i['email']
        score = solve(str(user_input), temp)
        if score >0 :
            oplist.append(i['userId']+" "+i['defaultFullName'])


    # for i in data["value"]:
    #     s = i["description"] + " " + i["assignedDate"] + " " + i["approver"]
    #     score = solve(s, processed_user_input)
    #     if score > 0:
    #         output_list.append(i["approvableUniqueName"]+":"+i['description'])

    # print(output_list)
    print(oplist) 
    memory['pr_array']=oplist
    return jsonify({"conversation": {"memory": memory}})
    



#userstring to userid
@app.route("/str_to_userid", methods=["POST"])
def str_to_userid():
    data = json.loads(request.get_data())
    id_and_desc = data["conversation"]["memory"]["id_and_desc"]
    memory=data["conversation"]["memory"]
    id_and_desc=id_and_desc.split()[0]
    memory['empid']=id_and_desc

    

    return jsonify({"conversation": {"memory": memory}})
#end of userstring to userid





@app.route("/errors", methods=["POST"])
def errors():
    print(json.loads(request.get_data()))
    return jsonify(status=200)




# REQUEST_TOKEN = "Token ceec15c164a74196f7a3ea321b83d562"

#   data = json.loads(request.get_data())
#   question = data['nlp']['source']
#   lang = data['nlp']['language']

#   r = requests.post('https://api.cai.tools.sap/train/v2/request/ask',
#   json={'text': question},
#   headers={'Authorization': REQUEST_TOKEN}
# )
#   data = r.json()
#   d= data['results']['faq']
#   c= d[0]['answer']
#  BASE_URL = "https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables"


# headers = {
#       'Authorization': 'Bearer 85e13c6c-d8da-4a12-ac3b-bc27de440898',
#       'Content-Type' : 'application/json',
#       'apiKey' : 'PWllhcWwVSHNXCnLeTjhqPD7zM99995G'
#   }

# params = {
#     "realm": "RCU-1",
#     "$filter": "approvableType eq 'requisitions'"
# }
# r = requests.get(BASE_URL, headers=headers, params=params)

# r = requests.get("https://mn2.openapi.ariba.com/api/approval/v2/prod/pendingApprovables?$realm=RCU-1&$filter=approvableType eq 'requisitions'",)


#SuccessFactors





#username from accessToken

@app.route("/username", methods=["POST"])
def username():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    atoken = data["conversation"]["memory"]["wusool"]
    memory=data["conversation"]["memory"]
    print(atoken)
 
    a = 'Bearer '+ atoken

    response = requests.get("https://wusool.rcu.gov.sa/affwebservices/CASSO/oidc/MyRCU/userinfo",
    headers = {
        'Authorization': a,
        'Content-Type' : 'application/json',
      }
    )

    data = response.json()
    print(data["username"])
          
    # json_url = os.path.join("/", "/", "pa.json")
    # data = json.load(open(json_url))
    # data=pa.json
    # t=open(pa.json,r)
    # f = open("pa.json")
    # data = json.load(f)
    username=data['username']
    memory['username']=username

    # Date = str(Date)
    return jsonify(
        {
            "conversation": {
                "memory": memory
            }
        }
    )


#get userid from username

@app.route("/userid", methods=["POST"])
def userid():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1
    username = data["conversation"]["memory"]["username"]
    print(username)
    memory=data["conversation"]["memory"]
    

    response = requests.get("https://api23preview.sapsf.com/odata/v2/User?$format=json",
    auth=HTTPBasicAuth("Cbot_t@theroyalcoT1","Rcu@1234")
    )

    data = response.json()
    data=data["d"]["results"]
    for k in data:
        if((k["username"])==username):
            result_id=k["userId"]
          
    # json_url = os.path.join("/", "/", "pa.json")
    # data = json.load(open(json_url))
    # data=pa.json
    # t=open(pa.json,r)
    # f = open("pa.json")
    # data = json.load(f)
    memory["userid"]=result_id


    # Date = str(Date)
    return jsonify(
        {
            "conversation": {
                "memory": memory
            }
        }
    )


#BMC system
# incident creation(ITSM)


@app.route("/itsm_incident_creation", methods=["POST"])

def itsm_incident_creation():
    data = json.loads(request.get_data())
    # a1 = data['conversation']['memory']['API_Key']['access_token']
    # print (a1)
    # a = 'Bearer '+ a1

    incident_desc = data["conversation"]["memory"]["desc"]
    print(incident_desc)

    url = "https://itsmweblb.rcu.gov.sa/arsys/WSDL/public/itsmapplb/RCU_AH_Create_INC_Chatbot"
    client = Client(url)
    auth_ele = client.get_element('ns0:AuthenticationInfo')
    auth = auth_ele(userName='chatbot.integration', password='Rcu#123')
    print(auth)

    incident_no=client.service.Create_INC_Chatbot(Cat1="Incident", Cat2="Issue", Cat3="Chatbot",AssignedComany="", AssignedOrg="IT Support", AssignedGroup="IT HelpDesk", Reported_Source="Web", Summary="Chatbot", Impact="4-Minor/Localized", Urgency="4-Low", Service_Type="User Service Restoration", Status="", Description= "incident_desc",  Login_ID="a.bay" ,_soapheaders=[auth])

    print(incident_no)



    # Date = str(Date)

    return jsonify({"conversation": {"memory": {"incident_no": incident_no, "link": link, }}})


@app.route("/itsmticketbyuid", methods=["POST"])
def itsmticketbyuid():
    print("itsmticketdetails")
    data = json.loads(request.get_data())
    u_id = data["conversation"]["memory"]["u_id"]
    print(u_id)

    url = "https://itsmweblb.rcu.gov.sa/arsys/WSDL/public/itsmapplb/RCU_AH_Get_Open_REQ_Chatbot"
    Operation = Client('https://itsmweblb.rcu.gov.sa/arsys/WSDL/public/itsmapplb/RCU_AH_Get_Open_REQ_Chatbot')
    auth_element = Operation.get_element('ns0:AuthenticationInfo')
    auth = auth_element(userName='chatbot.integration', password='Rcu#123')

    itsm_by_uid = Operation.service.New_GetList_Operation_0(startRecord="",maxLimit="", User_ID="m.alsobhi" ,_soapheaders=[auth])
    

    # structured XML
#     payload = """<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope" xmlns:urn="urn:RCU_AH_Get_Open_REQ_Chatbot">
#    <soapenv:Header>
#       <urn:AuthenticationInfo>
#          <urn:userName>chatbot.integration</urn:userName>
#          <urn:password>Rcu#123</urn:password>
#          <!--Optional:-->
#          <urn:authentication>?</urn:authentication>
#          <!--Optional:-->
#          <urn:locale>?</urn:locale>
#          <!--Optional:-->
#          <urn:timeZone>?</urn:timeZone>
#       </urn:AuthenticationInfo>
#    </soapenv:Header>
#    <soapenv:Body>
#       <urn:New_GetList_Operation_0>
#          <urn:startRecord></urn:startRecord>
#          <urn:maxLimit>?</urn:maxLimit>
#          <urn:User_ID>{}</urn:User_ID>
#       </urn:New_GetList_Operation_0>
#    </soapenv:Body>
# </soapenv:Envelope>""".format(u_id)
#     # headers
#     headers = {
#         'Content-Type': 'application/soap+xml; charset=utf-8'
#     }
#     # POST request
#     response = requests.post(url, headers=headers, data=payload)
#     s = response.text
#     obj=xmltodict.parse(s)
#     result=json.dumps(obj)
#     result1=json.loads(result)
#     resArray=result1["soapenv:Envelope"]["soapenv:Body"]["ns0:New_GetList_Operation_0Response"]["ns0:getListValues"]

#     for k in resArray:
#         print(k["ns0:REQ_ID"]+"-"+k["ns0:Summary"]+"-"+k["ns0:Status"])
#     # print(s)
#     # start = "</ns0:getListValues>"
#     # end = "</ns0:getListValues>"
#     # incident_no = (s.split(start))
#     # op=[]
#     # for i in incident_no:
#     #     id = int(i[45:53])
#     #     desc = ""
#     #     op.append(id , desc)

    return jsonify({"conversation": {"memory": {"indident_id": "m.alsobhi","description":"desc", "link": link, }}})







@app.route("/itsmticketdetails", methods=["POST"])
def itsmticketdetails():
    print("itsmticketdetails")
    data = json.loads(request.get_data())
    u_id = data["conversation"]["memory"]["u_id"]
    #incident_num = data["conversation"]["memory"]["ticket_number"]["raw"]
    #print(incident_num)

    url = "https://itsmweblb.rcu.gov.sa/arsys/services/ARService?server=itsmapplb&webService=RCU_AH_Get_Open_REQ_Chatbot"
    # structured XML
    payload = """<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope" xmlns:urn="urn:RCU_AH_Get_Open_REQ_Chatbot">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>chatbot.integration</urn:userName>
         <urn:password>Rcu#123</urn:password>
         <!--Optional:-->
         <urn:authentication>?</urn:authentication>
         <!--Optional:-->
         <urn:locale>?</urn:locale>
         <!--Optional:-->
         <urn:timeZone>?</urn:timeZone>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:New_GetList_Operation_0>
         <urn:startRecord></urn:startRecord>
         <urn:maxLimit>?</urn:maxLimit>
         <urn:User_ID>m.alsobhi</urn:User_ID>
      </urn:New_GetList_Operation_0>
   </soapenv:Body>
</soapenv:Envelope>"""
    # headers
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8'
    }
    # POST request
    response = requests.post(url, headers=headers, data=payload)
    s = response.text
    obj=xmltodict.parse(s)
    result=json.dumps(obj)
    result1=json.loads(result)
    resArray=result1["soapenv:Envelope"]["soapenv:Body"]["ns0:New_GetList_Operation_0Response"]["ns0:getListValues"]

    for k in resArray:
        if(u_id==k["ns0:REQ_ID"]):
            print(k["ns0:REQ_ID"]+"-"+k["ns0:Summary"]+"-"+k["ns0:Status"])
            div1=k["ns0:Submit_Date"][0:10].partition("-")
            div2=div1[2].partition("-")
            print(type(date(int(div1[0]),int(div2[0]),int(div2[2]))))


    return jsonify({"conversation": {"memory": {"incident_desc": "not found", "link": link, }}})

@app.route("/itsmticketdetailsbydate", methods=["POST"])
def itsmticketdetailsbydate():
    print("itsmticketdetails")
    data = json.loads(request.get_data())
    s_d = data["conversation"]["memory"]["start_date"]
    e_d = data["conversation"]["memory"]["end_date"]
    #incident_num = data["conversation"]["memory"]["ticket_number"]["raw"]
    #print(incident_num)

    url = "https://itsmweblb.rcu.gov.sa/arsys/services/ARService?server=itsmapplb&webService=RCU_AH_Get_Open_REQ_Chatbot"
    # structured XML
    payload = """<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope" xmlns:urn="urn:RCU_AH_Get_Open_REQ_Chatbot">
   <soapenv:Header>
      <urn:AuthenticationInfo>
         <urn:userName>chatbot.integration</urn:userName>
         <urn:password>Rcu#123</urn:password>
         <!--Optional:-->
         <urn:authentication>?</urn:authentication>
         <!--Optional:-->
         <urn:locale>?</urn:locale>
         <!--Optional:-->
         <urn:timeZone>?</urn:timeZone>
      </urn:AuthenticationInfo>
   </soapenv:Header>
   <soapenv:Body>
      <urn:New_GetList_Operation_0>
         <urn:startRecord></urn:startRecord>
         <urn:maxLimit>?</urn:maxLimit>
         <urn:User_ID>m.alsobhi</urn:User_ID>
      </urn:New_GetList_Operation_0>
   </soapenv:Body>
</soapenv:Envelope>"""
    # headers
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8'
    }
    # POST request
    response = requests.post(url, headers=headers, data=payload)
    s = response.text
    obj=xmltodict.parse(s)
    result=json.dumps(obj)
    result1=json.loads(result)
    resArray=result1["soapenv:Envelope"]["soapenv:Body"]["ns0:New_GetList_Operation_0Response"]["ns0:getListValues"]
    div1=s_d.partition("-")
    div2=div1[2].partition("-")
    d1=date(int(div1[0]),int(div2[0]),int(div2[2]))
    print(d1)
    div1=e_d.partition("-")
    div2=div1[2].partition("-")
    d2=date(int(div1[0]),int(div2[0]),int(div2[2]))
    print(d2)


    for k in resArray:
            # print(k["ns0:REQ_ID"]+"-"+k["ns0:Summary"]+"-"+k["ns0:Status"])
            div1=k["ns0:Submit_Date"][0:10].partition("-")
            div2=div1[2].partition("-")
            d=date(int(div1[0]),int(div2[0]),int(div2[2]))
            # print(d)
            if d1<d<d2:
                print(d)


    return jsonify({"conversation": {"memory": {"incident_desc": "not found", "link": link, }}})


@app.route("/joke" , methods=["POST"])
def joke():
    data = json.loads(request.get_data())
    
    joke  = pyjokes.get_joke()
    memory=data["conversation"]["memory"]
    memory['joke']=joke

    return jsonify({"conversation": {"memory": memory}})


@app.route("/meetingtoday", methods=["POST"])
def meetingtoday():
    v = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkkwTXBha2ZwMEdzMXNtdFFsMVNhaXNSUU1va0ZoVkdpSjRFRkN4OGVSZDQiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84N2EyNWMyYS0yY2I0LTRjNDAtOWNiYy01MjY4YzBlZDFlZWIvIiwiaWF0IjoxNjcyNzMwMDg2LCJuYmYiOjE2NzI3MzAwODYsImV4cCI6MTY3MjczNDExMywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQXRYMjZITEFqUktjdTMySTR4ZGdZWEZRalVpU1JvMDRYb052L0QxWVFaZVBUNDRvRkxOMjdXVUlSUGU5T0FTaGFHV1czYzR3SytaWjg1K2taYjdwMndJeHF5RW9pbk5RNzluRFZKdkNncTVjPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiS3VtYXJhdmVsIiwiZ2l2ZW5fbmFtZSI6IkhhcmlzaCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ljk3LjIzMC4xNjIiLCJuYW1lIjoiSGFyaXNoIEt1bWFyYXZlbCIsIm9pZCI6ImFkM2RlNWExLTM2Y2YtNDI4ZC1hYzM5LTJjYzRhOGI1YWZjMSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xMTQ0NDkzNzI2LTQyMjMzMzAzODktNjIyMDI3MDM5LTMzNTc5IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAxQzc2NzBCMEIiLCJyaCI6IjAuQVZRQUtseWloN1FzUUV5Y3ZGSm93TzBlNndNQUFBQUFBQUFBd0FBQUFBQUFBQUJVQUljLiIsInNjcCI6IkFjY2Vzc1Jldmlldy5SZWFkLkFsbCBBY2Nlc3NSZXZpZXcuUmVhZFdyaXRlLkFsbCBBZ3JlZW1lbnQuUmVhZC5BbGwgQWdyZWVtZW50LlJlYWRXcml0ZS5BbGwgQWdyZWVtZW50QWNjZXB0YW5jZS5SZWFkIEFncmVlbWVudEFjY2VwdGFuY2UuUmVhZC5BbGwgQXBwQ2F0YWxvZy5SZWFkV3JpdGUuQWxsIEF1ZGl0TG9nLlJlYWQuQWxsIENhbGVuZGFycy5SZWFkLlNoYXJlZCBDYWxlbmRhcnMuUmVhZFdyaXRlIENhbGVuZGFycy5SZWFkV3JpdGUuU2hhcmVkIENvbnRhY3RzLlJlYWQgQ29udGFjdHMuUmVhZC5TaGFyZWQgQ29udGFjdHMuUmVhZFdyaXRlIENvbnRhY3RzLlJlYWRXcml0ZS5TaGFyZWQgRGV2aWNlLkNvbW1hbmQgRGV2aWNlLlJlYWQgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5Qcml2aWxlZ2VkT3BlcmF0aW9ucy5BbGwgRGV2aWNlTWFuYWdlbWVudE1hbmFnZWREZXZpY2VzLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWRXcml0ZS5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZFdyaXRlLkFsbCBEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QWRtaW5pc3RyYXRpb24uUmVhZCBFZHVBZG1pbmlzdHJhdGlvbi5SZWFkV3JpdGUgRWR1QXNzaWdubWVudHMuUmVhZCBFZHVBc3NpZ25tZW50cy5SZWFkQmFzaWMgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZUJhc2ljIEVkdVJvc3Rlci5SZWFkQmFzaWMgRmlsZXMuUmVhZCBGaWxlcy5SZWFkLkFsbCBGaWxlcy5SZWFkLlNlbGVjdGVkIEZpbGVzLlJlYWRXcml0ZSBGaWxlcy5SZWFkV3JpdGUuQWxsIEZpbGVzLlJlYWRXcml0ZS5BcHBGb2xkZXIgRmlsZXMuUmVhZFdyaXRlLlNlbGVjdGVkIEZpbmFuY2lhbHMuUmVhZFdyaXRlLkFsbCBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIElkZW50aXR5Umlza0V2ZW50LlJlYWQuQWxsIE1haWwuUmVhZFdyaXRlIE1haWxib3hTZXR0aW5ncy5SZWFkV3JpdGUgTm90ZXMuUmVhZFdyaXRlLkFsbCBvcGVuaWQgUGVvcGxlLlJlYWQgcHJvZmlsZSBSZXBvcnRzLlJlYWQuQWxsIFNpdGVzLlJlYWRXcml0ZS5BbGwgVGFza3MuUmVhZFdyaXRlIFVzZXIuUmVhZCBVc2VyLlJlYWQuQWxsIFVzZXIuUmVhZEJhc2ljLkFsbCBVc2VyLlJlYWRXcml0ZSBVc2VyLlJlYWRXcml0ZS5BbGwgVXNlckFjdGl2aXR5LlJlYWRXcml0ZS5DcmVhdGVkQnlBcHAgZW1haWwiLCJzdWIiOiIxMXMtX2RaNTRBWEhEVFcxVkdjWGRPUlFnc21MUWZ4MnNhY2JGWklHMVFVIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkFTIiwidGlkIjoiODdhMjVjMmEtMmNiNC00YzQwLTljYmMtNTI2OGMwZWQxZWViIiwidW5pcXVlX25hbWUiOiJraGFyaXNoQGthYXJ0ZWNoLmNvbSIsInVwbiI6ImtoYXJpc2hAa2FhcnRlY2guY29tIiwidXRpIjoiZkswOUttZTBCRWFyN2tXY3JsUVNBZyIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19zdCI6eyJzdWIiOiJrNFREVEw0WndMRTY2RHpjd0pjMEpza3ltdlg4bU11OFN4MUhza1pzaThjIn0sInhtc190Y2R0IjoxNDM0MTA3NjU5fQ.FZKleIhD3BmW4Ys3NIGoNh4xTjou9SQcsjFRsB_mDv4GsJh621qwc2shVGrg7_dkQx86XLGkKcROIUbA3K-kyWZX-lFjqxKsWi_AF-NTfPHukhmyFPXq_pax7oYnhO4avhyAga3IKGb5h-PNY6ZVc1brdBuD5c_CtZIkfnh1Ppc8QyWLCDQfpcN-6FA7ZUwkLg79FGw9Io3lzTFUafL_GPXo4h6l34t-yRiOvvYfd2RWUnFwisZQODN8OOz8rZdRawTseyKP05pjGqzWLeAQWZkESJtpBv_-oYktu5k99qmcT1ebmtKcmnByN2awQVV_xj8TGIfBuTTH3MqLCkrgiA'
    from datetime import date
    from datetime import datetime
    from datetime import timedelta
    today = date.today()
    yesterday = today - timedelta(days = 1)
    d1 = today.strftime("%Y-%m-%d")
    d2 = yesterday.strftime("%Y-%m-%d")
    now = datetime.now()
    data = json.loads(request.get_data())
    memory=data["conversation"]["memory"]

    current_time = now.strftime("%H:%M:%S")
    response = requests.get("https://graph.microsoft.com/v1.0/me/calendarview?startdatetime="+d2+"T"+current_time+".549Z&enddatetime="+d1+"T23:59:30.549Z",
    headers = {
        'Authorization': v,
      }
    )
    data = response.json()
    data = data['value']
    list=""
    no=0
    for i in data:
        sh = ( int(i['start']['dateTime'][11:-14]) + 5 )%12 + ((int(i['start']['dateTime'][14:-11] ) + 30 )//60)
        eh =( int(i['end']['dateTime'][11:-14] )  + 5 )%12 + ((int(i['end']['dateTime'][14:-11] ) + 30 )//60)
        sm = mod60(int(i['start']['dateTime'][14:-11] ) + 30 ) 
        em = mod60(int(i['end']['dateTime'][14:-11] ) + 30 )
        list=list+(i['subject'] + " starts on "+str(sh)+":"+sm+"pm" + " and ends at "+str(eh)+ ":"+em+"pm"+'\n'+'\n')
        no=no+1
    memory['pr_array']=list
    memory['no']=no
    


    return jsonify({"conversation": {"memory": memory}})



@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__":
    # app.run()
  app.run(host='0.0.0.0', port=5000)
    




