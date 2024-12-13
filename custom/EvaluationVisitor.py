from antlr.CalculatorLexer import CalculatorLexer
from antlr.CalculatorParser import CalculatorParser
from antlr.CalculatorVisitor import CalculatorVisitor
from antlr4 import *


class EvaluationVisitor(CalculatorVisitor):
    def visitNumber(self, ctx: CalculatorParser.NumberContext):
        # Convert the NUMBER token to an integer
        return int(ctx.getText())

    def visitParentheses(self, ctx: CalculatorParser.ParenthesesContext):
        # Evaluate the expression inside the parentheses
        return self.visit(ctx.expression())

    def visitMultiplication(self, ctx: CalculatorParser.MultiplicationContext):
        # Evaluate left and right expressions and multiply them
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left * right

    def visitDivision(self, ctx: CalculatorParser.DivisionContext):
        # Evaluate left and right expressions and divide them
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left / right

    def visitAddition(self, ctx: CalculatorParser.AdditionContext):
        # Evaluate left and right expressions and add them
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left + right

    def visitSubtraction(self, ctx: CalculatorParser.SubtractionContext):
        # Evaluate left and right expressions and subtract them
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left - right
