set FIRE; # fire stations
set POLICE; # police stations
set ACCIDENT; # potentially fatal accidents

param fx {FIRE}; # fire station locations x
param fy {FIRE}; # fire station locations y
param px {POLICE}; # police station locations x
param py {POLICE}; # police station locations y
param ax {ACCIDENT}; # potentially fatal accident locations x
param ay {ACCIDENT}; # potentially fatal accident locations y
param incompatibility {i in POLICE, j in FIRE} = 
	sum {k in ACCIDENT} <<0; -1, 1>>(<<0; -1, 1>>(px[i] - ax[k]) 
						+ <<0; -1, 1>>(py[i] - ay[k])
						- <<0; -1, 1>>(fx[j] - ax[k])
						- <<0; -1, 1>>(fy[j] - ay[k])) ; # how poorly i and j would work together

var match {i in POLICE, j in FIRE} binary; # whether i and j get matched

minimize Total_Incompatibility:
	sum {i in POLICE, j in FIRE} incompatibility[i,j] * match[i,j];

subject to Fire_Match{j in FIRE}:
	sum {i in POLICE} match[i,j] == 1;
	
subject to Police_Match{i in POLICE}:
	sum {j in FIRE} match[i,j] >= 1;