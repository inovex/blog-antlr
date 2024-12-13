import sys
from antlr4 import *
from antlr.CalculatorLexer import CalculatorLexer
from antlr.CalculatorParser import CalculatorParser
from custom.EvaluationVisitor import EvaluationVisitor


def main(argv):
    input_expr = "".join(argv)
    input_stream = InputStream(input_expr)
    
    lexer = CalculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    
    # Start parsing at the 'expression' rule
    tree = parser.expression()
    
    # Create a visitor and evaluate the expression
    evaluator = EvaluationVisitor()
    result = evaluator.visit(tree)
    
    print(f"The result of '{input_expr}' is: {result}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculate_with_visitor.py <expression>")
        sys.exit(1)
    main(sys.argv[1:])