from flask import Blueprint, jsonify

from . import db_session

from .jobs import Jobs

blueprint = Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    json_object = jsonify(
        {
            'jobs': [
                item.to_dict(only=Jobs.__table__.columns.keys()) for item in jobs
            ]
        }
    )
    db_sess.close()
    return json_object


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(job_id: int):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        db_sess.close()
        return jsonify({'error': 'Not found'})

    json_object = jsonify(
        {
            'job': job.to_dict(only=Jobs.__table__.columns.keys())
        }
    )
    db_sess.close()
    return json_object
