text = list(input())
open_scopes = []
for i in range(len(text)):
    ch = text[i]
    if ch == '(':

        open_scopes.append(i)
    elif ch == ')':

        open = open_scopes.pop()

        current_text = text[open:i + 1]
        print(''.join(current_text))



