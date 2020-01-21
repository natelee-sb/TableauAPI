# This is testing that python urllib works: swap out the different test URL in requests.get

# import urllib.request
#
# URL = "http://tableau.bcg.com/views/SalesPotential/SalesPotential?Color By=1&Bubble Color=1&:embed=y&:toolbar=no&:format=png"
# urlhk = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Hong_Kong_at_night.jpg/2400px-Hong_Kong_at_night.jpg"
# URL_tab = "http://tableau.bcg.com/views/SalesPotential/SalesPotential.png"
#
#
# urllib.request.urlretrieve(urlhk, "wikiTest_1.jpg")


##############################################################################

# This is testing that python requests works: swap out the different test URL in requests.get

urlhk = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Hong_Kong_at_night.jpg/2400px-Hong_Kong_at_night.jpg"

URL_tab = "http://tableau.bcg.com/views/SalesPotential/SalesPotential.png"
URL_Tableau2 = "http://tableau.bcg.com/views/SalesPotential/SalesPotential.png?Color%20By=2&Bubble%20Color=1&:embed=y&:toolbar=no&"
URL_Tableau_Public = "https://public.tableau.com/en-us/s/gallery/fortune-magazines-stock-picks-2019.png?gallery=votd"

import requests


def load_requests(source_url, sink_path):
	"""
	Load a file from an URL (e.g. http).

	Parameters
	----------
	source_url : str
		Where to load the file from.
	sink_path : str
		Where the loaded file is stored.
	"""

	r = requests.get(source_url, stream=True)

	if r.status_code == 200:
		with open(sink_path, 'wb') as f:
			for chunk in r:
				f.write(chunk)
	else:
		print(r.status_code)


load_requests(URL_Tableau_Public, "test1.png")


##############################################################################

# This is testing that a webrowser can open the link

# import webbrowser
#
# # a_website = "https://www.google.com"
# a_website = "http://tableau.bcg.com/views/SalesPotential/SalesPotential?Color By=1&Bubble Color=1&:embed=y&:toolbar=no&:format=png"
#
# # Open url in a new window of the default browser, if possible
# webbrowser.open_new(a_website)
#
# # Open url in a new page (“tab”) of the default browser, if possible
# # webbrowser.open_new_tab(a_website)

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
#
# import time
#
#
# urlhk = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Hong_Kong_at_night.jpg/2400px-Hong_Kong_at_night.jpg"
# URL_tab = "https://tableau.bcg.com/views/SalesPotential/SalesPotential.png"
#
# URL_Tableau = "https://tableau.bcg.com/views/SalesPotential/SalesPotential?Color%20By=1&Bubble%20Color=1&:embed=y&:toolbar=no&:format=.png"
# URL_Tableau2 = "https://tableau.bcg.com/views/SalesPotential/SalesPotential.png?Color%20By=2&Bubble%20Color=1&:embed=y&:toolbar=no&"
#
# # driver = webdriver.Chrome(ChromeDriverManager().install())
#
# # options = we
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument("--test-type")
# # options.binary_location = "/usr/bin/chromium"
#
# # driver = webdriver.Chrome(chrome_options=options)
#
# driver = webdriver.Chrome("C://Users//lee nate//Downloads//chromedriver_win32//chromedriver.exe")
#
# driver.get(urlhk)
# # time.sleep(2)
# driver.save_screenshot("screenshot1.png")
#
# driver.close()



# import os
# import shutil
# import tkinter as tk
# from tkinter.filedialog import askopenfilename
#
# print("Select zip file location")
# zip_directory = tk.filedialog.askdirectory()
# zip_directory = zip_directory + "/Tableau_ZipOutput"
#
# shutil.make_archive(zip_directory, 'zip', "C://Users//lee nate//Documents//TableauTest")


# import csv
# import tableauserverclient as TSC
#
# def csv_header(csv_reader, ):
#
# 	line_count = 0
#
# 	for row in csv_reader:
# 		if line_count == 0:
# 			num_col = len(row)
# 			column_header = row
# 			print("\n {}".format(column_header))
# 			line_count += 1



# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
# message = Mail(
#     from_email="natelee.sb@gmail.com",
#     to_emails='lee.nate@bcg.com',
#     subject='BCG Email Test!',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)
