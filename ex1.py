# Noam Cohen, 208995902, Gal Marcovich, 208715367

import hashlib


# ----------------------  Class Node  ---------------------- #


"""
The class creates Nodes for the merkle
tree.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# ----------------------  Proof Of Inclusion  ---------------------- #


# the function creates proof of inclusion for the received node and root
def create_proof_of_inclusion(leaf, root):
    ans = ""
    fatherNode, direction = search_node(root, leaf)
    while True:
        if direction == "l":
            ans += direction + " " + str(fatherNode.left.data)
        else:
            if fatherNode.right:
                ans += direction + " " + str(fatherNode.right.data)
        # if the function search_node return the root - finish and break
        if fatherNode == root:
            break
        else:
            fatherNode, direction = search_node(root, str(fatherNode.data))
            ans += " "
    return ans


# the function search for the parent of the received node and return the direction of its son
def search_node(node, data):
    # if node is a leaf return None
    if node.left is None and node.right is None:
        return None
    if node.left.data == data:
        return node, "r"
    if node.right.data == data:
        return node, "l"

    ans = search_node(node.left, data)
    if ans:
        return ans

    return search_node(node.right, data)


# the function checks the received proof of inclusion
def check_proof_of_inclusion(leaf, root, listOfProof):
    ans = leaf
    for i in range(0, len(listOfProof), 2):
        if listOfProof[i] == "l":
            ans = encrypt_string(listOfProof[i+1] + ans)
        else:
            ans = encrypt_string(ans + listOfProof[i+1])
    if ans == root:
        return "True"
    else:
        return "False"


# ----------------------  Merkle Tree  ---------------------- #


# the function creates the merkle tree
def create_merkle_tree(nodesList):
    listOfNodes = []
    # return the root
    if len(nodesList) == 1:
        return nodesList[0]
    # go over the list of nodes and calculate their parents
    for i in range(0, len(nodesList), 2):
        if (i+1) == len(nodesList):
            newNode = Node(encrypt_string(str(nodesList[i].data)))
            newNode.left = nodesList[i]
            listOfNodes.append(newNode)
        else:
            newNode = Node(encrypt_string(str(nodesList[i].data) + str(nodesList[i+1].data)))
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
        listOfNodes.append(Node(str(leaves[i])))
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


# ----------------------  Main  ---------------------- #


def choose_main():
    root = None
    leaves = []
    loop = True
    while loop:
        # gets the choice of the user
        choice = input().split(" ")
        if len(choice) == 0:
            break
        # option 1
        if choice[0] == "1":
            if len(choice) < 2:
                break
            if choice[1] == "":
                break
            leaves = choice[1:]
            root = create_list(choice[1:])
            print(root.data)
        # option 2
        elif choice[0] == "2":
            if root is None or len(choice) != 2:
                break
            if choice[1].startswith('-'):
                break
            if choice[1].isdigit() is False:
                break
            if int(choice[1]) >= len(leaves):
                break
            print(create_proof_of_inclusion(leaves[int(choice[1])], root))
        # option 3
        elif choice[0] == "3":
            if len(choice) < 5:
                break
            leaf = choice[1]
            root3 = choice[2]
            proof = choice[3:]
            for i in range(0, len(proof), 2):
                if (str(proof[i]) != 'l') and (str(proof[i]) != 'r'):
                    loop = False
                    break
            if loop is False:
                break
            print(check_proof_of_inclusion(leaf, root3, proof))
        # option 4
        elif choice[0] == "4":
            if root is None or len(choice) != 2:
                break
            if choice[1].startswith('-'):
                break
            if choice[1].isdigit() is False:
                break
            if int(choice[1]) < 1:
                break
            winningNumber, result = check_for_zeros(int(choice[1]), root)
            print(str(winningNumber) + " " + str(result))
        # option 5
        elif choice[0] == "5":
            break
        else:
            break
    return


# main
if __name__ == "__main__":
    choose_main()
