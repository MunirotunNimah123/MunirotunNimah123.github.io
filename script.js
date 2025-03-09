let data = []; // Array untuk menyimpan data

function tampilkanData() {
    let tabel = document.getElementById("dataMahasiswa");
    tabel.innerHTML = ""; // Hapus isi tabel sebelum update

    data.forEach((item, index) => {
        let row = `<tr>
            <td>${index + 1}</td>
            <td>${item.nama}</td>
            <td>${item.jurusan}</td>
            <td>${item.usia}</td>
            <td>
                <button onclick="editData(${index})">Edit</button>
                <button onclick="hapusData(${index})">Hapus</button>
            </td>
        </tr>`;
        tabel.innerHTML += row;
    });
}

function tambahData() {
    let nama = document.getElementById("nama").value;
    let jurusan = document.getElementById("jurusan").value;
    let usia = document.getElementById("usia").value;

    if (nama && jurusan && usia) {
        data.push({ nama, jurusan, usia }); // Tambahkan data ke array
        tampilkanData();

        // Kosongkan input setelah menambah data
        document.getElementById("nama").value = "";
        document.getElementById("jurusan").value = "";
        document.getElementById("usia").value = "";
    } else {
        alert("Harap isi semua kolom!");
    }
}

function editData(index) {
    let namaBaru = prompt("Masukkan Nama Baru:", data[index].nama);
    let jurusanBaru = prompt("Masukkan Jurusan Baru:", data[index].jurusan);
    let usiaBaru = prompt("Masukkan Usia Baru:", data[index].usia);

    if (namaBaru && jurusanBaru && usiaBaru) {
        data[index] = { nama: namaBaru, jurusan: jurusanBaru, usia: usiaBaru };
        tampilkanData();
    }
}

function hapusData(index) {
    if (confirm("Yakin ingin menghapus data ini?")) {
        data.splice(index, 1); // Hapus data dari array
        tampilkanData();
    }
}

tampilkanData();
