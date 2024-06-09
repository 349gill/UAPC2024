# I think this one times out. Unverified answer, as I couldn't run tests on this.

n, m = map(int, input().split())
A = input().strip()
B = input().strip()

len_A = len(A)
len_B = len(B)
    
for start in range(len_A):
    for end in range(start + 1, len_A + 1):
        substring = A[start:end]
        repeated_string = substring * (len_B // len(substring))
        if repeated_string == B:
            print("yes")
print("no")
