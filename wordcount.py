# put your code here.
# file_ref = open('twain.txt')
# stats = {}

# for line in file_ref:
#     line = line.rstrip()
#     line = line.split(" ")
#     for word in line:
#         stats[word] = stats.get(word, 0) + 1

# file_ref.close()

# for stat in stats:
#     print stat, stats[stat]

file_ref = open('twain.txt')
stats = {}

for line in file_ref:
    line = line.rstrip()
    line = line.split(" ")
    for word in line:
        stats[word] = stats.get(word, 0) + 1

file_ref.close()

for word, stat in stats.iteritems():
    print word, stat
