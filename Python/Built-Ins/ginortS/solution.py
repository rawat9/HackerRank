from string import ascii_letters

s = input()
print(*sorted(s, key=(ascii_letters + "1357902468").index), sep="")
