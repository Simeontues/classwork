#1. Да се приеме 1 стринг и всичките гласни да се повторят 4 пъти.
sentence = str(input('Enter your sentence: ' ))
vowels = ('aeiouAEIOU')

for vowel in vowels:
    sentence = sentence.replace(vowel, vowel * 4)
print(sentence)

#2. Напишете програма, която взима число и проверява дължината му БЕЗ ДА СЕ ИЗПОЛЗВА ВГРАДЕНАТА ФУНКЦИЯ len.
num = int(input("Enter a number: ")) 
count = 0

while (num >= 10 ** count):
    count += 1
    
print(count)

#3. Напишете програма, която прилага корен квадратен точно толкова пъти необходими да направи числото по-малко от 2 ...
num = int(input("Enter a number: "))
count = 0

while(num >= 2):
    num **= .5
    count += 1
print("Square root: ", count)

#4. Напишете програма, която взима число от потребителя и намира всички прости числа до това число и ги събира.
num = int(input("Enter a number: "))
i = 0

for n in range(2, num + 1):
    prime = True
    for m in range(2, n):
        if n % m == 0:
            prime = False
            break
    if prime:
        i += n

print(num,"->",i)