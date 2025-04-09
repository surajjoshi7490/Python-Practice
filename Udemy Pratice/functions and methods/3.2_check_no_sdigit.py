# check how many digits are there in a strig
from collections import Counter
check="string 1 and there are 2 and 5 anf 4"

check_is=[char for char in check if char.isdigit()]
count=Counter(check_is)
print(count)
# s="string 1 and there are 2 and 5 anf 4"
# digits = [char for char in s if char.isdigit()]
# count = Counter(digits)
# print(count)