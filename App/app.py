# app.py
from flask import Flask, render_template, request
from astar import astar
from kecamatan import kecamatan
from bus import bus_transportation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', kecamatan=kecamatan.keys())

@app.route('/search', methods=['POST'])
def search():
    start_location = request.form['start_location']
    end_location = request.form['end_location']
    fuel_price = float(request.form['fuel_price'])
    fuel_efficiency = float(request.form['fuel_efficiency'])

    result = astar(kecamatan, start_location, end_location)
    path, total_distance = result

    if isinstance(path, list):
        total_cost = (total_distance / fuel_efficiency) * fuel_price
        total_fuel_used = total_distance / fuel_efficiency

        bus_info = {}
        for location in path:
            if location in bus_transportation:
                bus_info[location] = {
                    'transport': bus_transportation[location]['transport'],
                    'routes': bus_transportation[location]['routes']
                }
    else:
        total_distance = 0
        total_cost = 0
        total_fuel_used = 0
        bus_info = {}

    return render_template(
        'result.html',
        start=start_location,
        end=end_location,
        path=path,
        graph=kecamatan,
        total_distance=total_distance,
        total_cost=total_cost,
        total_fuel_used=total_fuel_used,
        bus_info=bus_info 
    )

if __name__ == '__main__':
    app.run(debug=True)
