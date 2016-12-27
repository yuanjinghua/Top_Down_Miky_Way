#!/usr/bin python
#

from astropy.io import votable as vo
from astropy.io import ascii
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib as mpl
import aplpy as ap
import numpy as np
import scipy as sp
import time
import os
from astropy import units as u
import astropy.coordinates as coords
from astropy.table import Table, Column, vstack, join

mpl.rc("font", family="Complex", size=16)
mpl.rc("axes", linewidth = 1.0)
mpl.rc("lines", linewidth = 1.0)
mpl.rc("xtick.major", pad = 8, width = 1)
mpl.rc("ytick.major", pad = 8, width = 1)
mpl.rc("xtick.minor", width = 1)
mpl.rc("ytick.minor", width = 1)

hmscFullFile = '../../Tables/hmscList_full_20161218.txt'
hmscFull = ascii.read(hmscFullFile)
hmscFull = hmscFull[hmscFull['Dist_B'].mask == False]

coord = coords.SkyCoord(hmscFull['ra'].data, hmscFull['dec'].data, 
	frame = 'fk5', unit = (u.deg, u.deg))

lDet = Column(coord.galactic.l.rad, name = 'lDet')
bDet = Column(coord.galactic.b.rad, name = 'bDet')

xDet = hmscFull['Dist_B']*np.cos(bDet)*np.sin(lDet)
yDet = 8.34 - hmscFull['Dist_B']*np.cos(bDet)*np.cos(lDet)

#ap.make_rgb_cube(['./mwRed.fits',
#	'./mwGreen.fits',
#	'./mwBlue.fits'],
#	'./mwRGB.fits', system = 'GAL')
#
#ap.make_rgb_image('./mwRGB.fits',
#	'./mwRGB.png',embed_avm_tags = False)

fig = plt.figure(figsize = (8,8))

fb1 = ap.FITSFigure('./mwRed.fits',
	figure = fig, subplot = [0.2, 0.1, 0.7, 0.7], 
	aspect="auto")
fb1.ticks.set_length(10)
fb1.show_rgb('./mwRGB.png')
fb1.recenter(0, 0, radius = 18)
fb1.tick_labels.set_xformat("dd.dd")
fb1.tick_labels.set_yformat("dd.dd")
fb1.ticks.set_xspacing(5)
fb1.ticks.set_yspacing(5)
fb1.axis_labels.hide() 
fb1.tick_labels.hide() 
ax = fig.add_axes([0.2, 0.1, 0.7, 0.7])
ax.set_xlim(-18,18)
ax.set_ylim(-18,18)
ax.set_axis_bgcolor('None')
ax.tick_params(width = 0)
ax.set_xlabel('X (kpc)')
ax.set_ylabel('Y (kpc)')

ax.text(3.10382,13.6415,'1', color='yellow', 
	verticalalignment='center', horizontalalignment='center')

ax.text(-10, 10.1853,'2', color = 'yellow',
	verticalalignment='center', horizontalalignment='center')

ax.text(-2, 9,'3', color = 'yellow',
	verticalalignment='center', horizontalalignment='center')

ax.text(-12.5, -6,'4', color = 'yellow',
	verticalalignment='center', horizontalalignment='center')

ax.text(-9.5, -2,'5', color = 'yellow',
	verticalalignment='center', horizontalalignment='center')

ax.text(-1.5, -7.2,'6', color = 'yellow',
	verticalalignment='center', horizontalalignment='center')

ax.plot([-20,20], [8.34,8.34], '--y', zorder = 1)
ax.plot([0,0], [-20,20], '--y', zorder = 1)

odCoords = [49, 31, 23, 15, 11, -8, -23., -27., -33., -55.]
odMarkx  = [14.487, 14.939, 11.244, 7.625, 3.251, -2., -8.436, -13, -14.9, -14.9]
odMarky  = [-6.281, -13.52, -15.3, -15.3, -15.3, -15.3, -15.3, -15.3, -12.087, -3.944]
odMark   = [r'$49{\degree}$', '31${\degree}$', '23${\degree}$', '15${\degree}$', '11${\degree}$', 
			'352${\degree}$', '337${\degree}$', '333${\degree}$', '327${\degree}$', '305${\degree}$']
line_list = []
for iod in range(10):
	ix = 28.5*np.tan(np.deg2rad(odCoords[iod]))
	ax.plot([0,ix],[8.34,-20],'-', color='white')
	ax.text(odMarkx[iod], odMarky[iod], odMark[iod], color = 'white',
		verticalalignment='center', horizontalalignment='center')

ax.scatter(xDet, yDet, s = 85, marker = '+', edgecolor = 'None', 
	linewidth = 1, facecolor = 'red', zorder = 100)
ax.scatter(0,8.34, s = 85, marker = 'o', c = 'cyan',
	edgecolors = 'cyan', zorder = 100)

plt.savefig('../../epsFigs/MW_face_on.eps', bbox_inches='tight',
		papertype='a2')
plt.savefig('../../epsFigs/MW_face_on.pdf', bbox_inches='tight',
		papertype='a2')
