---
title: "Menulis blog Naver dengan AI, otomatisasi penuh sampai tepat sebelum simpan sementara"
date: 2026-10-19
series: naver-blog-automation
part: 1
summary: "Unggahan blog Naver yang dulu saya kerjakan manual lebih dari 30 menit sekali, kini dikerjakan AI dengan mengendalikan browser langsung: isi, foto, keterangan foto, sampai judul dimasukkan lalu disimpan sementara."
---

Unggahan blog Naver, satu tulisan per hari yang dulu saya kerjakan manual lebih dari 30 menit setiap kali,
**kini saya otomatiskan sampai AI mengendalikan browser langsung, memasukkan isi, foto, keterangan foto, dan judul, lalu menyimpannya sebagai draf.**

Kemarin untuk pertama kalinya semuanya berhasil sampai akhir.
Yang saya lakukan hanya membuka draf yang tersimpan, membacanya sekilas, lalu menekan tombol terbit.
Makna terbesar dari pekerjaan ini: hasilnya sudah cukup baik untuk langsung dipakai di pekerjaan kantor.

## Dulu begini

Saya memindahkan artikel blog perusahaan, yang ditulis pihak vendor di inblog, ke blog Naver. Artikelnya tidak disalin begitu saja. Gaya bahasa dan strukturnya saya ubah supaya cocok dengan pencarian Naver, mesin pencari utama di Korea. Kira-kira satu artikel per hari. Penulisan ulangnya sudah saya kerjakan bersama AI. Tapi setiap kali masih ada yang tersisa: memasukkannya ke editor Naver sambil mengklik sana-sini, mengunggah foto, dan menyesuaikan lagi dengan gaya saya.

Blog Naver tidak punya API resmi untuk menerbitkan tulisan. Jadi tulisan yang dibuat AI pada akhirnya harus dipindahkan dengan tangan.
Untuk mengurangi itu, saya membuat tombol bookmark (bookmarklet) dan perintah PowerShell.

| Urutan | Pelaku | Pekerjaan |
|---|---|---|
| 1 | AI | Membuat lembar kerja berisi isi tulisan, kandidat judul, daftar foto, dan keterangan foto |
| 2 | Manusia | Menyalin "perintah mengambil foto" dari lembar kerja lalu menempelkannya ke PowerShell |
| 3 | Manusia | Menekan "salin isi" lalu menempelkannya ke editor Naver |
| 4 | Manusia | Menekan bookmark "ubah format" (mengganti bentuk kutipan dan garis pemisah) |
| 5 | Manusia | Menekan bookmark "masukkan foto" sebanyak jumlah foto, memilih foto di jendela pilih file setiap kali |
| 6 | Manusia | Mengklik kolom keterangan di tiap foto lalu menempelkan keterangannya |
| 7 | Manusia | Mengetik judul, memeriksa kartu tautan, menerbitkan |

Berkat tombol-tombol itu pekerjaan memang berkurang. Tapi kalau fotonya lebih dari sepuluh, klik-nya tetap puluhan kali.
Keterangan foto gagal dimasukkan otomatis, jadi saya hanya menyalinnya ke clipboard dan menempelkannya sendiri.
**Satu tulisan paling cepat tetap makan 30 menit.**

## Cara baru: AI mengendalikan browser lewat kode

Intinya adalah Playwright MCP.
Playwright adalah alat untuk mengoperasikan browser lewat kode, dan kalau dihubungkan lewat MCP, AI bisa memakainya langsung.
AI tidak menangkap layar lalu mengklik koordinat. Ia membaca struktur halaman, memilih elemen, lalu mengoperasikannya. Karena itu cepat, dan jarang meleset.

Cara menghubungkannya seperti ini.

| Langkah | Isi |
|---|---|
| 1 | Tambahkan `--remote-debugging-port=9222` di akhir target pintasan Whale (browser buatan Naver), lalu jalankan Whale lewat pintasan itu |
| 2 | Daftarkan Playwright MCP di file pengaturan aplikasi desktop Claude, supaya terhubung ke Whale yang sudah menyala (port 9222) |
| 3 | Tutup aplikasi sepenuhnya, lalu buka lagi |

