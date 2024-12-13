# Blog: ANTLR Calculator
- The project demonstrates the following concepts of ANTLR4 considering the "Calculator" example using the Python language:
    - Grammar
    - Lexer
    - Parser
    - Difference between Visitor and Listener

## Project Setup
- Requirements
    - Python 3
    - Java

### ANTLR Setup
1) Download the antlr jar into `/usr/local/lib` directory
```
cd /usr/local/lib
curl -O http://www.antlr.org/download/antlr-4.13.1-complete.jar
```
2) Add the path in the `CLASSPATH`
```
export CLASSPATH="/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH"
```
3) Create alias to use ANTLR tools with a shorter command
```
alias antlr4=' java -jar /usr/local/lib/antlr-4.13.1-complete.jar'
```

### Python environment setup
1) Create a Python virtual environment
    ```
    virtualenv path/to/venv/antlr_env
    ```
2) Activate the virtual environment
    ```
    source path/to/venv/antlr_env/bin/activate
    ```
3) Install packages
    ```
    pip install -r requirements.txt
    ```

## Generate ANTLR Lexer, Parser, Listener, Visitor

- To generate lexer, parser, listener, and visitor files from the grammar execute the command:
```
antlr4 -Dlanguage=Python3 -visitor antlr/Calculator.g4
```

## Visualize parsed input as tree
- To visualize the parsed input as tree execute the command (here "3+5*(2-8)" is considered as an example expression)
- Press Ctrl+D additionally after typing the expression (if you can not see the tree visualization directly)
```
antlr4-parse antlr/Calculator.g4 expression -gui
3+5*(2-8)
```

![Parsed tree image](images/antlr4_parse_tree.png "Parsed tree image")

## Evaluate expression using Visitor/Listener

**Visitor:**
- To evaluate an expression using visitor execute the command:
```
python3 calculate_with_visitor.py 3+5*(2-8)
```
- You should get the output
```
The result of '3+5*(2-8)' is: -27
```
**Listener:**
- To evaluate an expression using listener execute the command:
```
python3 calculate_with_listener.py 3+5*(2-8)
```
- You should get the output
```
The result of '3+5*(2-8)' is: -27
```
