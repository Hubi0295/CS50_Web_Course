from Classes import  Point
from Flight import Flight
def main():
    print(show())
    plane()
    hello()

    people = [
        {"name": "harry", "House":"Gryffindor"},
        {"name": "Draco", "House": "Ravenclaw"},
        {"name": "Brace", "House": "Slytherin"}
    ]
    try:
        people.sort(key=lambda person: person["name"])#lambda
        print(people)
    except:
        print("Wrong")
def show():
    x = int(input("Input x: "))
    y = int(input("Input y: "))
    p = Point(x,y)
    return p.x, p.y


def plane():
    x=int(input("Input number of open seats: "))
    flight = Flight(x)
    people = adding()
    if len(people) > x:
        x = input("There is not available seats for everyone of you. Do you still want to get ticket? Type y or n: ")
        if x == 'n' or x== 'N':
            print("End of program bye")
            return 0
    for x in people:
        if flight.add_passenger(x):
            print(f'Person: {x} Added')
        else:
            print(f"We not have open seats for {x}")
def adding():
    list_of_people = []
    flag = True
    while flag:
        list_of_people.append(input("Input name: "))
        x= input("Do you wanna add next person? Type y if yes, n if no: ")
        if x == 'n' or x == 'N':
            flag = False
    return list_of_people

def announce(f):#Decorators
    def wrapper():
        print("About to run the function.. ")
        f()
        print("Done with the function")
    return wrapper
@announce
def hello():
    print("hello")




if __name__ == '__main__':
    main()
