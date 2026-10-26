---
title: "Saya membuat film untuk upacara pernikahan kami dengan Higgsfield: cara menjelaskan adegan ke AI"
date: 2026-10-27
series: wedding-ai
part: 1
cover: /images/20261027-higgsfield-wedding-film/01-물병-건네는-컷.webp
summary: "Saya membuat film yang diputar di tengah upacara pernikahan kami dengan Higgsfield. Yang paling lama bukan membuat videonya, tetapi menjelaskan setiap adegan ke AI dengan tepat."
---

Saya membuat film yang diputar di tengah upacara pernikahan kami dengan Higgsfield. Yang paling lama bukan membuat videonya, tetapi menjelaskan setiap adegan ke AI dengan tepat.

Film ini diputar di pernikahan kami pada 19 September, tepat sebelum pengantin pria masuk. Saya tidak memakai aktor; sebagian besar adegan yang menampilkan saya dan istri dibuat dengan AI. Semua adegan video di tulisan ini dibuat dengan AI.

![Seorang pria lelah duduk di bangku taman sementara tangan yang memegang botol air terulur masuk](/images/20261027-higgsfield-wedding-film/01-물병-건네는-컷.webp)
<small>Shot bangku dari sudut rendah. Tangan yang menyodorkan air adalah tangan istri saya (dibuat AI)</small>

## Ceritanya dimulai dengan bertanya kepada AI tentang kebahagiaan

Saya menulis storyboard lebih dulu. Kamera, arahan, dan suara untuk setiap potongan dimasukkan ke satu lembar.

![Storyboard adegan 1, studio, dengan kolom nomor potongan, sketsa, kamera, arahan, dan audio](/images/20261027-higgsfield-wedding-film/02-식중영상-콘티.webp)
<small>Adegan 1 di storyboard. Saat dikerjakan kami menyebutnya film sebelum upacara</small>

| Adegan | Isi |
|---|---|
| Studio | Larut malam saya bertanya kepada AI cara paling pasti agar seseorang bahagia. Jawabannya: "Keluarlah, akan muncul seseorang, dan sesuatu akan berkilat di depan matamu" |
| Pencarian | Wajah saya tetap di tengah layar, hanya latarnya yang berganti: kafe, taman, bulan, gunung bersalju, jalan di musim panas |
| Bangku | Saat saya duduk kelelahan di bangku, seseorang menyodorkan botol air. Ketika saya mendongak, cahaya dari belakang memudar dan di sana ada istri saya. Foto dan video asli yang kami ambil melintas di dalam pupil mata saya |
| Gedung | Dari ekspresi itu langsung berpindah ke saya yang memakai tuksedo dan berbicara langsung kepada para tamu |

Layar obrolan AI di monitor tidak dibuat dengan AI. Saya membuat layar obrolan itu terpisah dengan HTML, merekamnya, lalu menempelkannya ke monitor di Premiere. Untuk layar yang teksnya harus persis, menempel lebih cepat daripada membuat.

![Jendela obrolan AI di monitor dengan teks "kilat"](/images/20261027-higgsfield-wedding-film/03-AI-대화-화면.webp)
<small>Kata "kilat" dalam jawaban AI muncul lagi di bagian akhir</small>

## Saya membuat tempatnya dulu, lalu memasukkan orang

Di Higgsfield, tempat dan karakter bisa disimpan sebagai elemen lalu dipanggil di prompt. Saya membuat studio, taman, kafe, bulan, gunung bersalju, dan jalan musim panas sebagai elemen tempat.

![Layar elemen Higgsfield yang menampilkan tempat bg-snow-5, bg-moon-4, room, bg-summer, dan bg-park](/images/20261027-higgsfield-wedding-film/04-힉스필드-장소-요소.webp)
<small>Sebagian elemen tempat yang disimpan di Higgsfield</small>

Urutannya tidak pernah berubah. **Buat gambar tempatnya dulu, lalu gambar orang di dalam tempat itu, lalu gerakkan gambar tersebut.** Kalau tempat dan orang dimasukkan terpisah di tahap video, keduanya tidak menyatu. Gambar yang saya berikan sebagai frame pertama masuk ke video apa adanya.

Untuk adegan pencarian yang latarnya berganti, saya merekam klip swafoto 15 detik dengan GoPro dan mengubahnya dengan Seedance 2.5 Edit. Gerakan berjalan saya tetap, hanya latar dan pakaiannya yang diganti.

![Seorang pria berbaju astronaut berdiri di bulan dengan Bumi di belakangnya](/images/20261027-higgsfield-wedding-film/05-배경만-바뀌는-컷.webp)
<small>Bulan di adegan pencarian. Posisi wajah tetap, hanya latarnya yang berganti</small>

## Untuk wajah, sudut lebih penting daripada jumlah foto

Awalnya saya membuat elemen karakter dari satu foto wajah, tetapi wajahnya lemah. Jadi saya memasukkan foto langsung sebagai referensi, bukan elemen. Namun menambah foto tidak membuat hasilnya lebih baik.

Ketika foto depan, samping, dan menunduk dimasukkan bersamaan, sudut-sudutnya dirata-rata dan wajahnya jadi kabur. Satu foto dengan sudut yang mirip dengan shot yang ingin dibuat bekerja paling baik, dan kalau tidak ada, saya memakai satu foto depan yang bagus dan satu foto samping yang bagus.

