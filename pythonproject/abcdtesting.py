def abcd(n):
    l = len(n)
    print("String Is =",n)
    print("Length Of String =",l)
    # for i in range(l):
    #     if n[i]=='a'or n[i]=='A':
    #         print("Total No of A =", n.count('a') + n.count('A'))
    #     elif n[i]=='b'or n[i]=='B':
    #         print("Total No of B =", n.count('b') + n.count('B'))
    #     elif n[i]=='c'or n[i]=='C':
    #         print("Total No of C =", n.count('c') + n.count('C'))
    #     elif n[i] == 'd' or n[i] == 'D':
    #         print("Total No of D =", n.count('d') + n.count('D'))
    #     elif n[i] == 'e' or n[i] == 'E':
    #         print("Total No of E =", n.count('e') + n.count('E'))
    #     elif n[i] == 'f' or n[i] == 'F':
    #         print("Total No of F =", n.count('f') + n.count('F'))
    #     elif n[i] == 'g' or n[i] == 'G':
    #         print("Total No of G =", n.count('g') + n.count('G'))
    #     elif n[i] == 'h' or n[i] == 'H':
    #         print("Total No of H =", n.count('h') + n.count('H'))
    #     elif n[i] == 'i' or n[i] == 'I':
    #         print("Total No of I =", n.count('i') + n.count('I'))
    #     elif n[i] == 'j' or n[i] == 'J':
    #         print("Total No of J =", n.count('j') + n.count('J'))
    #     elif n[i] == 'k' or n[i] == 'K':
    #         print("Total No of K =", n.count('k') + n.count('K'))
    #     elif n[i] == 'l' or n[i] == 'L':
    #         print("Total No of L =", n.count('l') + n.count('L'))
    #     elif n[i] == 'm' or n[i] == 'M':
    #         print("Total No of M =", n.count('m') + n.count('M'))
    #     elif n[i] == 'n' or n[i] == 'N':
    #         print("Total No of N =", n.count('n') + n.count('N'))
    #     elif n[i] == 'o' or n[i] == 'O':
    #         print("Total No of O =", n.count('o') + n.count('O'))
    #     elif n[i] == 'p' or n[i] == 'P':
    #         print("Total No of P =", n.count('p') + n.count('P'))
    #     elif n[i] == 'q' or n[i] == 'Q':
    #         print("Total No of Q =", n.count('q') + n.count('Q'))
    #     elif n[i] == 'r' or n[i] == 'R':
    #         print("Total No of R =", n.count('r') + n.count('R'))
    #     elif n[i] == 's' or n[i] == 'S':
    #         print("Total No of S =", n.count('s') + n.count('S'))
    #     elif n[i] == 't' or n[i] == 'T':
    #         print("Total No of T =", n.count('t') + n.count('T'))
    #     elif n[i] == 'u' or n[i] == 'U':
    #         print("Total No of U =", n.count('u') + n.count('U'))
    #     elif n[i] == 'v' or n[i] == 'V':
    #         print("Total No of V =", n.count('v') + n.count('V'))
    #     elif n[i] == 'w' or n[i] == 'W':
    #         print("Total No of W =", n.count('w') + n.count('W'))
    #     elif n[i] == 'x' or n[i] == 'X':
    #         print("Total No of X =", n.count('x') + n.count('X'))
    #     elif n[i] == 'y' or n[i] == 'Y':
    #         print("Total No of Y =", n.count('y') + n.count('Y'))
    #     elif n[i] == 'z' or n[i] == 'Z':
    #         print("Total No of Z =", n.count('z') + n.count('Z'))
print("Enter Your String")
n = str(input())
abcd(n)
print("Total No of A =", n.count('a') + n.count('A'))
print("Total No of B =", n.count('b') + n.count('B'))
print("Total No of C =", n.count('c') + n.count('C'))
print("Total No of D =", n.count('d') + n.count('D'))
print("Total No of E =", n.count('e') + n.count('E'))
print("Total No of F =", n.count('f') + n.count('F'))
print("Total No of G =", n.count('g') + n.count('G'))
print("Total No of H =", n.count('h') + n.count('H'))
print("Total No of I =", n.count('i') + n.count('I'))
print("Total No of J =", n.count('j') + n.count('J'))
print("Total No of K =", n.count('k') + n.count('K'))
print("Total No of L =", n.count('l') + n.count('L'))
print("Total No of M =", n.count('m') + n.count('M'))
print("Total No of N =", n.count('n') + n.count('N'))
print("Total No of O =", n.count('o') + n.count('O'))
print("Total No of P =", n.count('p') + n.count('P'))
print("Total No of Q =", n.count('q') + n.count('Q'))
print("Total No of R =", n.count('r') + n.count('R'))
print("Total No of S =", n.count('s') + n.count('S'))
print("Total No of T =", n.count('t') + n.count('T'))
print("Total No of U =", n.count('u') + n.count('U'))
print("Total No of V =", n.count('v') + n.count('V'))
print("Total No of W =", n.count('w') + n.count('W'))
print("Total No of X =", n.count('x') + n.count('X'))
print("Total No of Y =", n.count('y') + n.count('Y'))
print("Total No of Z =", n.count('z') + n.count('Z'))


# def abcd(st):
#     z= sorted(st)
#     print(z)
#     for i in range(1,len(st)+1):
#         c1 = 'a'
#         c2 = 'A'
#         for j in range(26):
#             if z[i-1]==c1 or z[i-1]==c2:
#                 print(st.count(c1)+st.count(c2))
#                 if z[i]==c1 or z[i]==c2:
#                     break
#             c1=chr(ord(c1)+1)
#             c2 = chr(ord(c2) + 1)
# st=str(input())
# abcd(st)



