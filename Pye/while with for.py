from importlib.abc import Traversable


travalling = input("yes or no:")
while travalling == 'yes':
    num = int(input("number of people travelling"))

    for num in range(1, num + 1):
        name = input("Name:")

        age = input("Age")

        sex = input("Male or female:")

        print(name)
        print(age)
        print(sex)
    teavelling = input('Oops! forgot someone')
    