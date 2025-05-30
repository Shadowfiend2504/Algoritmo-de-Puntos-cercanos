from flask import Flask, render_template, request
import math
import random
import time

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

def divide_y_venceras(points):
    def closest_pair(px, py):
        n = len(px)
        if n <= 3:
            return fuerza_bruta(px)
        mid = n // 2
        Qx = px[:mid]
        Rx = px[mid:]
        midpoint = px[mid][0]
        Qy = list(filter(lambda x: x[0] <= midpoint, py))
        Ry = list(filter(lambda x: x[0] > midpoint, py))
        (p1, q1, dist1) = closest_pair(Qx, Qy)
        (p2, q2, dist2) = closest_pair(Rx, Ry)
        if dist1 < dist2:
            d = dist1
            mn = (p1, q1)
        else:
            d = dist2
            mn = (p2, q2)
        strip = [p for p in py if abs(p[0] - midpoint) < d]
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                p, q = strip[i], strip[j]
                dst = math.dist(p, q)
                if dst < d:
                    d = dst
                    mn = (p, q)
        return mn[0], mn[1], d
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair(px, py)

# K-D Tree simple para demo (solo para 2D y búsqueda del par más cercano)
from scipy.spatial import KDTree
def kd_tree_method(points):
    tree = KDTree(points)
    min_dist = float('inf')
    pair = (None, None)
    for i, p in enumerate(points):
        d, idx = tree.query(p, k=2)
        if d[1] < min_dist:
            min_dist = d[1]
            pair = (p, points[idx[1]])
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
    t0 = time.perf_counter()
    closest_brute = fuerza_bruta(points)
    t1 = time.perf_counter()
    time_brute = t1 - t0

    t0 = time.perf_counter()
    closest_divide = divide_y_venceras(points)
    t1 = time.perf_counter()
    time_divide = t1 - t0

    t0 = time.perf_counter()
    closest_kdtree = kd_tree_method(points)
    t1 = time.perf_counter()
    time_kdtree = t1 - t0

    return render_template(
        'index.html',
        points=points,
        closest_brute=closest_brute,
        closest_divide=closest_divide,
        closest_kdtree=closest_kdtree,
        time_brute=time_brute,
        time_divide=time_divide,
        time_kdtree=time_kdtree,
        num_points=num_points
    )

if __name__ == '__main__':
    app.run(debug=True)