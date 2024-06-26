def solve_expression(exprression):
    try:
        result=eval(expression)
        return result
    except Exception as e:
        return f"Error:{str(e)}"
