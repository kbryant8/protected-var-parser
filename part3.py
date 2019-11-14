import ast
import inspect
import sys
import astor
import aspectlib
from aspectlib import Aspect
from aspectlib import weave
from aspectlib import Return
from aspectlib import Proceed

## INSTRUMENTATION VERSION
def instrument(code):
    # codes = inspect.getsource(code)
    tree = ast.parse(code)

    print('input code ----------------------------')
    print(code)
    print('---------------------------------------')

    # find function definitions and instrument the body of each function
    statements = []
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef):
            print('hello')
            statement = instrument_body(statement)
        statements.append(statement)

    tree.body = statements
    code = astor.to_source(tree)
    

    print('output code --------------------------')
    print(code)
    print('---------------------------------------')

    return code


def instrument_body(function_def):
    statements = []
    variables = []
    for y in function_def.args.args:
    	if y.arg.startswith('_n_'):
    		variables.append(y.arg)
    i = 0
    for statement in function_def.body:
        if i == 0:
            vals = []
            for x in variables:
            	 #statements += instrument_statement(statement, variables,function_def.name)
            	time_statement = ast.parse("if " + x + " is None: raise Exception ('" + x + ' is given None in ' + str(function_def.name) + "')")
            	statements.append(time_statement)

            i+=1
        
        statements.append(statement)
    print(statement)
    function_def.body = statements
    return function_def

# ASPECT ORIENTED PORTION

@Aspect(bind=True)
def time_aspect2(cutpoint, *args, **kwargs):
    result = yield Proceed(*args, **kwargs)
    if cutpoint.__name__.startswith('_n_'): # call the actual function with all parameters
        if result == None:
            raise ValueError('None type computed')
        yield Return(result) # return the result
    

def null_weave(args):
    for x in args:
        weave(x, time_aspect2)

if __name__ == '__main__':
    # filename = "/Users/kylebryant/Desktop/cs591/CS591Project2/problem1/test1.ipynb"
    filename = sys.argv[1]
    
    with open(filename, 'r') as code_file:
        code = code_file.read()
        instrument(code)  
