numOfUnheard,numOfUnseen = map(int,input().split())
listUnheard = [None] * numOfUnheard
listUnseen = [None] * numOfUnseen
listResult = []

for i in range(0, numOfUnheard):
    listUnheard[i] = input()
for i in range(0, numOfUnseen):
    listUnseen[i] = input()

if numOfUnheard>numOfUnseen:
    listResult = list(set(listUnheard)-(set(listUnheard)-set(listUnseen)))
else:
    listResult = list(set(listUnseen)-(set(listUnseen)-set(listUnheard)))

listResult.sort()
print(len(listResult))
for i in range(0, len(listResult)):
    print(listResult[i])
