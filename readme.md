# Python program to check for valid places in Google Places

This program reads an input text file containing multiple lines of text to be queried for valid places entries within Google Maps/Places. 

It will generate an output file containing results for each text query from the input file to the matching Google Places API for finding places by text. For more details on the Google Places API, refer to their documentation [here](https://developers.google.com/places/web-service/search).

# Requirements

 - Google developer account
	 - For your key to access the API
	 - For any payment to access the API ([free $200 credit per month!](https://cloud.google.com/maps-platform/pricing/))
 - Python

## Python libraries used

 - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - json
 - requests
 - urllib.request
 - time
 - re
 - datetime

# Files In This Package

## Sample Files
An input.txt file includes examples of text to be queried against the Google Places API. 
An output file (results_fp.txt) contains the results from Google Places API. 

## The Main Program File
gp_fp.py - The python file containing the program.

# Any Other Notes

Feel free to pull and modify the program to suit your needs. 
