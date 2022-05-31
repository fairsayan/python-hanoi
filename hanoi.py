state = {'A':[3, 2, 1], 'B':[], 'C':[]}
pegNames = set(state.keys())

def getSupportPeg(source, dest):
    other = pegNames - { source, dest }
    return other.pop()

def move(state, source, dest, numOfDiscs):
    if numOfDiscs == 1:
        disc = state[source].pop()
        print('{}: {} -> {}'.format(disc, source, dest))
        state[dest].append(disc)
    else:
        suppPeg = getSupportPeg(source, dest)
        move(state, source, suppPeg, numOfDiscs - 1)
        move(state, source, dest, 1)
        move(state, suppPeg, dest, numOfDiscs - 1)

move(state, 'A', 'C', 3)