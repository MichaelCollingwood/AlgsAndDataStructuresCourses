import sys


sys.stdin.readline()
list_of_numbers = sys.stdin.read().split()

sorted_list_of_numbers = sorted([int(e) for e in list_of_numbers])

output = sorted_list_of_numbers[-1] * sorted_list_of_numbers[-2]
sys.stdout.write(str(output))
