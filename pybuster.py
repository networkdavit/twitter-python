import requests
import sys

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
	print(" -------------------------------------------------------------------------------------------")
	print("| Welcome to pybuster                                                                       |")
	print("| -------------------------------------                                                     |")
	print("| A typical attack looks like this: python3 pybuster.py http://<ip> wordlist.txt output.txt |")
	print("| ----------------------------------------------------------------------------------------- |")
	print("| replace http://ip with the website                                                        |")
	print("| replace wordlist.txt with your wordlist                                                   |")
	print("| replace output.txt with your desired name (this is an optional argument)                  |")
	print("| if not specified file output will autosave to 'output.txt' file                           |")
	print("  ------------------------------------------------------------------------------------------ ")
	sys.exit()


url = sys.argv[1]
directory_list = sys.argv[2]


try:
	output_file_name = sys.argv[3]
	output = open(output_file_name, "w")

except IndexError:
	output_file_name = "output.txt"

output = open(output_file_name, "w")	

with open(directory_list , "r") as file:
	print(f"Enumerating directories for {url}")
	print("---------------------------------------------------")
	for line in file:
		for directory in line.split():
			new = requests.get(f"{url}/{directory}")
			if new.status_code == 200:
				found = f"FOUND: {directory} ==> {url}/{directory}"
				print(found)
				print(found, file=output)

print(f"Out put saved in {output_file_name}")
