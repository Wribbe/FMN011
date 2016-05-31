import os
import subprocess
import sys

FNULL = open(os.devnull, 'w')

pdfs = sorted([filename for filename in os.listdir('.') if '.pdf' in filename])
message = "Start at specific lecture? (default=000): "

start_at = input(message).strip()
if start_at:
    """ Iterate over list until index of starting file is found, slice list so
    that in begins on that file. If no file matches, no slicing and all files
    will be read. """
    for index, filename in enumerate(pdfs):
        if filename.startswith(start_at):
            pdfs=pdfs[index:]
            break

for filename in pdfs:
    command = "evince {}".format(filename).split()
    process = subprocess.Popen(command,
            stderr=FNULL,
            stdout=subprocess.PIPE,)

    process.communicate()
    message = "Continue with next? y/n: "
    display_next = input(message).lower().strip() == 'y'
    if not display_next:
        break
