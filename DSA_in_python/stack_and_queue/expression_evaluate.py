import random

expression = "(a + b) / c / d"

for i in range(50):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    d = random.randint(1, 1000)

    eval_expression = expression.replace("a", str(a)).replace("b", str(b)).replace("c", str(c)).replace("d", str(d))
    result = eval(eval_expression)
    
    print(i+1)
    print(f"Expression: {eval_expression}")
    print(f"Result: {result}")
    print("-" * 40)
