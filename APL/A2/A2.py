from sys import argv
import os


import numpy as n
from numpy.core.records import array

'The Below Function makes a row, for the Conductance Matrix. Each row is a Dict, with Variables as its Key and the Values are initialized to 0'


def rowMaker(variables):
    temp = dict()
    for i in variables:
        temp[i] = 0
    return temp


'Function For Printing the Final Output'


def printer(variables, final):
    k = 0
    for i in list(final):
        temp = list(variables[k])
        if temp[0] == 'V':
            temp.remove('V')
            print('Voltage at node {} is {}'.format(''.join(temp), i))
        if temp[0] == 'I':
            print(
                'Current flowing through Voltage Source {} is {}'.format(temp[1], i))
        k = k+1


'It validates basic format rules, such as presence of .circuit and .end in the netlist'


def formatChecker(lines, Circuit, End):
    start = 0
    end = 0
    k = False
    m = False
    for line in lines:
        temp = line.split()
        if Circuit in temp:
            k = True
        if End in temp:
            m = True
        if k and m:
            break
    if (k and m) == False:
        if k == False:
            print('Invalid Circuit Def: Include .ciruit')
            exit()
        if m == False:
            print('Invalid Circuit Def: Include .end')
            exit()
    for line in lines:
        if Circuit in line:
            start = lines.index(line)
        if End in line:
            end = lines.index(line)
    if start >= end:
        print('Invalid Circuit Def')
        exit()
    return start, end


'Checks if the Circuit is AC or DC. Returns a Boolean'


def acChecker(lines):
    temp = lines[-1].split()
    if temp[0] == '.ac':
        return True
    else:
        return False


'It removes comments, extra lines, etc'


def refineLine(lines, end, start, Circuit, End):
    realLine = []
    tempLines = []
    for i in range(end, start, -1):
        tempLines = [lines[i]] + tempLines
    for i in tempLines:
        i = i.strip('\n')
        if Circuit in i or End in i:
            continue
        else:
            temp = i.split('#')
            realLine = realLine + [temp[0]]
    for i in realLine:
        if i == '\n':
            realLine.remove('\n')
    return realLine


'Each line of the netlist is split, for extracting the variables, Value of the Elements, Nodes. It returns '


def splitLine(realLine):
    par = []
    for i in realLine:
        par = par + [i.split()]
    for i in par:
        if i[3] == 'ac':
            i[4] = float(i[4])
            i.remove('ac')
        else:
            i[3] = float(i[3])
    return par


'Genereates a variable List'


def genVariables(par):
    variables = []
    for i in par:
        if i[0][0] == 'V':
            variables = variables + ['I{}'.format(i[0][1])]
        if 'V{}'.format(i[1]) not in variables and i[1] != 'GND':
            variables = variables + ['V{}'.format(i[1])]
        if 'V{}'.format(i[2]) not in variables and i[2] != 'GND':
            variables = variables + ['V{}'.format(i[2])]
    variables = variables + ['b']
    return variables


'Finds all the Nodes and stores them as a list'


def genNodes(par):
    nodes = []
    for i in par:
        if i[1] not in nodes:
            nodes = nodes + [i[1]]
        if i[2] not in nodes:
            nodes = nodes + [i[2]]
    return nodes


'Creates a List of Dict. Each Dict corresponds to a Nodal Eq and, has the variables as its key, and the value corresponds to the coeffecient of the Variable in each Nodal Eq'


