---
title: Menyamakan jam rekam lima kamera dan membuat sequence Premiere per tanggal
date: 2026-10-18
series: video-archive-ai
part: 2
cover: /images/20261018-time-sync-sequences/01-timeline-camera-tracks.webp
summary: 905 klip dari kamera dengan jam yang kacau saya cocokkan ke waktu rekam sebenarnya memakai GPS dan foto, lalu sequence Premiere per tanggal dengan track terpisah per kamera dibuat otomatis.
---

905 klip dari kamera yang jamnya berantakan saya cocokkan ke waktu rekam sebenarnya memakai GPS dan foto,
**lalu sequence Premiere per tanggal dengan track terpisah per kamera dibuat otomatis.**

Di bagian 1 semua video sudah terkumpul di satu hard disk. Sekarang tahap menyusunnya supaya siap diedit.
Kameranya lima jenis: Osmo Nano, GoPro, Canon 100D, Canon G7X (kamera istri saya), dan ponsel.

## Menyamakan waktu rekam: jam di setiap kamera berbeda

Untuk mengedit, video dari beberapa kamera harus disusun sesuai urutan rekam yang sebenarnya.
Masalahnya, patokan jam di setiap kamera berbeda. Waktu lokal di Tanzania adalah UTC+3, enam jam di belakang zona waktu rumah saya (UTC+9).

AI menarik waktu rekam dari 905 file, lalu memeriksanya per kamera.

| Kamera | Kondisi jam | Cara menyamakan |
|---|---|---|
| Osmo (412 klip) | Nama file memakai jam rumah (UTC+9) | Waktu di nama file dikurangi 9 jam jadi UTC, lalu ditambah 3 jam jadi waktu lokal |
| GoPro (215 klip) | Berantakan | Dibahas terpisah di bawah |
| Canon 100D dan G7X (276 klip) | Bukan waktu lokal | Awalnya salah dianggap UTC, di sesi berikutnya dipastikan memakai jam rumah |
| Lainnya (2 klip) | File yang dipisahkan | Track tersendiri |

### GoPro

GoPro selalu minta jam diatur setiap kali dinyalakan, jadi karena malas, cukup banyak yang saya isi asal-asalan. Mungkin ada juga yang tahunnya ngawur seperti 2016.
Karena itu waktu yang tercatat di file tidak bisa dipercaya.

Petunjuk yang ditemukan AI adalah data GPS yang direkam GoPro di dalam video. GPS menyimpan waktu yang tepat dari satelit.
File yang sempat menangkap GPS langsung memakai waktu itu. Untuk yang tidak, AI memanfaatkan fakta bahwa jam yang salah itu melesetnya konsisten.
AI mencari rentang nomor file yang direkam dengan setelan jam yang sama, menghitung selisihnya per rentang, lalu mengoreksi semuanya sekaligus.

| Rentang nomor file | Seberapa jauh jamnya meleset |
|---|---|
| 0418–0433 | Hampir tepat |
| 0434–0460 | Sekitar satu hari |
| 0461–0479 | Sekitar 3 jam 20 menit, ke arah sebaliknya |
| 0482–0636 | Sekitar 153 hari |
| 0637–0640 | Sekitar 163 hari |

Dengan cara ini 214 dari 215 klip berhasil dipulihkan. Satu sisanya (GX010479) saya tandai dengan label "perkiraan waktu" di namanya.
Bagian yang direkam bersamaan dengan Osmo saya cek dengan membandingkan gelombang suaranya, dan selisihnya di bawah 10–20 detik.

### Canon

Canon awalnya dianggap memakai jam rumah, lalu dianggap memakai waktu lokal, dan perbandingan suara dijalankan dua kali. Dua-duanya sia-sia.
Akhirnya terpecahkan oleh satu foto. Di jam yang sama, Osmo merekam siang hari sementara Canon merekam makan malam.
Sudah jelas bukan waktu lokal, dan karena kemungkinan besar UTC, untuk sementara dimasukkan dengan +3 jam.
Ini terbalik di sesi berikutnya. Semua foto yang menurut jam kamera diambil pukul 8–10 malam ternyata adegan safari siang bolong (zebra, singa, gajah), dan ketika dimundurkan 9 jam, hasilnya paling banyak tumpang tindih dengan GPS GoPro dan Osmo. **Canon 100D dan G7X ternyata sama-sama memakai jam rumah.** Hanya video G7X (MP4) yang catatan waktunya sudah benar, jadi tidak dikoreksi.

## Sequence Premiere per tanggal

Setelah waktunya beres, sisanya tinggal disusun sesuai aturan.
AI membuat file sequence untuk Premiere (XML) dengan skrip, lalu di-import ke Premiere.
Pertama dicoba dulu dengan DAY 1 saja, setelah caranya terbukti benar baru semuanya dibuat sekaligus.

