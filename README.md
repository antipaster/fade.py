# fade.py

![Windows Terminal 1](/resources/WindowsTerminal_4GzDCG9Iba.png)
![Windows Terminal 2](/resources/WindowsTerminal_j04T602Qqq.png)
![Windows Terminal 3](/resources/WindowsTerminal_K0XUjbJkh6.png)
![Windows Terminal 4](/resources/WindowsTerminal_KA4abd0TU2.png)
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
