def calculateletoperation(operand1,operand2,operation):
    if operation=="add":
        result=operand1+operand2
        return result
    elif operation=="sub":
        result=operand1-operand2
        return result
    elif operation=="mul":
        result=operand1*operand2
        return result
    elif operation=="div":
        result=operand1/operand2
        return result

print(calculateletoperation(1,4,"sub"))