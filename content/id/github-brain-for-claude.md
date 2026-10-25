---
title: "Capek menjelaskan ulang di setiap chat Claude, saya membuat otak AI di GitHub"
date: 2026-10-26
series: ai-orchestration
part: 1
summary: "Supaya hasilnya sama dari perangkat atau jendela chat mana pun, saya memindahkan aturan dan status kerja ke repositori GitHub di luar Claude. Setelah seminggu mencoba, jendela baru kini melanjutkan pekerjaan hanya dari satu kalimat: “sambungkan blog”."
cover: /images/20261026-github-brain/01-블로그-연결-시작판.webp
---

Supaya hasilnya sama dari perangkat atau jendela chat mana pun saya memberi perintah, **saya membuat otak AI di repositori GitHub di luar Claude.**

Makin sering memakai Claude, makin sering saya memberi pekerjaan dari PC rumah, lalu dari laptop, lalu dari ponsel.
Kadang di jendela chat ini, kadang di jendela itu. Semuanya jadi terlalu rumit.
Padahal setiap membuka jendela chat baru, saya harus memuat tulisan sebelumnya dan menjelaskan sudah sampai mana. Itu benar-benar melelahkan.

Saya sampaikan dulu: pekerjaan ini adalah bagian dari proses membangun orkestrasi, dan tulisan ini catatan kerjanya.
Jujur, menurut saya ini cara yang cukup tidak efisien. Pasti sudah banyak orang yang membangun cara yang jauh lebih efisien.
Tetap saja, saya tinggalkan di sini untuk berbagi proses yang saya jalani.

![Layar "papan mulai koneksi blog": panduan satu halaman agar tiga akun dan beberapa PC memulai pekerjaan dengan urutan yang sama](/images/20261026-github-brain/01-블로그-연결-시작판.webp)

## Yang saya mau cuma satu

Menaruh otak di web, lalu dari perangkat mana pun saya meminta, permintaan itu melewati otak tersebut (GitHub) dan mengikuti prosedur yang sudah ditetapkan (skill, dokumen md) sehingga hasilnya selalu konsisten.
Dari luar kelihatannya "bukannya tinggal begitu saja?", tapi ternyata tidak mudah.
Hampir seminggu saya habiskan untuk membangun sistem ini. Banyak sekali jendela chat, banyak sekali tes, banyak sekali token terbuang.
Dan sampai sekarang masih terus saya optimalkan.

Beginilah lingkungan kerja saya. Masalahnya, semuanya berjalan sendiri-sendiri.

| Bagian | Yang saya pakai |
|---|---|
| Perangkat | PC rumah, PC kantor, laptop, ponsel |
| Akun Claude | Dua pribadi, satu kantor. Tiga akun |
| Jendela chat | Chat aplikasi desktop, tab Code, sesi cloud, aplikasi seluler |
| Hasil | Kang PD Log, situs multibahasa Cutroom Notes (5 bahasa), blog Naver |

Claude juga punya memori. Tapi memori itu menumpuk terpisah di tiap akun.
Memori satu akun kemasukan aturan blog kantor, akun lain kemasukan aturan blog pribadi. Jendela baru jadi mengikuti aturan yang salah.
Jadi saya putuskan menyimpan ingatan itu di luar Claude, bukan di dalamnya.

## Yang saya coba selama seminggu

Saya tidak langsung sampai di struktur yang sekarang. Percobaan yang gagal justru lebih banyak.

