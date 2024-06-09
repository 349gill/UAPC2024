N = int(input())
elements = ['keys', 'phone','wallet']
for i in range(N):
    obj = str(input())
    if obj in elements:
        elements.remove(obj)
if elements == []:
    print("ready")
else:
    for i in elements:
        print(f"{i}\n")