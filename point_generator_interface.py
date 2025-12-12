"""
Başlangıç-Bitiş Noktası Oluşturucu Modül - Interface
Bu dosya nokta oluşturucu modülün nasıl olması gerektiğini gösterir
"""
import random 
import math # Minimum mesafe hesaplaması için eklendi
from typing import Tuple, List


def generate_start_end_points(grid_size: int = 20,
                              obstacles: List[Tuple[int, int]] = None) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Rastgele başlangıç ve bitiş noktaları oluşturur.
    Noktaların engellerle çakışmadığından ve birbirinden yeterince uzak olduğundan emin olur.

    Args:
        grid_size: Matris boyutu (varsayılan 20)
        obstacles: Engel listesi (noktalar engel üzerine düşmemeli)

    Returns:
        (başlangıç, bitiş) tuple formatında
    """
    
    MAX_ATTEMPTS = 1000  # Sonsuz döngüyü önlemek için güvenlik limiti
    MIN_DISTANCE_THRESHOLD = grid_size * 0.20  # Minimum mesafe (Matrisin %20'si)
    
    if obstacles is None:
        obstacles = []
    
    # 1. Başlangıç Noktasını Bulma (Engel Olmayacak Şekilde)
    attempts = 0
    start = None
    while start is None or start in obstacles:
        
        if attempts >= MAX_ATTEMPTS:
            raise RuntimeError("Hata: Başlangıç noktası için yeterli boş alan bulunamadi (Çok fazla engel var).")
        
        rand_x = random.randint(0, grid_size - 1)
        rand_y = random.randint(0, grid_size - 1)
        test_point = (rand_x, rand_y)
        
        if test_point not in obstacles:
            start = test_point

        attempts += 1

    # 2. Bitiş Noktasını Bulma (Engel, Başlangıç Noktası veya Çok Yakın Olmayacak Şekilde)
    attempts = 0
    end = None
    
    while end is None or end in obstacles or end == start:

        if attempts >= MAX_ATTEMPTS:
            raise RuntimeError("Hata: Bitiş noktası için yeterli boş alan bulunamadi veya mesafe kuralı sağlanamadi.")
        
        rand_x = random.randint(0, grid_size - 1)
        rand_y = random.randint(0, grid_size - 1)
        test_point = (rand_x, rand_y)
        
        # Öklid mesafesi hesaplama
        distance = math.sqrt((test_point[0] - start[0])**2 + (test_point[1] - start[1])**2)
        
        # Validasyon Kontrolü: Engel değil, başlangıç değil VE minimum mesafeden büyük olmalı
        if (test_point not in obstacles and 
            test_point != start and
            distance >= MIN_DISTANCE_THRESHOLD):
            
            end = test_point

        attempts += 1

    return start, end 

# Test fonksiyonu
if __name__ == "__main__":
    # Test engelleri
    test_obstacles = [(5, 5), (10, 10), (0, 0), (1, 1)] 
    
    print("--- Test Başlatıldı (15x15 Harita) ---")
    start, end = generate_start_end_points(obstacles=test_obstacles, grid_size=15)
    
    print(f"Başlangıç: {start}")
    print(f"Bitiş: {end}")
    
    # Doğrulama testleri
    min_dist = 15 * 0.20
    euclidean_dist = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    
    assert start != end 
    assert start not in test_obstacles
    assert end not in test_obstacles
    assert euclidean_dist >= min_dist
    print(f"Testler başarılı. Mesafe (Öklid): {euclidean_dist:.2f} (Min mesafe: {min_dist:.2f})")