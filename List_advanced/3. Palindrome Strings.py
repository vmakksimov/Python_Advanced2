palindrome = input().split(' ')
searched_palindrome = input()

result = [el for el in palindrome if el == el[::-1]]

print(result)
print(f'Found palindrome {result.count(searched_palindrome)} times')

