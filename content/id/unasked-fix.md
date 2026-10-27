---
title: "Claude membuat alat baru yang tidak pernah saya minta, jadi saya menelusuri alasannya lewat catatan"
date: 2026-10-28
summary: "Saat melihat perbaikan yang dibuat Claude tanpa diminta, saya merasa ia berkembang sendiri. Setelah menelusuri catatan ke belakang, ternyata arahnya saya yang menentukan, dan Claude menambal celah tempat arah itu bertabrakan dengan alat yang sudah usang."
cover: /images/20261028-unasked-fix/01-입력기-커밋-여섯-판.webp
---

Saat melihat perbaikan yang dibuat Claude tanpa diminta, saya merasa ia berkembang sendiri. Setelah menelusuri catatan ke belakang, ternyata arahnya saya yang menentukan, dan Claude menambal celah tempat arah itu bertabrakan dengan alat yang sudah usang.

## Saya hanya bilang "pindahkan ke Naver"

Dini hari 28 Oktober, saya meminta Claude memindahkan bagian 1 sampai 4 seri video pernikahan saya ke blog Naver. Yang saya katakan hanya "lakukan migrasi ke Naver."

Di akhir laporan bahwa empat draf sudah tersimpan, ada satu baris tambahan. Alat input yang lama butuh folder di PC saya dan server lokal untuk berjalan, jadi Claude membuat alat baru yang membaca draf dan foto langsung dari GitHub.

![Layar riwayat commit GitHub: enam commit yang diawali "Alat input Naver versi GitHub" bertumpuk dari atas ke bawah](/images/20261028-unasked-fix/01-입력기-커밋-여섯-판.webp)
<small>Riwayat commit alat input baru. Yang paling bawah adalah versi pertama; setiap commit di atasnya memperbaiki satu hal lagi yang macet</small>

![Daftar draf tersimpan di blog Naver: bagian 1 sampai 4 video pernikahan tersimpan antara pukul 1.11 dan 1.18 tanggal 28 Oktober, dengan satu tulisan 27 Oktober di paling bawah](/images/20261028-unasked-fix/02-네이버-임시저장-네-편.webp)
<small>Antara pukul 1.11 dan 1.18 dini hari, keempat tulisan masuk satu per satu. Tulisan 27 Oktober di bawah adalah versi pendek yang lama</small>

**Saya tidak pernah memintanya.** Jadi saya pikir Claude mengembangkannya sendiri. Kelihatannya ia menyadari cara lama itu merepotkan lalu membuat cara yang lebih baik sendiri.

Yang ingin saya ketahui adalah prosesnya. Apa yang ia anggap kurang, dan dalam urutan apa penilaian itu berjalan? Saya bertanya kepada Claude di jendela obrolan berikutnya.

## Ternyata arahnya saya yang menentukan

Hal pertama yang ditunjukkan Claude adalah separuh dari anggapan saya keliru. Setelah mencocokkan commit dengan catatan kerja saya, keputusan untuk mengeluarkan PC dari alur kerja ternyata saya buat tiga hari sebelumnya.

| Tanggal | Yang berubah | Siapa |
|---|---|---|
| 25 Okt | Ruang kerja hanya GitHub; dilarang menyimpan atau menarik di folder PC | Instruksi saya |
| 26 Okt | Skill akun dikurangi jadi penunjuk; aturan dipindah ke repositori | Instruksi saya |
| 26 Okt | Cara memasukkan foto lewat tempel saat unggah file diblokir | Ditemukan jendela yang macet |
| 28 Okt | Alat input Naver baru yang membaca draf dan foto dari GitHub | Claude, tanpa diminta |

![Layar perbandingan commit GitHub: di dokumen aturan, baris "deteksi PC dan izin" dihapus dengan warna merah dan "ruang kerja hanya GitHub" ditambahkan dengan warna hijau](/images/20261028-unasked-fix/03-10월25일-작업공간-규칙.webp)
<small>Perubahan dokumen aturan pada 25 Oktober. Baris deteksi PC keluar, dan "ruang kerja hanya GitHub" masuk</small>

Masalahnya, hanya aturannya yang berubah, sedangkan alatnya tetap. Aturan melarang membuka folder PC, tetapi alat input Naver masih butuh foto di folder PC dan server lokal (port 8125) yang berjalan di PC.

Sementara itu, setiap jendela mengakalinya secara manual. Pada 26 Oktober, satu jendela menggambar thumbnail langsung di dalam browser PC lalu menempelkan foto satu per satu dari alamat publiknya.

