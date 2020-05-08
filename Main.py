import MerkleTree
import ProofOfInclusion


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
            root = MerkleTree.create_list(choice[1:])
            print(root.data)
        # option 2
        elif choice[0] == "2":
            if root is None or len(choice) != 2:
                break
            if MerkleTree.check_node(root, choice[1]) is None:
                break
            if choice[1] not in leaves:
                break
            print(ProofOfInclusion.create_proof_of_inclusion(choice[1], root))
        # option 3
        elif choice[0] == "3":
            if len(choice) < 5:
                break
            leaf = choice[1]
            root3 = choice[2]
            proof = choice[3:]
            for i in range(0, len(proof), 2):
                if proof[i] != "l" or proof[i] != "r":
                    loop = False
                    break
            if loop is False:
                break
            print(ProofOfInclusion.check_proof_of_inclusion(leaf, root3, proof))
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
            winningNumber, result = MerkleTree.check_for_zeros(int(choice[1]), root)
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
