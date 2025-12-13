"""
MatrixRoute - Ana Pathfinding Modülü
En kısa yol bulma algoritması (A* Algorithm)
"""

import heapq
from typing import List, Tuple, Optional, Set


class PathFinder:
    """
    20x20 matris üzerinde A* algoritması ile en kısa yolu bulan sınıf
    """

    def __init__(self, grid_size: int = 20):
        """
        Args:
            grid_size: Matris boyutu (varsayılan 20x20)
        """
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.obstacles = set()
        self.start = None
        self.end = None

    def set_obstacles(self, obstacles: List[Tuple[int, int]]) -> None:
        """
        Engelleri matrise yerleştirir

        Args:
            obstacles: Engel koordinatları listesi [(x1, y1), (x2, y2), ...]
        """
        self.obstacles = set(obstacles)
        for x, y in obstacles:
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.grid[x][y] = 1

    def set_start_end(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Başlangıç ve bitiş noktalarını ayarlar

        Args:
            start: Başlangıç koordinatı (x, y)
            end: Bitiş koordinatı (x, y)
        """
        self.start = start
        self.end = end

    def _heuristic(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """
        Manhattan mesafesi hesaplama (heuristic fonksiyonu)

        Args:
            pos1: İlk nokta
            pos2: İkinci nokta

        Returns:
            İki nokta arası Manhattan mesafesi
        """
        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])

        # Standart Manhattan mesafesi
        manhattan = dx + dy

        # Tie-breaking: Hedefe daha direk giden yolu tercih et
        # Çok küçük bir değer (0.001) ekliyoruz ki optimal yolu bozmayalım
        tie_breaker = manhattan * 0.001
        return manhattan + tie_breaker

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Bir noktanın komşu hücrelerini döndürür (yukarı, aşağı, sol, sağ)
        Hedefe yakın olanları önceliklendirir (gereksiz manevralar azalır)

        Args:
            pos: Kontrol edilecek pozisyon

        Returns:
            Geçerli komşu hücreler listesi (hedefe yakınlığa göre sıralı)
        """
        x, y = pos
        neighbors = []

        # 4 yönlü hareket: yukarı, aşağı, sol, sağ
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Sınırlar içinde ve engel değilse
            if (0 <= new_x < self.grid_size and
                0 <= new_y < self.grid_size and
                (new_x, new_y) not in self.obstacles):

                # Hedefe olan mesafeyi hesapla (önceliklendirme için)
                if self.end:
                    dist_to_target = abs(new_x - self.end[0]) + abs(new_y - self.end[1])
                    neighbors.append(((new_x, new_y), dist_to_target))
                else:
                    neighbors.append(((new_x, new_y), 0))

        # Hedefe en yakın komşuları önce döndür
        neighbors.sort(key=lambda x: x[1])
        return [pos for pos, _ in neighbors]

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        """
        A* algoritması ile en kısa yolu bulur

        Returns:
            Yol varsa koordinat listesi, yoksa None
        """
        if self.start is None or self.end is None:
            raise ValueError("Başlangıç ve bitiş noktaları ayarlanmalı!")

        if self.start in self.obstacles or self.end in self.obstacles:
            return None

        # Priority queue: (f_score, counter, position)
        counter = 0
        open_set = [(0, counter, self.start)]
        heapq.heapify(open_set)

        # Her düğümün geldiği düğümü sakla
        came_from = {}

        # g_score: başlangıçtan bu düğüme gelen en kısa yol maliyeti
        g_score = {self.start: 0}

        # f_score: g_score + heuristic
        f_score = {self.start: self._heuristic(self.start, self.end)}

        # Ziyaret edilen düğümler
        visited = set()

        while open_set:
            current_f, _, current = heapq.heappop(open_set)

            # Hedefe ulaştık
            if current == self.end:
                return self._reconstruct_path(came_from, current)

            if current in visited:
                continue

            visited.add(current)

            # Komşuları kontrol et
            for neighbor in self._get_neighbors(current):
                if neighbor in visited:
                    continue

                # Geçici g_score
                tentative_g_score = g_score[current] + 1

                # Daha iyi bir yol bulduysak
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self._heuristic(neighbor, self.end)

                    counter += 1
                    heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))

        # Yol bulunamadı
        return None

    def _reconstruct_path(self, came_from: dict, current: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Bulunan yolu baştan sona doğru yeniden oluşturur

        Args:
            came_from: Her düğümün geldiği düğümü saklayan dict
            current: Hedef düğüm

        Returns:
            Başlangıçtan hedefe giden yol
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def get_path_info(self, path: Optional[List[Tuple[int, int]]]) -> dict:
        """
        Yol hakkında bilgi döndürür

        Args:
            path: Bulunan yol

        Returns:
            Yol bilgileri dict
        """
        if path is None:
            return {
                "success": False,
                "path_length": 0,
                "path": None,
                "direction_changes": 0,
                "message": "Yol bulunamadı!"
            }

        # Yön değişimlerini say
        direction_changes = self._count_direction_changes(path)

        return {
            "success": True,
            "path_length": len(path),
            "path": path,
            "direction_changes": direction_changes,
            "message": f"Yol bulundu! Uzunluk: {len(path)} adım, Yön değişimi: {direction_changes}"
        }

    def _count_direction_changes(self, path: List[Tuple[int, int]]) -> int:
        """
        Yoldaki yön değişimlerini sayar

        Args:
            path: Yol koordinatları

        Returns:
            Toplam yön değişimi sayısı
        """
        if len(path) < 2:
            return 0

        changes = 0
        prev_direction = None

        for i in range(1, len(path)):
            # Mevcut yönü hesapla
            dx = path[i][0] - path[i-1][0]
            dy = path[i][1] - path[i-1][1]
            current_direction = (dx, dy)

            # Önceki yönle karşılaştır
            if prev_direction is not None and prev_direction != current_direction:
                changes += 1

            prev_direction = current_direction

        return changes


# Ekip arkadaşlarınızın modüllerini entegre etmek için fonksiyonlar
def integrate_obstacles(obstacle_generator) -> List[Tuple[int, int]]:
    """
    Engel oluşturucu modülünü entegre eder

    Args:
        obstacle_generator: Engel oluşturucu modülün fonksiyonu

    Returns:
        Engel koordinatları listesi
    """
    return obstacle_generator()


def integrate_start_end(point_generator) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Başlangıç-bitiş noktası oluşturucu modülünü entegre eder

    Args:
        point_generator: Nokta oluşturucu modülün fonksiyonu

    Returns:
        (start, end) tuple
    """
    return point_generator()


def integrate_visualization(visualizer, grid_size: int, obstacles: List[Tuple[int, int]],
                           start: Tuple[int, int], end: Tuple[int, int],
                           path: Optional[List[Tuple[int, int]]]) -> None:
    """
    Görselleştirme modülünü entegre eder

    Args:
        visualizer: Görselleştirme modülün fonksiyonu
        grid_size: Matris boyutu
        obstacles: Engeller
        start: Başlangıç noktası
        end: Bitiş noktası
        path: Bulunan yol
    """
    visualizer(grid_size, obstacles, start, end, path)


if __name__ == "__main__":
    # Test kodu
    print("MatrixRoute - Pathfinding Ana Modülü")
    print("=" * 50)

    # PathFinder oluştur
    pf = PathFinder(grid_size=20)

    # Test engelleri
    test_obstacles = [
        (5, 5), (5, 6), (5, 7), (5, 8),
        (10, 10), (10, 11), (10, 12),
        (15, 3), (15, 4), (15, 5)
    ]

    # Test başlangıç-bitiş
    test_start = (0, 0)
    test_end = (19, 19)

    # Ayarla
    pf.set_obstacles(test_obstacles)
    pf.set_start_end(test_start, test_end)

    # Yol bul
    print(f"\nBaşlangıç: {test_start}")
    print(f"Bitiş: {test_end}")
    print(f"Engel sayısı: {len(test_obstacles)}")
    print("\nYol aranıyor...")

    path = pf.find_path()
    info = pf.get_path_info(path)

    print(f"\n{info['message']}")
    if info['success']:
        print(f"İlk 5 adım: {path[:5]}")
        print(f"Son 5 adım: {path[-5:]}")
