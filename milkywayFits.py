import numpy as np 
from PIL import Image
from astropy.io import fits

pandaImage = Image.open('./MilkyWay.jpg')

xsize, ysize = pandaImage.size
r,g,b = pandaImage.split()

rdata = r.getdata()
gdata = g.getdata()
bdata = b.getdata()

npr = np.reshape(rdata, (ysize,xsize))
npg = np.reshape(gdata, (ysize,xsize))
npb = np.reshape(bdata, (ysize,xsize))

for data in [npr, npg, npb]:
	xx =  data.copy()
	for i in range(xx.shape[0]):
		for j in range(xx.shape[1]):
			data[i,j] = xx[-(j+1),i]

for data in [npr, npg, npb]:
	xx =  data.copy()
	for i in range(xx.shape[0]):
		for j in range(xx.shape[1]):
			data[i,j] = xx[-(j+1),i]


red   = fits.PrimaryHDU(npr)
green = fits.PrimaryHDU(npg)
blue  = fits.PrimaryHDU(npb)
imsize = 0.12
for hdu in [red,green,blue]:
	hdu.header['CTYPE1']  = 'GLON-CAR'                                      
	hdu.header['CRVAL1']  =      0                           
	hdu.header['CDELT1']  =      0.05010916215741394                   
	hdu.header['CRPIX1']  =      hdu.header['NAXIS1']/2+0.5                        
	hdu.header['CTYPE2']  = 'GLAT-CAR'                                      
	hdu.header['CRVAL2']  =      0                          
	hdu.header['CDELT2']  =      0.05010916215741394                    
	hdu.header['CRPIX2']  =      hdu.header['NAXIS2']/2+0.5

red.writeto('./mwRed.fits', clobber = True)
green.writeto('./mwGreen.fits', clobber = True)
blue.writeto('./mwBlue.fits', clobber = True)
