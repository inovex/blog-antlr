from antlr.CalculatorLexer import CalculatorLexer
from antlr.CalculatorParser import CalculatorParser
from antlr.CalculatorListener import CalculatorListener
from antlr4 import *


class EvaluationListener(CalculatorListener):
    def __init__(self):
        self.stack = []

    def exitNumber(self, ctx: CalculatorParser.NumberContext):
        # Push the number onto the stack
        number = int(ctx.getText())
        self.stack.append(number)

    def exitParentheses(self, ctx: CalculatorParser.ParenthesesContext):
        # Evaluate the expression inside the parentheses
        pass  # No action needed; the result will be handled in the parent operation

    def exitMultiplication(self, ctx: CalculatorParser.MultiplicationContext):
        right = self.stack.pop()
        left = self.stack.pop()
        result = left * right
        self.stack.append(result)

    def exitDivision(self, ctx: CalculatorParser.DivisionContext):
        right = self.stack.pop()
        left = self.stack.pop()
        result = left / right
        self.stack.append(result)

    def exitAddition(self, ctx: CalculatorParser.AdditionContext):
        right = self.stack.pop()
        left = self.stack.pop()
        result = left + right
        self.stack.append(result)

    def exitSubtraction(self, ctx: CalculatorParser.SubtractionContext):
        right = self.stack.pop()
        left = self.stack.pop()
        result = left - right
        self.stack.append(result)

    def getResult(self):
        # The final result will be the last item on the stack
        return self.stack.pop() if self.stack else None