| Tanggal | Percobaan | Hasil |
|---|---|---|
| 10/23 | Merancang struktur: saya menulis instruksi di satu dokumen di repositori, lalu program pemantau mengeceknya setiap 1–2 jam dan mengirim pekerjaan ke jendela chat khusus per bidang (blog, Naver, Premiere) | Baru menentukan arah |
| 10/24 | Memindahkan antrean tugas ke GitHub Issues. Membuat 11 label (perlu dipilah, menunggu, sedang dikerjakan, terhambat, per penanggung jawab, per PC), template issue, dan dokumen aturan operasional | Kerangkanya berdiri |
| 10/24 | Menjalankan tugas terjadwal "sesi komando" setiap 2 jam dari pukul 09.00 sampai 23.00 untuk memilah dan membagikan issue baru | Pemilahan berjalan baik. Membuka jendela chat penanggung jawab tidak bisa |
| 10/24 | Workflow GitHub Actions yang menjalankan terjemahan otomatis lewat Gemini API | Tidak stabil karena error 429 dan 503, token juga lebih boros, jadi saya batalkan |
| 10/24 | Melepas semuanya dan merangkum jadi satu skill yang menjalankan prosedur tetap sampai selesai dari satu perintah: "ayo tulis blog" | Titik awal cara yang sekarang |
| 10/25 | Struktur bersama untuk tiga akun dan beberapa PC. Aslinya hanya satu repositori, akun dan PC hanya menyimpan pintu masuk | Papan mulai di atas lahir di sini |
| 10/25 | Berhenti menyimpan ke folder PC juga. Ruang kerjanya hanya GitHub | Struktur sekarang |
| 10/26 | Skill pintu masuk dipangkas jadi tiga baris, semua aturan dipindah ke repositori | Pintu masuk v2 |

Saya cukup berharap pada Gemini API. Rasanya bagus kalau pekerjaan seperti terjemahan bisa diserahkan tanpa terikat batas Claude.
Tapi ternyata saya harus meyakinkan Gemini dan Claude sekaligus. Kalau salah satu saja meleset, beban kerjanya jadi dua kali lipat.
Jadi untuk sekarang saya putuskan pakai Claude saja.

Saya juga mencoba tugas terjadwal yang mengecek Git setiap selang waktu tertentu, supaya pekerjaan berjalan sendiri setiap ada file yang berubah.
Masalahnya, setiap kali saya mengedit buku aturan (dokumen aturan menulis), itu juga terhitung perubahan dan memicu pengecekan. Token cuma bocor.
Selain itu, sesi yang dijalankan tugas terjadwal tidak punya fitur untuk membuka jendela chat baru. Saya jalankan dua kali untuk memastikan.
Akhirnya pemantauan otomatis saya tutup sebagai kegagalan. Kalaupun dibuat, akan saya pasang paling akhir, setelah seluruh rancangan selesai.

## Struktur sekarang: pintu masuk tipis, otak di repositori

![Diagram: dari perangkat mana pun permintaan datang, ia melewati pintu masuk lalu menghasilkan keluaran sesuai aturan di repositori GitHub](/images/20261026-github-brain/02-저장소-뇌-구조도.webp)

Diagram ini saya gambar sendiri. Kuncinya, hampir tidak ada yang disimpan di akun dan PC.

| Lapisan | Isinya | Di mana |
|---|---|---|
| Pintu masuk | Instruksi singkat: kalau saya bilang "sambungkan blog", baca repositori dulu | Satu skill per akun (blog-connect), dan satu blok instruksi global di PC yang memakai Claude Code |
| Otak | Instruksi awal, log kerja, buku aturan, skill prosedur menulis | Repositori privat blog-notes |
| Hasil | Tulisan, terjemahan, foto | Dua repositori publik (Kang PD Log, Cutroom Notes) |

Saya tidak menulis aturan di pintu masuk. Kalau ditulis, versinya akan berbeda di tiap akun, dan setiap perbaikan berarti harus mengedit tiga tempat.
Tugas pintu masuk hanya "pergi ke repositori dan baca dengan urutan ini". Saya memberi nomor versi (v1) pada pintu masuk, dan kalau tidak cocok dengan nomor di instruksi awal repositori, jendela akan bilang satu baris "tolong perbarui pintu masuknya". Awalnya v1, lalu sehari kemudian jadi v2 karena alasan yang saya tulis di bawah.

![Bagian "pertama kali di akun baru" pada papan mulai, terbuka menampilkan cara mendaftarkan skill pintu masuk blog-connect dengan menempelkan teks lengkapnya](/images/20261026-github-brain/03-새-계정-입구-스킬.webp)

Saat menambah akun baru, cukup ikuti bagian ini. Kalau jendelanya tidak bisa membaca repositori, saya tempelkan seluruh teks skill lalu mendaftarkannya.

