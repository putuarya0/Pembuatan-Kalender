# Pembuatan-Kalender
Program ini dibuat untuk menampilkan kalender dari bulan dan tahun yang dimasukkan oleh pengguna. Program memvalidasi input agar hanya menerima bulan (1-12) dan tahun (0-9999).

## Cara Penggunaan

1. Jalankan program.
2. Masukkan nomor bulan (1-12).
3. Masukkan tahun (0-9999).
4. Program akan menampilkan kalender dari bulan dan tahun yang dimasukkan.

### Contoh Input dan Output

#### Contoh 1: Input yang Valid
- **Input:**
  ```
  Masukkan bulan: 5
  Masukkan tahun: 2023
  ```
- **Output:**
  ```
       May 2023
  Mo Tu We Th Fr Sa Su
   1  2  3  4  5  6  7
   8  9 10 11 12 13 14
  15 16 17 18 19 20 21
  22 23 24 25 26 27 28
  29 30 31
  ```

#### Contoh 2: Input yang Tidak Valid (Bulan)
- **Input:**
  ```
  Masukkan bulan: 13
  Masukkan tahun: 2023
  ```
- **Output:**
  ```
  Bulan tidak valid
  ```

#### Contoh 3: Input yang Tidak Valid (Tahun)
- **Input:**
  ```
  Masukkan bulan: 5
  Masukkan tahun: 10000
  ```
- **Output:**
  ```
  Tahun tidak valid
  ```

#### Contoh 4: Input yang Tidak Valid (Bulan dan Tahun)
- **Input:**
  ```
  Masukkan bulan: 0
  Masukkan tahun: -5
  ```
- **Output:**
  ```
  Bulan dan tahun tidak valid
  ```

## Persyaratan

- Python versi 3.x

## Modul yang Digunakan

- **calendar**: Modul bawaan Python untuk menampilkan kalender.

## Penjelasan Program

1. **Input**: Program meminta pengguna untuk memasukkan bulan dan tahun.
2. **Validasi**: Program memeriksa apakah bulan berada dalam rentang 1-12 dan tahun dalam rentang 0-9999.
3. **Output**:
   - Jika input valid, program akan menampilkan kalender untuk bulan dan tahun tersebut.
   - Jika input tidak valid, program akan memberikan pesan kesalahan yang sesuai.

## Lisensi

Program ini dapat digunakan dan dimodifikasi sesuai kebutuhan. Tidak ada lisensi khusus yang diterapkan.
