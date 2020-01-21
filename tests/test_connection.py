# import tableauserverclient as TSC
#
# # Basic Test to check that you can access the tableau.bcg.com server
# username = "Lee Nate"
# password = "******"
# site_id_test = "GeoApps"
# server_BCG = "https://tableau.bcg.com"
#
# tableau_auth = TSC.TableauAuth(username, password, site_id=site_id_test)
#
# # create an instance for your server
# server = TSC.Server(server_BCG, use_server_version=True)
#
# # call the sign-in method with the auth object
# server.auth.sign_in(tableau_auth)
# server.auth.sign_out()


import tableauserverclient as TSC

# create an auth object

username = "LastName FirstName" # Fill this in
password = "LoginPassword" # Fill this in

site_id_test = "GeoApps" # Leave for this demo

server_BCG = "https://tableau.bcg.com"

tableau_auth = TSC.TableauAuth(username, password, site_id=site_id_test)

# create an instance for your server

server = TSC.Server(server_BCG, use_server_version=True)

# # call the sign-in method with the auth object
# server.auth.sign_in(tableau_auth)
#
# server.auth.sign_out()

with server.auth.sign_in(tableau_auth):

	# The below four segments explore the four different folders in GeoApps - YMMV in the names / types of folders
	# in the site_id folder

	all_datasources, datasource_items = server.datasources.get()
	print("\nThere are {} datasources on site: ".format(datasource_items.total_available))
	print([datasource.name for datasource in all_datasources])

	all_projects, projects_item = server.projects.get()
	print("\nThere are {} projects on site: ".format(projects_item.total_available))
	print([projects.name for projects in all_projects])

	all_views, views_item = server.views.get()
	print("\nThere are {} views on site: ".format(views_item.total_available))
	print([views.name for views in all_views])

	all_workbooks, workbooks_item = server.workbooks.get()
	print("\nThere are {} workbooks on site: ".format(workbooks_item.total_available))
	print([workbooks.name for workbooks in all_workbooks])


	# https://tableau.bcg.com/#/site/GeoApps/views/Sales/SalesPotential
	# Want to access Sales Potential - Have to look at naming convention inside Sales folder
	# To change dashboard type to access, change "Sales Potential" to whatever name

	req_option = TSC.RequestOptions()
	req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name, TSC.RequestOptions.Operator.Equals,'Sales Potential'))

	# Also note the server.views - this references a specific folder that I knew the dashboard was in (see printout for
	# more clarification)
	all_views, pagination_item = server.views.get(req_option)

	# This is unecessary, but sometimes useful
	print(all_views)
	print(pagination_item)

	view_item = all_views[0]
	print(view_item)

	image_req_option = TSC.ImageRequestOptions(imageresolution=TSC.ImageRequestOptions.Resolution.High)

	print('Populating image')
	server.views.populate_image(view_item, image_req_option)

	print('Got image')

	image_filepath = 'TableauDashboardImage.png'

	with open(image_filepath, "wb") as image_file:
		image_file.write(view_item.image)

server.auth.sign_out()