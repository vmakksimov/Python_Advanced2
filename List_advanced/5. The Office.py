happiness = input().split()
h_improvment_factor = int(input())
happiness = [int(el) * h_improvment_factor for el in happiness]
average_new = sum(happiness) / len(happiness)
#average = list(filter(lambda x: x >= (sum(happiness) / len(happiness)), happiness))

#if len(average) >= len(happiness) / 2:
    #print(f'Score:{len(average)}/{len(happiness)}. Employees are happy!')
#else:
    #print(f'Score: {len(average)}/{len(happiness)}. Employees are not happy!')
people = [el for el in happiness if el >= average_new]
if len(people) >= len(happiness) / 2:
    print(f'Score: {len(people)}/{len(happiness)}. Employees are happy!')
elif len(people) < len(happiness):
    print(f'Score: {len(people)}/{len(happiness)}. Employees are not happy!')


