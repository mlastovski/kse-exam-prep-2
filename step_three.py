sal = {
    "John":1500, 
    "Rebecca":2500, 
    "Bob":3000
}

pos = {
    "John": "Intern", 
    "Rebecca": "Engineer", 
    "Bob": "Engineer"
}

def average_salary(salary, position, search_position):
    res = 0
    amount = 0
    for key, value in position.items():
        if value == search_position:
            res += salary[key]
            amount += 1

    if res == 0:
        return None
    else:
        return (res/amount)    

print(average_salary(salary=sal, position=pos, search_position="Engineer"))
print(average_salary(salary=sal, position=pos, search_position="Intern"))
print(average_salary(salary=sal, position=pos, search_position="CEO"))




