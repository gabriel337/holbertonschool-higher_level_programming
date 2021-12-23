def remove_char_at(str, n):
    if str > n:
        str = str[0:n:] + str[n + 1::]
