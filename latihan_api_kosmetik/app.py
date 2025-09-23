from flask import Flask, jsonify, request

app = Flask(__name__)

# Data awal disimpan di dalam list
kosmetik = [
    {"id": 1, "nama": "Lipstik Merah", "harga": 50000, "stok": 20},
    {"id": 2, "nama": "Bedak Tabur", "harga": 75000, "stok": 15},
    {"id": 3, "nama": "Maskara Waterproof", "harga": 65000, "stok": 10}
]

# Route utama
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Selamat datang di API Kosmetik",
        "info": "Gunakan endpoint /kosmetik untuk melihat data"
    })

# GET - Menampilkan semua produk
@app.route('/kosmetik', methods=['GET'])
def get_all_kosmetik():
    return jsonify({"success": True, "data": kosmetik}), 200

# GET - Menampilkan produk berdasarkan ID
@app.route('/kosmetik/<int:id>', methods=['GET'])
def get_kosmetik_by_id(id):
    produk = next((item for item in kosmetik if item["id"] == id), None)
    if produk:
        return jsonify({"success": True, "data": produk}), 200
    return jsonify({"success": False, "message": "Produk tidak ditemukan"}), 404

# POST - Menambahkan produk baru
@app.route('/kosmetik', methods=['POST'])
def add_kosmetik():
    data = request.get_json()
    new_id = kosmetik[-1]['id'] + 1 if kosmetik else 1
    new_produk = {
        "id": new_id,
        "nama": data.get("nama"),
        "harga": data.get("harga"),
        "stok": data.get("stok")
    }
    kosmetik.append(new_produk)
    return jsonify({
        "success": True,
        "message": "Produk berhasil ditambahkan",
        "data": new_produk
    }), 201

# PUT - Update produk berdasarkan ID
@app.route('/kosmetik/<int:id>', methods=['PUT'])
def update_kosmetik(id):
    produk = next((item for item in kosmetik if item["id"] == id), None)
    if not produk:
        return jsonify({"success": False, "message": "Produk tidak ditemukan"}), 404

    data = request.get_json()
    produk["nama"] = data.get("nama", produk["nama"])
    produk["harga"] = data.get("harga", produk["harga"])
    produk["stok"] = data.get("stok", produk["stok"])
    
    return jsonify({
        "success": True,
        "message": "Produk berhasil diperbarui",
        "data": produk
    }), 200

# DELETE - Hapus produk berdasarkan ID
@app.route('/kosmetik/<int:id>', methods=['DELETE'])
def delete_kosmetik(id):
    global kosmetik
    kosmetik = [item for item in kosmetik if item["id"] != id]
    return jsonify({
        "success": True,
        "message": f"Produk dengan ID {id} berhasil dihapus"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
