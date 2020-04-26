import hashlib

def create_proof_of_inclusion(leaf, root):
    ans = ""
    fatherNode, direction = search_node(root, leaf)
    while True:
        if direction == "l":
            ans += direction + " " + str(fatherNode.left.data)
        else:
            if fatherNode.right:
                ans += direction + " " + str(fatherNode.right.data)

        if fatherNode == root:
            break
        else:
            fatherNode, direction = search_node(root, str(fatherNode.data))
            ans += " "
    return ans


def search_node(node, data):
    """
    Search function will search a node into tree.
    """
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


def encrypt_string(hash_string):
    return str(hashlib.sha256(hash_string.encode()).hexdigest())
