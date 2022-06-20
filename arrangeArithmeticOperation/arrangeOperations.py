    
class ArithmeticOperation:
    def __init__(self, operation1, operator, operation2):
        self.operation1 = operation1
        self.operator = operator
        self.operation2 = operation2
        padding = len(self.operation1) if len(self.operation1)>len(self.operation2) else len(self.operation2)
        self.operand = self.operand = self.operator +' '+self.operation2.rjust(padding)
        self.dashes = ''
        self.result = 0
    def getOperation1(self):        
        return self.operation1.rjust(len(self.operand))
    def getOperand(self):
        return self.operand
    def getDashes(self):
        return self.dashes.rjust(len(self.operand),'-')
    def getResult(self):
        if self.operator == '+':
            self.result = int(self.operation1) + int(self.operation2)
        else:
            self.result = int(self.operation1) - int(self.operation2)
        return str(self.result).rjust(len(self.operand))
    def isValidDigitOperands(self):
        valid = True
        if self.operation1.isdigit()  == False or self.operation2.isdigit() == False:
            return False
        return valid
    def isValidOperator(self):
        if self.operator == '+' or  self.operator == '-':
            return True
        else:
            return False
    def isValidLength(self):
        if len(self.operation1) > 4 or len(self.operation2) > 4:
            return False
        else:
            return True


def arithmetic_arranger(ops,answer = False): 
    if len(ops) > 5:
       return "Error:Too many problems."
    oper = ''
    operands = ''
    dashes = ''
    results = ''
    for opera in ops:
        operators = opera.split()
        arith = ArithmeticOperation(operators[0],operators[1],operators[2])
        if arith.isValidDigitOperands():
            if arith.isValidLength():
                if arith.isValidOperator():
                    oper = arith.getOperation1() if oper == '' else '{}    {}'.format(oper,arith.getOperation1()) 
                    operands = arith.getOperand() if operands == '' else '{}    {}'.format(operands,arith.getOperand()) 
                    dashes = arith.getDashes() if dashes == '' else '{}    {}'.format(dashes,arith.getDashes())
                    if answer:
                        results = arith.getResult() if results == '' else '{}    {}'.format(results,arith.getResult())                      
                else:
                   return "Error: Operator must be '+' or '-'."                    
            
            else:
               return "Error: Numbers cannot be more than four digits."                

        else:
            return 'Error: Numbers must only contain digits.'             
    oper= oper.rstrip()
    operands= operands.rstrip()
    dashes= dashes.rstrip()
    results = results.rstrip()
    cad = '{}\n{}\n{}'.format(oper,operands,dashes) 
    if answer:       
        cad = '{}\n{}'.format(cad,results) 
    return cad
   

print(arithmetic_arranger(['3 + 855', '988 + 40'],True))


