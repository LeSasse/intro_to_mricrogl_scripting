# Intro to mricrogl scripting

Introduction to scripting with MRIcroGL to make nice plots of brain maps with less effort.

# Why MRIcroGL

There are many nice options to view NIfTI images and to make good looking plots of the
brain. One of the natural choices when using Python is to use [nilearn.plotting](https://nilearn.github.io/stable/plotting/index.html).
I really like nilearns plotting functionality, since it is very easy to use indeed,
well documented, and seemlessly integrates into any python-based workflows/scripting tasks.

However, I personally also like the flexibility and user-interface that MRIcroGL
provides when viewing images interactively, and recently also discovered its python
scripting interface, which makes it very easy to run a set of repetitive tasks in the
viewers and create nice images. Another feature of MRIcroGL I absolutely love, is
the rendering of 3D volumes rather than just plotting of slices at specific coordinates.
It just looks fancy!

# Installation

Download the version that works for your system from the [MRIcroGL NITRC page](https://www.nitrc.org/projects/mricrogl).

I can provide some instructions on how I like to set it up on my system (Ubuntu 20.04),
but check what works for your system. Instructions for a [mac can be found in this
video by Andy Jahn](https://www.youtube.com/watch?v=Htid2mbyav8). He also provides a
nice series of videos on using MRIcroGL's UI to analyse your results (and many
other useful neuroimaging videos, so check him out).

I like to install it as follows. After downloading the zipped MRIcroGL files, run:
```
unzip MRIcroGL_linux.zip
```
Then I move or copy the folder into `/usr/local` where MRIcroGL will try to find
its ressources/files when starting up.
```
sudo cp -r MRIcroGL /usr/local
```
To be able to use the MRIcroGL binary from anywhere, add the `MRIcroGL` directory
to `$PATH` in your `zshrc` (or `bashrc` or some similar file):
```
export PATH=$PATH:/usr/local/MRIcroGL
```
Make sure to source the `zshrc` or start up a new terminal:
```
source ~/.zshrc
```
Now, running `MRIcroGL` should open up the viewer.
However, for ease of use I like to set an alias in addition, since I don't like
switching between the upper and lower cased letters. Again, in your `zshrc` add:
```
alias mricrogl="MRIcroGL"
```
and again make sure to source the `zshrc` or start up a new terminal. Now, running
`mricrogl` should start up the program also. From now on, I will only use `mricrogl`
in any of the instructions. Note, that if you didn't set the alias, you can and should
run `MRIcroGL` instead.