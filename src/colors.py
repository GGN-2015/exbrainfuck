import sys



RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
END = '\033[0m'



def error_log(msg, ret): # die and log on the stderr
    sys.stderr.write(RED + ("%s\n" % msg) + END)
    exit(ret)



def info_log(msg):
    sys.stderr.write(CYAN + ("%s\n" % msg) + END)