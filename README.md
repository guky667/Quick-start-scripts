# Quick-start-scripts
Quick-start scripts for new projects

# XHRs.py
Module that provides an easy way to do async XHR (Xml Http Request) - WITHOUT ENCODING  
If you wish to have your URL encoded just change [encoded=True] to False in the xhrHandler  
Takes either a single URL or a list of URLs, and an optional 2nd param for a dict of headers  
Returns the .json representation of the response  

To start, just add [from XHRs import get] to the beggining of your imports  
To call:  
get('some url')   
or  
get(['a','list','of','urls'])  
  
Only error handling it has is reporting when URLs failed to be hit  
  