![Daftar file repositori privat blog-notes: folder skill, rencana, Naver, foto masuk, serta CLAUDE.md dan log kerja](/images/20261026-github-brain/04-비공개-저장소-blog-notes.webp)

Inilah repositori privat yang berperan sebagai otak. Jendela baru hanya membaca ini, dengan urutan ini.

| Urutan | File | Yang dibaca |
|---|---|---|
| 1 | CLAUDE.md | Semuanya. Instruksi awal yang pendek |
| 2 | 작업일지.md (log kerja) | Hanya "status sekarang". Dilarang membaca semuanya |
| 3 | 계획/준구블로그_법전.md (buku aturan) | Hanya bab yang diperlukan untuk pekerjaan saat itu |
| 4 | .claude/skills/blog-write | Hanya bagian prosedur menulis yang relevan |

Membaca seluruhnya saya larang karena token. Membaca seluruh log kerja setiap kali saja sudah menggerus batas.
Saat selesai, jendela harus memperbarui "status sekarang" di log kerja lalu commit dan push. **Pekerjaan yang belum di-push tidak terlihat di perangkat lain.**

Di tengah jalan memang sempat ada kecelakaan. Jendela lain mengambil buku aturan blog kantor dan bekerja dengan itu.
Di bagian paling atas folder kerja ada dokumen kantor yang namanya mengandung kata "buku aturan", jadi dokumen itu yang muncul duluan di pencarian.
Maka saya tegaskan di instruksi awal: "buku aturan blog-blog ini hanya file ini". Saya juga menambahkan baris agar ia mencari di buku aturan dulu sebelum menanyakan aturan seperti ukuran foto kepada saya.

![Bagian "kalau tidak berhasil" pada papan mulai: gejala yang benar-benar saya alami, seperti ditanya blog yang mana atau bekerja dengan buku aturan kantor, beserta penyebab dan solusinya](/images/20261026-github-brain/05-안-될-때.webp)

Gejala yang benar-benar saya alami saya kumpulkan satu per satu di bagian "kalau tidak berhasil" pada papan mulai.

## HTML papan mulai juga saya tinggalkan

Foto paling atas itulah papan mulainya. Setiap menambah akun baru atau PC baru saya selalu bingung, jadi saya buat HTML satu halaman.
Isinya tujuh bagian: saat membuka chat, saat selesai, pertama kali di akun baru, pertama kali di PC baru, progres sekarang, kalau tidak berhasil, dan di mana semuanya berada.
Awalnya setiap perintah hanya punya tombol "salin". Di versi publik, tombolnya saya hapus dan saya simpan ulang dengan semua perintah dan kalimat terbuka penuh.

