# MatrixRoute - En Kısa Yol Bulma Projesi

20x20 matris üzerinde engeller arasından en kısa yolu bulan ve görselleştiren Python projesi.

## Proje Açıklaması

Bu proje A* algoritması kullanarak bir matris üzerinde başlangıç noktasından bitiş noktasına en kısa yolu bulur. Proje modüler yapıda geliştirilmiş olup, her modül farklı takım üyeleri tarafından tamamlanmıştır.

### Özellikler
- ✅ 20x20 matris boyutu
- ✅ Random engel oluşturma (pattern desteği ile)
- ✅ Random başlangıç ve bitiş noktaları (minimum mesafe kontrolü ile)
- ✅ A* pathfinding algoritması
- ✅ Matplotlib ile görselleştirme
- ✅ Tam entegrasyon ve çalışır durumda

## Takım Görev Dağılımı

| Takım Üyesi | Branch | Görev | Dosya | Durum |
|-------------|--------|-------|-------|-------|
| Ana Kod | `main` | Pathfinding algoritması | `pathfinder.py`, `main.py` | ✅ Tamamlandı |
| Engel Oluşturucu | `main` | Random engel oluşturma | `obstacle_generator.py` | ✅ Tamamlandı |
| Nokta Oluşturucu (@azratashan) | `feature/start_goal_points` | Random başlangıç/bitiş | `point_generator_interface.py` | ✅ Tamamlandı (Merged) |
| Görselleştirme (@rabiacey26-cloud) | `visualizer-feature` | Matplotlib görselleştirme | `visualizer.py` | ✅ Tamamlandı (Merged) |

## Geliştirme Süreci

Proje modüler yapıda geliştirildi ve tüm modüller başarıyla entegre edildi:

1. ✅ **Ana Pathfinding Algoritması** - A* algoritması implementasyonu
2. ✅ **Engel Oluşturucu** - Random engel üretimi ve pattern desteği
3. ✅ **Nokta Oluşturucu** - Akıllı başlangıç/bitiş noktası seçimi
4. ✅ **Görselleştirme** - Matplotlib ile interaktif görselleştirme
5. ✅ **Entegrasyon** - Tüm modüller `main.py` içinde birleştirildi

### Merge Edilen Pull Request'ler

- **PR #1**: Nokta oluşturucu modülü (@azratashan)
- **PR #2**: Nokta oluşturucu son düzeltmeler (@azratashan)
- **PR #3**: Görselleştirme modülü (@rabiacey26-cloud)

## Kurulum ve Çalıştırma

### 1. Repository'yi Clone Et
```bash
git clone <repository-url>
cd MatrixRoute
```

### 2. Gereksinimleri Kur
```bash
pip install matplotlib numpy
```

### 3. Programı Çalıştır
```bash
python main.py
```

Program şu adımları otomatik olarak gerçekleştirir:
1. 50 adet random engel oluşturur
2. Başlangıç ve bitiş noktalarını seçer (minimum mesafe kontrolü ile)
3. A* algoritması ile en kısa yolu bulur
4. Sonuçları görselleştirir (Matplotlib penceresi açılır)

## Proje Dosya Yapısı

```
MatrixRoute/
│
├── pathfinder.py                    # ✅ Ana pathfinding algoritması (A*)
├── main.py                          # ✅ Tüm modülleri entegre eden ana dosya
│
├── obstacle_generator_interface .py # ✅ Engel oluşturucu (pattern desteği ile)
├── point_generator_interface.py     # ✅ Nokta oluşturucu (minimum mesafe kontrolü)
├── visualizer.py                    # ✅ Matplotlib görselleştirme
│
├── obstacle_generator_interface.py  # Interface örneği (kullanılmıyor)
├── requirements.txt                 # Gerekli Python paketleri
└── README.md                        # Bu dosya
```

## Modül Detayları

### 1. PathFinder (`pathfinder.py`)
**A* algoritması implementasyonu**

**Sınıf:** `PathFinder`
- `set_obstacles(obstacles)`: Engelleri matrise yerleştirir
- `set_start_end(start, end)`: Başlangıç ve bitiş noktalarını ayarlar
- `find_path()`: A* algoritması ile en kısa yolu bulur
- `get_path_info(path)`: Yol bilgilerini (uzunluk, başarı durumu) döndürür

**Özellikler:**
- Manhattan distance heuristic kullanımı
- Priority queue ile optimal performans
- 4 yönlü hareket (yukarı, aşağı, sol, sağ)

### 2. Obstacle Generator (`obstacle_generator.py`)
**Random engel oluşturma modülü**

**Fonksiyonlar:**
- `generate_obstacles(grid_size, obstacle_count)`: Basit random engeller
- `generate_obstacles_with_patterns(grid_size, obstacle_count, pattern)`: Pattern destekli engeller
  - `"random"`: Tamamen rastgele dağılım
  - `"walls"`: Dikey duvarlar oluşturur
  - `"clusters"`: Küme şeklinde engeller

