import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def cli():
    pass


if __name__ == '__main__':
    cli()

#Generate a random grid of 0 and 1
def random_grid(size):
    return np.random.choice([0,1], size * size, p=[0.5, 0.5]).reshape(size, size)

#Update the grid for each frame
def update(frameNum, img, grid, size):
    newGrid = grid.copy()
    for i in range(size):
        for j in range(size):
            #Calcule le nombre de cellule en vie dans un square 8x8 pour chque cell
            neighbors = (
                        grid[(i - 1) % size, (j - 1) % size] + \
                        grid[(i - 1) % size, j % size] + \
                        grid[(i - 1) % size, (j + 1) % size] + \
                        grid[i % size, (j - 1) % size] + \
                        grid[i % size, (j + 1) % size] + \
                        grid[(i + 1) % size, (j - 1) % size] + \
                        grid[(i + 1) % size, j % size] + \
                        grid[(i + 1) % size, (j + 1) % size]
            )
            
            #Regle du jeu de la vie
            if grid[i, j] == 1:
                if (neighbors < 2) or (neighbors > 3): 
                    newGrid[i, j] = 0

                else:
                    if neighbors == 3:
                        newGrid[i, j] = 1

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

size = 50
num_frames = 10000000000
interval = 100

# Set up the figure and axis
fig, ax = plt.subplots()
grid = random_grid(size)
img = ax.imshow(grid, interpolation='nearest', extent=(0, size, 0, size))
ax.set_xticks(np.arange(0, size+1, 1))
ax.set_yticks(np.arange(0, size+1, 1))
ax.grid(True, linewidth=0.5, color='black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(img, grid, size), interval=200)

# Display the animation
plt.show()
    

 