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





    
    


    

