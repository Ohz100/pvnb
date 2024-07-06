# Longitud
cm = 0.01
mm = 0.001
inch = 0.0254
ft = 12*inch

# Volumen
litre = 0.001
gal = 231*inch**3

# Masa
lbm = 0.45359237

# Fuerza
kgf = 9.80665
lb = 0.45359237*9.80665

# Presión
kPa = 1000
MPa = 1000000
bar = 100000
psi = lb/inch**2
atm = 101325

# Ángulo
deg = math.pi/180

def degF_degC(x):
    return (x - 32)*5/9

def degC_degF(x):
    return 9*x/5 + 32

def fraction(x, n = 16):
    if x < 0:
        negative = True
        x = -x
    else:
        negative = False
    a = int(x)
    b = round(n*(x - a))
    if b == 0:
        return str(a)
    elif b == n:
        return str(a + 1)
    else:
        s = math.gcd(b, n)
        if a == 0:
            y = str(int(b/s)) + '/' +  str(int(n/s))
        else:
            y = str(a) + ' ' + str(int(b/s)) + '/' +  str(int(n/s))
    if negative:
        return '-' +y
    else:
        return y

def res(x):
    y = x/inch
    print(str(x/mm) + ' mm')
    print(str(y) + ' in')
    print(fraction(y) + ' in')

def vol_horizontal_hemi(z, r_h, r_s, L, cb = 0):
    L_a = L - 2*cb/r_s**2*(r_h**2 - 1/3*cb**2)
    if z < -r_h:
        v_h = 0
    elif z < r_h:
        v_h = math.pi * (r_h + z)**2 * (2 * r_h - z) / 3
    else:
        v_h = 4 * math.pi * r_h**3 / 3
    if z < -r_s:
        v_s = 0
    elif z < r_s:
        v_s = L_a * (r_s**2 * math.asin(z / r_s) + z * math.sqrt(r_s**2 - z**2) + math.pi * r_s**2 / 2)
    else:
        v_s = L_a * math.pi * r_s**2
    return v_h + v_s

def vol_horizontal_ellip(z, r_h, r_s, L, sf):
    if z < -r_h:
        v_h = 0
    elif z < r_h:
        v_h = math.pi * (r_h + z)**2 * (2 * r_h - z) / 6
    else:
        v_h = 4 * math.pi * r_h**3 / 6
    if z < -r_s:
        v_s = 0
    elif z < r_s:
        v_s = (L + 2 * sf) * (r_s**2 * math.asin(z / r_s) + z * math.sqrt(r_s**2 - z**2) + math.pi * r_s**2 / 2)
    else:
        v_s = (L + 2 * sf) * math.pi * r_h**2
    return v_h + v_s

def z_horizontal_hemi(v, r_h, r_s, L, cb = 0):
    def f(x):
        return vol_horizontal_hemi(x, r_h, r_s, L, cb) - v
    return fsolve(f, 0)[0]

def z_horizontal_ellip(v, r_h, r_s, L, sf):
    def f(x):
        return vol_horizontal_ellip(x, r_h, r_s, L, sf) - v
    return fsolve(f, 0)[0]

# fin