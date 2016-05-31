import os
import re
import subprocess
import sys


def main():

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

def renumber(filename):
    line_buffer = []
    lines = [line.strip(os.linesep) for line in open(filename).readlines()]
    current = 0
    for line in lines:
        if re.match(r"^\d\d\d", line):
            new_line = re.sub("\d\d\d", "{0:03d}".format(current), line)
            line_buffer.append(new_line)
            current += 1
        else:
            line_buffer.append(line)
    print(os.linesep.join(line_buffer))

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    if "renumber" in args:
        renumber(args[1])
    else:
        main()
