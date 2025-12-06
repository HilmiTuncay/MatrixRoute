"""
Engel Oluşturucu Modül - Interface
Bu dosya engel oluşturucu modülün nasıl olması gerektiğini gösterir
"""

from typing import List, Tuple


def generate_obstacles(grid_size: int = 20, obstacle_count: int = 50) -> List[Tuple[int, int]]:
    """
    Random engeller oluşturur

    Args:
        grid_size: Matris boyutu (varsayılan 20)
        obstacle_count: Oluşturulacak engel sayısı (varsayılan 50)

    Returns:
        Engel koordinatları listesi [(x1, y1), (x2, y2), ...]

    Örnek:
        obstacles = generate_obstacles(grid_size=20, obstacle_count=50)
        # [(3, 5), (7, 12), (15, 8), ...]
    """
    # BURASI EKİP ARKADAŞINIZ TARAFINDAN DOLDURULACAK
    # Örnek placeholder:
    return []


# Test fonksiyonu
if __name__ == "__main__":
    obstacles = generate_obstacles()
    print(f"Oluşturulan engel sayısı: {len(obstacles)}")
    print(f"İlk 10 engel: {obstacles[:10]}")
