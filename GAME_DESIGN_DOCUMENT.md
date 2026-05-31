# Ottoman Rage — Game Design Document

## Genel Bakış

| Özellik | Değer |
|---------|-------|
| Motor | Unreal Engine 5.7 |
| Tür | İzometrik Aksiyon RPG |
| Perspektif | Top-down / İzometrik |
| Geliştirme | Blueprint (Visual Scripting) |
| Platform | PC (Windows) |

## Hikaye

**Yıl: 1462.** Sultan II. Mehmed, Eflak Voyvodası Vlad Dracul'u (Kazıklı Voyvoda) bertaraf etmek için gizli bir operasyon emri verir. İstanbul'dan yola çıkan seçilmiş bir ajan, Bükreş'e ulaşana kadar Osmanlı topraklarında ve düşman arazisinde çeşitli görevler tamamlayacak, Vlad'ın karanlık ağını çözecektir.

**Ana Görev Zinciri:** İstanbul → Edirne → Filibe → Sofya → Niş → Belgrad → Bükreş

---

## Karakterler / Sınıflar

### 1. Yeniçeri (Janissary) — *Warrior*
- **Rol:** Tank / Yakın dövüş
- **Silah:** Pala, kalkan, balta
- **Pasif:** *Ocak Disiplini* — blok sonrası karşı saldırı hasarı +40%
- **Özel Yetenek:** *Toplu Hücum* — yakındaki düşmanları iter ve sersemletir
- **Ult:** *Yeniçeri Seferi* — 5 saniyelik hasar bağışıklığı + alan hasarı

### 2. Abdal — *Druid*
- **Rol:** Destek / İyileştirici / DoT
- **Silah:** Asa, nazarlık
- **Pasif:** *Tekke Huzuru* — dururken her 3 sn'de canı yeniler
- **Özel Yetenek:** *Beddua* — hedefe zehir + yavaşlama debuff uygular
- **Ult:** *Rüzgar Ruhu* — Alan içindeki müttefikleri iyileştirir, düşmanları geri iter

### 3. Deli — *Barbarian*
- **Rol:** DPS / Berserk saldırıcı
- **Silah:** İki el kılıcı, balta, kalkan yok
- **Pasif:** *Kan Öfkesi* — can %30'un altına düşünce hasar +60%, hız +30%
- **Özel Yetenek:** *Çılgın Koşu* — hedef yönüne fırlar, ilk düşmanı yere serer
- **Ult:** *Deli Fişeği* — 8 saniyelik kontrol edilemez berserk modu

### 4. Ozan — *Bard*
- **Rol:** Destek / Buff / Debuff
- **Silah:** Saz, hançer
- **Pasif:** *İlham* — ateşlenen her yetenekten sonra yakın müttefiklere hız bonusu
- **Özel Yetenek:** *Destan* — alandaki düşmanları büyüler (durdurur), müttefiklere hasar bonusu
- **Ult:** *Savaş Türküsü* — 10 saniyelik ekip çapı tüm stat +25%

### 5. İmam — *Wizard*
- **Rol:** Büyü hasarı / Alan kontrolü
- **Silah:** Kuran, asa, tılsımlı nesneler
- **Pasif:** *Fatiha Kalkanı* — her 15 sn'de otomatik bir kalkan yenilenir
- **Özel Yetenek:** *Nazar Oku* — tek hedefe yüksek hasar + kör efekti
- **Ult:** *İlahi Gazap* — geniş alan yakıp geçen kutsal enerji dalgası

### 6. Sipahi — *Ranger*
- **Rol:** Uzak mesafe / Atış / Keşif
- **Silah:** Yay, kargı, pallaş
- **Pasif:** *At Üstü Taktik* — hareket ederken hasar -20% azalır (diğer sınıflarda -40%)
- **Özel Yetenek:** *Yağmur Okları* — seçili alana ok sağanağı
- **Ult:** *Akıncı Baskını* — sanal süvari ültimatifi, alanı kat kat geçer

