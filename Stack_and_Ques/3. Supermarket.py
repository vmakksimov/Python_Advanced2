from collections import deque

name = input()
#all_names = []
#while name:
    #if name == 'End':
        #break
    #all_names.append(name)
    #name = input()

queque = deque([])

while not name == 'End':
    if name != 'Paid':
        queque.append(name)
    elif name == 'Paid':
        for names in range(len(queque)):
            print(queque.popleft())

    name = input()

print(f'{len(queque)} people remaining.')