---
title: "Ingin ikut program reviewer Coupang tapi review menumpuk puluhan? Coba cara ini"
date: 2026-10-26
summary: "Saya hanya memberi kata kunci untuk 20 review Coupang: Claude mengarahkan, Gemini menulis, lalu Claude mengunggahnya. Ini kegagalan dan urutan yang akhirnya berhasil."
series: ai-orchestration
part: 2
cover: /images/20261026-coupang-gemini-reviews/01-제미나이-작성-화면.webp
---

Saya hanya memberi kata kunci untuk 20 review Coupang, **Gemini yang menulis teksnya, dan Claude yang mengunggahnya.**

Saya ingin mencoba program reviewer Coupang, tetapi di akun saya menumpuk review yang belum ditulis. Coupang tidak punya simpan draf, jadi begitu dibuka, review harus diselesaikan saat itu juga. Saya terus menundanya.

Satu hal dulu: program reviewer Coupang tidak punya tempat untuk mendaftar. Sejauh yang saya cari, Coupang mengundang orang yang rutin menulis review, dan tombol daftar tidak muncul. Jadi saya memutuskan membangun riwayat review dulu.

![Gemini menulis review per nomor, dengan judul, tiga baris ringkasan, alasan membeli, ulasan pemakaian, dan kesimpulan](</images/20261026-coupang-gemini-reviews/01-제미나이-작성-화면.webp>)

## Saya membagi peran

Gemini pandai menulis review, dan Claude yang mengklik halaman web untuk mengunggahnya. Saya membaginya begini untuk menghemat token.

| Peran | Tugas |
|---|---|
| Saya | Melempar kata kunci tiap produk: alasan membeli dan kesan memakainya |
| Claude | Merapikan kata kunci, mengirimnya ke Gemini, lalu mengunggah dan mengedit hasilnya di Coupang |
| Gemini | Mengembangkan kata kunci menjadi review lengkap |

Saya memakai chat Gemini biasa dengan model Flash, bukan AI Studio. Jika akun Google dihubungkan di browser Whale, Claude bisa mengoperasikan jendela itu langsung.

## Awalnya terlalu pendek dan tanpa pemisah baris

Review pertama yang saya unggah berupa satu blok teks, tanpa paragraf dan tidak panjang. Dibuka di ponsel, terlihat seperti dinding.

![Review awal yang dibuka di ponsel, satu blok teks tanpa pemisah paragraf](</images/20261026-coupang-gemini-reviews/02-처음-줄바꿈-없는-후기.webp>)

Review bagus milik orang lain punya kesamaan: bagian alasan membeli, kesan pemakaian, dan kesimpulan, dengan baris ringkasan di atas. Saya menyuruh Gemini memakai format persis seperti itu.

| Bagian | Isi |
|---|---|
| Judul | Satu baris untuk seluruh review |
| 3 baris ringkasan | Kalimat pendek yang diawali tanda centang |
| Alasan membeli | Kenapa saya membelinya |
| Ulasan pemakaian | Dua paragraf |
| Kesimpulan | Untuk siapa saya merekomendasikannya |

## Yang terjadi saat memakai Gemini

Tidak langsung berhasil. Berikut urutan yang saya alami.

| Masalah | Solusi |
|---|---|
| Hasil JSON terputus di tengah dan pemisah baris hilang | Beralih ke teks biasa dengan pemisah bernomor |
| Diminta 500 karakter, hasilnya sekitar 380 sampai 430 | Gemini menghitung terlalu sedikit. Meminta 580 sampai 750 menghasilkan sekitar 500 |
| Kadang menolak dengan "Saya tidak bisa membantu" | Mengirim ulang permintaan yang sama dengan kata-kata berbeda |
| Menyisipkan frekuensi seperti "setiap hari" yang tidak pernah saya katakan | Mencari kata itu dan menghapusnya sebelum diunggah |

Baris terakhir paling penting. Saya menyuruhnya mengembangkan agar enak dibaca, tetapi tidak boleh mengarang pengalaman yang tidak saya ceritakan. Jadi ia hanya boleh memakai fakta dari saya, dan untuk produk yang belum dipakai ia menulis "belum dipakai" apa adanya.

## Coupang diam-diam menolak penyimpanan

Saat Claude menekan simpan di halaman edit Coupang, sering gagal tanpa pesan galat. Penyebabnya, tab Coupang tidak berada di depan. Setelah pindah ke tab Gemini dan kembali, Coupang tetap di belakang, dan dalam kondisi itu penyimpanan gagal secara diam-diam. Saya membuatnya membawa tab ke depan sebelum setiap penyimpanan dan memeriksa halaman daftar setelahnya untuk melihat apakah teks berubah. Pesan galat selalu tersembunyi di halaman, jadi tidak bisa dipercaya sebagai tanda gagal.

Isi yang terlalu pendek, sekitar 60 karakter, juga gagal disimpan.

## Hasil

Saya memperbaiki 20 review ke format baru dan mengunggahnya. Yang saya tulis hanya kata kunci.

![Daftar review yang telah ditulis di Coupang, masing-masing dengan judul, tiga baris ringkasan bertanda centang, alasan membeli, ulasan pemakaian, dan kesimpulan](</images/20261026-coupang-gemini-reviews/03-최종-후기-쿠팡.webp>)

Masih ada yang tersisa. Foto akan saya unggah sendiri nanti, dan review produk yang belum dipakai akan saya ubah setelah dipakai. Saya juga mencari tahu soal Coupang Partners, tetapi pendaftarannya butuh verifikasi identitas dan wajib mencantumkan keterangan imbalan, jadi saya sendiri yang harus mendaftar.

Saya berencana menyimpan proses ini sebagai skill "menulis review Coupang", supaya lain kali cukup kata kunci untuk menjalankan langkah yang sama.
