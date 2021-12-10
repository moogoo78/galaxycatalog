from flask import (
    Blueprint,
    render_template,
    jsonify,
)
from sqlalchemy import select

from app.database import session
from app.models import (
    Collection,
    Person
)

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template('admin.html', name='foo')

@admin.route('/api/collection')
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


@admin.route('/api/person')
def get_person_list():
    data = {
        'header': (
            ('pk', '#', {'align':'right'}),
            ('full_name', '全名', {'align': 'right'}),
            ('other_name', '英文名', {'align': 'right'}),
            ('is_collector', '採集者', {'align': 'right', 'type': 'radio'}),
            ('is_identifier', '鑒定者', {'align': 'right', 'type': 'radio'}),
        ),
        'rows': [],
        'model': 'person',
    }
    #result = session.execute(select(Collection))
    #print (result.all())
    rows = Person.query.all()
    for r in rows:
        data['rows'].append(r.todict())

    return jsonify(data)

@admin.route('/api/collection/<int:collection_id>/form')
def get_collection_form(collection_id):
    '''for frontend to render <form>'''
    col = session.get(Collection, collection_id)
    #print(col.todict())

    result = Person.query.filter(Person.is_collector==True).all()
    collector_list = [{'id': x.id, 'label': f'{x.full_name} ({x.other_name})'} for x in result]
    field_number = ''
    if fns := col.field_numbers:
        field_number = fns[0].todict().get('value', '')
    data = {
        'form': (
            (('collector_id', '採集者', 'x_collector', col.collector_id, {'options': collector_list}),
             ('field_number', '採集號', 'text', field_number)),
            (('collect_date', '採集日期', 'text', col.collect_date),),
            (('units', '標本', 'x_units', [x.todict() for x in col.units]),),
        ),
        'value': {
            'collector_id': col.collector_id,
        },
    }


    return jsonify(data)

@admin.route('/api/collection/<int:collection_id>/edit')
def post_collection(collection_id):
    #return redirect('')
    pass
