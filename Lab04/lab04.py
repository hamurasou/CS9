
from Stack import Stack

def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push((startX, startY))

    step_count = 1
    north = (-1, 0)
    west = (0, -1)
    south = (1, 0)
    east = (0, 1)
    directions = [east, south, west, north]
    # it stacks in the order of east, south, west, and north
    # (east at the bottom and north at the top)
    # stack executes its values from the top
    # therefore, it excutes in the order of north, west, south, and esat

    # I could do the same computation by keeping the direction in the right order
    # and used reversed(directions) in the loop below
    # for direction in reversed(direction):

    result = False

    while not stack.isEmpty():
        current_position = stack.pop()
        current_x = current_position[0]
        current_y = current_position[1]

        if maze[current_x][current_y] == 'G':
        # when the stack coordinate meets the condition (G)
            result = True
            return result, maze

        if maze[current_x][current_y] == ' ':
        # when the stack coordinate is empty (not marked with any numbers)
            maze[current_x][current_y] = step_count
            step_count += 1

            for direction in directions:
                new_x = current_x + direction[0]
                new_y = current_y + direction[1]

                if maze[new_x][new_y] in [' ', 'G']:
                    stack.push((new_x, new_y))

    return result, maze

##########

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

maze = [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', ' ', '+', ' ', ' ', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['+', ' ', '+', '+', ' ', '+'],
        ['+', ' ', ' ', '+', ' ', '+'],
        ['+', '+', '+', '+', '+', '+']
    ]

startX = 3
startY = 3
result, updated_maze = solveMaze(maze, startX, startY)
print("Path found:", result)
printMaze(updated_maze)
