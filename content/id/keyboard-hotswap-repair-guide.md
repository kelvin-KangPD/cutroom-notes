---
title: "Panduan perbaikan PCB keyboard sendiri: dari tombol hot-swap yang tidak terbaca sampai menyolder pad tembaga AULA yang copot"
date: 2026-11-03
summary: "Saat satu tombol di keyboard hot-swap tidak berfungsi, inilah bagian yang perlu dicek dulu untuk tiap gejala, sesuai urutan yang saya periksa sendiri saat memperbaiki AULA F108."
cover: /images/20261102-aula-f108-keyboard-repair/12-뜯긴-패드-자리.webp
---

Saat satu tombol di keyboard hot-swap tidak berfungsi, cari gejala Anda di bawah lalu langsung lompat ke nomornya.

```
Tombol tidak terbaca
├ Switch lain bisa → selesai
└ Tetap mati → langkah 2
   ├ Soket terangkat → langkah 3
   │  └ Pad cokelat → langkah 4
   ├ Dua tombol ikut → langkah 5
   └ Pad hilang → langkah 6
```

| Kondisi saya sekarang | Lompat ke |
|---|---|
| Belum tahu gejalanya apa | [1. Pilah dulu berdasarkan gejala](#s1) |
| Ganti switch tidak membantu | [2. Singkirkan dugaan switch dan buka casing](#s2) |
| Soket di bagian belakang terangkat | [3. Solder ulang soket yang terangkat](#s3) |
| Bekas soket berwarna cokelat | [4. Cek apakah pad tembaga copot](#s4) |
| Dua tombol tertekan bersamaan | [5. Dua tombol sekaligus berarti korsleting jalur](#s5) |
| Pad hilang, tidak ada tempat menempel soket | [6. Tanpa pad, sambung memutar dengan kabel](#s6) |
| Sudah beres tapi masih ada yang janggal | [7. Yang tersisa setelah diperbaiki](#s7) |

Urutan ini adalah jalan yang benar-benar saya lalui saat memperbaiki tombol X di AULA F108 Pro. Itu pertama kalinya saya menyolder, dan saya tidak punya multimeter. Bagaimana saya sampai di sini saya tulis terpisah di [catatan perbaikan sendiri](/id/posts/aula-f108-keyboard-repair/).

| Yang dibutuhkan | Yang saya pakai |
|---|---|
| Solder dan timah | Beli di Daiso |
| Alat pembuka casing | Benda keras apa saja |
| Alat pencari korsleting | Tusuk gigi dan situs tes keyboard |
| Kabel jalur memutar | Sehelai dari kabel LAN |
| Soket cadangan | Diambil dari posisi tombol yang tidak terpakai |
| Multimeter | Tidak perlu |

## 1. Pilah dulu berdasarkan gejala {#s1}

Tiap gejala punya penyebab dan titik perbaikan yang berbeda. Berdasarkan yang benar-benar saya lihat, pembagiannya seperti ini.

| Gejala | Yang dicurigai | Ke |
|---|---|---|
| Satu tombol mati, bisa dengan switch lain | Switch | Selesai |
| Satu tombol mati, tetap sama dengan switch lain | Soket hot-swap di papan | 2 → 3 |
| Satu sisi soket menonjol dari papan | Solderan soket atau pad tembaga | 3 → 4 |
| Sejak disolder, dua tombol tak terkait tertekan bersamaan | Korsleting jalur | 5 |
| Pad di bekas soket kosong dan cokelat | Pad tembaga copot | 4 → 6 |

Kita samakan dulu istilahnya. Bagian hitam tempat switch dicolok adalah soket hot-swap, dan pelat perak tempat kakinya menempel adalah pad tembaga. Dioda adalah komponen kecil terpisah di samping soket.

## 2. Singkirkan dugaan switch dan buka casing {#s2}

Yang pertama dilakukan adalah mencolokkan switch lain ke posisi yang mati. Saya mengganti semua switch ke switch Peach karena keyboard-nya berisik, lalu X tidak berfungsi. Dengan switch lain pun tetap mati, jadi sejak itu saya anggap masalahnya di papan.

Casing bawah lebih mudah dibuka dari dugaan.

| Langkah | Yang dilakukan |
|---|---|
| 1 | Cabut hanya keycap di sekitar celah pengunci casing bawah |
| 2 | Masukkan alat keras ke celah dan congkel seperti tuas |
| 3 | Lepas pelan-pelan hanya bagian yang perlu |
| 4 | Cabut sambungan baterai begitu terbuka |

![Mencongkel casing bawah dengan alat keras di celah](/images/20261102-aula-f108-keyboard-repair/06-지렛대로-하판-열기.webp)
<small>Casing bawah yang dibuka dengan alat sebagai tuas di celah</small>

Bahwa baterai wajib dicabut saya pelajari dari [tulisan perbaikan AULA F99](https://blog.naver.com/ststeel/224044004123). Kalau keyboard nirkabel, lakukan ini lebih dulu.

![Bagian dalam keyboard saat pertama dibuka, terlihat busa, kabel, dan kabel baterai](/images/20261102-aula-f108-keyboard-repair/07-첫-오픈-배터리.webp)
<small>Kabel baterai yang terlihat saat casing bawah pertama dibuka</small>

## 3. Solder ulang soket yang terangkat {#s3}

Kalau di bagian belakang tombol yang mati satu sisi soket sedikit menonjol, Anda ada di sini. Kalau timahnya terangkat dan kaki lepas dari pad, cukup disolder ulang.

![Soket X sedikit terangkat dan menonjol dari papan](/images/20261102-aula-f108-keyboard-repair/09-튀어나온-소켓.webp)
<small>Soket hot-swap X dengan satu sisi terangkat dari papan</small>

Awalnya cara menyolder saya salah. Saya hanya melelehkan timah lalu meneteskannya ke tempat soket, padahal **cara yang benar adalah memanaskan papan dulu lalu menekan timah di atasnya**. Klip di bawah ini cara yang salah.

![Percobaan solder pertama, melelehkan timah dan meneteskannya ke tempat soket](/images/20261102-aula-f108-keyboard-repair/움짤1-첫-납땜.webp)
<small>Cara yang salah: meneteskan timah leleh tanpa memanaskan papan</small>

Kalau soketnya lepas sama sekali, ambil dari posisi tombol yang tidak terpakai. Saya mengambil dari F10, dan belakangan menyesal kenapa tidak dari Pause. Pilih tombol yang jarang dipakai.

![Satu soket hot-swap hitam yang lepas, di atas telapak tangan](/images/20261102-aula-f108-keyboard-repair/10-떨어진-소켓.webp)
<small>Soket hot-swap yang lepas dari papan</small>

Sebelum menyolder, selalu cek langkah 4 dulu. Kalau yang terangkat ternyata pad, bukan timah, menempelkannya lagi tidak akan berhasil dan malah memperparah.

## 4. Cek apakah pad tembaga copot {#s4}

Lihat warna pad di bekas soket. Kalau pad tombol lain berwarna perak dan hanya titik ini yang cokelat, pad-nya copot.

![Bagian belakang posisi X: area pad persegi kiri kosong dan cokelat, dengan bekas terbakar di sekitarnya](/images/20261102-aula-f108-keyboard-repair/12-뜯긴-패드-자리.webp)
<small>Posisi X yang memperlihatkan dasar cokelat, bukan pad perak</small>

Saya mengeriknya pelan dengan cutter dan tidak muncul apa-apa. Itu memastikannya.

| Cek | Kesimpulan |
|---|---|
| Pad perak dan hanya timahnya yang lepas | Kembali ke langkah 3 dan solder ulang |
| Bekas pad cokelat dan dikerik tidak ada logam | Pad copot. Langkah 6 |

Pad tembaga adalah tembaga yang tercetak di papan, jadi tidak bisa diambil dari tempat lain lalu ditempel. Yang bisa dipindahkan hanya soket; **pad yang hilang harus diganti dengan kabel.**

## 5. Dua tombol sekaligus berarti korsleting jalur {#s5}

Kalau setelah menyolder dua tombol tak terkait mulai tertekan berpasangan, itu korsleting jalur. Pada saya, ini terjadi tepat setelah solder pertama.

![Menekan tombol di sekitar X pada keyboard yang sudah dirakit memunculkan huruf yang salah di Notepad](/images/20261102-aula-f108-keyboard-repair/움짤2-첫-결과-메모장.webp)
<small>Menekan tombol di Notepad setelah solder pertama</small>

| Tombol ditekan | Hasil |
|---|---|
| Ctrl atau Shift | Keduanya tertekan bersamaan |
| Alt | Tertekan bersama Z |
| Spasi | Tertekan bersama B |
| . | Tertekan bersama Fn |
| ↑ | Tertekan bersama ↓ |
| A·S·D·F·G, C·V·N·M | Masing-masing normal |

Setiap pasangan selalu satu tombol dari baris Shift dan tombol tepat di bawahnya di baris Ctrl. Keyboard mengirim sinyal ke satu kolom bergantian sambil membaca baris, jadi kalau dua baris tersambung, tombol atas dan bawah di kolom yang sama terbaca bersamaan ([dokumentasi QMK](https://develop-docs.qmk.fm/how_a_matrix_works)). C·V·N·M normal karena baris di bawahnya adalah spasi, jadi tidak punya pasangan.

![Foto seluruh papan dengan pasangan tombol yang tertekan bersamaan ditandai lingkaran oranye dan garis merah](/images/20261102-aula-f108-keyboard-repair/13-같이-눌리는-짝.webp)
<small>Peta pasangan tombol yang tertekan bersamaan, ditandai di papan</small>

![Foto papan dengan jalur baris Shift dan jalur baris Ctrl digambar, bertemu di satu titik](/images/20261102-aula-f108-keyboard-repair/14-두-줄-쇼트-원리.webp)
<small>Cara kerja korsleting jalur: baris Shift dan baris Ctrl bersentuhan di satu titik</small>

Titik korsleting bisa ditemukan tanpa multimeter.

| Langkah | Yang dilakukan |
|---|---|
| 1 | Sambungkan keyboard dan buka situs tes keyboard |
| 2 | Tahan satu tombol dari pasangan (saya pakai Ctrl). Pasangannya (Shift) ikut menyala di layar |
| 3 | Tekan-tekan area yang dikerjakan di sana-sini dengan tusuk gigi |
| 4 | Titik di mana tombol pasangan padam adalah lokasi korsleting |

Tusuk gigi tidak menghantarkan listrik, jadi tidak mengacaukan hasil. Saat menekan, terdengar bunyi "tik", lalu Shift mulai bekerja sendiri. Sepertinya ujung jalur tembaga yang terangkat menyentuh jalur baris di bawahnya, lalu terlepas.

![Foto close-up area yang copot dengan zona yang perlu ditekan tusuk gigi dilingkari oranye](/images/20261102-aula-f108-keyboard-repair/15-이쑤시개로-쇼트-찾기.webp)
<small>Zona yang ditekan dengan tusuk gigi</small>

Ini juga yang sempat saya coba sebelum menemukan korsleting tapi tidak membantu. Kalau gejalanya sama, ini boleh dilewati.

| Yang dicoba | Hasil |
|---|---|
| Mengambil serpihan logam di papan dengan pinset | Tidak berubah |
| Membersihkan bekas flux terbakar | Tidak berubah |
| Merapikan gumpalan timah | Tidak menyentuh jalur sebelah, jadi tidak relevan |
| Mencabut switch tombol yang mati lalu tes | Tidak berubah |

## 6. Tanpa pad, sambung memutar dengan kabel {#s6}

Sambungkan kaki soket di sisi yang copot langsung ke jalur tujuannya dengan kabel. Titik sambungnya dicari dengan menempelkan kabel menggunakan tangan sebelum menyolder. Cara ini saya ambil dari [kasus perbaikan di KeebTalk](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075).

**Yang paling penting adalah mencolokkan switch dan menahannya sambil menempelkan kabel.** Dua kaki soket hanya tersambung saat switch ditekan. Awalnya saya menempel tanpa switch dan lama kebingungan karena hanya X yang tidak terbaca.

| Langkah | Yang dilakukan |
|---|---|
| 1 | Solder kaki soket di sisi yang masih punya pad |
| 2 | Solder satu ujung kabel ke kaki di sisi yang copot |
| 3 | Colokkan switch, tahan tombol itu, lalu tempelkan ujung kabel satunya ke tiap kandidat pad |
| 4 | Cari pad yang membuat tombol itu muncul di layar tes |
| 5 | Solder kabel ke pad tersebut |

![Foto sekitar X dengan titik tetap dan kandidat ①–⑦ dilingkari](/images/20261102-aula-f108-keyboard-repair/16-X-연결-후보.webp)
<small>Tujuh kandidat pad untuk ditempel kabel</small>

Untuk kabel, saya menarik satu helai dari kabel LAN dan mengupas kedua ujungnya. Karena tipis, mudah diselipkan di antara pad.

![Kabel tipis dari kabel LAN yang sudah dikupas](/images/20261102-aula-f108-keyboard-repair/17-랜선-전선.webp)
<small>Sehelai kabel LAN dengan kedua ujung dikupas</small>

Begitu ditempel, hasilnya langsung terlihat. Pada saya, menempel ke pad D49 dan D48 di atas memunculkan D. Artinya kaki di sisi yang copot sudah tersambung ke jalur yang sama dengan D. Menempel ke pad D63 tepat di sebelahnya memunculkan X. Bukan S yang saya duga, bukan pula D, kandidat berikutnya. Jadi **daripada menebak, lebih cepat menempelkan ke semua kandidat.**

![Menyolder kabel dari kaki kiri soket X ke pad sebelah](/images/20261102-aula-f108-keyboard-repair/움짤3-전선-납땜.webp)
<small>Menyolder kabel dari kaki soket ke pad sebelah</small>

![Jalur yang menghubungkan pad D63 dan kaki soket X digambar dengan garis biru](/images/20261102-aula-f108-keyboard-repair/18-D63-연결.webp)
<small>Jalur akhir dari kaki soket X ke pad D63</small>

Setelah tersambung, pastikan diam saat tidak ditekan dan terbaca sekali saat ditekan.

![Situs tes keyboard yang menunjukkan tombol X terbaca](/images/20261102-aula-f108-keyboard-repair/움짤4-X-테스트-완료.webp)
<small>Input X setelah perbaikan, terkonfirmasi di situs tes keyboard</small>

## 7. Yang tersisa setelah diperbaiki {#s7}

Tombol yang diselamatkan lewat jalur kabel tidak persis sama seperti aslinya. Pada saya, ini yang tersisa.

| Yang tersisa | Status |
|---|---|
| X dan C bersamaan | Tidak bisa, karena X meminjam dioda milik C. Bisa diperbaiki dengan memindahkan kabel ke kaki dioda X sendiri |
| Tombol asal soket (F10) | Kosong. Pindahkan soket tombol yang tak terpakai (Pause dan lain-lain) atau atur ulang tombol |
| Soket yang disambung memutar | Lemah karena satu pad hilang. Topang soket dari belakang saat mencabut switch |

Untuk mengetik sehari-hari tidak masalah, jadi saya rakit apa adanya.

Sumber

| Sumber | Isi |
|---|---|
| [Tombol AULA F99 tidak berfungsi (bahasa Korea)](https://blog.naver.com/ststeel/224044004123) | Membuka casing bawah, mencabut baterai |
| [QMK: How a Keyboard Matrix Works](https://develop-docs.qmk.fm/how_a_matrix_works) | Matriks baris dan kolom serta cara kerja dioda |
| [KeebTalk: Need help fixing lifted pads Hotswap socket](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075) | Menyambung pad yang copot dengan kabel |
