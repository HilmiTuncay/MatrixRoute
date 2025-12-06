"""
Görselleştirme Modülü - Interface
Bu dosya görselleştirme modülün nasıl olması gerektiğini gösterir
"""

from typing import List, Tuple, Optional


def visualize_path(grid_size: int,
                   obstacles: List[Tuple[int, int]],
                   start: Tuple[int, int],
                   end: Tuple[int, int],
                   path: Optional[List[Tuple[int, int]]]) -> None:
    """
    Matrisi, engelleri ve yolu görselleştirir

    Args:
        grid_size: Matris boyutu
        obstacles: Engel koordinatları listesi
        start: Başlangıç noktası (x, y)
        end: Bitiş noktası (x, y)
        path: Bulunan yol koordinatları listesi (None ise yol yok)

    Beklenen görselleştirme:
        - Boş hücreler: ' ' veya '.'
        - Engeller: '#' veya '█'
        - Başlangıç: 'S'
        - Bitiş: 'E'
        - Yol: '*' veya '+'

    Örnek çıktı:
        S . . # . . .
        * . . # . . .
        * * . # . . .
        . * * * . . .
        . . . * * * E
    """
    # BURASI EKİP ARKADAŞINIZ TARAFINDAN DOLDURULACAK
    # Matplotlib, pygame, tkinter veya konsol çıktısı kullanılabilir

    # Örnek basit konsol çıktısı:
    print("\n" + "=" * 50)
    print("MatrixRoute Görselleştirme")
    print("=" * 50)
    print(f"Grid: {grid_size}x{grid_size}")
    print(f"Engel sayısı: {len(obstacles)}")
    print(f"Başlangıç: {start}")
    print(f"Bitiş: {end}")
    if path:
        print(f"Yol uzunluğu: {len(path)} adım")
    else:
        print("Yol bulunamadı!")
    print("=" * 50)


# Test fonksiyonu
if __name__ == "__main__":
    test_obstacles = [(5, 5), (5, 6), (5, 7)]
    test_start = (0, 0)
    test_end = (10, 10)
    test_path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]

    visualize_path(20, test_obstacles, test_start, test_end, test_path)
