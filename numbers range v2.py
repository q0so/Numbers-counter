from1 = int(input('Enter the start number : '))
to2 = int(input('Enter the end number : '))

with open('num.txt', 'w') as file:
    for num in range(from1, to2 + 1): 
        file.write(f"{num}\n") 
print("Numbers have been saved in 'num.txt'")
