# 10. Pattern Printing: Use nested loops toprint the following pattern:
#
# *
# **
# ***
# ****
# *****

s = 0
while s < 6:
    for i in range(6):
        print('*' * i)
        s += 1

