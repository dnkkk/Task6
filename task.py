class Worker:
    def __init__(self, surname, experience, hourly_wag, hours_work):
        self.surname = surname
        self.experience = max(experience, 0)
        self.hourly_wage = max(hourly_wag, 0)
        self.hours_work = max(hours_work, 0)
        self.salary = self.calculate_salary(self.hours_work, self.hourly_wage)
        self.premium = round(self.calculate_premium(self.experience, self.salary))

    @staticmethod
    def calculate_premium(experience, salary):
        if experience < 1:
            return 0
        elif experience < 3:
            return salary * 0.05
        elif experience < 5:
            return salary * 0.08
        else:
            return salary * 0.15

    @staticmethod
    def calculate_salary(hours_work, hourly_wage):
        return hours_work * hourly_wage

    def __str__(self):
        return "Surname: " + str(self.surname) + \
               "\nExperience: " + str(self.experience) + "\n" + \
               str(self.surname) + " has worked: " + str(self.hourly_wage) + " hours\n" + \
               "Salary: " + str(self.salary) + "\n" + "Premy: " + str(self.premium)

    def in_file(self):
        file_name = self.surname + ".txt"
        with open(file_name, "w") as file:
            file.write(self.__str__())

        print("Information about", self.surname, "was written in file", file_name)


surname = input("Enter surname: ")
experience = int(input("Enter experience: "))
hourly_wage = int(input("Enter hourly wage: "))
hours_work = int(input("Enter how much worker worked: "))

worker = Worker(surname, experience, hourly_wage, hours_work)
print()
print(worker)

print()
worker.in_file()
