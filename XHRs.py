import aiohttp,asyncio,json,yarl
from aiohttp import ClientSession

loop = asyncio.get_event_loop()

async def xhrHandler(endpoint,headers=None):
    """# Callback handler for get XHR"""
    try:
        async with ClientSession() as session:
            async with session.get(yarl.URL(endpoint,encoded=True),headers=headers) as response:
                response = await response.read()
                print (response)
    
    except Exception as e:
        print('Unhandled exception for URL: ',e)


def get(endpoint):
    """# GET XHR
    Takes either a single URL or a list of URLS;
    Can take headers dict as the 2nd param
    """

    if isinstance(endpoint,str):
        tasks = [asyncio.ensure_future(xhrHandler(endpoint))]
        loop.run_until_complete(asyncio.wait(tasks))

    if isinstance(endpoint,list):
        tasks = [asyncio.ensure_future(xhrHandler(url))
        for url in endpoint]
        loop.run_until_complete(asyncio.wait(tasks))
