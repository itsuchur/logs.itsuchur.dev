import os
from dotenv import load_dotenv
from flask import Flask, render_template, abort, request, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
app = Flask(__name__)

# Required for normal functioning of the headers since the traffic is going through NGINX serving as a proxy
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

load_dotenv()
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://sentinel:{POSTGRES_PASSWORD}@localhost:5432/sentinel" # db
# user:password:@localhost:5432/database_name
db.init_app(app)

class Log(db.Model):
    __tablename__ = 't_logs'
    id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.BigInteger)
    raid_time = db.Column(db.DateTime(timezone=True))
    raiders_id = db.Column(db.ARRAY(db.BigInteger))

    def __repr__(self):
        return f"Log(id={self.id}, guild_id={self.guild_id}, raid_time={self.raid_time}, raiders_id={self.raiders_id})"
    
class Report(db.Model):
    __tablename__ = 't_reports'
    id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.BigInteger)
    search_initiated_by_id = db.Column(db.BigInteger)
    search_initiated_by_name = db.Column(db.Text)
    search_initiated_at = db.Column(db.DateTime(timezone=True))
    search_from = db.Column(db.DateTime(timezone=True))
    search_until = db.Column(db.DateTime(timezone=True))
    found_ids = db.Column(db.ARRAY(db.BigInteger))

    def __repr__(self):
        return f"Log(id={self.id}, guild_id={self.guild_id}.)"

@app.route('/')
def index():
    data = {'message': """Please enter the log's ID to proceed. An example of a correct URL is: https://logs.itsuchur.dev/id=1, where 1 is the ID associated with the log entry."""}
    return jsonify(data), 200
    # return render_template('index.html', servers_counter=5)

@app.route('/id=<int:log_id>', methods=['GET'])
def logs(log_id=None):
    if log_id is not None:
        log = Log.query.get(log_id)
        if log:
            return render_template('id.html', log=log)
    abort(404)

@app.route('/reports/id=<int:report_id>', methods=['GET'])
def reports(report_id=None):
    if report_id is not None:
        report = Report.query.get(report_id)
        if report:
            return render_template('report.html', report=report)
    abort(404)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    # set debug to True during development stage. !!Set debug to False before shipping to prod!!
    app.run(host='127.0.0.1', debug=False)