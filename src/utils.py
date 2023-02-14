def img2ascii(img_data: list[list[int]], black: str = "#", white: str = ".") -> str:
    """
    Transforme the image data in form of a list in a string
    """
    return "".join(
        [
            "".join([black if char == 1 else white for char in line] + ["\n"])
            for line in img_data
        ]
    )[:-1]


def load_pbm(filename: str) -> list[list[int]]:
    """
    load the data in the file and return it in a list form
    """
    with open(filename, "r") as f:
        data = [line.replace("\n", "").split(" ") for line in f if line[0] != "#"]
    size = data[1]
    row = int(size[0])
    line = int(size[1])
    image = list("".join([item for sublist in data[2:] for item in sublist]))
    final_list = split_list(image, line, row)
    return final_list


def split_list(data: list, line: int, row: int) -> list[list[int]]:
    i: int = 0
    current_list = []
    final_list = []
    for _ in range(line):
        for _ in range(row):
            current_list += [int(data[i])]
            i += 1
        final_list += [current_list]
        current_list = []
    return final_list

def surrounding(i: int, j: int):
    return [[i - 1, j - 1], [i + 1, j - 1], [i - 1, j + 1], [i + 1, j + 1]]

def positions_to_change(data_line: list[int], n_line: int) -> list[int]:
    for i in range(n_line):
        positions_to_consider = surrounding(n_line, i)
        for position in positions_to_consider:
            line, row = position
            return controll(data_line, line, row, len_line, len_row)

def controll(data_line: list[int], line: int, row: int, len_line: int, len_row: int) -> None or list[int]:
    if line not in range(len_line) or row not in range(len_row) or data_line[row] == 0:
        return [line, row]
    
def n_step(img: list[list[int]], len_line: int, len_row: int):
    changes: list[list[int]] = []
    for i in range(len_line):
        changes += positions_to_change(data[i], i) 
    
def erosion(img: list[list[int]], n: int) -> list[list[int]]:
    data = img
    len_line: int = len(data)
    len_row: int = len(data[0])
    for _ in range(n):
        n_postitions_to_change = n_step(img, len_line, len_row)    
        for position in n_postitions_to_change:
            i, j = position
            data[i, j] = 0
    return data

zoom = 0.5
img = load_pbm("cross.pbm")
print(img2ascii(img))
