class Human:
    def __init__(self, name="John", age=0, sex="Male"):
        self.name = name
        self.age = age
        self.sex = sex
        print("Create object of Human class")

    def speak(self, name):
        return print("I`m a {}.".format(name))

    def print_info(self):
        print("Name human is {}, age: {} years old and sex: {}.".format(self.name, self.age, self.sex))

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
