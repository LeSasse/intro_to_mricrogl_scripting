# Intro to MRIcroGL scripting

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

# Set up for the tutorial

git clone https://github.com/LeSasse/intro_to_mricrogl_scripting.git
cd intro_to_mricrogl_scripting  

# Install MRIcroGL

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
and again make sure to source the `zshrc` or start up a new terminal.
```
source ~/.zshrc
```
Now, running `mricrogl` should start up the program also. From now on, I will only use `mricrogl`
in any of the instructions. Note, that if you didn't set the alias, you can and should
run `MRIcroGL` instead.

# Using the program for interactive viewing

Most features of the program when interactively viewing NIfTI images are covered
by the series of videos that Andy Jahn made (linked above) and by the useful videos
provided by Chris Rorden himself on his youtube channel (for example: [MRIcroGL Introduction](https://www.youtube.com/watch?v=CL9X3zPUYN0)).
For this reason, I will not go into the interactive viewing myself.

# Using MRIcroGL for scripting

MRIcroGL provides some instructions and help regarding scripting [here](https://github.com/rordenlab/MRIcroGL/blob/master/PYTHON.md).
Here, I want to provide a few useful step-by-step guide to use some of its scripting features
with some example data. Although I am sure much more is possible than what I show here,
it will set you up for a good start and already provide you some powerful possibilities.

Overall, you can write your scripts using Python code. However, it is not run via
the typical python interpreter but via MRIcroGL. So, as the instructions linked above
state, you can run a script (for example `my_script.py`) using `mricrogl my_script.py`.