Isi file pengaturannya seperti ini. Saya sudah memakai MCP Premiere, jadi keduanya ada di sana.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest", "--cdp-endpoint", "http://localhost:9222"]
    },
    "premiere-pro": { "...": "..." }
  }
}
```

Yang penting, ini bukan membuka Whale baru, melainkan menyambung ke Whale yang biasa saya pakai.
Login Naver sudah aktif, jadi saya tidak perlu memberikan ID dan kata sandi ke AI.

## Bergulat dengan editor Naver

Editor Naver (SmartEditor) cukup rewel untuk diotomatiskan. Saya catat tempat saya benar-benar tersangkut dan cara mengatasinya.

| Masalah | Solusi |
|---|---|
| Menempel isi tulisan | Tidak memakai clipboard. Peristiwa tempel palsu dikirim langsung ke area input di dalam editor. HTML masuk apa adanya, jadi tabel, huruf tebal, dan pindah baris tetap terjaga |
| Jarak antarparagraf | Naver mengabaikan margin paragraf. Baris kosong harus dimasukkan sebagai paragraf kosong sungguhan |
| Bentuk kutipan | Kutipan yang ditempel lewat HTML selalu masuk sebagai kutipan bertanda petik. Setelah menempel, tekan kutipan lalu ganti bentuknya dengan tombol bentuk |
| Tempat foto | Di isi tulisan saya taruh baris penanda seperti <code>[📸 foto 01 &#124; keterangan: …]</code>, lalu di tempat baris itu dihapus saya tekan tombol foto |
| Menghapus baris | Tombol seleksi seperti Shift+Home ditangkap editor. Klik di ujung baris, lalu tekan Backspace sebanyak jumlah hurufnya |
| Mengunggah foto | Jendela pilih file tidak dimunculkan; file langsung dimasukkan lewat fitur unggah file Playwright. Tapi file di luar folder kerja ditolak, jadi salinannya saya taruh di folder kerja |
| Kolom keterangan | Kolom keterangan baru muncul setelah fotonya diklik. Inilah sebab penyisipan keterangan otomatis dulu gagal |
| Memeriksa unggahan | Sesaat setelah naik, alamat foto tampak seperti penanda svg. Itu normal. Tunggu beberapa detik |
| Tombol tidak mau ditekan | Tertutup panel samping atau sedang dalam animasi. Posisi tombol dihitung ulang setiap kali lalu ditekan dengan mouse |
| Tab tersembunyi | Kalau tab ada di belakang, layar tidak merespons. Bawa tab ke depan dulu, baru lanjut |

Kode untuk menempel isi tulisan seperti ini. Setelah bagian ini berhasil, sisanya ikut terpecahkan.

```js
async (page) => {
  const HTML = `...HTML isi tulisan...`;
  const fr = page.frame({ name: 'mainFrame' }) || page.mainFrame();
  await fr.locator('.se-component.se-text .se-text-paragraph').first().click();
  await page.waitForTimeout(400);
  await fr.evaluate((h) => {
    const ib = [...document.querySelectorAll('iframe')]
      .map(i => { try { return i.contentDocument } catch (e) { return null } })
      .find(x => x && x.body && x.body.isContentEditable);
    const W = ib.defaultView, dt = new W.DataTransfer();
    dt.setData('text/html', h);
    dt.setData('text/plain', h.replace(/<[^>]+>/g, ''));
    ib.body.dispatchEvent(new W.ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
  }, HTML);
  await page.waitForTimeout(4000);
}
```

Foto dikerjakan satu per satu secara berulang. Sekali dijalankan, ia melakukan "memasukkan keterangan ke foto sebelumnya" dan "menghapus penanda 📸 berikutnya lalu menekan tombol foto" sekaligus, dan begitu masuk ke keadaan pilih file, foto dengan nomor urut itu diunggah. Terus berputar sampai tidak ada lagi penanda 📸.

## Tombol terbit tidak boleh tertekan

Langkah terakhir adalah simpan sementara. Yang paling saya jaga di sini adalah agar tombol terbit tidak tertekan, bahkan karena kecelakaan.
Tombol di editor Naver berlabel bahasa Korea: 저장 berarti "simpan" dan 발행 berarti "terbit". Label tombol dibaca dulu, dan kalau bukan 저장 atau mengandung 발행, kode berhenti tanpa menekan.
Keberhasilan dipastikan dari angka di samping tombol simpan yang bertambah 1.

```js
async (page) => {
  const fr = page.frame({ name: 'mainFrame' }) || page.mainFrame();
  const btn = fr.locator('button[class*="save_btn"]').first();
  const label = (await btn.textContent()).trim();
  if (!/저장/.test(label) || /발행/.test(label)) return { error: label };
  const cnt = () => fr.evaluate(() => document.querySelector('[class*="save_btn"]').parentElement.textContent);
  const before = await cnt();
  const b = await btn.boundingBox();
  await page.mouse.click(b.x + b.width / 2, b.y + b.height / 2);
  await page.waitForTimeout(2500);
  return { before, after: await cnt() };
}
```

Penerbitan sengaja saya sisakan untuk manusia.
Tulisannya menjadi publik dan terbit atas nama perusahaan, jadi pemeriksaan terakhir saya yang pegang.
**Selain pemeriksaan itu, tidak ada lagi yang perlu saya sentuh.**

| Tahap | Dulu | Sekarang |
|---|---|---|
| Menulis | AI | AI |
| Menyiapkan foto | Menempelkan perintah ke PowerShell | AI |
| Memasukkan isi | Salin dan tempel | AI |
| Merapikan format | Tombol bookmark | AI |
| Foto dan keterangan | Klik sebanyak jumlah foto, tempel keterangan | AI |
| Judul dan kartu tautan | Manusia | AI |
| Simpan sementara | Manusia | AI |
| Pemeriksaan dan penerbitan | Manusia | Manusia |

## Saya buatkan juga untuk blog pribadi

Cara yang sama saya rapikan sebagai skill terpisah agar bisa dipakai juga untuk blog Naver pribadi saya.
Bedanya dengan versi kantor ada di gaya bahasa. Saya minta AI membaca beberapa tulisan lama saya, lalu mengambil kebiasaan saya, yaitu akhiran kalimat, emoji, panjang paragraf, dan penataan foto, dalam bentuk tabel, dan menulis dengan gaya itu.
Cukup beri folder foto dan catatan kasar, maka tulisan dibuat lalu disimpan sementara.

| Item | Isi |
|---|---|
| Masukan | Jalur folder foto + catatan |
| Gaya bahasa | Sekali di awal, membaca struktur 5 tulisan terakhir lalu menyimpan profil gaya |
| Tidak mengarang | Nama toko, harga, dan tanggal yang tidak ada di catatan atau foto tidak ditulis, ditandai `[perlu dicek]` |
| Foto | HEIC diubah ke JPG, yang terlalu besar dikecilkan, dan kalau mau memakai salinan tanpa data lokasi |
| Akhir | Simpan sementara. Terbitnya saya sendiri |

File skill-nya saya buka untuk umum (isinya dalam bahasa Korea). Tinggal dimasukkan ke Claude sebagai skill.

| File | Isi |
|---|---|
| [SKILL.md](https://kelvin-kangpd.github.io/files/naver-personal-draft/SKILL.md) | Seluruh prosedur dan kode |
| [my-blog.md](https://kelvin-kangpd.github.io/files/naver-personal-draft/my-blog.md) | Formulir kosong profil gaya bahasa |

Di PC rumah saya juga sedang memasang koneksi yang sama, tapi berhenti di tengah. File pengaturan sudah dimasukkan, tetapi aplikasi Claude belum juga mengenali Playwright. Saya akan mulai lagi dengan memeriksa file pengaturan mana yang dibaca aplikasi di tab pengembang pada pengaturannya.

Di tulisan berikutnya saya menulis apa yang saya pikirkan setelah ini berhasil. Kenapa setelah alat ini ada, saya merasa harus bergegas.
