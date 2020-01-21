"""EmailScript

This script allows for the option of either emailing a zipped folder of images created by other scripts
to an email address, or for individual PDF images to be sent to individual email addresses.

This script requires that `sendgrid` be installed within the Python
environment you are running this script in.
Note that the sendgrid_api_key needs to be set in the CLI for sendgrid to work correctly - in this example, it was
set as SENDGRID_API_KEY, hence why SendGridAPIClient(os.environ.get('***')) is so.

This file can also be imported as a module and contains the following
functions:

    * email_zip_whole - returns the column headers of the file
    * email_singlePDF - the main function of the script
"""

import base64
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

def emailList():

	email_data = [
		"Lee.Nate@bcg.com",
		"natelee.sb@gmail.com",
	]

	return email_data



def email_zip_whole(zipdirectory ):
	# Make this readable from a CSV - easy
	# problems with BCG email - not automatically let through

	message = Mail(
		from_email="Lee.Nate@bcg.com",
		to_emails= emailList(),
		subject='SendGrid Python Test - BCG email only',
		html_content=' Nate - python script test - can see all recipients.  BCG email'
	)

	zip_filePath = zipdirectory + ".zip"

	with open(zip_filePath, 'rb') as file_:
		data = file_.read()
		file_.close()

	encoded = base64.b64encode(data).decode()
	attachment = Attachment()
	attachment.file_content = FileContent(encoded)
	attachment.file_type = FileType('application/zip')
	attachment.file_name = FileName('test_1.zip')
	attachment.disposition = Disposition('attachment')
	attachment.content_id = ContentId('Example Content')
	message.attachment = attachment

	try:
		sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e.message)


def email_singlePDF( email_address, PDF_filepath, PDF_Name, fromEmailAddress ):


	if email_address not in (None, ""):
		message = Mail(
			from_email = fromEmailAddress,
			to_emails = email_address,
			subject='Python Script - Tableau Dashboard Output - PDF',
			html_content=' Individual PDF Test'
		)

		with open(PDF_filepath, 'rb') as file_:
			data = file_.read()
			file_.close()

		encoded = base64.b64encode(data).decode()
		attachment = Attachment()
		attachment.file_content = FileContent(encoded)
		attachment.file_type = FileType('application/pdf')
		attachment.file_name = FileName(PDF_Name + '.pdf')
		attachment.disposition = Disposition('attachment')
		attachment.content_id = ContentId('PDF Document File')
		message.attachment = attachment

		try:
			sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
			response = sg.send(message)
			# print(response.status_code)
			# print(response.body)
			# print(response.headers)
		except Exception as e:
			print(e.message)




