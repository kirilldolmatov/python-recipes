#
# Reading multiple files with generators power
#

# Lets say we want to write a program that takes a list of filenames as arguments
#  and prints contents of all those files, like cat command in unix.

# The traditional way to implement it is:

def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line)
# Now, lets say we want to print only the line which has a particular substring, like grep command in unix.

def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line)
# Both these programs have lot of code in common. It is hard to move the common part to a function.
# But with generators makes it possible to do it.

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line)

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

# The code is much simpler now with each function doing one small thing.
# We can move all these functions into a separate module and reuse it in other programs.
