---
title: "Alat input blog Naver saya kini membaca dari GitHub, tanpa folder PC dan server lokal"
date: 2026-10-28
series: ai-orchestration
part: 3
summary: "Saat saya menyerahkan migrasi ke Naver, Claude mengubah alat input yang butuh folder PC dan server lokal menjadi alat yang membaca draf dan foto langsung dari GitHub. Kini PC cukup menyediakan satu jendela browser Whale yang sudah login."
cover: /images/20261028-naver-driver-github/01-입력기-커밋-여섯-판.webp
---

Saat saya menyerahkan migrasi ke Naver, Claude mengubah alat input yang butuh folder PC dan server lokal menjadi alat yang membaca draf dan foto langsung dari GitHub. Kini PC cukup menyediakan satu jendela browser Whale yang sudah login.

Dini hari 28 Oktober, saya meminta Claude memindahkan bagian 1 sampai 4 seri video pernikahan saya ke Naver. Sambil menyimpan empat draf, Claude menulis ulang alat input, lalu setelah selesai menyebutkannya dalam satu baris di akhir laporan.

![Layar riwayat commit GitHub: enam commit yang diawali "Alat input Naver versi GitHub" bertumpuk dari atas ke bawah](/images/20261028-naver-driver-github/01-입력기-커밋-여섯-판.webp)
<small>Riwayat commit alat input baru. Yang paling bawah adalah versi pertama; setiap commit di atasnya memperbaiki satu bagian lagi yang macet</small>

Alat input adalah skrip yang mengendalikan browser Whale lewat Playwright untuk memasukkan tulisan ke editor Naver. Kalau Playwright adalah tangan, alat input adalah lembar urutan kerja yang dipegang tangan itu. Ia membaca draf dan menentukan urutan memasukkan judul, subjudul bergaya kutipan, tabel, dan foto. Yang berubah kali ini bukan tangannya, melainkan lembar urutan kerjanya.

## Aturannya hanya GitHub, tapi alatnya terikat ke PC

Pada 25 Oktober, saya menetapkan GitHub sebagai satu-satunya ruang kerja blog. Tujuannya agar dari akun, PC, atau ponsel mana pun pekerjaan berlanjut dari keadaan yang sama. Jadi saya menambahkan aturan di instruksi awal: tidak ada yang disimpan ke atau ditarik dari folder PC.

![Layar perbandingan commit GitHub: di instruksi awal, baris "deteksi PC dan izin" dihapus dengan warna merah dan "ruang kerja hanya GitHub" ditambahkan dengan warna hijau](/images/20261028-naver-driver-github/02-작업공간-규칙-변경.webp)
<small>Perubahan instruksi awal pada 25 Oktober. Baris deteksi PC keluar, dan "ruang kerja hanya GitHub" masuk</small>

Namun alat input Naver masih bekerja dengan cara lama. Untuk menjalankan alat lama (`naver_driver.js`), PC perlu persiapan seperti ini.

| Persiapan | Alat input lama |
|---|---|
| Draf | Dibaca lewat server lokal yang dinyalakan dengan `python -m http.server 8125` di folder blog-notes pada PC |
| Foto | Disalin ke folder PC yang diizinkan Playwright dengan nama `up0.webp`, `up1.webp` |
| Pengaturan | Alat disalin ke folder yang sama sebagai `drv.js`, nama draf dan posisi awal ditulis di `naver_params.json` |
| Masukkan foto | Saat berhenti di foto, unggah dengan `browser_file_upload` lalu jalankan lagi |

Menurut aturan, semua langkah yang memakai folder PC tidak boleh dilakukan. Dua hari sebelumnya, untuk tulisan ulasan Coupang, sebuah jendela cloud mengakalinya secara manual. Ia menggambar thumbnail di kanvas dalam browser PC dan menempelkan foto satu per satu dari alamat publiknya di Kang PD Log.

## Diuji dulu dengan dua alamat

Claude lebih dulu mengunggah empat draf dan thumbnail ke repositori privat di GitHub. Bahan harus ada di repositori, bukan di PC, agar sesuai aturan.

Lalu, alih-alih langsung membuat alat, ia menguji dulu. Whale sudah login ke akun GitHub saya. Kalau begitu, bisakah Whale juga mengambil file dari repositori privat? Ia meminta dua alamat lewat Whale, satu thumbnail dan satu draf, dan keduanya berhasil diterima.

**Satu uji itu menghapus kebutuhan akan folder PC.** Draf dan thumbnail diambil dari repositori privat, dan foto isi diambil dari alamat Kang PD Log yang sudah terbit. Bagian depan draf cukup diberi satu baris nama folder foto (`imgdir`).

| Bahan | Asal yang dipakai alat baru |
|---|---|
| Draf | Repositori privat blog-notes, `네이버/*.md` |
| Thumbnail | Repositori yang sama, `네이버/썸네일/<slug>.webp` |
| Foto isi | Alamat publik Kang PD Log `images/<imgdir>/` |
| Alat itu sendiri | Repositori yang sama, `tools/naver_driver_gh.js`, dikunci dengan commit |

Alatnya sendiri juga dibaca dari GitHub. Caranya dengan memberi tahu Whale, "ambil alat input di commit ini lalu jalankan." Karena commit-nya dikunci, setiap perbaikan cukup dengan mengunggah commit baru lalu memanggilnya lagi dengan nomor baru.

```js
async (page) => {
  const SHA = '<커밋 번호>';
  const s = await (await page.request.get('https://github.com/kelvin-KangPD/blog-notes/raw/' + SHA + '/tools/naver_driver_gh.js')).text();
  return await eval(s)(page, { SHA, FILE: '<원고 파일>', PHASE: 'write', START: 0, CLEAR: true });
}
```

