This is the AMPL code, a PDF of the poster, and the PowerPoint slides from 
the Data to Policy project for Integer Programming done by 
Christina Ebben and Eric Culver. 
For more information visit the project's [page](http://math.ucdenver.edu/~sborgwardt/wiki/index.php/Coordinating_Response_to_Fatal_Accidents) 
on the [UCDenver Optimization Wiki](http://math.ucdenver.edu/~sborgwardt/wiki/index.php/Main_Page).

# Files Included
* fire_police.mod - AMPL model file for fire-police matching problem
* fire_police.dat - AMPL data file for fire-police matching problem
* fire_police.run - AMPL script which sets up and solves the problem, then displays result (type "commands fire_police.run;" in AMPL to run)
* test_fire_police.dat - test (made-up) data for testing validity of fire-police model
* convert.py - Python script to convert CSV data files to a form AMPL accepts
* Accidents_fatal.csv - raw data, fatal accidents in Denver during Jan 2018 - Mar 2019
* fire_stations_lat_and_lon.csv - raw data, location of fire stations serving Denver County
* police_stations_lat_and_lon.csv - raw data, location of police station in Denver County
* README.md - this file
