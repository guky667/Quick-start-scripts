import asyncio,json,yarl
from aiohttp import ClientSession

loop = asyncio.get_event_loop()

async def xhrGetHandler(endpoint, headers):
    """# Callback handler for get XHR"""
    try:
        async with ClientSession() as session:
            async with session.get(yarl.URL(endpoint, encoded = True), headers = headers) as response:
                print(response.status)
                response = await response.read()
                response = json.loads(response)
                print (response)
    
    except Exception as err:
        print('Unhandled exception for URL: ',err)

async def xhrPutHandler(endpoint, payload, headers):
    """# Callback handler for put XHR"""
    try:
        async with ClientSession() as session:
            async with session.put(yarl.URL(endpoint, encoded = True), data = payload, headers = headers) as response:
                print(response.status)
                response = await response.read()
                response = json.loads(response)
                print (response)
    
    except Exception as err:
        print('Unhandled exception for URL: ',err)

async def xhrPostHandler(endpoint, payload, headers):
    """# Callback handler for post XHR"""
    try:
        async with ClientSession() as session:
            async with session.post(yarl.URL(endpoint,encoded = True), data = payload, headers = headers) as response:
                print(response.status)
                response = await response.read()
                response = json.loads(response)
                print (response)
    
    except Exception as err:
        print('Unhandled exception for URL: ',err)


def get(endpoint, headers = None):
    """# GET XHR
    Takes either a single URL or a list of URLS;
    Can take headers dict as the 2nd param
    """

    if isinstance(endpoint,str):
        tasks = [asyncio.ensure_future(xhrGetHandler(endpoint, headers))]
        loop.run_until_complete(asyncio.wait(tasks))

    if isinstance(endpoint,list):
        tasks = [asyncio.ensure_future(xhrGetHandler(url, headers)) for url in endpoint]
        loop.run_until_complete(asyncio.wait(tasks))

def put(endpoint, payload, headers = None):
    """# PUT XHR
    Takes a single URL and the payload to put
    Can take headers dict as the 3rd param
    """
    tasks = [asyncio.ensure_future(xhrPutHandler(endpoint, payload, headers))]
    loop.run_until_complete(asyncio.wait(tasks))

def post(endpoint, payload, headers):
    """# POST XHR
    Takes a single URL and the payload to post
    Can take headers dict as the 3rd param
    """

    tasks = [asyncio.ensure_future(xhrPostHandler(endpoint, payload, headers))]
    loop.run_until_complete(asyncio.wait(tasks))
