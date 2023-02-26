'''
start 20220303
end
'''

import sys

def check(a):
    if ord(a) in range(97,123) or ord(a) in range(65,91):
        return True
    else:
        return False

while True:
    str = sys.stdin.readline()
    if str[:-1] == '.':
        break
    st = []
    test = ['(',')','[',']']
    s = True
    for i in range(len(str)):
        if str[i] == '(':
            st.append(0)
        elif str[i] == '[':
            st.append(1)
        elif str[i] == ')':
            try:
                tmp = st.pop()
                if tmp == 1:
                    s = False
                    break
            except:
                s = False
                break
        elif str[i] == ']':
            try:
                tmp = st.pop()
                if tmp == 0:
                    s = False
                    break
            except:
                s = False
                break
    if s == True and st == []:
        print('yes')
    else:
        print('no')