"""Folder Views

This script has two purposes - TableauFolderViews shows each of the files within the four common Tableau server
folders - data sources, projects, views, and workbooks.  The user has provider the name of the workbook and the view,
and the workbooks and views are filtered to match the name.  checkMatch first looks at the filtered views to see if
the user provided views and worksbooks exist, and if so, whether the views and workbooks' ID match each other, for cases
where there exist multiple views of the same name.

This file can also be imported as a module and contains the following
functions:

    * checkMatch - returns the column headers of the file
    * TableauFolderViews - the main function of the script
"""

import sys


def checkMatch(filter_DB, views_item, filter_WB, workbooks_item):

	if len(filter_DB) == 0:
		sys.exit(" No Dashboard View Matching that name")
	elif len(filter_WB) == 0:
		sys.exit(" No Workbook Matching that name ")

	# Case Multiple Dashboards Same Name - return the correct one belonging to the Workbook
	try:
		for view_i in range(views_item.total_available):
			for workbook_i in range(workbooks_item.total_available):
				if (filter_DB[view_i].workbook_id == filter_WB[workbook_i].id):
					return view_i, workbook_i

		return TypeError
	except TypeError:
		sys.exit(" No Dashboard ID and Workbook ID match")


def TableauFolderViews(Tableau_server):

	# The below four segments explore the four different folders in GeoApps - YMMV in the names / types of folders
	# in the site_id folder

	all_datasources, datasource_items = Tableau_server.datasources.get()
	print("\nThere are {} datasources on site: ".format(datasource_items.total_available))
	print([datasource.name for datasource in all_datasources])

	all_projects, projects_item = Tableau_server.projects.get()
	print("\nThere are {} projects on site: ".format(projects_item.total_available))
	print([projects.name for projects in all_projects])

	all_views, views_item = Tableau_server.views.get()
	print("\nThere are {} views on site: ".format(views_item.total_available))
	print([views.name for views in all_views])

	all_workbooks, workbooks_item = Tableau_server.workbooks.get()
	print("\nThere are {} workbooks on site: ".format(workbooks_item.total_available))
	print([workbooks.name for workbooks in all_workbooks])
