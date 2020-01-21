"""Tableau Connector

This is the main function for the Dashboard Emailer.  It prints to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) only, and can only export files as PNG, JPGs, and PDFs

This script requires that all libraries be installed as stated in the requirements.txt file.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""


import tableauserverclient as TSC
import tkinter as tk
from tkinter import filedialog
import time
import os

import EnterCredentials as entCred
import ReadCSV_CreateImage as dashboardViewer


def main():

	print("Select CSV File")

	CSV_filename = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select CSV file", filetypes = (("csv files","*.csv"),("all files","*.*")))

	print("Select End File Location")
	Save_location = tk.filedialog.askdirectory(initialdir = os.getcwd(), title = "Choose Directory")

	userName, password, serverInstance, siteName, workbook_Name, dashboard_Name, user_Email = entCred.enterCredentailsAutomatic()
	print (userName, siteName, workbook_Name, dashboard_Name )

	TableauAuthentication = TSC.TableauAuth(userName, password, site_id=siteName)

	TSC_server = TSC.Server(serverInstance, use_server_version=True)

	start_time = time.time()

	dashboardViewer.CSV_ImageRequest(TSC_server, TableauAuthentication, CSV_filename, Save_location, workbook_Name, dashboard_Name, user_Email )

	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()