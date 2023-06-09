''' 
This script is a preliminary version of index calculation python file for my final project
Currently contains 3 functions each implementing one index. 
Three indices currently represented are Normalized Vegetaion Index (ndvi), Enhanced Vegetation Index (evi), Normalised Water Index (ndwi)

It does not yet read the actual band values from actual imagery. It is just meant to show that the indices work.
Therefore, you only need specify the values either directly or assigned to variables.

Call the individual index functions, inputing the required args. 

e.g ndvi(nir, red)
    evi(nir, red, blue)
    ndwi(nir, green)

where,
	red: red band of your dataset
	nir: near infrared band of your dataset
	blue: blue band of your dataset	
	green: green band of your dataset

Dont forget to encase this in a print statement to actually see your results.

import this module to run the functions in any python enviroment

'''

import numpy as np


# nir = 10
# red = 5
# blue = 2
# green = 4

##NDVI

def ndvi(nir, red):
    """args are nir (first position) and red(second position) values

	Formula
	ndvi = (nir-red)/(nir+red)
    """

    ndvi = np.where((nir+red)==0., 0, # if nir plus red gives a fraction (0.), tranfrom to 0 
                    (nir-red)/(nir+red) #else, run this 
                    )
    return ndvi


print(ndvi(nir, red))


##EVI

def evi(nir, red, blue, G = 2.5, L = 1, C1 = 6, C2 = 7.5 ):
    """args are nir (first position) and red(second position) and blue (third position) values. 
    
	Optional params and default values
	G = 2.5,
	L = 1,
	C1 = 6,
	C2 = 7.5,

    Formula
	G * ((nir - red)/(nir + C1 * red - C2 * blue + L))
    
    """

    evi = np.where((nir+red)==0., 0,
                   G * ((nir - red)/(nir + C1 * red - C2 * blue + L))
                   )
    return evi

print(evi(nir, red, blue))


##NDWI

def ndwi(nir, green):
    """args are nir (first position) and green(second position) values

	Formula
	(green - nir)/(green + nir)
    """

    ndwi = np.where((nir + green)==0., 0,
                    (green - nir)/(green + nir)
                    )
    return ndwi

print(ndwi(nir, green))