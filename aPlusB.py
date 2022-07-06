import sys

input_numbers = sys.stdin.read().split()
sum_of_nums = 0
sum_of_nums += int(input_numbers[0])
sum_of_nums += int(input_numbers[1])
sys.stdout.write(str(sum_of_nums))
