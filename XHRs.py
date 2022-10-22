import asyncio,json,yarl
from aiohttp import ClientSession

loop = asyncio.get_event_loop()

async def xhrGetHandler(endpoint, headers):
    """# Callback handler for get XHR"""
    try:
        async with ClientSession() as session:
            async with session.get(yarl.URL(endpoint, encoded = True), headers = headers) as response:
                try:
                    response = json.loads(response)                    
                except:
                    response = json.loads(response.content.decode('utf-8'))
                finally:
                    return response
    
    except Exception as err:
        print('Unhandled exception for URL: ', endpoint, err)

async def xhrPutHandler(endpoint, payload, headers):
    """# Callback handler for put XHR"""
    try:
        async with ClientSession() as session:
            async with session.put(yarl.URL(endpoint, encoded = True), data = payload, headers = headers) as response:
                print('Status code: ', response.status)
                try:
                    response = json.loads(response)                    
                except:
                    response = json.loads(response.content.decode('utf-8'))
                finally:
                    return response
    
    except Exception as err:
        print('Unhandled exception for URL: ', endpoint, err)

async def xhrPostHandler(endpoint, payload, headers):
    """# Callback handler for post XHR"""
    try:
        async with ClientSession() as session:
            async with session.post(yarl.URL(endpoint,encoded = True), data = payload, headers = headers) as response:
                response = await response.read()
                try:
                    response = json.loads(response)                    
                except:
                    response = json.loads(response.content.decode('utf-8'))
                finally:
                    return response

    except Exception as err:
        print('Unhandled exception for URL: ', endpoint, err)


def get(endpoint, headers = None):
    """# GET XHR
    Takes either a single URL or a list of URLS;
    Can take headers dict as the 2nd param
    """

    if isinstance(endpoint,str):
        tasks = [asyncio.ensure_future(xhrGetHandler(endpoint, headers))]
        loop.run_until_complete(asyncio.wait(tasks))
        return tasks[0]._result

    if isinstance(endpoint,list):
        tasks = [asyncio.ensure_future(xhrGetHandler(url, headers)) for url in endpoint]
        loop.run_until_complete(asyncio.wait(tasks))
        responses = {}
        for i in range(len(endpoint)):
            responses[endpoint[i]] = tasks[i]._result
        return responses

def put(endpoint, payload, headers = None):
    """# PUT XHR
    Takes a single URL and the payload to put
    Can take headers dict as the 3rd param
    """
    tasks = [asyncio.ensure_future(xhrPutHandler(endpoint, payload, headers))]
    loop.run_until_complete(asyncio.wait(tasks))
    return tasks[0]._result

def post(endpoint, payload, headers = None):
    """# POST XHR
    Takes a single URL and the payload to post
    Can take headers dict as the 3rd param
    """

    tasks = [asyncio.ensure_future(xhrPostHandler(endpoint, payload, headers))]
    loop.run_until_complete(asyncio.wait(tasks))
    return tasks[0]._result
