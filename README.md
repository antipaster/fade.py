# fade.py

![Windows Terminal 5](/resources/WindowsTerminal_r0b4oQOSe8.png)

example usage:
```python
import fade

print(fade.rainbow("HELLO WORLD"))
print(fade.fire("ALERT"))
print(fade.gradient("CUSTOM", (255, 0, 0), (0, 255, 0)))
print(fade.gradient_progress(72, style="neon"))
```

One-stop styles:
- `purplepink`, `water`, `fire`, `green`, `blue`, `gold`, `silver`, `neon`, `pink`, `toxic`, `lava`, `ice`, `forest`, `sunset`, `doom`, `cyberpunk`, `shadow`, `snow`

Multi-stop styles:

- `rainbow`, `galaxy`, `aurora`, `candy`, `heatmap`, `matrix`, `pride`
