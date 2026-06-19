expression = []
value = int(input("Enter the number of Expressions: "))

for i in range(value):
    values = int(input("the values for the expression levels are:-\n"))
    expression.append(values)

max_value = expression[0]
peak_hour = 0 

for i in range(len(expression)):
    if expression[i] > max_value:
        max_value = expression[i]
        peak_hour = i  
print("The Highest Expression is", max_value)
print("the time is", peak_hour, "hours")
                                             