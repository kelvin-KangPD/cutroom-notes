---
title: Membuat subtitle untuk 62 jam video perjalanan, dan efisiensi kerja dengan AI
date: 2026-10-19
series: video-archive-ai
part: 4
cover: /images/20261019-captions-efficiency/01-caption-track.webp
summary: Subtitle 62 jam video perjalanan saya ubah caranya, posisi ucapan ditangkap dulu dengan transkripsi Premiere lalu hanya bagian penting yang dirapikan dengan Gemini. Biaya kerja AI ternyata ditentukan oleh panjang percakapan dan jumlah bolak-balik.
---

Subtitle 62 jam video perjalanan saya ubah caranya: posisi ucapan ditangkap dulu dengan transkripsi Premiere, lalu hanya bagian penting yang dirapikan dengan Gemini.
**Biaya kerja AI ternyata ditentukan oleh panjang percakapan dan jumlah bolak-balik.**

Ini bagian terakhir dari catatan kerja. Isinya subtitle, biaya, dan rekaman lama yang ikut saya rapikan dengan alur yang sama.

## Subtitle: transkripsi Premiere + Gemini

Untuk subtitle, SRT dari Gemini yang paling akurat. Tapi 62 jam tidak mungkin dimasukkan semua ke Gemini, jadi caranya saya ubah.

| Langkah | Isi |
|---|---|
| 1 | Ekspor sequence per tanggal jadi MP3 dengan Media Encoder |
| 2 | Jalankan transkripsi Premiere dulu untuk menangkap posisi ucapan. Bahasa default-nya ternyata bahasa Inggris, jadi diganti ke bahasa yang benar |
| 3 | Dari hasil transkripsi (json), buang bagian yang tidak dikenali supaya suara radio pemandu safari ikut tersaring |
| 4 | Buat SRT dari json, lalu naikkan caption track ke sequence v2 lewat MCP |
| 5 | Koreksi Gemini hanya untuk bagian yang benar-benar akan dipakai saat edit, bukan semuanya. Bagian dengan obrolan paling padat dipilih dengan skor, dipotong per 2 menit. Awalnya per 3 menit, tapi aplikasi Gemini hanya menuliskan sampai sekitar 2 menit dengan lengkap, jadi diperpendek |

![Blok subtitle berjajar di caption track C1 paling atas pada timeline Premiere](/images/20261019-captions-efficiency/01-caption-track.webp)
*C1 paling atas di sequence v2 adalah caption track. Karena bentuknya caption, bukan klip teks, gampang diekspor lagi jadi SRT atau diperbaiki.*

Transkripsi saya antrekan per tanggal di Premiere dan dibiarkan jalan sendiri. Awalnya dicek setiap 3 menit dan diproses satu per satu, tapi dari pemeriksaan di tengah jalan ketahuan itu tidak efisien, jadi diganti: setiap 30–40 menit, tanggal yang sudah selesai diproses sekaligus.

Saya juga sempat menyuruh AI mengirim notifikasi ke ponsel setiap kali pekerjaan selesai. Di sisi AI tercatat sudah terkirim beberapa kali, tapi tidak satu pun sampai. Akhirnya saya putuskan sering-sering mengecek sendiri saja.

## Biaya dan efisiensi

Ini pertama kalinya saya benar-benar memperhatikan pemakaian.
Setiap kali mengirim satu perintah, AI membaca ulang seluruh percakapan sampai titik itu. Jadi makin panjang percakapannya, pekerjaan yang sama bisa jadi berkali-kali lipat lebih mahal.
Menunggu 20 menit hampir tidak memakan biaya. Yang mahal adalah jumlah bolak-baliknya.

Di tengah jalan saya tanya, apakah cara kerja tadi efisien? Jawabannya: setengah-setengah.

| Pekerjaan | Penilaian |
|---|---|
| Memulihkan waktu GoPro | Dua-tiga kali jalankan skrip, puluhan file beres sekaligus, verifikasi juga lolos sekali jalan |
| Merapikan lokasi simpan project | Selesai dalam beberapa langkah |
| Mengecek waktu Canon | Tidak efisien. Mencoba menarik suara dari seluruh hard disk eksternal lalu menyerah karena lambat, menerima log error 260 ribu karakter apa adanya, dan percaya asumsi tanpa verifikasi lalu menjalankan perbandingan suara dua kali. Padahal satu foto saja sudah cukup |

Jadi di akhir, AI menulis catatan serah terima di folder kerja, dan saya pindah ke percakapan baru begitu batas pemakaian di-reset.
AI bahkan menyiapkan pesan pertama untuk ditempel di percakapan baru.

```
Baca catatan serah terima di folder edit Tanzania di PC rumah (drive I:), lalu lanjutkan editing Tanzania.
Minta semua izin yang dibutuhkan sekaligus di awal, dan jalankan pekerjaan secara paralel.
```

Di catatan serah terima itu juga masuk tips yang saya pelajari kali ini.

| Tips | Isi |
|---|---|
| Membaca hard disk eksternal | Lambat. Jangan baca file utuh, ambil bagian yang perlu saja |
| Output | Terima ringkasannya saja. Log yang membanjir semuanya jadi biaya |
| Verifikasi | Sebelum menjalankan proses lama, uji dulu dugaannya dengan satu sampel |
| Salin massal | 7-Zip File Manager lebih cepat daripada salin lewat perintah |
| Sinkron suara | Samakan dengan membandingkan perubahan volume suara dua video |

## Rekaman lama juga pakai kerangka yang sama

Yang saya rapikan bukan cuma video perjalanan. 14 folder rekaman pribadi dari sebelum perjalanan juga disamakan strukturnya.

| Item | Isi |
|---|---|
| Struktur | Asli\Video, Asli\Foto, Lainnya, Project |
| Aturan | Video dan audio ke Asli\Video, foto ke Asli\Foto, hasil olahan seperti foto edit dan grafis ke Lainnya, file project ke Project |
| Verifikasi | Jumlah file dipastikan sama dengan sebelum dirapikan |
| Yang tidak disentuh | Folder yang sudah punya struktur, project yang sedang diedit (takut tautannya rusak), folder tanpa tanggal |
| Berikutnya | Membuat project di setiap folder sampai sequence dengan track per kamera |

## Yang masih tersisa

| Pekerjaan | Catatan |
|---|---|
| DAY 4 dan DAY 6 | Data dari laptop sudah dipindah ke hard disk eksternal. Tinggal disambungkan dan dimasukkan |
| DAY 9 | Folder kosong di semua media penyimpanan |
| 343 foto RAW | Ekspor ke JPG dari Lightroom lalu tambahkan |
| Subtitle | Transkripsi tanggal yang tersisa, transkripsi khusus klip baru, koreksi Gemini untuk bagian penting |
| Sequence rekaman lama | Per project, setelah transkripsi selesai |
| Salinan cloud | OneDrive 1TB dua akun, Google Drive 400GB |

Catatan kerjanya sampai di sini. Mulai tulisan berikutnya saya ingin merapikan pikiran tentang akan jadi apa video-video yang sudah menumpuk ini nantinya.