**Özellikler:**
- Çakışma kontrolü (set kullanımı)
- Maximum engel sayısı kontrolü
- Farklı pattern'ler ile test senaryoları

### 3. Point Generator (`point_generator_interface.py`)
**Akıllı başlangıç/bitiş noktası seçimi** - *@azratashan tarafından geliştirildi*

**Fonksiyon:** `generate_start_end_points(grid_size, obstacles)`

**Özellikler:**
- Engel kontrolü: Noktalar engel üzerine düşmez
- Minimum mesafe kontrolü: Öklid mesafesi ile grid_size * 0.20 kontrolü
- Sonsuz döngü koruması: Maximum 1000 deneme limiti
- Exception handling: Yeterli alan yoksa hata fırlatır

### 4. Visualizer (`visualizer.py`)
**Matplotlib görselleştirme** - *@rabiacey26-cloud tarafından geliştirildi*

**Sınıf:** `Visualizer`
- `visualize(grid, start, end, path)`: Matrisi görselleştirir

**Renk Kodları:**
- Boş alanlar: Beyaz
- Engeller: Siyah
- Başlangıç: Yeşil nokta
- Bitiş: Kırmızı nokta
- Yol: Mavi çizgi

**Özellikler:**
- 7x7 inç figür boyutu
- Y ekseni ters çevrilmiş (matris formatına uygun)
- Legend ile açıklamalar
- Interaktif matplotlib penceresi

## Entegrasyon

Tüm modüller başarıyla entegre edildi! `main.py` dosyası tüm modülleri kullanarak çalışıyor:

```python
from pathfinder import PathFinder
from obstacle_generator import generate_obstacles
from point_generator_interface import generate_start_end_points
from visualizer import Visualizer
```

### Çalışma Akışı (`main.py`)
1. **Engel Oluşturma**: `generate_obstacles()` ile 50 engel
2. **Nokta Seçimi**: `generate_start_end_points()` ile başlangıç/bitiş
3. **Yol Bulma**: `PathFinder.find_path()` ile A* algoritması
4. **Görselleştirme**: `Visualizer.visualize()` ile matplotlib çıktısı

## Test Etme

### Ana Program
```bash
python main.py
```

### Modül Testleri
Her modülün kendi test kodu var:

```bash
# Pathfinder testi
python pathfinder.py

# Engel oluşturucu testi
python obstacle_generator.py

# Nokta oluşturucu testi
python point_generator_interface.py
```

**Not:** `visualizer.py` ve `main.py` birlikte çalışır, ayrı test gerekmez.

## Gereksinimler

**Python 3.6 veya üzeri**

### Gerekli Kütüphaneler
```bash
pip install matplotlib
pip install numpy
```

### Kullanılan Standart Kütüphaneler
- `heapq` - Priority queue (A* algoritması için)
- `typing` - Type hints
- `random` - Random sayı üretimi
- `math` - Matematiksel işlemler (Öklid mesafesi)
- `sys`, `io` - Windows console encoding desteği

## Örnek Çıktı

```
============================================================
MatrixRoute - En Kısa Yol Bulma Projesi
============================================================

1. Engeller oluşturuluyor...
   ✓ 50 engel oluşturuldu

2. Başlangıç ve bitiş noktaları oluşturuluyor...
   ✓ Başlangıç: (2, 5)
   ✓ Bitiş: (18, 15)

3. En kısa yol aranıyor...
   ✓ Yol bulundu!
   ✓ Yol uzunluğu: 28 adım

4. Görselleştirme yapılıyor...
   [Matplotlib penceresi açılır]

============================================================
Program tamamlandı!
============================================================
```

## Teknik Özellikler

### Algoritma Karmaşıklığı
- **A* Algoritması**: O((V + E) log V)
  - V: Grid'deki hücre sayısı (20x20 = 400)
  - E: Her hücrenin 4 komşusu var

### Optimizasyonlar
- Set kullanımı ile O(1) engel kontrolü
- Priority queue ile optimal düğüm seçimi
- Ziyaret edilen düğümlerin tekrar işlenmemesi

## Katkıda Bulunanlar

- **Ana Pathfinding**: Proje sahibi
- **Engel Oluşturucu**: `obstacle_generator.py` - Pattern desteği ile gelişmiş engel üretimi
- **Nokta Oluşturucu**: [@azratashan](https://github.com/azratashan) - Akıllı nokta seçimi ve mesafe kontrolü
- **Görselleştirme**: [@rabiacey26-cloud](https://github.com/rabiacey26-cloud) - Matplotlib entegrasyonu

## Lisans

Bu proje eğitim amaçlıdır.
