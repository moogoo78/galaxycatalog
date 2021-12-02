from sqlalchemy import create_engine

from app.models import Unit, Gathering, Person, FieldNumber, GatheringNamedArea, NamedArea, Identification
from app.database import session

def make_person(con):
    rows = con.execute('SELECT * FROM specimen_person ORDER BY id')
    for r in rows:
        #print(r)
        org = ''
        atom_name = {}
        abbr_name = ''
        full_name = r[6]
        if len(r[1]) > 0:
            # has source_data
            org = r[1]['organAbbr']
            abbr_name = r[1]['nameAbbr']
            atom_name = {
                'en': {
                    'given_name': r[1]['firstName'],
                    'inherited_name': r[1]['lastName'],
                }
            }
            if name_other := r[1]['nameOther']:
                atom_name['other'] = name_other

        if not full_name:
            name_list = []
            if first_name := r[1]['firstName']:
                name_list.append(first_name)
            if last_name := r[1]['lastName']:
                name_list.append(last_name)
            full_name = ' '.join(name_list)

        p = Person(
            full_name=full_name,
            abbreviated_name=abbr_name,
            atomized_name=atom_name,
            source_data=r[1],
            is_collector=r[3],
            is_identifier=r[4],
            organization=org)
        session.add(p)
    session.commit()

def make_named_area(con):
    rows = con.execute('SELECT * FROM specimen_namedarea ORDER BY id')
    for r in rows:
        na = NamedArea(id=r[0], name=r[1], name_en=r[6], area_class_id=r[4], source_data=r[5])
        session.add(na)
    session.commit()

def make_unit_gathering(con):
    rows = con.execute('SELECT * FROM specimen_specimen ORDER BY id LIMIT 5')
    for r in rows:
        #print(r)
        gid = r[0]
        field_number = r[2].replace('::', '')

        # Gathering
        gath = Gathering(
            id=gid,
            collect_date=r[32],
            collector_id=r[6],
            collector_text='{}::{}'.format(r[14] if r[14] else '', r[15] if r[15] else ''),
            locality_text='{}::{}'.format(r[5] if r[5] else '', r[13] if r[13] else ''),
            altitude=r[11],
            altitude2=r[12],
            latitude_decimal=r[9],
            longitude_decimal=r[10],
        )
        if r[39] or r[41] or r[42] or r[43]:
            gath.verbatim_latitude = "{}{}°{}'{}\"".format(r[39], r[41], r[42], r[43])
        if r[40] or r[44] or r[45] or r[46]:
            gath.verbatim_longitude = "{}{}°{}'{}\"".format(r[40], r[44], r[45], r[46])
        session.add(gath)
        session.commit()

        # NamedArea
        na_list = [r[33], r[37], r[34], r[38], r[36], r[35]]
        for na in na_list:
            if na:
                gath_na = GatheringNamedArea(
                    gathering_id=gid,
                    named_area_id=na
                )
                session.add(gath_na)
        session.commit()

        rows2 = con.execute(f"SELECT * FROM specimen_accession WHERE specimen_id ={r[0]}  ORDER BY id")
        for r2 in rows2:
            acc_num = ''
            if an := r2[1]:
                acc_num = an

            # Unit
            u = Unit(
                gathering_id=gid,
                accession_number=acc_num,
                acquisition_source_text=r[47],
                source_data=r[4])
            session.add(u)
            session.commit()

            # FieldNumber
            fn = FieldNumber(
                unit_id=u.id,
                record_number=field_number,
                collector_id=r[6])
            if an2 := r2[3]:
                fn.record_number2 = an2
            session.add(fn)

            # Iden.
            iden = Identification(
                unit_id=u.id
            )
            session.add(iden)
            session.commit()

    session.commit()

def conv_hast21():
    engine2 = create_engine('postgresql+psycopg2://postgres:example@postgres:5432/hast21', convert_unicode=True)
    with engine2.connect() as con:
        #make_person(con)

        #make_named_area(con)

        make_unit_gathering(con)