Setiap potongan kode Playwright harus selesai dalam 60 detik. Karena itu setelah 40 detik alat mengembalikan nomor yang berarti "sudah dimasukkan sampai sini" lalu berhenti. Kalau dipanggil lagi dari nomor itu, ia melanjutkan. Setelah isi selesai, tahap penyelesaian dipanggil terpisah untuk menerapkan gaya "Tabel 2", ukuran foto (foto utama lebar 600, foto yang melebar dikembalikan ke lebar aslinya), font isi NanumSquare, dan menyimpan draf.

## Foto macet dua kali

Saat versi pertama dijalankan, yang macet adalah foto. Dalam sembilan menit terkumpul enam commit.

| Waktu | Yang diubah | Alasan |
|---|---|---|
| 1.03 | Versi pertama | Membaca draf dan foto dari GitHub tanpa folder PC atau server lokal |
| 1.04 | Foto lewat pemilih file | Memasukkan file langsung ke kolom input tidak berhasil |
| 1.06 | Foto lewat peristiwa tempel | Playwright mencegat pemilih file sehingga tidak bisa dipakai |
| 1.06 | Tidak membuka ulang kalau sudah di layar menulis | Setiap kali dibuka ulang muncul dialog "tinggalkan halaman ini?" |
| 1.09 | Tangkap kursor sebelum foto, cek posisi | Tepat setelah tabel atau foto kursor tidak tertangkap, dan foto masuk ke paling atas tulisan |
| 1.12 | Kosongkan isi sepenuhnya, tunggu foto lebih lama | Mencegah mulai dengan tulisan yang belum bersih dan lanjut sebelum foto selesai masuk |

Cara tempel itu ditemukan jendela obrolan lain dua hari sebelumnya dan dicatat di skill. Kalau foto dibuat sebagai objek file di dalam editor lalu dikirim bersama sinyal "baru saja terjadi tempel", editor Naver menerima foto itu seolah orang menekan Ctrl+V. Saat macet, Claude mengambil catatan itu dan memasukkannya ke alat.

Masalah kursor masih tertulis di komentar alat. Tepat setelah tabel masuk, editor tidak bisa memindahkan kursor keluar dari tabel, sehingga foto mendarat di paling atas tulisan. Kini kursor ditangkap dengan mengetik satu huruf lalu menghapusnya, dan setelah foto masuk alat memeriksa apakah blok terakhir adalah foto, lalu berhenti kalau bukan.

## Empat tulisan masuk dalam tujuh menit

Dengan versi keenam, bagian 1 sampai 4 masuk satu per satu. Bagian 1 tersimpan pukul 1.11 dan bagian 4 pukul 1.18.

![Daftar draf tersimpan di blog Naver: bagian 1 sampai 4 video pernikahan tersimpan antara pukul 1.11 dan 1.18 tanggal 28 Oktober, dengan satu tulisan 27 Oktober di paling bawah](/images/20261028-naver-driver-github/03-네이버-임시저장-네-편.webp)
<small>Daftar draf tersimpan. Bagian 1 sampai 4 masuk berurutan dalam tujuh menit. Tulisan 27 Oktober di bawah adalah versi pendek yang lama</small>

**Tidak ada persiapan apa pun di PC.** Tidak menyalakan server, tidak menyalin foto. Selama jendela Whale terbuka dan login ke Naver serta GitHub, selesai.

Setelah selesai, Claude menulis satu baris cara pakai alat baru di skill. Namun prosedur lama untuk alat lama masih tersisa. Beberapa jam kemudian jendela lain menunjukkan bahwa instruksi awal dan skill mengatakan hal berbeda, dan ketika saya menyuruhnya merapikan, ia menghapus prosedur lama itu.

![Layar perbandingan commit GitHub: di instruksi awal, baris "server lokal" yang menyuruh menyalakan server dihapus dan diganti "tidak perlu"](/images/20261028-naver-driver-github/04-시작-지침-정리.webp)
<small>Instruksi awal yang sudah dirapikan. Baris yang menyuruh menyalakan server lokal kini berbunyi "tidak perlu"</small>

## PC hanya meminjamkan satu jendela Whale

Dalam susunan sekarang, tugas PC hanya menyediakan browser yang sudah login. Pekerjaan berjalan di jendela cloud, dan Whale di PC hanya dipinjam saat diperlukan.

| Pekerjaan | Di mana |
|---|---|
| Draf, thumbnail, konversi foto, terbit di Kang PD Log dan situs multibahasa | Jendela cloud (repositori GitHub) |
| Simpan draf Naver | Jendela Whale di PC (alat baru membaca dari GitHub lalu memasukkan) |
| Tangkapan layar web | Diambil di jendela Whale PC lalu dibawa ke cloud |
| Saat Whale mati | Hanya draf yang dibuat dan diantrekan di `네이버/대기열.md` |

Tangkapan layar di tulisan ini juga didapat dengan cara yang sama. Whale memotret layar GitHub, mengembalikan data gambar dalam bentuk teks, lalu sisi cloud mengubahnya lagi menjadi file gambar. Font untuk thumbnail tidak bisa diunduh dari cloud karena alamatnya diblokir, jadi Whale yang mengambilnya dan menyerahkannya dalam dua bagian.

Di titik aturan dan alat tidak cocok, ia tidak berhenti dan tidak melanggar aturan, melainkan mengecek dulu dengan uji murah apakah ada jalan. Lalu ia memperbaiki satu hal demi satu hal sampai keempat tulisan masuk. Untuk yang satu ini, Claude bekerja dengan baik.
