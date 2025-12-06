"""
Başlangıç-Bitiş Noktası Oluşturucu Modül - Interface
Bu dosya nokta oluşturucu modülün nasıl olması gerektiğini gösterir
"""

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
        # start = (0, 0)
        # end = (19, 19)
    """
    # BURASI EKİP ARKADAŞINIZ TARAFINDAN DOLDURULACAK
    # Örnek placeholder:
    if obstacles is None:
        obstacles = []

    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    return start, end


# Test fonksiyonu
if __name__ == "__main__":
    test_obstacles = [(5, 5), (10, 10)]
    start, end = generate_start_end_points(obstacles=test_obstacles)
    print(f"Başlangıç: {start}")
    print(f"Bitiş: {end}")
