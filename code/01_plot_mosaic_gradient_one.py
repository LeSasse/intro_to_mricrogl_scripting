import gl
import sys

import os

print(sys.version)
print(gl.version())

# set defaults and load a template
gl.resetdefaults()
gl.loadimage("mni152")

# set up background colors and colorbar
gl.backcolor(255, 255, 255)
gl.colorbarposition(2)
gl.colorbarcolor(255, 255, 255, 0)
gl.colorbarsize(0.03)

# view and cross-hairs
gl.linewidth(1)

# plot window size and position (left, top, width, height)
gl.windowposition(2000, 200, 3010, 1000)

# path to the gradient directory
gradient_file_dir = (
    "../data/gradients/AOMIC_PIOP1_AVG_CONNECTOME_"
    "Schaefer400Tian32_gradients/approach-dm/kernel-normalized_angle"
)

# filename of the first component
gradient = "spars-0.9_appr-dm_kernel-normalized_angle_comp-1_gradient.nii.gz"
nii = os.path.join(gradient_file_dir, gradient)

# Load the gradient as an overlay
gl.overlayload(nii)

# the opacity function changes the opacity of the image loaded which in our
# case is the mni152 template loaded in the beginning. It does not change the
# opacity of the overlay. The first input (0) gives determines the layer for which
# to set the opacity, 0 being the template, 1 being the first overlay and so on.
# I like to make the template slightly translucent, so that you can still see the template
# but the overlay has somewhat more intense colors
gl.opacity(0, 40)

# load one of the colormaps included in MRIcroGL (you can also add more colormaps)
# if you want, although I won't cover it here yet.
gl.colorname(1, "blue2red")

# This function creates a mosaic plot. It takes a "mosaic string" and parses it
# to create the image. Essentially rows are separated by ";". There are different
# letters to denote different views {'A' (Axial), 'C' (Coronal), 'S' (Sagittal),
# 'R' (Render)} and numbers to denote coordinates, directions, and coordinates.
# This may seem confusing, but MRIcroGL makes it very easy to create your own 
# "mosaic strings" interactively.
gl.mosaic("A R 0 C R 0 S R 0; A R -0 C R -0 S R -0")

# Save a png of the plot you have created
gl.savebmp(f"../images/gradient_one.png")

# And Done

