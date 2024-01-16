#-*- coding: utf-8 -*-

{
	"name": "Geolocation System",
	"version": "1.0",
	"depends": [
		"base"
	],
	"author": "Dino Herlambang",
	"category": "Utility",
	"website": "https://www.instagram.com/_dinoherlambang_/",
	"images": [
		"static/description/images/main_screenshot.jpg"
	],
	"price": "100",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "Simple Odoo Geolocation module",
	"description": "Get employee simple geolocation",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/HrEmployee.xml",
		"view/ConfigSettings.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True
}