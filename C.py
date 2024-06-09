box, ray = input().split("\n");
X1, X2, Y1, Y2 = map(int, box.split(" "))
XS, YS, XR, YR = map(int, ray.split(" "))

dx, dy = XR - XS, YR - YS

if (dx != 0):
    tx1 = (X1 - XS) / dx
    tx2 = (X2 - XS) / dx
else:
    tx1 = tx2 = float("inf")

if (dy != 0):
    ty1 = (Y1 - YS) / dy
    ty2 = (Y2 - YS) / dy
else:
    ty1 = ty2 = float("inf")
    
tx = min(tx1 if tx1 > 0 else float("inf"), tx2 if tx2 > 0 else float("inf"))
ty = min(ty1 if ty1 > 0 else float("inf"), ty2 if ty2 > 0 else float("inf"))

if tx < ty:
    if tx == tx1:
        print("left")
    else:
        print("right")
elif ty < tx:
    if ty == ty1:
        print("bottom")
    else:
        print("top")
        
else:
    if tx == tx1 and ty == ty1:
        print("bottom-left")
    elif tx == tx1 and ty == ty2:
        print("top-left")
    elif tx == tx2 and ty == ty1:
        print("bottom-right")
    else:
        print("top-right")