"""
Başlangıç-Bitiş Noktası Oluşturucu Modül - Interface
Bu dosya nokta oluşturucu modülün nasıl olması gerektiğini gösterir
"""
import random 
from typing import Tuple, List


def generate_start_end_points(grid_size: int = 20,
                              obstacles: List[Tuple[int, int]] = None) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Random başlangıç ve bitiş noktaları oluşturur

    Args:
        grid_size: Matris boyutu (varsayılan 20)
        obstacles: Engel listesi (noktalar engel üzerine düşmemeli)

    Returns:
        (başlangıç, bitiş) tuple formatında
        başlangıç: (x, y) koordinatı
        bitiş: (x, y) koordinatı

    Örnek:
        start, end = generate_start_end_points(grid_size=20, obstacles=[(5,5), (6,6)])
    """
    
    if obstacles is None:
        obstacles = []
    
    # 1. Başlangıç Noktasını Bulma (Engel Olmayacak Şekilde)
    start = None
    while start is None or start in obstacles:
        rand_x = random.randint(0, grid_size - 1)
        rand_y = random.randint(0, grid_size - 1)
        test_point = (rand_x, rand_y)
        
        if test_point not in obstacles:
            start = test_point

    # 2. Bitiş Noktasını Bulma (Engel veya Başlangıç Noktası Olmayacak Şekilde)
    end = None
    while end is None or end in obstacles or end == start:
        rand_x = random.randint(0, grid_size - 1)
        rand_y = random.randint(0, grid_size - 1)
        test_point = (rand_x, rand_y)
        
        if test_point not in obstacles and test_point != start:
            end = test_point

    return start, end 

# Test fonksiyonu
if __name__ == "__main__":
    # Test engelleri, bu noktalar başlangıç veya bitiş olamaz
    test_obstacles = [(5, 5), (10, 10), (0, 0)] 
    start, end = generate_start_end_points(obstacles=test_obstacles, grid_size=15)
    
    print(f"Başlangıç: {start}")
    print(f"Bitiş: {end}")
    
    # Başlangıç ve bitiş noktalarının engellerde veya aynı yerde olmadığını kontrol eder.
    assert start != end 
    assert start not in test_obstacles
    assert end not in test_obstacles
    print("Testler başarılı!")