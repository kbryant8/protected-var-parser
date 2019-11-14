import ast, inspect

#def null_cast(x):
#	print(x)
#	if isinstance(x, ast.NameConstant):
#		raise ValueError("this is invalid")
#	if isinstance(x, ast.Constant):
#		if x.value == None:
#			raise ValueError("this is invalid")
#	return x

def null_cast(x):
	if x == None:
		raise ValueError("this is invalid")
	return x