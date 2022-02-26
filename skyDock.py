# docker run image <cmd> <params>
# python skyDock.py run <cmd> <params>

import sys, os, time

def main():
	if sys.argv[1]=="run":
		run()
	else:
		print("Bad Command :(")

def run():
	print("Running", sys.argv[2:])
	cmd = str(sys.argv[2]) + " " + " ".join(sys.argv[3:])
	print(cmd)
	os.system(cmd)
	time.sleep(5)

# Main program starts here :)
main()