---
title: "Membuat AI bisa mengoperasikan Premiere langsung: catatan memasang Premiere MCP"
date: 2026-10-18
series: video-archive-ai
part: 3
cover: /images/20261018-premiere-mcp-setup/01-mcp-bridge-connected.webp
summary: Lewat aplikasi desktop Claude dan Premiere MCP, saya hubungkan AI supaya bisa mengoperasikan PC dan Premiere saya langsung, lalu satu per satu membereskan jebakan instalasi sampai rebutan port.
---

Lewat aplikasi desktop Claude dan Premiere MCP, saya hubungkan AI supaya bisa mengoperasikan PC dan Premiere saya langsung,
**lalu satu per satu membereskan jebakan instalasi sampai rebutan port.**

Pekerjaan di bagian 1 dan 2 bisa jalan karena koneksi ini.

## Apa yang dihubungkan, dan bagaimana

Kalau AI hanya memberi instruksi lalu saya yang mengerjakan dengan tangan, volume sebesar ini tidak mungkin selesai.

| Koneksi | Yang dikerjakan AI |
|---|---|
| Aplikasi desktop Claude + koneksi jarak jauh | Walaupun saya mengobrol dari ponsel atau dari kantor, pekerjaannya berjalan di PC rumah |
| File dan command line | Melihat daftar drive, mencocokkan hasil salinan, mengambil waktu rekam dan suara dengan ffmpeg, menjalankan skrip Python |
| Kontrol layar | Mengoperasikan 7-Zip, Premiere, dan Media Encoder dengan klik |
| Premiere MCP | Membuat sequence dan caption track lewat panel bridge di dalam Premiere, lalu menyimpan project |
| Media Encoder | Mengekspor sequence per tanggal jadi MP3 untuk transkripsi |

Kontrol layar juga ada batasnya. Di File Explorer hanya bisa klik, sementara salin, tempel, dan drag-and-drop diblokir. Jadi perangkat tanpa huruf drive seperti ponsel harus saya pindahkan sendiri.

## Premiere MCP

MCP adalah cara menghubungkan AI supaya bisa memakai program lain seperti alat kerja.
Untuk Premiere saya memakai Adobe-Premiere-Pro-MCP yang dibagikan terbuka di GitHub. Di sisi Premiere terpasang panel ekstensi "MCP Bridge", dan di dalam PC berjalan server kecil (port 8097) yang meneruskan perintah AI menjadi skrip Premiere (ExtendScript).

![Panel MCP Bridge di Premiere dalam status Connected, dengan log koneksi terlihat](/images/20261018-premiere-mcp-setup/01-mcp-bridge-connected.webp)
*Panel MCP Bridge. Perintah AI baru masuk ke Premiere kalau tulisan hijau Connected muncul.*

Pertama kali saya pasang awal September, waktu mengerjakan video pembuka pernikahan. Saya kira cukup menjalankan file instalasi, ternyata jebakannya banyak.
Bulan Oktober saya pasang juga di PC kantor, dan ada satu masalah tambahan yang hanya muncul di jaringan kantor.

| Gejala | Penyebab | Solusi |
|---|---|---|
| Aplikasi Claude sama sekali tidak menjalankan server | Aplikasi versi Store membaca file pengaturan dari lokasi lain | Daftarkan di lokasi yang sebenarnya (di bawah LocalCache) |
| Pengaturan diabaikan diam-diam | Skrip instalasi menyisipkan BOM (karakter tak terlihat) di awal file pengaturan | Simpan ulang tanpa BOM |
| Server gagal jalan | Di pengaturan hanya tertulis node, aplikasi tidak bisa menemukannya | Pakai path lengkap node.exe |
| Panel bilang Connected tapi perintah tidak masuk | Setiap jendela chat menjalankan server sendiri dan berebut satu port | Bereskan proses server yang tersisa lalu sambungkan ulang |
| Keyboard tidak berfungsi di Premiere | Panel bridge mengambil input keyboard | Tutup panel saat mengedit manual |
| Instalasi gagal di PC kantor | Node tidak memercayai sertifikat perangkat keamanan kantor | Opsi agar Node memakai penyimpanan sertifikat Windows |

