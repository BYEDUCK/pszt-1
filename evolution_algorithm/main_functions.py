import sys
import random


# Mutation of ONLY one number
def mutate(subject, sigma):
    x = random.randint(0, len(subject) - 2)
    if type(subject[0]) == int or type(subject[0]) == float:
        subject[x] = random.gauss(subject[x], sigma)
    elif type(subject[0]) == list:
        y = random.randint(0, len(subject[x]) - 1)
        subject[x][y] = random.gauss(subject[x][y], sigma)
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Mutation - unknown subject element')
    return subject


def crossover(base, subject):
    pom = random.randint(0, len(base) - 1)
    pom_pair = base[pom]
    if type(subject[0]) == int or type(subject[0]) == float:
        for i in range(len(subject) - 1):
            subject[i] = random.uniform(subject[i], pom_pair[i])
    elif type(subject[0]) == list:
        pom_lists = [[0 for x in range(len(subject[0]))] for y in range(len(subject))]
        for i in range(len(subject) - 1):
            for j in range(len(subject[i])):
                pom_lists[i][j] = (random.uniform(subject[i][j], pom_pair[i][j]))
        subject = pom_lists
    # TODO Czy sopdziewamy się czegoś innego niż int/float lub list???
    else:
        sys.exit('Crossover - unknown subject element')
    return subject


def replacing(base, insert):
    pom_list = base + insert
    pom_list.sort(key=lambda pom: pom[len(base[0]) - 1])
    # return only best numbers
    return pom_list[:len(base)]
