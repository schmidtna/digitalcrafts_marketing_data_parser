# should_continue = True
# if should_continue:
#     print("hello")

# known_people = ["John", "Anna", "Mary"]

# person = input("Enter a person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You do not know {}!".format(person))

## Exercise

def who_do_you_know():
    people = input("Type a list of people you know, separated by commas: ")
    people_list = people.split(",")
    
    normalised_list = [person.strip() for person in people_list]

    return normalised_list
    

def ask_user():
    person = input("Enter a person you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()
    