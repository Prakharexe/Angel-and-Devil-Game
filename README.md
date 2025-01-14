# Angel and Devil Game

This repository contains a Python implementation of the **Angel and Devil** game. The game is played on an `n x n` grid where each cell can be either an "angel" (positive integer value) or a "devil" (negative integer value). Over successive generations, the values of the cells are updated based on the average of their neighbors, according to specified rules.

## Features

The implementation includes the following features:

1. **Create an Empty Grid**: Initialize an empty `n x n` grid with all entries set to 0.
2. **Update Grid with Input**: Populate the grid based on user input, marking cells as "angel" or "devil."
3. **Calculate Neighbor Mean**: Compute the mean value of neighboring cells for any given cell.
4. **Update Game Configuration**: Update the grid to the next generation based on the calculated neighbor means and predefined rules.

## Rules of the Game

1. Each cell in the grid has a value:
   - Positive values (> 0) represent "angel" cells.
   - Negative values (< 0) represent "devil" cells.
2. The value of each cell in the next generation is determined by:
   ```
   V_new = V + round(V_mean_neighbor / 2)
   ```
   where `V` is the current cell value and `V_mean_neighbor` is the mean value of its neighbors.
3. The grid updates iteratively, and the evolution can be visualized if desired.

## File Overview

- `a3q2.py`: The main Python script containing the game logic.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/angel-and-devil-game.git
   cd angel-and-devil-game
   ```

2. Run the program:
   ```bash
   python a3q2.py
   ```

3. Follow the on-screen prompts to input cell values and observe the game's evolution.

## Functions Included

- **`create_empty_grid(n)`**:
  Creates an `n x n` grid with all entries initialized to 0.

- **`update_grid_with_input(G, val)`**:
  Updates the grid `G` based on user input for angel/devil cell positions.

- **`cal_neighbor_mean(x, y, G)`**:
  Calculates the mean value of neighbors for the cell at position `(x, y)`.

- **`update_game_config(G)`**:
  Generates the next generation of the grid based on the rules.

## Example

Input:
```
Enter grid size: 3
Enter angel cell coordinates (x y): 1 1
Enter devil cell coordinates (x y): 0 0
- -  # End input
```

Output:
```
Generation 0:
0  0  0
0  20 0
-20 0  0

Generation 1:
...
```


---

Feel free to contribute or provide feedback!
