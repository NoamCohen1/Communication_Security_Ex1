import hashlib
import Node


# the function creates the merkle tree
def create_merkle_tree(nodesList):
    listOfNodes = []
    # return the root
    if len(nodesList) == 1:
        return nodesList[0]
    # go over the list of nodes and calculate their parents
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


# calculate the hash of two nodes
def encrypt_string(hash_string):
    return str(hashlib.sha256(hash_string.encode()).hexdigest())


# create from the leaves a list of nodes and call the create_merkle_tree
def create_list(leaves):
    listOfNodes = []
    for i in range(len(leaves)):
        listOfNodes.append(Node.Node(str(leaves[i])))
    return create_merkle_tree(listOfNodes)


# receive the nonce (numOfZeros) and find a hash that match it
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


# the function search for the parent of the received node
def check_node(node, data):
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
