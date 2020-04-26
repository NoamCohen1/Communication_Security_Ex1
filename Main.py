import sys
import Node
import MerkleTree
import ProofOfInclusion


def choose_main():
    root = None
    loop = True
    while loop:
        choice = input().split(" ")
        if len(choice) == 0:
            break
        if choice[0] == "1":
            if len(choice) < 2:
                break
            if choice[1] == "":
                break
            root = MerkleTree.create_list(choice[1:])
            print(root.data)
        elif choice[0] == "2":
            if root is None or len(choice) != 2:
                break
            if MerkleTree.check_node(root, choice[1]) is None:
                break
            print(ProofOfInclusion.create_proof_of_inclusion(choice[1], root))
        elif choice[0] == "3":
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
        elif choice[0] == "4":
            if root is None or len(choice) != 2:
                break
            if choice[1].startswith('-'):
                if choice[1][1:].isdigit() is False:
                    loop = False
            if loop is False:
                break
            if choice[1].isdigit() is False:
                break
            winningNumber, result = MerkleTree.check_for_zeros(int(choice[1]), root)
            print(str(winningNumber) + " " + str(result))
        elif choice[0] == "5":
            break
        else:
            break
    return


if __name__ == "__main__":
    choose_main()
    #root = MerkleTree.create_list(sys.argv)
    #print(root.data)
    #ans = ProofOfInclusion.create_proof_of_inclusion("b", root)
    #print(ans)
    #print(ProofOfInclusion.check_proof_of_inclusion("b", root.data, ans.split(" ")))
    #winningNumber, result = MerkleTree.check_for_zeros(2, root)
    #print(str(winningNumber) + " " + str(result))
