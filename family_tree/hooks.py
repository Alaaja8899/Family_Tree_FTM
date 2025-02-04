app_name = "family_tree"
app_title = "Family Tree FTM"
app_publisher = "Abdirizak abdullahi (alaaja)"
app_description = "Family Tree – A Frappe app for managing and visualizing family relationships, helping users build, track, and explore their genealogy with ease. 🌳"
app_email = "cuzeyr6793@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "family_tree",
# 		"logo": "/assets/family_tree/logo.png",
# 		"title": "Family Tree FTM",
# 		"route": "/family_tree",
# 		"has_permission": "family_tree.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/family_tree/css/family_tree.css"
# app_include_js = "/assets/family_tree/js/family_tree.js"

# include js, css files in header of web template
# web_include_css = "/assets/family_tree/css/family_tree.css"
# web_include_js = "/assets/family_tree/js/family_tree.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "family_tree/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "family_tree/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "family_tree.utils.jinja_methods",
# 	"filters": "family_tree.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "family_tree.install.before_install"
# after_install = "family_tree.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "family_tree.uninstall.before_uninstall"
# after_uninstall = "family_tree.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "family_tree.utils.before_app_install"
# after_app_install = "family_tree.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "family_tree.utils.before_app_uninstall"
# after_app_uninstall = "family_tree.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "family_tree.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"family_tree.tasks.all"
# 	],
# 	"daily": [
# 		"family_tree.tasks.daily"
# 	],
# 	"hourly": [
# 		"family_tree.tasks.hourly"
# 	],
# 	"weekly": [
# 		"family_tree.tasks.weekly"
# 	],
# 	"monthly": [
# 		"family_tree.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "family_tree.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "family_tree.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "family_tree.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["family_tree.utils.before_request"]
# after_request = ["family_tree.utils.after_request"]

# Job Events
# ----------
# before_job = ["family_tree.utils.before_job"]
# after_job = ["family_tree.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"family_tree.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

