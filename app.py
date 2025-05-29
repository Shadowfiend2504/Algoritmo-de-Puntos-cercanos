from flask import Flask, render_template, request
import math
import random

app = Flask(__name__)

def fuerza_bruta(points):
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = math.dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair[0], pair[1], min_dist

@app.route('/', methods=['GET', 'POST'])
def home():
    num_points = 10
    if request.method == 'POST':
        if request.form.get('action') == 'random':
            try:
                num_points = int(request.form['num_points'])
                num_points = max(2, min(num_points, 30))
            except Exception:
                num_points = 10
    points = [(random.uniform(1, 10), random.uniform(1, 10)) for _ in range(num_points)]
    closest = fuerza_bruta(points)
    return render_template('index.html', points=points, closest=closest, num_points=num_points)

if __name__ == '__main__':
    app.run(debug=True)