---

## Dünya Haritası & Bölgeler

### Bölge 1 — İstanbul (Başlangıç Bölgesi)
- **Ortam:** Şehir içi sokaklar, kapalı çarşı, saray bahçeleri
- **Düşmanlar:** Casuslar, Venedikli ajanlar, suikastçılar
- **Görev:** Vlad'ın İstanbul'daki ajan ağını çözmek
- **Boss:** Venedikli Casusbaşı *Marco Foscari*

### Bölge 2 — Edirne Ormanları
- **Ortam:** Yoğun Balkan ormanı, nehir geçitleri, derme çatma köyler
- **Düşmanlar:** Eşkıyalar, Vlad'ın öncü kuvvetleri, kurt adamlar (efsane)
- **Görev:** Savaş malzemesi konvoyunu korumak
- **Boss:** Orman Haydutbaşı *Karaçoban*

### Bölge 3 — Filibe Bataklıkları
- **Ortam:** Loş bataklık, sis, çürük köprüler, kayıklar
- **Düşmanlar:** Bataklık yaratıkları, zehirli böcekler, sapkın tarikat üyeleri
- **Görev:** Kaybolan Osmanlı birliğini bulmak
- **Boss:** Tarikat Şeyhi *Mircea Cel Rău*

### Bölge 4 — Balkan Stebi (Sofya Ovası)
- **Ortam:** Açık step, tahıl tarlaları, yakılmış köyler, gece baskınları
- **Düşmanlar:** Süvari timi, Vlad'ın Peştemalcıları, akbabalar (boss mekanik)
- **Görev:** Sofya şehrine ulaşmak ve kaleyi geri almak
- **Boss:** Kale Komutanı *Bogdan of Moldavia*

### Bölge 5 — Makedonya Dağları
- **Ortam:** Karlı geçitler, mağaralar, yüksek rakım
- **Düşmanlar:** Dağ soygunculuğu yapan Sirplar, kar fırtınası mekanik, ayılar
- **Görev:** Gizli dağ geçidini bulmak
- **Boss:** Çift başlı troll *Vukodlak* (Slav mitolojisi)

### Bölge 6 — Eflak Düzlüğü (Vlad Toprakları)
- **Ortam:** Karanlık düzlük, kazıklar, yakılmış köyler, karanlık şato
- **Düşmanlar:** Vlad'ın vampir muhafızları, ölümsüzleştirilmiş askerler
- **Görev:** Şatoya sızıp Vlad'a ulaşmak
- **Boss:** Vlad Dracul — çok aşamalı boss dövüşü

### Bölge 7 — Bükreş Şatosu (Final)
- **Ortam:** Gotik Wallachia şatosu, karanlık ritüel odaları, tuzak dolu koridorlar
- **Düşmanlar:** Vampir lords, yarı insan bekçiler
- **Final Boss:** Vlad'ın 3 fazlı dövüşü:
  - Faz 1: Kılıç ustası
  - Faz 2: Yarı vampir formu
  - Faz 3: Tam Dracula dönüşümü (uçuş, yarasa sürüsü, kan büyüsü)

---

## Oyun Mekanikleri

