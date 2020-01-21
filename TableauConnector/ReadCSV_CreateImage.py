"""ReadCSV_CreateImage

This script takes in the fields that the user has specified in the main function (TableauConnector.py).  It signs
in to a Tableau Server Online using the user entered credentials.  It goes through the CSV file the User has entered,
where column[0] is the name of the file to be saved, column[1] is the image type, and column[2] is the email where we
send the images to.  Columns[3] to  Column[N] are the different parameters within the Tableau Dashboard that this function
calls to get the different filtered views.  It then emails the different views based on the email addresses provided.

This script requires that `tableauserverclient` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:
    * CSV_ImageRequest - the main function of the script
"""

import tableauserverclient as TSC
import csv

import FolderViews as folderExplore
import EmailScript as emailScript

def CSV_ImageRequest(server, tableau_auth, csv_filename, end_file_directory, WorkbookName, DashboardName, UserEmail ):

	with server.auth.sign_in(tableau_auth):

		folderExplore.TableauFolderViews(server)


		req_option1 = TSC.RequestOptions()
		req_option1.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
		                                 TSC.RequestOptions.Operator.Equals,
		                                 DashboardName))

		req_option2 = TSC.RequestOptions()
		req_option2.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
		                                 TSC.RequestOptions.Operator.Equals,
		                                 WorkbookName))

		all_views_filtered, views_items1 = server.views.get(req_option1)
		all_workbooks_filtered, workbooks_items1 = server.workbooks.get(req_option2)

		view_i, workbook_i = folderExplore.checkMatch(all_views_filtered, views_items1, all_workbooks_filtered, workbooks_items1)

		with open(csv_filename) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0

			for row in csv_reader:
				if line_count == 0:
					num_col = len(row)
					column_header = row
					print ("\n {}".format(column_header))
					line_count += 1
				else:
					if (row[1] == "PNG" or row[1] == "JPG"):

						# view item is the dashboard view.
						view_item = all_views_filtered[view_i]

						image_req_option = TSC.ImageRequestOptions(imageresolution=TSC.ImageRequestOptions.Resolution.High)

						# Assumes col 0,1,2 are imageName, FileType, and Email respectively

						for iter_ in range(3, num_col):
							# column_header[iter_] takes the nth item across in column header,
							# row header [iter_] takes the same nth item acrpss in the row
							# pases it to like this:
							# image_req_option.vf( Color By , 2)
							# image_req_option.vf( Bubble Color, 1)
							# image_req_option.vf( Sales Channel, Channel1)
							if (row[iter_] == "All"):
								image_req_option.view_filters.clear()
								break
							else:
								image_req_option.vf(column_header[iter_], row[iter_])


						server.views.populate_image(view_item, image_req_option)
						image_filepath = view_item.name

						with open(end_file_directory + "/" + image_filepath + row[0] + "." + row[1], "wb") as image_file:
							image_file.write(view_item.image)

					elif (row[1] == "PDF"):

						view_item = all_views_filtered[view_i]

						pdf_req_option = TSC.PDFRequestOptions(page_type=TSC.PDFRequestOptions.PageType.A4,
						                                       orientation=TSC.PDFRequestOptions.Orientation.Portrait)

						# Assumes col 0,1,2 are imageName, FileType, and Email respectively
						for iter_ in range(3, num_col):
							if (row[iter_] == "All"):
								pdf_req_option.view_filters.clear()
								break
							else:
								pdf_req_option.vf(column_header[iter_], row[iter_])

						server.views.populate_pdf(view_item, pdf_req_option)
						pdf_name = view_item.name

						with open(end_file_directory + "/" + pdf_name + row[0] + "." + row[1], "wb") as pdf_file:
							pdf_file.write(view_item.pdf)

							# full_path = end_file_directory + "/" + pdf_name + row[0] + "." + row[1]
							# emailScript.email_singlePDF(row[2], full_path, row[0], UserEmail)

					print(row)
					line_count += 1

			print(f'Processed {line_count} lines.')

	server.auth.sign_out()