## Urutan instalasi yang sudah dirapikan

Ini urutan yang saya rapikan setelah berkali-kali tersangkut. Untuk PC lain pun tinggal ikuti ini.

| Langkah | Di mana | Yang dilakukan |
|---|---|---|
| 1 | PowerShell | Cek Node.js sudah terpasang. Kalau belum, pasang lalu buka jendela baru |
| 2 | Browser | Unduh Adobe-Premiere-Pro-MCP dari GitHub sebagai ZIP dan ekstrak ke folder Documents. Kalau dipindah belakangan, koneksi ekstensi Premiere rusak, jadi langsung taruh di lokasi akhir |
| 3 | Notepad | Buka dan baca dulu isi install.bat. Kalau ada perilaku asing selain pengaturan registry, penautan folder ekstensi, instal dan build paket, serta penulisan pengaturan, hentikan |
| 4 | PowerShell | Jalankan install.bat, pastikan file server (dist\server.js) terbentuk |
| 5 | Premiere | Tutup total lalu buka lagi, buka panel Window > Extensions > MCP Bridge |
| 6 | Aplikasi Claude | Jalankan sekali lalu tutup supaya folder pengaturannya terbentuk |
| 7 | PowerShell | Daftarkan server di path file pengaturan yang sebenarnya. Simpan tanpa BOM, node pakai path lengkap |
| 8 | PowerShell | Tutup aplikasi Claude sepenuhnya lalu buka lagi. Pengaturan hanya dibaca sekali saat aplikasi dinyalakan |
| 9 | Premiere | Pastikan panel menampilkan Connected |
| 10 | Aplikasi Claude | Di chat baru, cek status koneksi, lalu suruh AI hanya membaca susunan track tanpa mengubah apa pun sebagai verifikasi |

Saya juga menetapkan urutan menyalakan sehari-hari.

| Urutan | Yang dilakukan |
|---|---|
| 1 | Tutup program MCP lain dan jendela chat Claude yang lain |
| 2 | Kalau ada server sisa yang memegang port 8097, bereskan |
| 3 | Buka Premiere, buka project dan sequence |
| 4 | Buka aplikasi Claude (server otomatis jalan) |
| 5 | Pastikan panel bridge Connected, lalu mulai kerja |
| 6 | Saat mengedit manual, tutup panelnya. Server tetap hidup, jadi begitu panel dibuka lagi langsung tersambung |

## Akhir pekan ini: rebutan port dan perbaikan bridge

Akhir pekan ini rebutan port terjadi lagi. Setiap pindah ke jendela chat baru, server dari jendela lama masih memegang port, jadi panel bilang Connected tapi perintahnya hilang begitu saja.
Awalnya saya bertahan dengan satu baris PowerShell yang membereskan semua server sisa sekaligus. Tapi harus diulang setiap kali pindah jendela chat, dan itu merepotkan.
Jadi kali ini AI memperbaiki kode bridge-nya sendiri. Server yang baru jalan meminta server lama "serahkan port-nya", lalu server lama mengalah. AI menyimulasikannya dulu di lokal, baru menerapkannya. Server baru hanya meminta selama 15 detik setelah jalan, dan server yang sudah mengalah tidak mencoba merebut kembali, cukup menunggu dengan tenang. Jadi biasanya jendela chat paling baru yang menang.
Yang diperbaiki adalah hasil build dan source aslinya sekaligus, jadi perbaikannya tetap ada walaupun nanti di-build ulang.
Meski begitu, di sesi pertama koneksinya tetap tidak mau tersambung, jadi sequence dibuat sebagai file XML dan di-import lewat kontrol layar. Mulai sesi berikutnya caption track dibuat lewat MCP sampai ke penyimpanan project.

Di tulisan berikutnya saya catat cara membuat subtitle untuk 62 jam video, dan apa saja yang saya pelajari soal menjalankan pekerjaan AI secara efisien.
