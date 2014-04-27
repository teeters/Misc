#Script to automatically name unnamed tracks in specified itunes folder. Uses echoprint.
#Assumes that the songs are all part of a compilation.

import sys
import os

import mutagen
from mutagen.easymp4 import EasyMP4

import pyechonest.config as config
import pyechonest.song as song

config.CODEGEN_BINARY_OVERRIDE = os.path.abspath("../echoprint/echoprint-codegen")
print os.path.abspath("../echoprint/echoprint-codegen")

config.ECHO_NEST_API_KEY='Z4KAQZLI0P1QNWKAG'

def lookup(file):
    # Note that song.identify reads just the first 30 seconds of the file
    # Also you'll need the codegen binary
    fp = song.util.codegen(file)
    if len(fp) and "code" in fp[0]:
        result = song.identify(query_obj=fp, version="4.12")
        if len(result):
            artist = result[0].artist_name
            title = result[0].title
            return (title, artist)
        else:
            return None
    else:
        print "Error: Couldn't decode", file
        
# def ascript(scpt):
#     '''Runs the applescript given by scpt, returns stdout and stderr.
#     Note: Do NOT use this function for scripts that will generate large outputs; the data
#     is read to PIPE and buffer overrun is a risk.'''
#     aprocess = Popen('osascript', stdin=PIPE, stdout=PIPE, stderr=PIPE)
#     return aprocess.communicate(scpt)

#Step 1: get the folder
mix_folder = ""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >>sys.stderr, "Usage: %s <compilation directory>" % sys.argv[0]
        sys.exit(1)
    mix_folder = sys.argv[1]
    
#If you're not running this from the command line, you can specify a value for mix_folder
#hereabouts. Make sure and use the full path, don't worry about spaces.

#Step 2: iterate through the tracks, lookup each one
track_names = os.listdir(mix_folder)
for fname in track_names:
    path = os.path.join(mix_folder, fname)
    found = lookup(path)
    if found:
        tune, artist = found
        #Step 3: get metadata for each track using mutagen, modify it.
        #IMPORTANT: the code below is for MP4 files only.
        track = EasyMP4(path)
        track['title'] = tune
        track['artist'] = artist
        track.save()
        print track['title'], track['artist']
    else:
        print "Could not identify:", path
        
#Notes for improvement: 
# -Need to find way to check the "part of compilation" box, so the songs 
# stay together in itunes.
# -Add support for non-mp4 file types.
    