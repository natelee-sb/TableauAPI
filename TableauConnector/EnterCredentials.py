"""Enter Credentials

This script allows the user to either enter credentials automatically or via command line prompt
Note that the input requires a space between the first and last name, which reflects
BCG Tableau username specifications.

This script requires that `getpass` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * enterCredentials - user-entered credentials
    * enterCredentailsAutomatic - pre-filled credentials for faster testing
"""


from getpass import getpass

def enterCredentials():

	while True:

		username = input("Enter Username (Last First): ")

		if (' ' in username):
			print ("Example URL: https://tableau.bcg.com/#/site/GeoApps/views/Sales/SalesPotential")
			passwd = getpass("Enter Password (BCG Login_Password) : ")
			serverInstance = input("Enter Server Instance Name (i.e. https://tableau.BCG.com): ")
			siteName = input ("Enter Site Name (GeoApps) :  ")
			workbookName = input("Enter Workbook Name (Sales): ")
			dashboardName = input("Enter Dashboard Name (Sales Potential - check if DashboardName has space!) : ")
			userEmail = input("Enter your email, will be the sent from  address:  ")

			break
		else:
			continue

	return username, passwd, serverInstance, siteName, workbookName, dashboardName, userEmail


def enterCredentailsAutomatic():

	username = "Lee Nate"
	passwd = "helloworld1!"
	serverInstance = "https://tableau.BCG.com"
	siteName = "GeoApps"
	workbookName = "Sales"
	dashboardName = "Sales Potential"
	userEmail = "Lee.Nate@bcg.com"

	return username, passwd, serverInstance, siteName, workbookName, dashboardName, userEmail