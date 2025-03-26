import time

password = input("Enter Password: ")
start = time.time()
chars = "ABCDEFGHIJKLMNabcdeOPQRSTUVWfghijklm*()_+|}{:?><nopqrstuXYZvwxyz!@#$%^&"
guess = []
for val in range(1, 51):
    a = [i for i in chars]
    for y in range(val):
        a = [x+i for i in chars for x in a]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = str(end - start)

print("Your password: " + password)
print("Time taken: " + clock)
