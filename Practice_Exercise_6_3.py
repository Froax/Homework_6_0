invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

woorden = invoer.split("-")
woorden.sort()
print(woorden)
print(max(woorden))
print(min(woorden))


list_a = []
for woord in woorden:
    list_a.append(int(woord))

avr = sum(list_a) / len(list_a)
print(avr)
