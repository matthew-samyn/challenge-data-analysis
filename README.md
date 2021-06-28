# challenge-data-analysis

# Cleaning the data

area: Removed NaN
price: Untouched
state_of_building:
	as_new = 4
	just_renovated = 3
	good = 2
	to renovate = 1
	to be done up = 1
	to restore = 1

facades = Untouched
bedrooms = Untouched, 1 big outlier
fully_equipped_kitchen:
	installed = installed
	usa installed = installed
	hyper equipped = hyper equipper
	usa hyper equipped = hyper equipped
	semi equipped = semi equipped
	usa semi equipped = semi equipped
	not installed = not installed
	usa installed = not installed

furnished:
	NaN = yes
	rest unchanged
open_fire: Untouched
open_fire_YN: From open_fire, only yes and no.
zip_code: Untouched
land_surface: Untouched
terrace:
	1 = yes
	2 = no
terrace_surface: Untouched
swimming_pool:
	NaN = no

type_property = Untouched
subtype_property = Untouched
garden:
	1 = yes
	2 = no
garden_surface: Untouched


	