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
gl.opacity(0, 40)
# path to the gradient directory

gradient_file_dir = (
    "../data/gradients/AOMIC_PIOP1_AVG_CONNECTOME_"
    "Schaefer400Tian32_gradients/approach-dm/kernel-normalized_angle"
)

# list all gradient files, so then the image for each gradient is just one
# for loop away:
gradients = os.listdir(gradient_file_dir)

for gradient in gradients:
    # get the filename without the extension to save the png with a related,
    # but unique name:
    gradient_name = gradient.split(".nii")[0]
    nii = os.path.join(gradient_file_dir, gradient)

    gl.overlayload(nii)
    gl.colorname(1, "blue2red")
    gl.mosaic("A R 0 C R 0 S R 0; A R -0 C R -0 S R -0")
    gl.savebmp(f"../images/{gradient_name}.png")
    # To make sure the previous overlay is closed and does not interfere
    # with the next we call:
    gl.overlaycloseall()