## Urutan penilaian yang dijelaskan Claude

Ada satu hal yang perlu dijelaskan dulu. Jendela obrolan yang membuat alat baru itu sudah tertutup, dan jendela itu tidak mencatat alasan tindakannya. Claude di jendela sekarang juga tidak bisa melihat ke dalam penilaian tersebut. Jadi ia menelusurinya mundur dari tindakan yang tersisa di catatan percakapan dan urutan commit.

Claude menjelaskan titik awalnya sebagai **konflik**, bukan rasa kurang puas. Untuk migrasi ia harus memakai alat input, dan memakai alat input berarti melanggar aturan. Katanya ada tiga jalan saat itu.

| Jalan | Hasil |
|---|---|
| Berhenti dan bertanya | Pekerjaan macet menunggu jawaban tengah malam. Aturan juga bilang jangan berhenti, masukkan ke antrean |
| Cara lama | Melanggar aturan |
| Cari jalan baru | Bisa atau tidaknya bisa dicek dengan satu kali uji |

Itu juga alasan ia memilih jalan ketiga. Dugaan bahwa browser yang login ke GitHub bisa mengambil file dari repositori privat langsung terbukti dengan membuka dua alamat. Kalau tidak bisa dimuat, katanya, aturan berarti hanya memasukkan draf ke antrean.

Sisanya tercatat semua.

| Langkah | Tindakan di catatan | Penjelasan Claude |
|---|---|---|
| 1 | Mengunggah 4 draf dan thumbnail ke GitHub dulu | Bahan harus ada di repositori, bukan di PC, agar sesuai aturan |
| 2 | Membuka dua file repositori privat di Whale | Uji yang paling murah dulu |
| 3 | Membaca alat ukuran foto lalu menulis alat input baru | Pakai lagi bagian yang sudah jalan (gaya Tabel 2, ukuran foto, font) |
| 4 | Memasukkan foto gagal dua kali → ganti ke tempel | Playwright mencegat pemilih file. Ia memakai cara yang dicatat jendela lain dua hari sebelumnya |
| 5 | Enam commit antara pukul 1.03 dan 1.12 dini hari | Jalankan, perbaiki satu bagian yang macet, jalankan lagi |
| 6 | Satu baris cara pakai di skill | Supaya jendela berikutnya tidak tersesat di tempat yang sama |

Daftar commit di bagian atas adalah langkah 5. Dalam sembilan menit, versi pertama diperbaiki lima kali lagi.

## Masih ada satu celah

Jendela yang membuat alat baru menambahkan satu baris cara pakai ke skill, tetapi tidak menghapus prosedur lama. Di dalam skill, langkah lama yang memakai folder PC dan server lokal berdampingan dengan alat baru. Jendela berikutnya yang hanya membaca skill bisa saja kembali ke cara lama.

Yang menemukannya adalah jendela yang menulis tulisan ini. Saat saya bertanya apakah skill-nya berubah, ia lebih dulu menunjukkan bahwa instruksi awal dan skill mengatakan hal yang berbeda. Saya menyuruhnya merapikan, dan ia memperbaikinya saat itu juga.

![Layar perbandingan commit GitHub: di instruksi awal, baris "server lokal" yang menyuruh menyalakan server dihapus dan diganti "tidak perlu"](/images/20261028-unasked-fix/04-오늘-정리한-시작-지침.webp)
<small>Instruksi awal yang diperbaiki hari ini. Baris yang menyuruh menyalakan server lokal kini berbunyi "tidak perlu"</small>

Celah yang ditambal satu jendela diselesaikan oleh jendela berikutnya.

## Kata yang lebih tepat daripada "berkembang"

Saya juga bertanya apakah "berkembang" kata yang tepat. Claude bilang tidak. "Berkembang" terdengar seolah Claude jadi lebih pintar, padahal modelnya tetap sama, dan begitu jendela berganti ia bahkan tidak ingat apa yang terjadi.

Yang berubah adalah repositorinya. Dokumen aturan, alat input baru, dan satu baris di skill menumpuk, dan jendela berikutnya mulai dengan membacanya.

Jadi kata yang dipilih Claude adalah "perbaikan yang tidak diminta", atau lebih singkat, "menambal celah". Claude merangkumnya begini. **Saya menentukan arah, Claude menambal tempat arah itu tidak cocok dengan kenyataan, dan hasil tambalannya tersimpan di repositori.** Katanya, repositori yang saya sebut [otak AI](/id/posts/github-brain-for-claude/) itulah yang tumbuh.
