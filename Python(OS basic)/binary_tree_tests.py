from binary_tree import add, remove, find


def test_add():
    tree = None
    tree = add(tree, 1)
    tree = add(tree, 2)
    tree = add(tree, 3)

    if find(tree, 1) is False:
        print("test_add failed: can't find value 1")
    elif find(tree, 2) is False:
        print("test_add failed: can't find value 2")
    elif find(tree, 3) is False:
        print("test_add failed: can't find value 3")
    else:
        return True


def test_remove():
    tree = None
    tree = add(tree, 4)
    tree = add(tree, 2)
    tree = add(tree, 7)
 
    if find(tree, 2) is False:
        print("test_delete failed: can't find value 2")
 
    tree = remove(tree, 2)
 
    if find(tree, 2) is True:
        print("test_delete failed: 2 must be deleted")
    if find(tree, 4) is False:
        print("test_delete failed: 2 must be deleted")
    if find(tree, 7) is False:
        print("test_delete failed: 2 must be deleted")
    else:
        return True


def test_root_remove1():
    tree = None
    tree = add(tree, 5)
    tree = add(tree, 7)
    tree = add(tree, 6)
    tree = add(tree, 8)
    tree = add(tree, 2)
 
    if find(tree, 7) is False:
        print("test_delete failed: can't find value 7")
 
    tree = remove(tree, 7)
 
    if find(tree, 7) is True:
        print("test_delete failed: 7 must be deleted")
    elif find(tree, 5) is False:
        print("test_delete failed: can't find 2")
    elif find(tree, 6) is False:
        print("test_delete failed: can't find 2")        
    elif find(tree, 8) is False:
        print("test_delete failed: can't find 2")
    elif find(tree, 2) is False:
        print("test_delete failed: can't find 2")
    else:
        return True


def test_root_remove2():
    tree = None
    tree = add(tree, 5)
    tree = add(tree, 7)
    tree = add(tree, 6)
    tree = add(tree, 8)
    tree = add(tree, 2)
 
    if find(tree, 5) is False:
        print("test_delete failed: can't find value 5")
 
    tree = remove(tree, 5)
 
    if find(tree, 5) is True:
        print("test_delete failed: 5 must be deleted")
    elif find(tree, 7) is False:
        print("test_delete failed: can't find 2")
    elif find(tree, 6) is False:
        print("test_delete failed: can't find 2")        
    elif find(tree, 8) is False:
        print("test_delete failed: can't find 2")
    elif find(tree, 2) is False:
        print("test_delete failed: can't find 2")
    else:
        return True


if __name__ == '__main__':
    test_add()
    test_remove()
    test_root_remove1()
    test_root_remove2()

    if test_add() and test_remove() and test_root_remove1() and test_root_remove2():
        print('Всё ок')
