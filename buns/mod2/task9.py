def gl_sogl(str):
    gl = "аоыуеиюёэя"
    str = str.replace(" ", "")
    count_gl = 0
    count_sogl = 0
    for i in range(len(str)):
        if str[i] in gl: count_gl += 1
    count_sogl = len(str) - count_gl
    return f"{count_gl} {count_sogl}"


str = input()
print(gl_sogl(str))
