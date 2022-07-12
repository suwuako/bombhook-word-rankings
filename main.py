letters = {
	"A" : 0,
	"B" : 0,
	"C" : 0,
	"D" : 0,
	"E" : 0,
	"F" : 0,
	"G" : 0,
	"H" : 0,
	"I" : 0,
	"J" : 0,
	"K" : 0,
	"L" : 0,
	"M" : 0,
	"N" : 0,
	"O" : 0,
	"P" : 0,
	"Q" : 0,
	"R" : 0,
	"S" : 0,
	"T" : 0,
	"U" : 0,
	"V" : 0,
	"W" : 0,
	"X" : 0,
	"Y" : 0,
	"Z" : 0}

wlist = open("wordlist", "r")

wordlist = []
lines = wlist.readlines()
for i in lines:
	wordlist.append(i.replace("\n", ""))

del(lines)

for word in wordlist:
	for letter in word:
		if letter in letters:
			letters[letter] += 1

def find_highest_set(letters):
	highest_value = 0
	current_winning = ""	
	for letter, ranking in letters.items():
		if ranking > highest_value:
			highest_value = ranking
			current_winning = letter

	return [current_winning, highest_value]

total_letters = 0
output = {}


for i in range(len(letters)):
	top = find_highest_set(letters)
	letters.pop(top[0])	
	total_letters += top[1]
	output[top[0]] = {"ranking" : top[1]}

outcopy = output

for letter, value in output.items():
	percentage = value["ranking"] / total_letters * 100
	outcopy[letter]["percentile"] = percentage

print("STATS: (in order of highest to lowest")
for k, v in outcopy.items():
	print(f"{k} - {v['ranking']} total letters, {v['percentile']}% of total wordset")

print("For bombhook dict format:")
print("{")
for k, v in outcopy.items():
	print(f"{k} : {v['percentile']}")
print("}")
