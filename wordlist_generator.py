import itertools

chrs = input("Please enter the characters to generate wordlist: ")
min_length = int(input("Please enter the minimum lenght of a word: "))
max_length = int(input("Please enter the maximum length of a word "))
file_name = input("Please enter a file name to save to: ")

for n in range(min_length, max_length+1):
    for xs in itertools.product(chrs, repeat=n):
        print(''.join(xs))
        with open(f"{file_name}.txt", "a") as f:
            f.write(''.join(xs))
            f.write("\n")
