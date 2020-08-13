@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/icons', 'icon-72x72.png')

@app.route('/icons/<string:filename>')
def icons(filename):
    return send_from_directory('static/icons', filename)