[Buka versi publik papan mulai](https://kelvin-kangpd.github.io/files/ai-brain/start-board.html)

Isinya sesuai keadaan siang hari 25 Oktober. Setelah itu berubah sekali lagi menjadi "tidak menyimpan ke folder PC, hanya memakai GitHub", jadi jalur folder PC dan perintah push PowerShell di papan itu sekarang hampir tidak saya pakai. Beberapa sebutan terkait kantor saya ganti dengan istilah umum. Skill pintu masuk juga berubah ke v2 sehari kemudian, jadi teks skill di papan mulai itu masih v1.

![Daftar file repositori publik Kang PD Log, dengan kelvin-KangPD dan claude sama-sama tercatat sebagai penulis commit](/images/20261026-github-brain/06-공개-저장소-강PD로그.webp)

Inilah repositori publik tempat hasil menumpuk. Di riwayat commit, nama saya dan claude tercatat bersama. Dari jendela mana pun pekerjaannya, hasilnya berkumpul di sini.

Tulisan ini juga dibuat dengan struktur itu. Hari ini saya hanya bilang "ayo tulis blog" di jendela chat baru.
Jendela itu membaca skill pintu masuk, mengambil repositori dari GitHub, membaca log kerja, dan melaporkan tugas berikutnya dalam satu baris. Ia tidak bertanya blog yang mana.
Saat pertama mengambil repositori, sempat tersendat sekali karena tidak ada autentikasi, lalu diambil ulang dengan cara menambahkan repositori ke sesi. Hambatan kecil seperti ini masih tersisa.

## Sehari kemudian, pintu masuk dipangkas sekali lagi

Pada malam hari saya membuat papan mulai, strukturnya saya ubah lagi. Masalah datang beruntun.

Satu jendela, padahal sedang berjalan di PC rumah, bilang "ini jendela cloud, jadi pekerjaan Naver harus dilanjutkan di PC rumah."
Di tengah percakapan sambungan ke PC sempat putus lalu tersambung lagi, dan ia memutuskan tanpa memeriksanya.
Setelah saya tegur, ia malah membuat prosedur untuk membedakan PC rumah dan PC kantor, lalu mengambil akses ke drive D.
Yang saya mau justru kebalikannya. **Tidak boleh ada yang disimpan di PC mana pun, supaya pekerjaan bisa dilanjutkan dari PC lain atau ponsel.**

Jadi saya tetapkan tiga hal.

| Prinsip | Isi |
|---|---|
| Ruang kerja | Hanya GitHub. Jendela mengambil repositori, bekerja di sana, dan langsung push dari sana. Folder PC tidak dibuka dan tidak ditulisi |
| Naver | Kalau jendela tidak bisa menyentuh Naver, ia tidak berhenti. Ia menambah satu baris ke file antrean md, lalu jendela yang tersambung ke Playwright menyelesaikan antrean itu sekaligus |
| Akun lain | Selama GitHub tersambung, akun mana pun mengerjakan hal yang sama |

Untuk menerapkannya, skill pintu masuk saya ubah tiga kali dalam sehari. Setiap kali saya harus menekan "simpan skill" lagi di akun.
Saya sudah bilang aturan tidak ditulis di pintu masuk, tapi skill v1 yang sebenarnya berisi urutan membuka repositori, urutan membaca, sampai apa yang dilakukan di akhir.
Artinya setiap ada aturan yang berubah, saya harus mengurus ketiga akun. Waktu saya tanya kenapa tidak begini dari awal, jawabannya ia menyalin skill buatan jendela sebelumnya apa adanya dan tidak melihat aturan yang tertulis di dua tempat sebagai masalah.

Pintu masuk v2 hanya meminta tiga hal.

| Urutan | Pintu masuk v2 |
|---|---|
| 1 | Ambil blog-notes dari GitHub. Jangan buka folder PC |
| 2 | Baca CLAUDE.md di repositori dan ikuti. Kalau berbeda dengan skill atau memori, repositori yang dipakai |
| 3 | Kalau tidak ada cara mengambilnya, sampaikan dalam satu baris lalu berhenti. Jangan bekerja dari ingatan atau tebakan |

Semua aturan lainnya pindah ke CLAUDE.md. Sekarang mengubah aturan sama sekali tidak menyentuh akun.

Ada satu masalah lagi. Jendela baru mengajak mengerjakan ulang tiga tulisan Naver yang sudah saya rapikan dan terbitkan.
Tulisannya sudah terbit, tapi nilai status di file draf dan antreannya tidak saya ubah. Saya tambahkan satu baris: kalau menerbitkan di Naver, ubah keduanya saat itu juga.

Lalu saya uji lagi di jendela baru. Yang saya kirim hanya dua baris: "ayo tulis blog baru, percakapan ini mulai di PC rumah."

![Di jendela chat baru, setelah "ayo tulis blog baru", ia mengambil repositori, menyelesaikan persiapan, lalu melaporkan folder foto masuk, antrean Naver, dan kandidat tulisan berikutnya dalam tabel](/images/20261026-github-brain/07-새-창-시험.webp)

Jendela itu mengambil repositori, menyelesaikan persiapan, lalu memberi tahu bahwa folder foto masuk kosong dan tidak ada draf Naver yang menunggu.
Ia menampilkan kandidat "tulisan berikutnya" dari log kerja dalam tabel, dan bilang sisa perbaikan terjemahan akan dikerjakan sekalian.
Ia tidak bertanya blog yang mana, dan tidak meminta saya membuka folder PC.

Yang tersisa adalah pemantauan otomatis. Sekarang saya masih harus membuka jendela dan mengucapkan satu kalimat.
Setelah rancangannya selesai semua, baru saya coba pasang di bagian paling akhir.
