
def prepros_n_print(text_file, line):
    line.replace("&lt;/lyrics&gt", " ")
    line.replace("&lt;lyrics&gt", " ")
    no_punct = ""
    for char in line:
        if char not in punctuations:
            line = line + char
    text_file.write(line)

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


i = 0

f = open('text/dump-newest.txt', 'r')

text_file = open("text/lyrics.txt", "w")

full_line = ""
copy = False
for line in f.readlines():
    i = 0

    if "&lt;/lyrics&gt;" in line:
        copy = False
        prepros_n_print(text_file, line)
    elif "&lt;lyrics&gt;" in line:
        copy = True
        prepros_n_print(text_file, line)
    elif copy:
        prepros_n_print(text_file, line)

text_file.close()
