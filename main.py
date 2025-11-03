<<<<<<< HEAD
def calculate_bonus(base_salary, bonus_percentage):
    return base_salary * bonus_percentage / 100
def calculate_discount(brute_salary, discount_percentage):
    return brute_salary * discount_percentage / 100
def calculate_net_salary(base_salary, bonus_percentage, discount_percentage):
    bonus = calculate_bonus(base_salary, bonus_percentage)
    brute_salary = base_salary + bonus
    discount = calculate_discount(brute_salary, discount_percentage)
    net_salary = brute_salary - discount
    return net_salary, bonus, discount

base_salary = float(input('Type your base salary: '))
bonus_percentage = float(input('Type your salary bonus (%): '))
discount_percentage = float(input('Type your salary discount (%): '))

net_salary, bonus, discount = calculate_net_salary(base_salary, bonus_percentage, discount_percentage)

print('-- RESULTS --')
print(f'Base salary: R${base_salary}')
print(f'Bonus of {bonus_percentage}%: {bonus:.2f}')
print(f'Discount of {discount_percentage}%: {discount:.2f}')
print(f'Net salary: {net_salary:.2f}')





    
    


    

=======
""" -- Salary Calculator --
A program that calculates the net salary of a employee based on the given information:
- Base salary
- Bonus percentage
- Discount percentage

-- Author: Pedro R F
-- Date: 11/03/2025 """



def calculate_bonus(base_salary, bonus_percentage):
    "Calculates the salary bonus based on a given percentage "
    return base_salary * bonus_percentage / 100


def calculate_discount(brute_salary, discount_percentage):
    "Calculates the salary discount based on a given percentage"
    return brute_salary * discount_percentage / 100


def calculate_net_salary(base_salary, bonus_percentage, discount_percentage):
    "Calculates the net salary based on the bonus percentage and the discount percentage "
    bonus = calculate_bonus(base_salary, bonus_percentage)
    brute_salary = base_salary + bonus
    discount = calculate_discount(brute_salary, discount_percentage)
    net_salary = brute_salary - discount
    return net_salary, bonus, discount

def main():
    "Main function where the data is input"
    try:
        base_salary = float(input('Type your base salary: '))
        bonus_percentage = float(input('Type your salary bonus (%): '))
        discount_percentage = float(input('Type your salary discount (%): '))

        net_salary, bonus, discount = calculate_net_salary(base_salary, bonus_percentage, discount_percentage)

        print('-- RESULTS --')
        print(f'Base salary: R${base_salary}')
        print(f'Bonus of {bonus_percentage}%: {bonus:.2f}')
        print(f'Discount of {discount_percentage}%: {discount:.2f}')
        print(f'Net salary: {net_salary:.2f}')
    except ValueError:
        print(f'Please enter valid numeric values for the calculation')
    except Exception as e:
        print(f'An unexpected error has occurred: {e}')
        

if __name__ == "__main__":
    main()




    
    


    

>>>>>>> 4cdfc57 (Adding the Salary calculator)
