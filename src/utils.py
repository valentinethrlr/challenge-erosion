from copy import deepcopy


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


def surrounding(line: int, row: int):
    return [[line - 1, row], [line + 1, row], [line, row - 1], [line, row + 1]]

def delete_first_last_line(line_to_delete :int, img: list[list[int]], nb_line: int, nb_row:int) -> list[list[int]]:
    for elem_row in range(nb_row):
            img[line_to_delete][elem_row] = 0
            img[nb_line-line_to_delete-1][elem_row] = 0
            
def delete_positions(considered_positions:list[list[int]], elem_line: int, elem_row: int, img:list[list[int]], copy_img: list[list[int]]) -> list[list[int]]:
    for position in considered_positions:
                        considered_line, considered_row = position
                        if(copy_img[considered_line][considered_row]==0):
                            img[elem_line][elem_row] = 0
                            break

def check_positions(nb_row: int, i: int, elem_line:int, img: list[list[int]], copy_img: list[list[int]]) -> None:
    for elem_row in range(i+1, nb_row-i-1):
        if img[elem_line][elem_row] == 1:
            considered_positions = surrounding(elem_line, elem_row)
            delete_positions(considered_positions, elem_line, elem_row, img, copy_img)
            

def erosion(img: list[list[int]], n: int) -> list[list[int]]:
    nb_line = len(img)
    nb_row = len(img[0])
    for i in range(n):
        copy_img = deepcopy(img)
        delete_first_last_line(i, img, nb_line, nb_row)
        # delete the first and last line and check all the other positions
        for elem_line in range(i+1, nb_line-i-1):
            img[elem_line][i] = 0
            img[elem_line][-1-i] = 0
            check_positions(nb_row, i, elem_line, img, copy_img)

    return img


zoom = 0.5
img = load_pbm("cross.pbm")
print(img2ascii(img))
