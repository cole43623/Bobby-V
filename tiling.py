map_data = """\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaJAJaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaC0Taaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaT0Caaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaJ69Caaaaaaaaaaaaaa
aaaaaaaaaaaaaaJJJJJJJJJa5aaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJpqqqnJJ009aaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJm+J-rqqqoaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJmJJJJCCCCaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJmT08aaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJmJ55aaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaEJTT99C-+aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaJJ0085aaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaa69aaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""

# =========================
# PREPARAZIONE MAPPA
# =========================

grid = [list(row) for row in map_data.splitlines()]
ROWS = len(grid)
COLS = len(grid[0])

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS
# =========================
# PARAMETRI
# =========================

VALID = set("EACJmnopqr6789+-*/()[]{}")

RULES = {
    frozenset(["down", "up", "right", "left"]): "b",
    frozenset(["down", "up"]): "c",
    frozenset(["down"]): "d",
    frozenset(["left", "down"]): "e",
    frozenset(["left", "up"]): "f",
    frozenset(["left"]): "g",
    frozenset(["right", "down"]): "h",
    frozenset(["right", "left"]): "i",
    frozenset(["right", "up"]): "j",
    frozenset(["right"]): "k",
    frozenset(["up"]): "l",
}
# =========================
# ELABORAZIONE
# =========================

new_grid = [row[:] for row in grid]

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] != "a":
            continue

        neighbors = set()

        if in_bounds(r-1, c) and grid[r-1][c] in VALID:
            neighbors.add("up")
        if in_bounds(r+1, c) and grid[r+1][c] in VALID:
            neighbors.add("down")
        if in_bounds(r, c-1) and grid[r][c-1] in VALID:
            neighbors.add("left")
        if in_bounds(r, c+1) and grid[r][c+1] in VALID:
            neighbors.add("right")

        key = frozenset(neighbors)
        if key in RULES:
            new_grid[r][c] = RULES[key]
# =========================
# OUTPUT
# =========================



def conta_iniziali(riga):
    c = 0
    for x in riga:
        if x == 'a':
            c += 1
        else:
            break
    return c

def conta_finali(riga):
    c = 0
    for x in reversed(riga):
        if x == 'a':
            c += 1
        else:
            break
    return c

def bilancia_righe_colonne(matrice):
    a, b = 0, 0
    for riga in matrice:
        if (riga.count('a') == len(riga)):
            a += 1
        else:
            break
    for riga in matrice[::-1]:
        if (riga.count('a') == len(riga)):
            b += 1
        else:
            break
    c = abs(b-a)//2
    print(a,b,c)
    if b > a:
        for _ in range(c):
            matrice.pop()
            matrice.insert(0, ['a']*COLS)
    elif a > b:
        for _ in range(c):
            matrice.pop(0)
            matrice.append(['a']*COLS)

    x, y = 9999,9999
    for riga in matrice:
        x = min(x, conta_iniziali(riga))
        y = min(y, conta_finali(riga))
    z = abs(y-x)//2
    if y > x:
        for i in range(len(matrice)):
            matrice[i] = ["a"] * z + matrice[i][:COLS-z]
    elif x > y:
        for i in range(len(matrice)):
            matrice[i] = matrice[i][z:] + ["a"] * z
    return matrice



new_grid = bilancia_righe_colonne(new_grid)

for row in new_grid:
    print("".join(row))
