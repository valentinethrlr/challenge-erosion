def img2ascii(img_data: list[list[int]], black: str = "#", white: str = ".") -> str:
    """
    Change the image in list in an image in string
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


def erosion(img: list[list[int]], n: int) -> list[list[int]]:
    data = load_pbm(img)
    line = len(data)
    row = len(data[0])
    for _ in range(n):
        for i in line:
            for j in row:
                if data[i][j] == 1:
                    positions = surrounding(i, j)
                    for position in positions:
                        if data[position] == 0:
                            data[i][j] = 0
    data = img2ascii(data)
    return data


def surrounding(i: int, j: int):
    return [[i - 1, j - 1], [i + 1, j - 1], [i - 1, j + 1], [i + 1, j + 1]]


