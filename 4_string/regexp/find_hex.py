import re

text = """ 
        #f00: Красный цвет. 3
        #ff00ff: Произвольный цвет. 6 
        #ffff00ff: Произвольный цвет. 8
"""

hex_color = re.findall(r"#([A-Fa-f0-9]{3,8})", text)

print(hex_color)