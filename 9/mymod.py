
def count_lines(name):
    with open(name) as f:
        lines = f.readlines()
    return len(lines)

def count_chars(name):
    with open(name) as f:
        text = f.read()
    return len(text)

def test(name):
    lines_num = count_lines(name)
    char_num = count_chars(name)
    print(lines_num, char_num)

test("E:/python_projects/beetroot/shota.txt")