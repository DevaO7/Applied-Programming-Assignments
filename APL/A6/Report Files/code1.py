# Intiatializing the Values
n = 100  # spatial grid size.
M = 5  # number of electrons injected per turn.
nk = 500  # number of turns to simulate.
u0 = 5  # threshold velocity.
p = 0.25  # probability that ionization will occur
Msig = 2  # Standard Deviation
xx = zeros(n*M)  # Electron Postion Vector
u = zeros(n*M)  # ELectron Velocity Vector
dx = zeros(n*M)  # DIsplacement in current turn
I = []  # Intensity of Emitted Light
X = []  # Electron Position
V = []  # DIsplacement in current turn dx
