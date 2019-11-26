import random

# Gene structure
#
# | Start | Index | Operator | Binding | Quantifying (x codons) | Stop |

# Trait indices

strength_index = [0, 0, 1]
size_index = [0, 0, 2]


strength_gene = [0, 1, 9, 0, 0, 1, 5, 7, 8, 5, 6, 7, 3, 4, 5, 6, 7, 8, 9, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 2, 3, 9, 8]
size_gene = [0, 1, 9, 0, 0, 2, 4, 5, 6, 8, 4, 4, 3, 6, 8, 9, 9, 9, 0, 8, 6, 3, 2, 3, 5, 6, 7, 8, 9, 8]

def random_code(length):
    code = []
    for j in range(length):
        code.append(random.randint(0, 9))
    return code


BASE_GENOME = random_code(10) + strength_gene + random_code(20) + size_gene


