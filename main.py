"""
MatrixRoute - Ana Program
Tüm modülleri entegre eden main dosyası
"""

from pathfinder import PathFinder

# Ekip arkadaşlarınızın modüllerini import edin
# from obstacle_generator import generate_obstacles
# from point_generator import generate_start_end_points
# from visualizer import visualize_path

# Şimdilik interface dosyalarını kullan
from obstacle_generator_interface import generate_obstacles
from point_generator_interface import generate_start_end_points
from visualizer_interface import visualize_path


def main():
    """
    Ana program akışı
    """
    print("=" * 60)
    print("MatrixRoute - En Kısa Yol Bulma Projesi")
    print("=" * 60)

    # Konfigürasyon
    GRID_SIZE = 20
    OBSTACLE_COUNT = 50

    # 1. Engelleri oluştur (Ekip arkadaşınızın modülü)
    print("\n1. Engeller oluşturuluyor...")
    obstacles = generate_obstacles(grid_size=GRID_SIZE, obstacle_count=OBSTACLE_COUNT)
    print(f"   ✓ {len(obstacles)} engel oluşturuldu")

    # 2. Başlangıç ve bitiş noktalarını oluştur (Ekip arkadaşınızın modülü)
    print("\n2. Başlangıç ve bitiş noktaları oluşturuluyor...")
    start, end = generate_start_end_points(grid_size=GRID_SIZE, obstacles=obstacles)
    print(f"   ✓ Başlangıç: {start}")
    print(f"   ✓ Bitiş: {end}")

    # 3. PathFinder ile yolu bul (Sizin modülünüz)
    print("\n3. En kısa yol aranıyor...")
    pathfinder = PathFinder(grid_size=GRID_SIZE)
    pathfinder.set_obstacles(obstacles)
    pathfinder.set_start_end(start, end)

    path = pathfinder.find_path()
    path_info = pathfinder.get_path_info(path)

    if path_info['success']:
        print(f"   ✓ Yol bulundu!")
        print(f"   ✓ Yol uzunluğu: {path_info['path_length']} adım")
    else:
        print(f"   ✗ {path_info['message']}")

    # 4. Görselleştir (Ekip arkadaşınızın modülü)
    print("\n4. Görselleştirme yapılıyor...")
    visualize_path(GRID_SIZE, obstacles, start, end, path)

    print("\n" + "=" * 60)
    print("Program tamamlandı!")
    print("=" * 60)


if __name__ == "__main__":
    main()
