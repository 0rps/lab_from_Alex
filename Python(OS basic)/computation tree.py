def computation(root):
    if root['types'] == 'op':
        if root['value'] == '*':
            return computation(root['left']) * computation(root['right'])
        elif root['value'] == '+':
            return computation(root['left']) + computation(root['right'])
        elif root['value'] == '/':
            return computation(root['left']) / computation(root['right'])
        elif root['value'] == '-':
            return computation(root['left']) - computation(root['right'])
    else:
        return root['value']
