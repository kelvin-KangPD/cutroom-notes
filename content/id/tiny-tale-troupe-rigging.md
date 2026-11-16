---
title: "Saya Membuat Shorts Animasi Dongeng dengan AI (Karakter dari Kode, Rigging After Effects, Latar dari Gemini)"
date: 2026-11-16
summary: "Saya meluncurkan Tiny Tale Troupe, kanal shorts tempat lima karakter yang sama memerankan dongeng berbeda di setiap episode. Karakternya digambar dengan kode, dipotong menjadi bagian dan di-rig di After Effects, dan latarnya dibuat oleh Gemini."
cover: /images/20261114-tiny-tale-troupe-rigging/07-완성-장면.webp
---

Saya tidak bisa menggambar animasi, tetapi bersama AI saya membuka kanal shorts animasi dongeng. Namanya Tiny Tale Troupe: lima karakter tetap memerankan dongeng rakyat yang berbeda di setiap episode. Karakternya digambar dengan kode, gerakannya dari rigging After Effects, dan latarnya dibuat dengan Gemini.

![Adegan jadi: karakter nenek dan pemuda berambut runcing berdiri di depan latar kolam](/images/20261114-tiny-tale-troupe-rigging/07-완성-장면.webp)
<small>Satu adegan dari episode 1, "Kapak Emas." Latar oleh Gemini; karakter digambar dengan kode dan digerakkan di After Effects</small>

