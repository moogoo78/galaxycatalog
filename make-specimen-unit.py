import json


a = open('specimen.json')
m = a.read()
data = json.loads(m)

out_unit = open('out-unit.sql', 'w')
out_gathering = open('out-gathering.sql', 'w')
out_field_number = open('out-field-number.sql', 'w')

def make_unit(pk, data):
    source_data = data['source_data'].replace("'", "''")

    sql = f"INSERT INTO unit (dataset_id, gathering_id, accession_number, source_data) VALUES ({dataset_id}, {gathering_id}, '{accession_number}', '{source_data}')"
    return sql

def make_gathering(pk, data):
    sql = f"INSERT INTO unit (dataset_id, gathering_id, accession_number, source_data) VALUES ({dataset_id}, {gathering_id}, '{accession_number}', '{source_data}')"
    return sql

def make_field_number():
    sql = f"INSERT INTO unit (dataset_id, gathering_id, accession_number, source_data) VALUES ({dataset_id}, {gathering_id}, '{accession_number}', '{source_data}')"
    return sql

count = 0
for i in data:
    if i['model'] == 'specimen.unit':
        sql = make_unit(i['pk'], i['fields'])
        print(sql)
        break
        #sql = make_gathering(i['pk'], i['fields'])
        count += 1

out_unit.close()
out_gathering.close()
out_field_number.close()
print(count)
