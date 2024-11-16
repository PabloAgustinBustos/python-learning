import random

def fetch(url, cb, catch):
    gen = random.choice("10")

    if(gen == "1"):
        cb({
            "name": "Pablo"
        })
    else:
        catch(400)


fetch("", lambda res: print(res), lambda err: print(err))

employees = [
    {
        "name": "Pablo",
        "salary": 700,
        "currency": "USD"
    },

    {
        "name": "Juan",
        "salary": 820,
        "currency": "USD"
    },

    {
        "name": "Lucas",
        "salary": 810000,
        "currency": "ARS"
    },

    {
        "name": "Ricardo",
        "salary": 1300000,
        "currency": "ARS"
    },
]

employees = map(lambda employee: { 
    **employee,
    "salary": employee["salary"]*1.3 if employee["currency"] == "ARS" else employee["salary"]*1.15
}, employees)

for employee in employees:
    print(employee)