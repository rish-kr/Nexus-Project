from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import uuid
import os
from datetime import datetime

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# ── MongoDB CONNECTION ────────────────────────────────────────
client = MongoClient('mongodb://localhost:27017/')
db = client['nexus_db']
registrations_col = db['registrations']

print("[NEXUS] MongoDB connected ✓")

# ── ROUTES ───────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate required fields
    required = ['full_name', 'student_id', 'email', 'event_id', 'event_name']
    for field in required:
        if not data.get(field, '').strip():
            return jsonify({'success': False, 'error': f'Missing field: {field}'}), 400

    reg_id = 'NEXUS-' + str(uuid.uuid4()).replace('-', '').upper()[:6]
    created_at = datetime.utcnow().isoformat()

    try:
        doc = {
            'id':          reg_id,
            'full_name':   data['full_name'].strip(),
            'student_id':  data['student_id'].strip(),
            'email':       data['email'].strip(),
            'event_id':    data['event_id'].strip(),
            'event_name':  data['event_name'].strip(),
            'semester':    data.get('semester', ''),
            'department':  data.get('department', ''),
            'notes':       data.get('notes', ''),
            'created_at':  created_at
        }

        registrations_col.insert_one(doc)

        print(f"[NEXUS] Registration saved: {reg_id} — {data['full_name']} → {data['event_name']}")

        return jsonify({
            'success': True,
            'registration_id': reg_id,
            'message': 'Registration confirmed. Node synchronized.',
            'timestamp': created_at
        }), 201

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/registrations', methods=['GET'])
def get_all():
    """Admin endpoint — list all registrations."""
    rows = list(registrations_col.find({}, {'_id': 0}).sort('created_at', -1))
    return jsonify({'count': len(rows), 'data': rows})


@app.route('/api/stats', methods=['GET'])
def stats():
    total = registrations_col.count_documents({})

    pipeline = [
        {'$group': {'_id': '$event_name', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ]
    by_event = [{'event': r['_id'], 'count': r['count']} for r in registrations_col.aggregate(pipeline)]

    return jsonify({'total_registrations': total, 'by_event': by_event})


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'NEXUS ONLINE', 'timestamp': datetime.utcnow().isoformat()})


# ── MAIN ─────────────────────────────────────────────────────
if __name__ == '__main__':
    print("[NEXUS] Starting server on http://localhost:5000")
    app.run(debug=True, port=5000)
