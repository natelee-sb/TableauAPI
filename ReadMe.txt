DashboardEmailer/
│
├── TableauConnector/
│   ├── TableauConnector.py (main file)
│   ├── FolderViews.py
│   ├── EnterCredentials.py
│   ├── EmailScript.py
│   └── Scheduler.py
├── tests/
│   ├── test_connection.py
│   └── helper_test.py
│
├── ReadMe.txt
└── requirements.txt

README:
Dashboard Emailer is a script that queries a Tableau Dashboard using the tableauserverclient API for Python.  It takes individual images (user defined either as a JPG / PNG or PDF) of different filters / views of the dashboard.  It then emails those images either zipped up to a single email or as individual files to individual emails.  

Individual explanations for the functions can be found in each file.  

Note: the sendgrid python library package requires you to create a SENDGRID_API_KEY thru their website, and to set that variable locally in the CLI ( set SENDGRID_API_KEY = "...") after installation.

CONTACT:

Example Run:
	In ..../DashboardEmailer_FileLocation> python TableauConnector.py
	Or to run the script as designated times:
		In ..../DashboardEmailer_FileLocation> python Scheduler.py

Python Library Installation - 
If pip install -r requirements.txt doesn't install all the libraries - install the following manually in IDE:

tableauserverclient
schedule
sendgrid*

Updated urllib3
Note: the sendgrid python library package requires you to create a SENDGRID_API_KEY thru their website, and to set that variable locally in the CLI ( set SENDGRID_API_KEY = "...") after installation.