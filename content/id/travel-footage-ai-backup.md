---
title: Backup video perjalanan, saya serahkan ke AI semalaman dan pagi-pagi dapat laporan verifikasi
date: 2026-10-18
series: video-archive-ai
part: 1
summary: Video perjalanan ke Tanzania yang tercecer di beberapa kamera dan hard disk saya serahkan ke AI semalaman untuk dikumpulkan ke satu hard disk, lalu paginya saya terima laporan verifikasi per file.
---

Video perjalanan ke Tanzania yang tercecer di beberapa kamera dan hard disk saya serahkan ke AI semalaman untuk dikumpulkan ke satu hard disk,
**lalu paginya saya terima laporan verifikasi yang mencocokkan file satu per satu.**

Kalau dikerjakan manual, ini bisa makan beberapa akhir pekan.
Saya cukup mencolokkan hard disk, tidur, lalu membaca laporannya di pagi hari.
Backup dimulai Rabu malam, akhir pekan sudah sampai ke sequence di Premiere, dan Senin pagi proses subtitle masih berjalan.
Karena isinya banyak, catatan kerja ini saya bagi jadi empat bagian. Bagian pertama ini tentang backup dan merapikan file.

## Titik awal: file tercecer dan hard disk penuh

Pulang dari perjalanan, video tersebar di setiap perangkat.

| Lokasi | Isi |
|---|---|
| Kartu SD Osmo Nano | Video paruh kedua perjalanan |
| Memori internal Osmo Nano | Video yang belum pindah ke kartu SD |
| Kartu SD GoPro | Video paruh kedua perjalanan |
| Hard disk eksternal 1TB | DAY 1–12 yang sudah dipindah selama perjalanan. Sisa ruang sekitar 6GB |
| Hard disk eksternal 2TB | Data lama seperti foto pernikahan, sekitar 320GB |
| Laptop lain | DAY 4 dan DAY 6, sekitar 300GB |

Kameranya ada lima jenis: Osmo Nano, GoPro, Canon 100D, Canon G7X (kamera istri saya), dan ponsel.

Masalahnya, besoknya saya ada syuting lagi, jadi kartu SD harus dikosongkan malam itu juga.
Rencana awalnya sederhana: kumpulkan semua file perjalanan ke hard disk 2TB, lalu pindahkan data lama di 2TB ke hard disk 1TB.

Di sini AI langsung menunjuk masalah urutan.
Hard disk 1TB hanya punya sisa 6GB, jadi 320GB tidak akan muat kalau langsung dipindah. Selain itu, kalau kartu SD ikut dikosongkan, file perjalanan hanya akan tersisa di satu tempat, yaitu hard disk 2TB.
Jadi rencananya saya ubah seperti ini.

| File | Dikumpulkan ke | Salinan kedua |
|---|---|---|
| DAY 1–12 di hard disk 1TB | Hard disk 2TB | Untuk sementara tetap dibiarkan di hard disk 1TB |
| Kartu SD Osmo dan GoPro, memori internal Osmo | Hard disk 2TB | Drive D di PC |
| Data lama di hard disk 2TB | Dipindah ke drive D di PC | |

Supaya tidak bingung, hard disk-nya juga saya beri nama. Yang 2TB pakai nama istri saya, yang 1TB pakai nama saya.

AI-nya saya pakai lewat aplikasi desktop Claude yang terhubung ke PC di rumah. AI sendiri yang membuka file, menyalin, dan membandingkan. Susunan koneksinya saya tulis terpisah di bagian 3.

## Salin dan verifikasi semalaman

Kalau menyalin data dalam jumlah besar lewat perintah teks, prosesnya lambat. Jadi AI membuka 7-Zip File Manager lewat kontrol layar dan menjalankan penyalinan dari sana.

Awalnya lambat karena setiap kali satu tugas selesai, AI bertanya dulu sebelum lanjut.
Saya tanya, ada alasan harus satu per satu? Katanya tidak ada. Setelah itu semua tugas dijalankan bersamaan.

Kondisi tepat sebelum saya tidur seperti ini.

| Tugas | Progres | Perkiraan selesai |
|---|---|---|
| Memori internal Osmo → hard disk 2TB dan drive D | Sebagian dari 43 file | Pukul 01.30 dini hari |
| Data lama hard disk 2TB → drive D | 32GB dari 257GB | Pukul 03.00, file asli dihapus setelah diverifikasi |
| DAY 1–12 dari hard disk 1TB → hard disk 2TB | 125GB dari 908GB | Pukul 05.00–06.00 |

AI juga merangkum apa yang harus saya jaga sebelum tidur: Osmo tetap tersambung, kedua hard disk tetap tercolok, aplikasi Claude dan jendela 7-Zip jangan ditutup.
Katanya laporan akan ditinggalkan sekitar pukul 06.20 pagi, dan memang ada.

| Tugas | Laporan pagi |
|---|---|
| Kartu SD Osmo (66 file, 103GB) | Tersalin ke dua tempat, hard disk 2TB dan drive D, cocok dengan aslinya |
| Kartu SD GoPro (19 file, 12GB) | Sama seperti di atas |
| Memori internal Osmo (22 file) | Sama seperti di atas |
| DAY 1–12 hard disk 1TB → hard disk 2TB | Nama dan ukuran 2.511 file semuanya cocok. Semua file besar ditambah sampel acak, total 299 file, dibandingkan sampai ke isinya |
| Data lama hard disk 2TB → drive D | 9.938 file dipastikan cocok, lalu yang di hard disk dihapus |
| 33 file GoPro (17,5GB) yang dobel di DAY 8 dan DAY 10–11 | Dipastikan file yang sama, lalu yang di DAY 10–11 dihapus |

**Hanya yang sudah lolos verifikasi yang ditulis "boleh dihapus".**
Untuk dua kartu SD dan memori internal Osmo, AI menyarankan supaya jangan dihapus dari komputer, tapi diformat dari kameranya. Itu yang saya lakukan sebelum berangkat kerja.

Setelah semua rapi, hard disk 2TB jadi khusus untuk perjalanan. DAY 1–15 masuk semua dan masih tersisa 794GB.
Saya merasa backup ganda belum perlu, jadi salinan perjalanan di hard disk 1TB akhirnya saya kosongkan dan hard disk itu dipakai untuk data lain.

Di tulisan berikutnya saya catat bagaimana waktu rekam 905 klip ini disamakan per kamera, lalu dibuat sequence Premiere per tanggal.