![Tiga foto orang yang sama berdampingan: samping, 45 derajat, dan depan](/images/20261027-higgsfield-wedding-film/06-얼굴-레퍼런스-각도.webp)
<small>Referensi wajah saya. Setiap sudut saya unggah terpisah dan hanya yang cocok dengan shot yang dipilih</small>

Saya juga membuat karakter Soul di Higgsfield, tetapi itu khusus untuk Soul Cinema dan tidak bisa dipanggil dari Nano Banana Pro atau Cinema Studio. Akhirnya tidak saya pakai.

## Tujuh kali percobaan untuk satu shot bangku

Pada shot sudut tinggi di adegan bangku, saat pertama ditonton harus terlihat seperti taman biasa, dan saat ditonton lagi penonton baru sadar, "oh, dia ada di sana", lalu melihat istri saya. Ia harus tersembunyi di balik dedaunan. Shot ini saya jalankan sekitar tujuh kali di Nano Banana Pro, dan setiap kali macet saya mengganti kata-katanya.

| Masalah | Kata yang diubah |
|---|---|
| Jarak | "Berjarak 7 meter" diabaikan. Menulisnya sebagai rasio layar, seperti "sosoknya mengisi seperdelapan tinggi frame", membuat kamera mundur |
| Sudut | Menulis tinggi, jarak, dan sudut sekaligus membuatnya bertabrakan. Cukup tinggi dan jarak horizontal, sudutnya mengikuti |
| Sembunyi | Menumpuk `not visible` dan `heavily shaded` membuat seluruh orang jadi luntur. Saya menuliskan keadaannya: "wajahnya tersembunyi di balik daun" |
| Daun | Hanya menulis "dekat lensa" membuatnya jadi pohon di latar. Saya menyimpulkan jaraknya harus dipatok, misalnya 30cm dari lensa, tetapi tetap tidak pernah benar-benar berhasil |
| Jalan | Meminta arah diagonal menghasilkan sudut yang canggung. "Kurang lebih horizontal" terlihat alami |
| Bangku | Kalimat andaian seperti "dua orang bisa duduk berdampingan" diabaikan atau malah menggambar dua orang. Saya menulis "tepat satu bangku, dengan ruang untuk satu orang lagi di sampingnya" |

Saat gambar yang sudah ada saya masukkan lagi sebagai referensi lalu minta diperbaiki, referensinya sering mengalahkan instruksi teks. Dalam kasus itu **saya membuat gambar dengan elemen bermasalah dihapus dulu, lalu menambahkan hanya yang saya mau di atasnya.** Kreditnya dua kali lipat, tetapi lebih murah daripada mengulang perbaikan yang sama terus-menerus.

Bahkan satu kata pun bermasalah. Saya sempat menulis `soft veil` untuk menggambarkan lens flare yang tipis, lalu menghapusnya. Dalam prompt yang berisi pengantin, gaun putih, dan pernikahan, "veil" bisa dibaca sebagai kerudung pengantin.

Yang tidak pernah berhasil adalah dedaunannya. Selama tujuh percobaan daunnya tidak pernah menutupi istri saya, jadi saya menyelesaikan gambarnya dengan Gemini, mengunggahnya ke Higgsfield, lalu menggerakkannya.

![Jalan setapak taman dan bangku dilihat dari atas, dengan orang yang duduk terlihat di balik dedaunan depan](/images/20261027-higgsfield-wedding-film/07-벤치-하이앵글.webp)
<small>Shot sudut tinggi yang sudah jadi. Istri saya duduk di balik daun di kanan bawah (dibuat AI)</small>

## Setiap jendela obrolan baru meninggalkan lubang

Saya bekerja bergantian di akun Claude saya dan akun istri saya. Saat percakapan memanjang, saya merangkumnya dan pindah ke percakapan baru, tetapi rangkuman hanya menyimpan kesimpulan dan menghilangkan alasan di baliknya. Bekerja dari rangkuman membuat saya mengulang kesalahan yang sama, dan ketika akhirnya seluruh percakapan sebelumnya saya ekspor ke Word, panjangnya lebih dari 230 halaman.

File itu saya unggah ke Google Drive dan Claude hanya membaca bagian yang diperlukan. Baru saat itulah keputusan-keputusan kembali, misalnya shot botol air di adegan bangku adalah satu take 12 detik, bukan dua potongan, atau ekspresi kaget harus dibuat dengan hanya memutar kepala sementara badan tetap. Itulah yang kemudian membuat saya [membangun otak AI di GitHub](/id/posts/github-brain-for-claude/).

Kredit juga jadi pikiran. Akun saya memakai paket Plus: 1.000 kredit masuk setiap tanggal 3 pukul 11 pagi waktu Korea, dan sisa kredit tidak terbawa ke bulan berikutnya, melainkan hilang. Saya memastikannya dengan menggulir seluruh riwayat transaksi. Satu gambar memakan 2 kredit, dan satu video memakan 20 hingga lebih dari 130 kredit per sekali jalan tergantung model dan kualitas. Pada 30 Agustus saja, yang sebagian besar untuk video, saya menghabiskan hampir 300 kredit.

## Kami memutarnya di pernikahan

Film yang sudah jadi diputar di upacara kami pada 19 September. Gambarnya berakhir sekitar 2 menit 15 detik dengan "Semuanya, silakan menoleh ke belakang", lalu setelahnya saya menyambungkan musik di atas layar hitam dalam file yang sama. Montase di dalam pupil memakai foto dan video asli yang kami ambil berdua.
