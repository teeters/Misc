This script uses an API called echoprint to identify unnamed songs in an
iTunes compilation and automatically fills in the name, artist, and other 
metadata.

Dependencies:

In order to use this script you will need to sign up for the echonest service
and enter your API key in the name_compilation.py file.
You will also need to install mutagen, a Python library for handling iTunes 
metadata. 
Finally, the codegen binary file from echonest requires a few depencies of its
own: TagLib and ffmpeg. See the echoprint README.md for details on installing
these.
