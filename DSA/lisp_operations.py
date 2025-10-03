def apply_function(func: str, a: float, b: float) -> float:
    if func == "add":
        return a + b
    elif func == "mul":
        return a * b
    elif func == "pow":
        return a ** b
    elif func == "div":
        if b == 0:
            return float('inf')  
        return a / b
    raise ValueError(f"Unknown function: {func}")

def evaluate(expression: str) -> float:

    def parse(index: int) -> tuple[float, int]:
        print(f"parsing index: {index}")
        # --------- Base Condtions -------
        #  if you find a number or digits we need to form a number and return which will be used as the argument
        if index < len(expression) and expression[index].isdigit():
            print("found number ")
            # number can be of 2 digit as well
            num = 0
            while index < len(expression) and expression[index].isdigit():
                num = num * 10 + int(expression[index])
                index += 1
            print(num)
            return num, index
        
        # Identify is this a function ?
        # if index value is alphabate , iterate till alphabets are there and we get function name
        # Parse function (e.g., add, mul, pow, div)
        
        func = ""
        while index < len(expression) and expression[index].isalpha():
            print("found function")
            func += expression[index]
            index += 1
        print(func)
        # Once function is done ( we will check for opening parenthesis)
        # Expect opening parenthesis
        if expression[index] == '(':
            index += 1
        
        ## Now once we have the function name and opening parenthesis we need to know the arguments
        # we will need the argument and the index output from parse function from the current index
        
        arg1, index = parse(index)
        
        # Once we have the first argument we need to check for the comma
        if expression[index] == ',':
            index += 1
        
        # Parse second argument it can be a fuction or it can be a digit
        arg2, index = parse(index)
        
        # Once we have the second argument we need to check for closing parenthesis
        # Expect closing parenthesis
        if  expression[index] == ')':
            index += 1
        
        # Apply the function to arguments
        print("Now Applying function", func, arg1, arg2)
        result = apply_function(func, arg1, arg2)
        print("answer is", result)
        
        return result, index
    
    # Start parsing from index 0
    print("starting parsing form index: 0")
    result, index = parse(0)
    
    return result








def evaluate(exp):    
    def apply_func(func_name, arg1, arg2):
        if func_name == "add":
            return arg1 + arg2
        elif func_name == "mul":
            return arg1 * arg2
        elif func_name == "pow":
            return arg1 ** arg2
        elif func_name == "div":
            if arg2!=0:
                return arg1/ arg2 
            else:return float("inf")
    
        
    # parse the expression, get function name, arguments, and apply functions
    def parse(ind, exp):
        # base condition to break, for arguments is that is number we can use it
        # I need to identify number
        if exp[ind].isdigit():
            num = ""
            while exp[ind].isdigit() or exp[ind] == ".":
                num += exp[ind]
                ind += 1
            num = float(num)
            return num, ind
        # identify if it is a character to do that I can use like set of aphabets to find it or I can use .isalpha()
        func = ""
        if exp[ind].isalpha():
            while exp[ind].isalpha():
                func += exp[ind]
                ind += 1
                
        # I have function name now I will be expecting a paranthesis
        if exp[ind] == "(":
            ind +=1
        
        # next I need to know the arguments and I will treat it as a new problem all together
        arg1,ind =  parse(ind, exp)
        
        # Now I will be expecting a ,
        if exp[ind] == ",":
            ind += 1
        
        arg2, ind = parse(ind, exp)

        if exp[ind] == ")":
            ind += 1
        
        res = apply_func(func, arg1, arg2)
        
        return res, ind
    
    result, index = parse(0,exp)
    
    return result
    
    

# # Test cases
if __name__ == "__main__":
    tests = [
        "add(mul(2.5,pow(5.4,2)),mul(2,pow(5,2)))",  # 5 + (2 * 5^2) = 55
        "div(10,2)",               # 10 / 2 = 5
        "mul(3,pow(2,3))",        # 3 * 2^3 = 24
        "add(10,div(20,4))",      # 10 + (20 / 4) = 15
        "div(5,0)",               # Should raise error
    ]
    
    for expr in tests:
        try:
            print(f"{expr} -> {evaluate(expr)}")
        except ValueError as e:
            print(f"{expr} -> Error: {e}")