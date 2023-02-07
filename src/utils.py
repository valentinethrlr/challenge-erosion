def img2ascii(img_data: list[list[int]], black: str = '#', white: str = '.') -> str:
    '''
    Change the image in list in an image in string
    '''
    return ''.join([''.join([black if char == 1 else white for char in line] + ['\n']) for line in img_data])[:-1]


