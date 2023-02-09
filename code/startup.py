import gl
import sys

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

