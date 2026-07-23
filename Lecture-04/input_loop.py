score = int(input('Enter s test score: '))
while score < 0 or score > 100:
    print('ERROR: The score cnnot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score: '))
    