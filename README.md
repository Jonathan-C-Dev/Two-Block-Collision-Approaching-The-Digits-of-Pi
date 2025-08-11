# π from Colliding Blocks

This program simulates a fascinating physics problem where the number of perfectly elastic collisions between two blocks and a wall encodes the digits of π.  

When the heavy block's mass is **100^(n−1)** times the small block’s mass, the **total number of collisions** (block-block + block-wall) equals the first **n** digits of π.

---

## How It Works

We have:

- **Wall** fixed at position `x = 0`
- **Small block** of mass `m₁`
- **Large block** of mass `m₂` moving toward the small block

Collisions are **perfectly elastic**:
- **Small block ↔ Wall** → Velocity simply reverses sign.
- **Block ↔ Block** → Velocities are updated from conservation laws.

Surprisingly, for certain mass ratios, the number of collisions matches digits of π.  
This result comes purely from Newtonian mechanics — no trigonometry or infinite series involved.

---

## Physics Derivation

For a perfectly elastic 1D collision between masses `m₁` and `m₂`:

**1. Conservation of momentum**
```
m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'
```

**2. Relative velocity relationship for elastic collisions**
```
v₁ − v₂ = −(v₁' − v₂')
```
This states that the velocity of approach before the collision equals the velocity of separation afterward (with opposite sign).

---

### Solving for v₁′ and v₂′

From the relative velocity equation:
```
v₁ − v₂ = −v₁' + v₂'
```
Rearrange:
```
v₂' = v₁ − v₂ + v₁'
```

Substitute into the momentum equation:
```
m₁v₁ + m₂v₂ = m₁v₁' + m₂(v₁ − v₂ + v₁')
```
```
m₁v₁ + m₂v₂ = m₁v₁' + m₂v₁ − m₂v₂ + m₂v₁'
```

Group v₁′ terms:
```
m₁v₁ + m₂v₂ − m₂v₁ + m₂v₂ = (m₁ + m₂)v₁'
```

Thus:
```
v₁' = ((m₁ − m₂)v₁ + 2m₂v₂) / (m₁ + m₂)
```

Using the relative velocity relation again:
```
v₂' = v₁ − v₂ + v₁' = ((m₂ − m₁)v₂ + 2m₁v₁) / (m₁ + m₂)
```

---

## The Connection to π

If we choose:
```
m₂ = 100^(n-1) × m₁
```
then:
- `n = 1` → π ≈ 3 collisions
- `n = 2` → π ≈ 3.1 collisions
- `n = 3` → π ≈ 3.14 collisions
- and so on.

The simulation counts **total collisions** (both with the wall and between blocks).  
As `n` increases, the count’s leading digits converge to π.

---

## Example Results

| n (Digits) | m₁   | m₂           | Collisions | Approximation |
|------------|------|--------------|------------|---------------|
| 1          | 1    | 1            | 3          | 3             |
| 2          | 1    | 100          | 31         | 3.1           |
| 3          | 1    | 10,000       | 314        | 3.14          |
| 4          | 1    | 1,000,000    | 3,141      | 3.141         |
| 5          | 1    | 100,000,000  | 31,415     | 3.1415        |
| 6          | 1    | 10¹⁰         | 314,159    | 3.14159       |

---

## How to Run

1. Save the simulation code as `main.py`.
2. Run:
   ```bash
   python main.py
   ```
3. Change `m2` to `100 ** (n - 1)` for `n` digits of π.

---

## References

- **Video:** [3Blue1Brown — Pi and the Blocks](https://youtu.be/6dTyOl1fmDo?si=GdI8XJKj-SU6Vx2b)
- Classical mechanics — perfectly elastic collisions
- Conservation of momentum + relative velocity derivation

---
