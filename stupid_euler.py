import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# initial values and constants

G = 6.67*10**(-11)
H0 = 0.0735    # this has h=0.72 and units of inverse Gyr
m2 = 1.*10**(-40)

a = 1.

adot = H0

phi = 1.
phidot = np.sqrt(1.4*(0.375/(np.pi*G))*H0**2 - m2*phi**2)

dt = 0.00001


# stupid euler routines

def D_phidot(a, adot, f, fdot):
    return fdot + (3*(adot/a)*fdot + m2*f)*dt

def D_phi(f, fdot):
    return f - fdot*dt

def D_a(a, adot):
    return a - adot*dt

def Friedman(a, f, fdot):
    return np.sqrt((0.3*H0**2)/a + ((4./3.)*np.pi*G)*(fdot**2 + m2*f**2))

# have at it

k = 1
alist = [a]
adotl = [adot]
phil = [phi]
phidotl = [phidot]
t = 0.
tlist = [0.]

while a > 0.00001 and k < 10000000:

    fdot_old = phidot
    phidot = D_phidot(a, adot, phi, phidot)
    phi = D_phi(phi, fdot_old)

    a = D_a(a, adot)

    adot = Friedman(a, phi, phidot)

    t -= dt

    tlist.append(t)
    alist.append(a)
#    adotl.append(adot)
#    phil.append(phi)
#    phidotl.append(phidot)

    k += 1


# Make the plots

tar = np.array(tlist)
arr = np.array(alist)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tar, arr)

fig.savefig("/home/kilian/public_html/quentin/euler.png")
