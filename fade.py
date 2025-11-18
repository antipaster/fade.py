# fade.py (github.com/antipaster)
def _rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def gradient(text, start, end):
    out = ""
    ln = max(len(text), 1)
    for i, ch in enumerate(text):
        t = i / (ln - 1) if ln > 1 else 0
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        out += _rgb(r, g, b, ch)
    return out

def multi_gradient(text, colors):
    out = ""
    n = len(colors) - 1
    length = len(text)
    for idx, ch in enumerate(text):
        t = idx / max(length - 1, 1)
        section = min(int(t * n), n - 1)
        local_t = (t * n) - section
        c1 = colors[section]
        c2 = colors[section + 1]
        r = int(c1[0] + (c2[0] - c1[0]) * local_t)
        g = int(c1[1] + (c2[1] - c1[1]) * local_t)
        b = int(c1[2] + (c2[2] - c1[2]) * local_t)
        out += _rgb(r, g, b, ch)
    return out


#onecolor
def purplepink(text): return gradient(text, (150, 50, 255), (255, 100, 200))
def water(text): return gradient(text, (0, 120, 255), (0, 220, 200))
def fire(text): return gradient(text, (255, 60, 0), (255, 255, 0))
def green(text): return gradient(text, (0, 200, 50), (0, 255, 180))
def blue(text): return gradient(text, (0, 80, 255), (100, 200, 255))
def gold(text): return gradient(text, (255, 215, 0), (255, 255, 150))
def silver(text): return gradient(text, (180, 180, 180), (240, 240, 240))
def neon(text): return gradient(text, (0, 255, 150), (150, 0, 255))
def pink(text): return gradient(text, (255, 100, 150), (255, 180, 230))
def toxic(text): return gradient(text, (50, 255, 0), (200, 255, 0))
def lava(text): return gradient(text, (255, 0, 0), (255, 140, 0))
def ice(text): return gradient(text, (100, 200, 255), (200, 240, 255))
def forest(text): return gradient(text, (0, 100, 0), (50, 255, 50))
def sunset(text): return gradient(text, (255, 94, 58), (255, 195, 113))
def doom(text): return gradient(text, (255, 0, 0), (100, 0, 0))
def cyberpunk(text): return gradient(text, (0, 255, 255), (255, 0, 255))
def shadow(text): return gradient(text, (40, 40, 40), (200, 200, 200))
def snow(text): return gradient(text, (200, 230, 255), (255, 255, 255))

# multicolor
def rainbow(text):
    return multi_gradient(text, [
        (255, 0, 0),
        (255, 165, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 127, 255),
        (0, 0, 255),
        (139, 0, 255)
    ])

def galaxy(text):
    return multi_gradient(text, [
        (20, 0, 40),
        (60, 0, 80),
        (120, 0, 200),
        (255, 0, 255),
        (0, 120, 255),
    ])

def aurora(text):
    return multi_gradient(text, [
        (0, 255, 150),
        (0, 200, 255),
        (100, 0, 255),
        (255, 0, 200),
    ])

def candy(text):
    return multi_gradient(text, [
        (255, 150, 180),
        (255, 80, 120),
        (255, 200, 230),
    ])

def heatmap(text):
    return multi_gradient(text, [
        (0, 0, 255),
        (0, 255, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 0, 0),
    ])

def matrix(text):
    return multi_gradient(text, [
        (0, 255, 0),
        (0, 180, 0),
        (0, 120, 0),
        (0, 255, 150),
    ])

def pride(text):
    return multi_gradient(text, [
        (228, 3, 3),    # red
        (255, 140, 0),  # orange
        (255, 237, 0),  # yellow
        (0, 128, 38),   # green
        (0, 77, 255),   # blue
        (117, 7, 135),  # purple
    ])


def gradient_progress(percent, length=30, style="water"):
    percent = max(0, min(percent, 100))
    filled = int((percent / 100) * length)

    bar_text = "█" * filled + "░" * (length - filled)

    if style in globals():
        fn = globals()[style]
    else:
        fn = water

    return fn(bar_text) + f" {percent:.1f}%"
