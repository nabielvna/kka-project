from flask import Flask, render_template, request
from astar import astar

app = Flask(__name__)

# Contoh data kecamatan dengan informasi tambahan
from kecamatan import kecamatan

@app.route('/')
def index():
    return render_template('index.html', kecamatan=kecamatan.keys())

@app.route('/search', methods=['POST'])
def search():
    start_location = request.form['start_location']
    end_location = request.form['end_location']
    fuel_price = float(request.form['fuel_price'])
    fuel_efficiency = float(request.form['fuel_efficiency'])

    path = astar(kecamatan, start_location, end_location)

    if isinstance(path, list):
        # Menghitung total jarak, biaya, dan bensin
        total_distance = sum(kecamatan[kecamatan_path]['neighbors'][kecamatan_path_next] for kecamatan_path, kecamatan_path_next in zip(path, path[1:]))
        total_cost = (total_distance / fuel_efficiency) * fuel_price
        total_fuel_used = total_distance / fuel_efficiency
    else:
        # Setel nilai default jika tidak ada jalur yang ditemukan
        total_distance = 0
        total_cost = 0
        total_fuel_used = 0

    return render_template('result.html', start=start_location, end=end_location, path=path, graph=kecamatan, total_distance=total_distance, total_cost=total_cost, total_fuel_used=total_fuel_used)

if __name__ == '__main__':
    app.run(debug=True)
