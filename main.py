class Employee:
    def __init__(self, name, age, expertise, happiness, ethic, status):
        self.name = name
        self.age = age
        self.expertise = expertise  # 0 - 10
        self.happiness = happiness  # 0 - 10
        self.ethic = ethic          # 0 - 10
        self.status = status        # Employed = 1, Not Employed = 0


employee1 = Employee('David Miles', 35, 9, 5, 8, 0)


def startUp(name):
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startUp('Test')


