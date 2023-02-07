def img2ascii(img_data: list[list[int]], black: str = '#', white: str = '.') -> str:
    '''
    Change the image in list in an image in string
    '''

    img_string: str = ''
    for line in img_data:
        for char in line:
            if char == 1:
                img_string += black
            else:
                img_string += white
        img_string += "\n"
    img_string = img_string[:-1]

    return img_string

    ''.join([black for char in [line for line in img_data] if char == '1' else white] + ['\n'])




if __name__ == '__main__':
    import doctest
    doctest.testmod

