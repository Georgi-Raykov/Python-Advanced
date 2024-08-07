def fill_the_box(height, lenght, width, *args):
    cube_size = height * lenght * width
    rest_cubes = []
    for cube in args:

        if cube == 'Finish':
            break
        if cube_size >= cube:
            cube_size -= cube
        else:
            cube -= cube_size
            rest_cubes.append(cube)
            cube_size = 0
    if cube_size > 0:

        return f"There is free space in the box. You could put {cube_size} more cubes."
    else:
        return f"No more free space! You have {sum(rest_cubes)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
