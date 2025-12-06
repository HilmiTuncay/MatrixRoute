# MatrixRoute - En Kısa Yol Bulma Projesi

20x20 matris üzerinde engeller arasından en kısa yolu bulan ve görselleştiren Python projesi.

## Proje Açıklaması

Bu proje A* algoritması kullanarak bir matris üzerinde başlangıç noktasından bitiş noktasına en kısa yolu bulur.

### Özellikler
- 20x20 matris boyutu
- Random engel oluşturma
- Random başlangıç ve bitiş noktaları
- A* pathfinding algoritması
- Görselleştirme

## Takım Görev Dağılımı

| Takım Üyesi | Branch | Görev | Dosya |
|-------------|--------|-------|-------|
| Ana Kod | `main` | Pathfinding algoritması | `pathfinder.py`, `main.py` |
| Engel Oluşturucu | `feature/obstacle-generator` | Random engeller | `obstacle_generator.py` |
| Nokta Oluşturucu | `feature/point-generator` | Random başlangıç/bitiş | `point_generator.py` |
| Görselleştirme | `feature/visualizer` | Görsel çıktı | `visualizer.py` |

## Branch Stratejisi

### 1. Ana Branch (main)
- Ana pathfinding kodu
- Entegrasyon dosyası (main.py)
- Interface dosyaları

### 2. Feature Branches

#### Engel Oluşturucu Branch
```bash
git checkout -b feature/obstacle-generator
```
**Görev:** `obstacle_generator.py` dosyası oluştur
- Fonksiyon: `generate_obstacles(grid_size, obstacle_count)`
- Return: `List[Tuple[int, int]]`
- Örnek için `obstacle_generator_interface.py` dosyasına bak

#### Nokta Oluşturucu Branch
```bash
git checkout -b feature/point-generator
```
**Görev:** `point_generator.py` dosyası oluştur
- Fonksiyon: `generate_start_end_points(grid_size, obstacles)`
- Return: `Tuple[Tuple[int, int], Tuple[int, int]]`
- Örnek için `point_generator_interface.py` dosyasına bak

#### Görselleştirme Branch
```bash
git checkout -b feature/visualizer
```
**Görev:** `visualizer.py` dosyası oluştur
- Fonksiyon: `visualize_path(grid_size, obstacles, start, end, path)`
- Return: None (ekrana çizim yapar)
- Örnek için `visualizer_interface.py` dosyasına bak
- Matplotlib, pygame, tkinter veya konsol kullanılabilir

## Çalışma Adımları

### 1. Repository'yi Clone Et
```bash
git clone <repository-url>
cd MatrixRoute
```

### 2. Kendi Branch'inizi Oluşturun
```bash
# Engel oluşturucu için
git checkout -b feature/obstacle-generator

# Nokta oluşturucu için
git checkout -b feature/point-generator

# Görselleştirme için
git checkout -b feature/visualizer
```

### 3. Kodunuzu Yazın
Interface dosyalarına bakarak kendi modülünüzü yazın.

### 4. Test Edin
Her modülün kendi test fonksiyonu var:
```bash
python obstacle_generator.py
python point_generator.py
python visualizer.py
```

### 5. Commit ve Push
```bash
git add .
git commit -m "feat: engel oluşturucu modülü eklendi"
git push origin feature/obstacle-generator
```

### 6. Pull Request Oluştur
GitHub'da kendi branch'inizden `main` branch'ine Pull Request açın.

## Proje Dosya Yapısı

```
MatrixRoute/
│
├── pathfinder.py                    # Ana pathfinding algoritması (A*)
├── main.py                          # Tüm modülleri entegre eden ana dosya
│
├── obstacle_generator_interface.py  # Engel modülü interface (örnek)
├── point_generator_interface.py     # Nokta modülü interface (örnek)
├── visualizer_interface.py          # Görsel modülü interface (örnek)
│
├── obstacle_generator.py            # [OLUŞTURULACAK] Engel oluşturucu
├── point_generator.py               # [OLUŞTURULACAK] Nokta oluşturucu
├── visualizer.py                    # [OLUŞTURULACAK] Görselleştirme
│
└── README.md                        # Bu dosya
```

## Modül Detayları

### 1. PathFinder (Ana Modül)
**Sorumluluk:** Ana kod yazarı

