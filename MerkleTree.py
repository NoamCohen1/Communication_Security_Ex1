import hashlib
import Node


def create_merkle_tree(nodesList):
    listOfNodes = []
    if len(nodesList) == 1:
        return nodesList[0]
    for i in range(0, len(nodesList), 2):
        if (i+1) == len(nodesList):
            newNode = Node.Node(encrypt_string(str(nodesList[i].data)))
            newNode.left = nodesList[i]
            listOfNodes.append(newNode)
        else:
            newNode = Node.Node(encrypt_string(str(nodesList[i].data) + str(nodesList[i+1].data)))
            newNode.left = nodesList[i]
            newNode.right = nodesList[i+1]
            listOfNodes.append(newNode)
    return create_merkle_tree(listOfNodes)


def encrypt_string(hash_string):
    return str(hashlib.sha256(hash_string.encode()).hexdigest())


def create_list(leaves):
    listOfNodes = []
    for i in range(len(leaves)):
        listOfNodes.append(Node.Node(str(leaves[i])))
    return create_merkle_tree(listOfNodes)


def check_for_zeros(numOfZeros, root):
    zeros = ""
    for i in range(numOfZeros):
        zeros += "0"
    winningNumber = 0
    while True:
        result = encrypt_string(str(winningNumber) + str(root.data))
        if result.startswith(zeros):
            break
        else:
            winningNumber += 1
    return winningNumber, result


def check_node(node, data):
    """
    Search function will search a node into tree.
    """
    # if node is a leaf return None
    if node.left is None and node.right is None:
        return None
    if node.left.data == data:
        return node
    if node.right.data == data:
        return node

    ans = check_node(node.left, data)
    if ans:
        return ans

    return check_node(node.right, data)
