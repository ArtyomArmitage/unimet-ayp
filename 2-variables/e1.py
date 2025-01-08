import typing

volumen_reservorio: float = 4.445e8
lluvia: float = 5e6

lluvia=lluvia*0.9
volumen_reservorio+=lluvia
volumen_reservorio=volumen_reservorio*(1+0.05)
volumen_reservorio=volumen_reservorio*0.98
volumen_reservorio-=2.5e5
print(volumen_reservorio)