**Sınıf:** `PathFinder`
- `set_obstacles(obstacles)`: Engelleri ayarla
- `set_start_end(start, end)`: Başlangıç/bitiş ayarla
- `find_path()`: En kısa yolu bul (A* algoritması)
- `get_path_info(path)`: Yol bilgilerini döndür

### 2. Obstacle Generator
**Sorumluluk:** Engel oluşturucu yazarı

**Fonksiyon:** `generate_obstacles(grid_size=20, obstacle_count=50)`
- Random koordinatlarda engeller oluştur
- Engeller çakışmamalı
- Return: `[(x1, y1), (x2, y2), ...]`

**Öneriler:**
- `random.sample()` kullanılabilir
- Engel yoğunluğu ayarlanabilir
- Engel pattern'leri (duvarlar, labirent) eklenebilir

### 3. Point Generator
**Sorumluluk:** Nokta oluşturucu yazarı

**Fonksiyon:** `generate_start_end_points(grid_size=20, obstacles=[])`
- Random başlangıç ve bitiş noktası
- Noktalar engel üzerine düşmemeli
- İki nokta farklı olmalı
- Return: `(start, end)` şeklinde tuple

**Öneriler:**
- `random.choice()` kullanılabilir
- Minimum mesafe kontrolü eklenebilir

### 4. Visualizer
**Sorumluluk:** Görselleştirme yazarı

**Fonksiyon:** `visualize_path(grid_size, obstacles, start, end, path)`
- Matrisi görselleştir
- Engelleri göster
- Başlangıç/bitiş işaretle
- Yolu çiz (varsa)

**Öneriler:**
- Matplotlib ile 2D plot
- Pygame ile interaktif görsel
- Tkinter ile GUI
- Konsola basit ASCII çıktısı

**Renk kodları önerisi:**
- Boş: Beyaz/Gri
- Engel: Siyah
- Başlangıç: Yeşil
- Bitiş: Kırmızı
- Yol: Mavi

## Entegrasyon

Tüm modüller tamamlandığında `main.py` dosyasındaki import satırları güncellenecek:

```python
# ÖNCESİ (Interface)
from obstacle_generator_interface import generate_obstacles
from point_generator_interface import generate_start_end_points
from visualizer_interface import visualize_path

# SONRASI (Gerçek modüller)
from obstacle_generator import generate_obstacles
from point_generator import generate_start_end_points
from visualizer import visualize_path
```

## Programı Çalıştırma

Tüm modüller tamamlandıktan sonra:
```bash
python main.py
```

## Test Etme

Her modül için ayrı test:
```bash
# Pathfinder testi
python pathfinder.py

# Engel oluşturucu testi
python obstacle_generator.py

# Nokta oluşturucu testi
python point_generator.py

# Görselleştirme testi
python visualizer.py
```

## Gereksinimler

```bash
pip install numpy  # (opsiyonel, hesaplamalar için)
pip install matplotlib  # (görselleştirme için, eğer kullanılırsa)
```

## Git Komutları Cheat Sheet

```bash
# Güncel main branch'i al
git checkout main
git pull origin main

# Yeni feature branch oluştur
git checkout -b feature/module-name

# Değişiklikleri kaydet
git add .
git commit -m "açıklama"
git push origin feature/module-name

# Main branch ile senkronize et
git checkout main
git pull origin main
git checkout feature/module-name
git merge main

# Merge conflict çözümü
# Dosyaları düzenle
git add .
git commit -m "merge conflict çözüldü"
```

## İletişim ve Koordinasyon

1. Her modül yazarı kendi interface dosyasına bakmalı
2. Interface'deki fonksiyon imzalarını değiştirmeyin
3. Pull Request açtığınızda diğer takım üyelerini bilgilendirin
4. Code review yapın
5. Test edildikten sonra merge edin

## Sorun Giderme

### Import Hatası
Eğer modüller import edilemiyorsa:
- Interface dosyalarını kullanın (geçici)
- Dosya adlarını kontrol edin
- Aynı dizinde olduğundan emin olun

### Merge Conflict
Eğer merge conflict olursa:
- Dosyayı manuel düzenleyin
- Conflict marker'ları (`<<<<`, `====`, `>>>>`) silin
- Test edin ve commit edin

## Lisans

Bu proje eğitim amaçlıdır.
