from flask import Flask, request, jsonify

app = Flask(__name__)

# Data sementara (seperti database)
tasks = [
    {"id": 1, "judul": "Belajar Flask", "status": "belum selesai"},
    {"id": 2, "judul": "Kerjakan UTS", "status": "belum selesai"}
]

# ----------------------------
# 1. GET - Ambil semua data
# ----------------------------
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# ----------------------------
# 2. GET - Ambil data berdasarkan ID
# ----------------------------
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({"message": "Data tidak ditemukan"}), 404

# ----------------------------
# 3. POST - Tambah data baru
# ----------------------------
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "judul": data['judul'],
        "status": data.get('status', 'belum selesai')
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# ----------------------------
# 4. PUT - Update seluruh data
# ----------------------------
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['judul'] = data['judul']
            task['status'] = data['status']
            return jsonify(task)
    return jsonify({"message": "Data tidak ditemukan"}), 404

# ----------------------------
# 5. PATCH - Update sebagian data
# ----------------------------
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def patch_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            if 'judul' in data:
                task['judul'] = data['judul']
            if 'status' in data:
                task['status'] = data['status']
            return jsonify(task)
    return jsonify({"message": "Data tidak ditemukan"}), 404

# ----------------------------
# 6. DELETE - Hapus data
# ----------------------------
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Data berhasil dihapus"})
    return jsonify({"message": "Data tidak ditemukan"}), 404

# ----------------------------
# Menjalankan server
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