| Item | Aturan |
|---|---|
| Sequence | 16 sequence per tanggal, 4K 29,97fps |
| Batas hari | Pukul 4 pagi. Rekaman lewat tengah malam masuk ke hari sebelumnya |
| Track | V1 Osmo, V2 GoPro, V3 Canon, V4 lainnya. Audio dua track per kamera |
| Rekaman bersamaan | Ditumpuk atas-bawah di titik yang sama |
| Jeda antar adegan | Dipadatkan jadi 2 detik |
| Marker | Waktu lokal di setiap adegan |
| Nama klip | Diakhiri [tanggal waktu] |
| Ukuran | Klip 2.7K diperbesar agar pas di 4K |
| Yang dibuang | File sinkronisasi sementara, file thumbnail dan proxy, klip di bawah 0,5 detik, file duplikat |

![Sequence 26/9 di timeline Premiere, dengan track Osmo, GoPro, Canon, foto, dan ponsel bertumpuk atas-bawah](/images/20261018-time-sync-sequences/01-timeline-camera-tracks.webp)
*Sequence 26/9 di sekitar menit ke-100. V1 Osmo, V2 GoPro, V3 Canon, V5 foto, V9 ponsel. Kamera yang merekam momen yang sama bertumpuk atas-bawah.*

Kalau dilihat per tanggal, hasilnya seperti ini.

| Tanggal | Klip | Susunan kamera | Durasi |
|---|---|---|---|
| 24/9 | 4 | Osmo | 2 menit |
| 25/9 | 54 | Osmo 41, GoPro 13 | 158 menit |
| 26/9 | 130 | Canon 68, Osmo 36, GoPro 26 | 232 menit |
| 27/9 | 182 | Canon 96, Osmo 66, GoPro 20 | 380 menit |
| 28/9 | 42 | Canon 33, GoPro 6, Osmo 2, lainnya 1 | 91 menit |
| 29/9 | 154 | Canon 75, Osmo 44, GoPro 35 | 454 menit |
| 30/9 | 2 | GoPro | 2 menit |
| 1/10 | 37 | Osmo 21, GoPro 16 | 387 menit |
| 2/10 | 51 | Osmo 36, GoPro 15 | 367 menit |
| 3/10 | 62 | Osmo 47, GoPro 15 | 281 menit |
| 4/10 | 41 | Osmo 31, GoPro 10 | 310 menit |
| 5/10 | 30 | GoPro 23, Osmo 7 | 322 menit |
| 6/10 | 38 | GoPro 27, Osmo 11 | 129 menit |
| 7/10 | 20 | Osmo | 244 menit |
| 8/10 | 13 | Osmo 9, GoPro 4 | 198 menit |
| 9/10 | 15 | Osmo 13, GoPro 2 | 119 menit |

Tanggal 29/9 saja lebih dari 450 menit.
Membuka semuanya satu per satu, menyusunnya per kamera, dan menyamakan waktunya adalah bagian editing yang paling malas saya kerjakan. Bagian itu sekarang hilang begitu saja.
Begitu import selesai, Premiere juga mulai menganalisis media dengan sendirinya.

File kerjanya saya simpan terpisah. Kalau nanti ada video tambahan, cukup jalankan ulang ini.

| File | Fungsi |
|---|---|
| clip_times_fixed.csv | Waktu rekam 905 klip yang sudah dikoreksi |
| make_all.py | Skrip pembuat sequence per tanggal. Dijalankan ulang saat waktu Canon diperbaiki |
| Catatan serah terima (.md) | Lokasi file, nilai koreksi per kamera, pekerjaan yang tersisa, tips kerja |

## Sequence v2 yang dibuat ulang di sesi berikutnya

Setelah waktu Canon dipastikan, sequence dibuat ulang di sesi percakapan baru.

| Tugas | Hasil |
|---|---|
| Waktu Canon | 100D dan G7X dipastikan memakai jam rumah, lalu dikoreksi |
| Track foto | 778 foto (100D 678, G7X 73, GoPro 15, Osmo 12) masuk ke track foto sebagai potongan 3 detik. 343 foto yang hanya ada dalam RAW (CR2) tidak bisa dibaca Premiere, jadi dikeluarkan dulu dan hanya daftarnya yang disimpan |
| Sequence v2 | Dibuat ulang dengan foto, jadi 17 sequence per tanggal. Lima foto yang diambil di rumah pada pagi hari keberangkatan menjadi satu sequence tambahan, 0923 |
| Rekaman baru | 407 klip dari G7X dan 100D yang belum di-backup, ditambah video ponsel, ditaruh di track baru. Supaya susunan track lama dan MP3 yang sudah diekspor tidak terganggu |
| Mencari file yang hilang | Dilacak dari nomor file kamera yang bolong. Nomor 4293–4532 di 100D, 240 file, pas dengan jumlah DAY 4, jadi kemungkinan besar ada di data laptop |

![Panel project Premiere berisi 17 sequence v2 perjalanan dari 0923 sampai 1009](/images/20261018-time-sync-sequences/02-v2-sequence-list.webp)
*Panel project. Bagian atas adalah MP3 per tanggal, bagian bawah 17 sequence v2 4K 29,97fps.*

Di tulisan berikutnya saya rangkum koneksi yang membuat AI bisa mengoperasikan Premiere langsung, yaitu Premiere MCP.