def circuitSolver(nodes, variables, par, w):
    mMatrix1 = []
    for i in nodes:
        if i == 'GND':
            continue
        temp = rowMaker(variables)
        temp2 = rowMaker(variables)
        for j in par:
            if i in j:
                if j[0][0] == 'V':
                    if 'GND' in j:
                        if j[2] == 'GND':
                            temp2['V{}'.format(i)] = 1
                            temp2['b'] = j[3]
                            mMatrix1 = mMatrix1 + [temp2]
                        if j[1] == 'GND':
                            temp2['V{}'.format(i)] = 1
                            temp2['b'] = j[3]*(-1)
                            mMatrix1 = mMatrix1 + [temp2]
                    else:
                        if i == j[1]:
                            temp2['V{}'.format(i)] = 1
                            temp2['V{}'.format(j[2])] = -1
                            temp2['b'] = j[3]
                            mMatrix1 = mMatrix1 + [temp2]
                        if i != j[1]:
                            temp2['V{}'.format(i)] = -1
                            temp2['V{}'.format(j[2])] = 1
                            temp2['b'] = j[3]
                            mMatrix1 = mMatrix1 + [temp2]
                if j[0][0] == 'V':
                    if i == j[1]:
                        temp['I{}'.format(j[0][1])] = -1
                    if i == j[2]:
                        temp['I{}'.format(j[0][1])] = 1
                if j[0][0] == 'R':
                    if i == j[1]:
                        temp['V{}'.format(i)] = temp['V{}'.format(i)] + 1/j[3]
                        if j[2] == 'GND':
                            continue
                        temp['V{}'.format(j[2])] = temp['V{}'.format(
                            j[2])] - 1/j[3]
                    if i == j[2]:
                        temp['V{}'.format(i)] = temp['V{}'.format(i)] + 1/j[3]
                        if j[1] == 'GND':
                            continue
                        temp['V{}'.format(j[1])] = temp['V{}'.format(
                            j[1])] - 1/j[3]
                if j[0][0] == 'C':
                    if i == j[1]:
                        temp['V{}'.format(i)] = temp['V{}'.format(
                            i)] + complex(0, j[3]*w)
                        if j[2] == 'GND':
                            continue
                        temp['V{}'.format(j[2])] = temp['V{}'.format(
                            j[2])] - complex(0, j[3]*w)
                    if i == j[2]:
                        temp['V{}'.format(i)] = temp['V{}'.format(
                            i)] + complex(0, j[3]*w)
                        if j[1] == 'GND':
                            continue
                        temp['V{}'.format(j[1])] = temp['V{}'.format(
                            j[1])] - complex(0, j[3]*w)
                if j[0][0] == 'L':
                    if i == j[1]:
                        temp['V{}'.format(i)] = temp['V{}'.format(
                            i)] + 1/complex(0, j[3]*w)
                        if j[2] == 'GND':
                            continue
                        temp['V{}'.format(j[2])] = temp['V{}'.format(
                            j[2])] - 1/complex(0, j[3]*w)
                    if i == j[2]:
                        temp['V{}'.format(i)] = temp['V{}'.format(
                            i)] + 1/complex(0, j[3]*w)
                        if j[1] == 'GND':
                            continue
                        temp['V{}'.format(j[1])] = temp['V{}'.format(
                            j[1])] - 1/complex(0, j[3]*w)

        mMatrix1 = mMatrix1 + [temp]
    return mMatrix1


'Generates the Conductance Matrix'


def mMatrixGenerator(mMatrix1):
    realM = []
    for i in mMatrix1:
        realM = realM + [list(i.values())]
    return realM


'Generates the Source Matrix'


def bMatrixGenerator(realM):
    realb = []
    for i in realM:
        realb = realb + [i[-1]]
        i.pop(-1)
    return realb


'Gets the Frequency of the Voltage Source'


def getFreq(lines):
    i = lines[-1].split()
    w = float(i[2])
    return w


print('EE19B018 CIRCUIT SOLVER'.center(150))
print('GuidLines')
print('The Netlist File has to be given as an argument in the Command Line')
print('What the Circuit Solver Can do?')
print('1)It can solve for Current through Voltage Sources and Nodal Voltages for DC')
print('2)For AC, the program can give only the Phasors. The real forced response can be got with the help of the Phasors(Output), which the program cannot do.')
print('3) It can handle multiple number of voltage sources, but cannot handle multiple frequencies')
print('4) It can handle ONLY circuits with the following elements - Resistors, Capacitors, Voltage Sources and Inductors\n')
print('Netlist Format to be passed')
print('1)The Ground Node should be represented as ONLY "GND"')
print('2)No restrictions for other Nodes are applied. They can be named as the user likes')
print('3)Amplitude of V must be given, not peak-peak')
print('4)Phase for the Voltage should not be mentioned')
print('5) The frequency in the Netlist must be the Angular Frequency\n')
print('Output =')


'Checks if the Input Netlist is in proper Format'
if len(argv) < 2:
    print('Input File Required')
    exit()
if os.path.exists(argv[1]) == False:
    print('The File does not exist in the computer, or check the file path')
    exit()

Circuit = '.circuit'
End = '.end'
f = open(argv[1])  # Opening the file
lines = f.readlines()  # Reading the lines from the Input File

"Main Function"
start, end = formatChecker(lines, Circuit, End)
isAC = acChecker(lines)

if not isAC:
    w = 1e-22
if isAC:
    w = getFreq(lines)


realLine = refineLine(lines, end, start, Circuit, End)
par = splitLine(realLine)
variables = genVariables(par)
nodes = genNodes(par)
mMatrix1 = circuitSolver(nodes, variables, par, w)
realM = mMatrixGenerator(mMatrix1)
realb = [bMatrixGenerator(realM)]
final = n.linalg.solve(n.array(realM), n.transpose(n.array(realb)))
printer(variables, final)
print('')
print('Incase the expected output doesnt turn up, refer to the guidlines\n')
