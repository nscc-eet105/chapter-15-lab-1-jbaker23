
import employee

employee1 = employee.Employee('George Jetson', 35.5, 22.75)
employee2 = employee.Employee('Jane Jetson', 40, 30.00)
salesperson1 = employee.Salesperson('Leroy Jetson', 25, 15.00, 2550.50, 0.03)
salesperson2 = employee.Salesperson('Judy Jetson', 30, 22.50, 4750.00, 0.05)

people = [employee1, employee2, salesperson1, salesperson2]

for person in people:
    print(person)
    print(f"Total pay for {person.name} is ${person.calc_pay():.2f}")
    print("-------------")