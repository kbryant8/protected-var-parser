import ast, sys, inspect
from problem1part2 import null_cast


        
def solution(x):
    for node in ast.walk(x): 
        if isinstance(node, ast.Assign):
            if str(node.targets[0].id).startswith('_n_'):
                if isinstance(node.value, ast.NameConstant):
                    print('A very specific none thing happened at line ' + str(node.lineno))
                if isinstance(node.value, ast.Name):
                     if not (str(node.value).startswith('_n_')):                   
                        print('A very specific name thing happened at line ' + str(node.lineno))
    function_info = {}
    for node in ast.walk(x):
        if isinstance(node, ast.FunctionDef):
            arguments = []
            for y in node.args.args:
                arguments.append(y.arg)
            function_info[node.name] = arguments
            if not (isinstance(node.body[-1], ast.Return)):
                
                print('A very specific no return thing happened at line ' + str(node.lineno))
            if isinstance(node.body[-1], ast.Return):
                
                if isinstance(node.body[-1].value, ast.Name):
                    if not (str(node.body[-1].value.id).startswith('_n_')):
                        print('A very specific return variable thing happened at line ' + str(node.lineno))
                if isinstance(node.body[-1].value, ast.Call):
                    if node.func.id == 'null_cast':
                        pass
                    else:
                        if not (str(node.body[-1].value.func).startswith('_n_')):
                            print('A very specific return function thing happened at line ' + str(node.lineno))
    for node in ast.walk(x):
        if isinstance(node, ast.Call):
            if node.func.id == 'null_cast':
                pass
            else:
                for z in range(len(node.args)):
                    if isinstance(node.args[z], ast.Name):
                        if function_info[node.func.id][z].startswith('_n_'):
                            #if not (node.args[z].id == function_info[node.func.id][z]):
                            if not (str(node.args[z].id).startswith('_n_')):
                                print('A very specific function thing happened at line ' + str(node.lineno))


            
    

    

if __name__ == '__main__':
    #filename = "/Users/kylebryant/Desktop/cs591/CS591Project2/problem1/test1.ipynb"
    filename = sys.argv[1]
    #filename = "test1.ipynb"
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        solution(tree)  # your solution function  