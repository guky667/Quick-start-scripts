import requests, json, base64, os, urllib.parse
from getpass import getpass

JiraInstance = 'https://MyJiraInstance.domain.whatever'

def login():
    username = input('Username:')
    password = getpass('Password:')

    params = {
        'username': username,
        'password': password
    }

    basic_plaintext = '{username}:{password}'.format(**params)
    basic_bytes = str.encode(basic_plaintext)
    basic_b64 = base64.b64encode(basic_bytes).decode("utf-8") 

    return basic_b64

def request(basic_b64): 
    Jql = urllib.parse.quote(jql)
    maxRes = str(maxResults)
    Fields = '%2C'.join(fields)
    URL = JiraInstance +'/rest/api/2/search?jql=' + Jql + '&maxResults=' + maxRes + '&fields=' + Fields
    print(URL)
    headers={'Authorization': 'Basic ' + basic_b64}

    xhr = requests.get(URL, headers=headers)
    xhr = json.loads(xhr.text)  

    return xhr

def export(issues):
    jayson = json.dumps(issues)
    path = 'C:\\Users\\' + os.getlogin() + '\\Desktop\\issues.json'

    with open(path, 'w') as outfile:
        json.dump(jayson, outfile)

    if os.path.exists(path):
        print ('JSON sucesfully created')
    else:
        print ('something went wrong >_<')

# variables
jql = 'project = ABC AND issuetype = Bug'
fields = ['fixVersions']
maxResults = 50

def process(data):
    ###### custom logic; replace with what you need
    issues = {}

    for issue in data['issues']:
        for fv in issue['fields']['fixVersions']:
            try:
                issues[issue['key']] = fv['releaseDate']
            except:
                pass
    ######
    return issues

# runtime
raw = request(login())
data = process(raw)
export(data)