### Savaş Sistemi
- Real-time, tıklama bazlı saldırı
- Q/W/E/R yetenek tuşları
- Stamina çubuğu (dodge + ağır saldırı için)
- Parry & Riposte sistemi (Janissary'e özel)
- Elemental hasar: Fizik, Kutsal, Zehir, Ateş, Buz

### İlerleme Sistemi
- XP → Level (maks. 30)
- Her level: 3 stat puanı (STR / DEX / INT / VIT / WIS)
- Yetenek ağacı: Her sınıf için 3 dal, 15 node
- Ekipman: Nadir / Epik / Efsanevi kalite

### Çevre Etkileşimi
- Bataklık: Hareket yavaşlar, zehir riski
- Orman: Gizlenme bonusu (Sipahi +50%)
- Step: Görüş mesafesi artar (tüm sınıflar)
- Kar/Dağ: Stamina tüketimi +30%

### Yardımcı Karakterler (Companions)
- Her bölgede 1 yerel NPC katılabilir (geçici)
- Kalıcı yoldaş sistemi: Tamamlanan görevler ile kazanılır

---

## Teknik Yapı (Unreal Engine 5.7)

### Blueprint Sınıf Hiyerarşisi
```
BP_OttomanCharacterBase
├── BP_Janissary
├── BP_Abdal
├── BP_Deli
├── BP_Ozan
├── BP_Imam
└── BP_Sipahi

BP_EnemyBase
├── BP_Enemy_Human
│   ├── BP_Enemy_Spy
│   ├── BP_Enemy_Bandit
│   └── BP_Enemy_VladSoldier
└── BP_Enemy_Creature
    ├── BP_Enemy_Werewolf
    ├── BP_Enemy_SwampCreature
    └── BP_Enemy_Vampire

BP_BossBase
├── BP_Boss_MarcoFoscari
├── BP_Boss_Karacoban
├── BP_Boss_MirceaCelRau
├── BP_Boss_Bogdan
├── BP_Boss_Vukodlak
└── BP_Boss_VladDracul

UI Widgets (WBP_*)
├── WBP_HUD (can, stamina, mini-harita, yetenek çubuğu)
├── WBP_Inventory
├── WBP_SkillTree
├── WBP_Dialogue
└── WBP_WorldMap
```

### Klasör Yapısı (Content Browser)
```
Content/
├── Characters/
│   ├── Player/
│   │   ├── Janissary/
│   │   ├── Abdal/
│   │   ├── Deli/
│   │   ├── Ozan/
│   │   ├── Imam/
│   │   └── Sipahi/
│   └── Enemies/
├── Levels/
│   ├── L_Istanbul
│   ├── L_Edirne
│   ├── L_Filibe
│   ├── L_Sofya
│   ├── L_Makedonia
│   ├── L_Eflak
│   └── L_Bukres
├── Blueprints/
│   ├── GameMode/
│   ├── Combat/
│   ├── AI/
│   └── Systems/
├── UI/
├── VFX/
├── Audio/
└── Environment/
    ├── Forest/
    ├── Swamp/
    ├── Steppe/
    ├── Mountain/
    └── City/
```

---

## Geliştirme Yol Haritası

### Milestone 1 — Temel Hareket & Savaş (Hafta 1-2)
- [ ] İzometrik kamera kurulumu
- [ ] Karakter hareketi (tıklama ile yürüme)
- [ ] Temel saldırı animasyonları
- [ ] Can/Stamina sistemi
- [ ] Basit düşman AI

### Milestone 2 — Sınıf Sistemi (Hafta 3-4)
- [ ] 6 sınıf Blueprint'i
- [ ] Yetenek sistemi (Q/W/E/R)
- [ ] Pasif yetenekler
- [ ] Ult mekanikleri

### Milestone 3 — Seviye Tasarımı (Hafta 5-6)
- [ ] İstanbul bölgesi (şehir)
- [ ] Edirne bölgesi (orman)
- [ ] İlk boss dövüşü

### Milestone 4 — Ekipman & İlerleme (Hafta 7-8)
- [ ] Envanter sistemi
- [ ] XP / Level sistemi
- [ ] Stat ağacı
- [ ] Loot tabloları

### Milestone 5 — Tüm Bölgeler & Boss'lar (Hafta 9-14)
- [ ] Filibe, Sofya, Makedonya, Eflak bölgeleri
- [ ] Tüm boss dövüşleri
- [ ] Vlad Dracul 3 fazlı final

### Milestone 6 — Cila & Yayın (Hafta 15-16)
- [ ] UI/UX tamamlama
- [ ] Ses efektleri & müzik
- [ ] Performans optimizasyonu
- [ ] Alpha test

---

*Ottoman Rage — © 2026 ibeypinar-spec*
