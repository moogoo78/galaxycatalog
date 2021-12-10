from flask import (
    Blueprint,
    render_template,
    jsonify,
    request,
)
from sqlalchemy import select

from app.database import session
from app.models import (
    Collection,
    Person
)

api = Blueprint('api', __name__)

@api.route('/api/collection')
def get_collection_list():
    data = {
        'header': (
            ('pk', '#', {'align':'right'}),
            ('collector__full_name', '採集者', {'align': 'right'}),
            ('display_field_number', '採集號', {'align': 'right', 'type': 'x_field_number'}),
            ('collect_date', '採集日期', {'align': 'right'}),
        ),
        'rows': [],
        'model': 'collection',
    }
    #result = session.execute(select(Collection))
    #print (result.all())
    rows = Collection.query.all()
    for r in rows:
        data['rows'].append(r.todict())
    #for r in result.all():s
    #print (r[0].collect_date, r[0].collector_id, r[0].collector.full_name)
    #d = {
    #        'collect_date': r[0].collect_date,
    #        'collector': r[0].collector.full_name
    #    }
    #data.append(d)

    return jsonify(data)


@api.route('/person')
def get_person_list():
    keyword = request.args.get('q', '')
    rows = []
    if keyword:
        result = Person.query.filter(Person.full_name.ilike(f'%{keyword}%') | Person.atomized_name['en']['given_name'].astext.ilike(f'%{keyword}%') | Person.atomized_name['en']['inherited_name'].astext.ilike(f'%{keyword}%')).all()
    else:
        result = Person.query.all()

    for r in result:
        rows.append(r.todict())

    return jsonify(rows)
