wall = 0.0     # wall at x = 0
m1 = 1.0       # small block mass
m2 = 10000.0   # big block mass
v1 = 0.0       # small block
v2 = -1.0      # big block (moving toward small block)
x1 = 1.0       # start position of small block
x2 = 3.0       # start position of big block
collisions = 0

def collide_wall(v):
    return -v

def collide_blocks(v1, v2):
    v1_prime = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_prime = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_prime, v2_prime

while True:
    # Time until small block hits wall
    if v1 < 0:
        t_wall = (wall - x1) / v1
    else:
        t_wall = float('inf')

    # Time until blocks collide
    if v1 > v2:
        t_blocks = (x2 - x1) / (v1 - v2)
    else:
        t_blocks = float('inf')

    # Pick the sooner collision
    t_next = min(t_wall, t_blocks)
    if t_next == float('inf'):
        break 

    x1 += v1 * t_next
    x2 += v2 * t_next

    if t_next == t_wall:
        v1 = collide_wall(v1)
        collisions += 1
    else:
        v1, v2 = collide_blocks(v1, v2)
        collisions += 1

print(collisions)