Episode 1 ada di sini: [Tiny Tale Troupe episode 1](https://youtube.com/shorts/Rechu83_CdA)

## Lima aktor, cerita berbeda setiap kali

Formatnya saya pinjam dari South Park. Aktor yang sama hanya berganti peran dan kostum untuk memerankan dongeng yang berbeda, dan kalimat pertama serta terakhir bertanya "Kalau kamu, bagaimana?" Saya tidak perlu membuat karakter baru, dan penonton jadi akrab dengan mereka.

![Lima karakter setinggi dua kepala berjajar: pemuda berbaju biru muda, pria berkumis dengan rompi ungu, nenek bersyal hijau, gadis berbaju kuning, dan wanita jangkung berambut merah](/images/20261114-tiny-tale-troupe-rigging/01-주연-다섯-명.webp)
<small>Lima pemeran utama. Dari kiri: Mo, Baba, Nana, Kiki, Tank</small>

| Karakter | Penampilan | Siapa dia bagi penonton |
|---|---|---|
| Mo | Pria kurus 20-an, rambut runcing, biru muda | "Aku." Orang biasa: baik, tetapi tidak mau rugi dan mudah tergoda |
| Baba | Pria gemuk 40-an, botak berkumis, ungu | Tokoh yang ditonton sambil dimaki. Penjahat, raja, orang kaya |
| Nana | Nenek bungkuk 70-an, tongkat, hijau | Pemberi ujian. Orang bijak, penyihir |
| Kiki | Gadis 10 tahun, rambut kuncir dua, kuning | Mengakali Baba dan membuat penonton puas |
| Tank | Wanita jangkung 30-an, rambut merah pendek, merah | Kekuatan dan aturan. Tembok, atau sekutu tak terduga |

Saya sengaja membuat ras, usia, dan bentuk tubuh semuanya berbeda, karena kanal ini untuk penonton di seluruh dunia.

## Gambar AI selalu menghasilkan orang yang berbeda

Awalnya saya ingin membuat karakter dengan AI juga. Di Higgsfield saya memakai Nano Banana Pro untuk membuat tiga gambar Baba, hanya mengubah tingkat kesederhanaannya.

![Pria berkumis yang sama digambar AI dalam tiga gaya: sangat sederhana di kiri, potongan kertas dengan sarung tangan oranye di tengah, detail dengan rompi bermotif dan jam saku di kanan](/images/20261114-tiny-tale-troupe-rigging/02-AI로-뽑은-세-단계.webp)
<small>Tiga gambar Baba dari deskripsi yang sama, hanya tingkat kesederhanaannya yang diubah (dibuat AI)</small>

Tidak ada yang jelek. Masalahnya, **ketiga gambar itu adalah tiga orang berbeda**. Dengan deskripsi yang sama pun, hasil berikutnya memberi karakter lain. Itu tidak cocok untuk kanal yang aktornya harus sama di setiap episode. Saya menulis "mitten hands" untuk tangan tanpa jari, dan AI benar-benar memakaikan sarung tangan oranye, lucu sekali.

Ketiganya juga terlalu rumit untuk digerakkan. Harus setingkat South Park: tubuh satu gumpalan, mata putih besar, mulut satu garis, dan karakter dibedakan hanya dari rambut, topi, dan warna. Jadi alih-alih alat gambar, saya menggambar SVG langsung dengan Python. Tanpa kredit, karakternya selalu sama, dan ekspresi atau topi bisa ditukar seperti suku cadang.

## Baru bisa bergerak setelah dipotong jadi bagian

Uji pertama hanya membuat satu gambar utuh memantul. Tubuhnya terlihat bergetar tidak wajar. Saya mempelajari lagi rigging animasi cutout dan memecah tiap karakter menjadi bagian.

![Karakter pemuda dipecah menjadi kaki, badan, kepala, lengan, mata, dan mulut yang dijajarkan](/images/20261114-tiny-tale-troupe-rigging/03-조각-나누기.webp)
<small>Satu karakter dipecah menjadi kaki, badan, kepala, lengan, mata, dan mulut</small>

Setiap bagian berada di tempatnya pada kanvas yang sama, jadi cukup ditumpuk untuk menjadi gambar asli. Lengan berputar di bahu, kepala di leher. Ada empat mulut: tertutup, sedikit terbuka, terbuka lebar, dan bulat.

![Pemuda yang sama dari depan, 45 derajat, samping, dan belakang](/images/20261114-tiny-tale-troupe-rigging/04-네-방향.webp)
<small>Untuk berbalik, seluruh gambarnya ditukar. Tampak belakang tidak punya mata dan mulut</small>

Memecah jadi bagian menimbulkan sambungan. Angkat lengan, bahunya terbuka; miringkan kepala, lehernya melayang. Saya membulatkan ujung sendi agar saling tumpang, lalu mengumpulkan semua lengan dan kepala pada putaran maksimum di satu lembar untuk memeriksa celah.

![Lima karakter berjajar dengan lengan terangkat dan kepala miring untuk pemeriksaan](/images/20261114-tiny-tale-troupe-rigging/05-이음매-확인판.webp)
<small>Lembar periksa dengan lengan dan kepala diputar maksimal agar sambungan tidak terbuka</small>

## Kenapa saya pindah ke After Effects

Awalnya gerakan juga saya render dengan kode lalu dirakit di Premiere. Tapi akting karakter ternyata lebih penting dari suara. Karakter terlihat hidup kalau mulut cocok dengan kata, tangan maju pada kata yang ditekankan, dan kepala menggeleng saat bilang "tidak." Memasang keyframe itu di Premiere per adegan berarti puluhan panggilan AI per adegan.

Di After Effects, setelah rig dibuat, expression mengurus sisanya. Sekarang saya cukup memasukkan rekaman dialog dan teksnya, dan ini terjadi:

| Bagian | Yang terjadi otomatis |
|---|---|
| Mulut | Memilih satu dari empat mulut menurut ejaan tiap kata, berganti satu tik sebelum suara |
| Mata | Berkedip sebelum bicara, sesudah selesai, dan sekitar tiap 3 detik saat mendengar |
| Kepala dan badan | Pada no atau not, menggeleng dan condong ke belakang; pada tanda tanya, memiringkan kepala |
| Lengan | Pada kata seperti this, mine, you, menunjuk ke arah lawan bicara; pada tanda seru, mengangkat tinggi |

![Ringkasan tujuh panel: nenek dan pemuda berganti ekspresi dan pose lengan sepanjang satu dialog](/images/20261114-tiny-tale-troupe-rigging/06-대사-요약판.webp)
<small>Satu dialog dipotong menjadi tujuh momen. Mata menutup dan membuka, mulut berganti, lengan maju pada kata penunjuk</small>

Yang saya tentukan per episode hanya satu baris per adegan: siapa mengucapkan dialog yang mana. Gerakan dipatah 15 kali per detik. Bergerak sedikit tersendat dengan sengaja cocok dengan gaya gambar ini. After Effects terhubung ke Claude lewat MCP, yang menjalankan skrip dan merakit adegan.

## Latar saya serahkan ke Gemini

Latar tidak berisi orang, jadi AI menanganinya dengan baik. Saya menjelaskan adegan ke Gemini, lalu di obrolan yang sama meminta "tata letak tetap, sederhanakan gaya gambarnya saja," dalam dua langkah. Kolam untuk episode 1 langsung pas di percobaan pertama.

Ada salah langkah juga. "Sederhana, 10 warna" membuatnya hambar, dan "banyak properti, terasa hidup" membuatnya seperti foto. Sekarang saya mengunggah satu gambar taman yang bagus dan menulis "dengan gaya gambar persis seperti gambar terlampir," lalu hanya menyebut tempat dan lima-enam properti. Saya minta 40% bagian bawah dibiarkan lantai kosong, karena di situ karakter berdiri. Tanda bintang Gemini di pojok kanan bawah dihapus dengan Python.

## Sejauh ini empat episode

![Halaman kanal YouTube Tiny Tale Troupe](/images/20261114-tiny-tale-troupe-rigging/08-유튜브-채널.webp)
<small>Kanal Tiny Tale Troupe</small>

Saya sudah mengunggah empat episode: Kapak Emas, Peniup Seruling, Mujina, dan Kantong Cerita. Saya tidak menggambar satu pun dengan tangan, tetapi hasilnya animasi tempat karakter berbicara dan bergerak. Saya sempat bertanya apakah hal seperti ini bisa dibuat dengan AI, dan ternyata bisa. Namun struktur yang membuat saya bisa terus memakai karakter yang sama lebih penting daripada AI yang membuat gambar.
