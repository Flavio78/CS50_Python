class Student:
    """
    Custom Class with attributes
    By default class is immutable
    """

    def __init__(self, name, house):
        """
        implement of the initialization in Python
        self get access to the object I have already created
        With self.name I create a new method
        Something different from creator function from other languages.
        self.name and self.house are created inside the object
        """
        if not name:  # if user pass an empty string
            # no return None because it is too late: the object is already been created
            raise ValueError("Missing name")  # I raise Excetion
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        """
        To customize the print this object as string
        """
        return f"{self.name} from {self.house}"


# I validate the data inside the class, keep all the related code together


def main():
    function7()


def function1():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def function2():
    student = get_student1()
    # In cannot change the values of the returned tuple
    # student[0] = "abc" --> immutability of tuple
    print(f"{student[0]} from {student[1]}")


def function3():
    student = get_student3()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def function4():
    student = get_student4()
    print(f"{student['name']} from {student['house']}")


def function5():
    student = get_student5()
    # dictionary as list are mutable
    # but we access with keys not in index as in list
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def function6():
    student = get_student6()
    print(f"{student.name} from {student.house}")


def function7():
    student = get_student7()
    print(student)


def get_name() -> str:
    name = input("Name: ")
    return name


def get_house() -> str:
    house = input("House: ")
    return house


def get_student1():
    """
    It returns a tuple
    """
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


def get_student3():
    """
    It returns a list
    """
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


def get_student4():
    """
    It returns a dictionary
    """
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


def get_student5():
    """
    It returns a dictionary
    """
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


def get_student6():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


def get_student7():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
