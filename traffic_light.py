from itertool import cycle
import time 

lights = [
    ('Green', 2),
    ('Yellow', 0.9),
    ('Red', 2)
]

colors = cycle(lights)
while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)
