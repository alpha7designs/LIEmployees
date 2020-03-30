Linkedin Employee Counter
=========================

There are 3 elements to this system:

1) SQL Exxress DB to store companies to track

	a) Install SQL Express
	b) Create a DB Called LinkedIn
	c) Execute the script SCHEMA.SQL found in the DB folder
	
2) Simple website for updating (1)

	a) Copy contents of the Site folder onto any IIS enabled device
	b) Modify YOUR SERVER NAME in the file includes\connect.asp to reflect the DB Server name
	
3) Python 3.6 code to scrape LinkedIn

	a) Install Python 3.6
	b) Install the following dependencies:
		
		selenium
		clicksend_client
		pyodbc
		
	c) Modify "server" in creds.py to reflect the DB Server name
	d) Modify top section of Employyes.py to set:
		
		Recipient phone number(s)
		Originating phone number
		ClickSend username
		ClickSend password
	
		