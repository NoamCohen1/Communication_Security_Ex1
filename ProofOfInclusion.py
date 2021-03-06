import hashlib


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


# calculate the hash of two nodes
def encrypt_string(hash_string):
    return str(hashlib.sha256(hash_string.encode()).hexdigest())
