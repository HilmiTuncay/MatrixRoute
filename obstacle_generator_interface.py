import random

# 1) Engelleri Oluşturma
# ------------------------------
def generate_obstacles(grid_size=20, obstacle_count=40):
    """
    Basit random engel üretme.
    Engel koordinatlarını liste olarak döndürür.
    """
    all_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    obstacles = random.sample(all_positions, obstacle_count)
    return obstacles


# 2) Başlangıç ve Bitiş Noktası
# ------------------------------
def generate_start_end_points(grid_size=20, obstacles=[]):
    """
    Engellere çarpmayan start ve end noktası üretir.
    """
    obs_set = set(obstacles)

    while True:
        start = (random.randint(0, grid_size - 1),
                 random.randint(0, grid_size - 1))

        end = (random.randint(0, grid_size - 1),
               random.randint(0, grid_size - 1))

        if start not in obs_set and end not in obs_set and start != end:
            return start, end


# 3) Basit Görselleştirme
# ------------------------------
def visualize(grid_size, obstacles, start, end, path=[]):
    """
    Konsola basit bir grid çizer.
    """
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    # Engeller
    for x, y in obstacles:
        grid[x][y] = "#"

    # Yol
    for x, y in path:
        if (x, y) not in (start, end):
            grid[x][y] = "*"

    # Start - End
    sx, sy = start
    ex, ey = end
    grid[sx][sy] = "S"
    grid[ex][ey] = "E"

    # Çıktı
    for row in grid:
        print(" ".join(row))


# 4) Test - Ana Çalışma
# ------------------------------
if __name__ == "_main_":
    grid_size = 10
    obstacle_count = 15

    obstacles = generate_obstacles(grid_size, obstacle_count)
    start, end = generate_start_end_points(grid_size, obstacles)

    # Şimdilik path boş (bulma algoritması sonra eklenir)
    path = []

    print("\n--- ENGELLER ---")
    print(obstacles)

    print("\n--- START / END ---")
    print("Start:", start)
    print("End:", end)

    print("\n--- GÖRSEL ---")
    visualize(grid_size, obstacles, start,end,path)