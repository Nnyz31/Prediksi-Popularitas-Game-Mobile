Project Overview

Google Play Store merupakan platform distribusi aplikasi terbesar untuk perangkat Android yang menyediakan jutaan aplikasi dan game. Persaingan yang tinggi menyebabkan pengembang perlu memahami faktor-faktor yang memengaruhi popularitas sebuah game agar dapat meningkatkan jumlah pengguna dan keberhasilan produk yang dikembangkan.

Popularitas game dapat diukur melalui jumlah instalasi (installs) yang diperoleh. Dengan memanfaatkan Machine Learning, proses prediksi popularitas game dapat dilakukan secara otomatis berdasarkan karakteristik aplikasi seperti rating dan jumlah ulasan pengguna.

Pada proyek ini dilakukan pembangunan model klasifikasi untuk memprediksi tingkat popularitas game mobile menggunakan algoritma Decision Tree dan Random Forest. Dataset yang digunakan berasal dari Kaggle yaitu Google Play Store Apps Dataset.

💡 Manfaat Proyek:

✔ Membantu pengembang memahami faktor yang memengaruhi popularitas game.

✔ Memberikan gambaran mengenai performa algoritma klasifikasi pada data aplikasi mobile.

✔ Menentukan model terbaik yang dapat digunakan untuk prediksi popularitas game.

Referensi:

Google Play Store Apps Dataset (Kaggle)

Lalu untuk Business Understanding:

Business Understanding
Problem Statements
Bagaimana membangun model Machine Learning yang mampu memprediksi popularitas game mobile berdasarkan karakteristik aplikasi?
Algoritma manakah yang memberikan performa lebih baik dalam melakukan prediksi popularitas game, Decision Tree atau Random Forest?
Goals
Mengembangkan model klasifikasi untuk memprediksi apakah sebuah game termasuk populer atau tidak populer.
Membandingkan performa algoritma Decision Tree dan Random Forest menggunakan metrik evaluasi klasifikasi.
Solution Approach

✔ Decision Tree

Menggunakan struktur pohon keputusan untuk melakukan klasifikasi berdasarkan fitur-fitur yang tersedia.

✔ Random Forest

Menggunakan kumpulan beberapa pohon keputusan (ensemble learning) sehingga mampu menghasilkan prediksi yang lebih stabil dan akurat.

Menurut saya, bagian berikutnya yang paling penting adalah Data Understanding karena harus disesuaikan dengan hasil dataset yang Anda gunakan.

Sebelum saya lanjut membuatkan Data Understanding, Data Preparation, Modeling, Evaluation, dan Kesimpulan lengkap, saya perlu melihat hasil notebook Anda, terutama:

Output df.info()
Output df.shape
Jumlah data setelah filter Category == 'GAME'
Akurasi Decision Tree
Akurasi Random Forest
