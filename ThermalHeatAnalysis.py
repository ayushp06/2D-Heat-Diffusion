import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from matplotlib.animation import FuncAnimation

gridX = 25
gridY = 25
grid = np.zeros((gridX, gridY))
grid[(gridX//2)-2:(gridX//2)+3, (gridY//2)-2:(gridY//2)+3] = 100

def heatSpread(grid, alpha = 2, dt = 0.1, dx = 1):
    newgrid = grid.copy()
    for i in range(1, gridX - 1):
        for j in range(1, gridY - 1):
            newgrid[i, j] = grid[i, j] + alpha * (dt/dx**2) * (grid[i - 1, j] + grid[i + 1, j] + grid[i, j - 1] + grid[i, j + 1] - 4 * grid[i, j])
    return newgrid

mainwindow = tk.Tk()
mainwindow.title('Thermal Analysis')

figure = Figure()
axis = figure.add_subplot(111)
gridimage = axis.imshow(grid, cmap = 'plasma', vmin = 0, vmax = 50)
axis.axis('off')

figurecanvas = FigureCanvas(figure, master = mainwindow)
figurecanvas.get_tk_widget().pack(fill = tk.BOTH, expand=True)

def animationUpdate(frame):
    global grid
    grid = heatSpread(grid)
    gridimage.set_data(grid)
    return [gridimage]

animation = FuncAnimation(figure, animationUpdate, frames = 100, interval = 50, blit = True)

mainwindow.mainloop()