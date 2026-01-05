map_data = """\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaJJJJaaCCCaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaJJJ8JJCCCaaaaaaaaaaaaaaaaa
aaaaaaaaaJJJaaJaaJaaCCCaaaaaaaaaaaaaaaaa
aaaaaaaaaJAJJJ8aaJaaa4aaaaaaaaaaaaaaaaaa
aaaaaaaaaJJJaaaaaJJJJJJaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaJJ5a5Jaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaJJJaaJJ6C6Jaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaJEJJJJJ5a5Jaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaJJJaaJJJJJJaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
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

VALID = set("EACJmnopqr056789")

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

for row in new_grid:
    print("".join(row))
