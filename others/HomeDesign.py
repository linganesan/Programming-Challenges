from pyevolve import G1DBinaryString, GSimpleGA, Mutators, Selectors, Consts

CONST_N = "00"
CONST_E = "01"
CONST_S = "10"
CONST_W = "11"

CONST_NS = "0"
CONST_EW = "1"
params = {"BR_NS": 5, "BR_EW": 4, "KT_NS": 4, "KT_EW": 3, "T_NS": 3, "T_EW": 2}


def eval_func(chromosome):
    return calculateArea(chromosome.getBinary())

def calculateArea (arg):
    # Divide the bit argument
    BR_1 = arg[:2]
    KT_1 = arg[2:4]
    T_1 = arg[4:6]

    BR_2 = arg[6:7]
    KT_2 = arg[7:8]
    T_2 = arg[8:9]

    result = predefineCheck(BR_1,KT_1,T_1)

    if result:
        Length_E_W = 5 + int(calRoomLength(BR_1, BR_2, 1, "BR")) + int(calRoomLength(KT_1, KT_2, 1, "KT")) + int(calRoomLength(T_1, T_2, 1, "T"))
        Length_N_S = 5 + int(calRoomLength(BR_1, BR_2, 0, "BR")) + int(calRoomLength(KT_1, KT_2, 0, "KT")) + int(calRoomLength(T_1, T_2, 0, "T"))

        Area = Length_E_W * Length_N_S
        print Area
        return Area
    else:
        return 100000
def calRoomLength (arg1, arg2, arg3, arg4):
    room = arg4

    if arg3 == 0:
        if arg1 == CONST_E or arg1 == CONST_W:
            return 0
        else:
            if arg2 == CONST_NS:
                return params.get(room+"_EW")
            else:
                return params.get(room+"_NS")
    else:
        if arg1 == CONST_N or arg1 == CONST_S:
            return 0
        else:
            if arg2 == CONST_NS:
                return params.get(room+"_NS")
            else:
                return params.get(room+"_EW")

def predefineCheck (arg1,arg2,arg3):
    if arg1 == arg2 and arg2 == arg3:
        return False
    elif arg1 == CONST_N and arg3 == CONST_S:
        return False
    elif arg1 == CONST_W and arg3 == CONST_E:
        return False
    elif arg1 == CONST_S and arg3 == CONST_N:
        return False
    elif arg1 == CONST_E and arg3 == CONST_W:
        return False
    elif arg1 == arg2:
        return False
    else:
        return True

if __name__ == "__main__":
    arg = "011001101"
    # Divide the bit argument
    BR_1 = arg[:2]
    KT_1 = arg[2:4]
    T_1 = arg[4:6]



    # Genome instance
    genome = G1DBinaryString.G1DBinaryString(9)

    #The evaluator function (objective function)
    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    # ga.selector.set(Selectors.GTournamentSelector)
    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setGenerations(70)

    # Do the evolution, with stats dump
    # frequency of 10 generations
    ga.evolve(freq_stats=20)

    # Best individual
    print ga.bestIndividual()
