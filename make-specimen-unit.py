import json


a = open('specimen.json')

m = a.read()
data = json.loads(m)

out_unit = open('out-unit.sql', 'w')
out_gathering = open('out-gathering.sql', 'w')
out_field_number = open('out-field-number.sql', 'w')

id_map = open('out-id-map.json')
n = id_map.read()
mapp = json.loads(n)

def make_unit_gathering(data, pk):
    source_data = '{}'
    sd_dict = {}
    if sd := data['source_data']:
        sd_dict = json.dumps(sd)
        source_data = sd_dict.replace("'", "''")

    collect_date = data['collect_date']
    #collector_text = data
    biotope = ''
    accession_number = ''
    unit_id = pk
    record_number = data['field_number'].replace('::', '')
    collector_id = mapp['person']['{}'.format(data['collector'])]
    sql_list = []
    sql = f"INSERT INTO field_number (unit_id, record_number, collector_id) VALUE({unit_id}, '{record_number}', {collector_id});\n"
    sql_list.append(sql)
    sql = f"INSERT INTO gathering (collect_date, collector_id) VALUES ('{collect_date}', {collector_id});\n"
    sql_list.append(sql)
    sql = f"INSERT INTO unit (gathering_id, accession_number, source_data) VALUES ({dataset_id}, {gathering_id}, '{accession_number}', '{source_data}');\n"
    sql_list.append(sql)
    return sql_list


count = 0
pk = 0
for i in data:
    if i['model'] == 'specimen.accession':
        pk += 1
        print(i)
        #sql_list = make_unit_gathering(i['fields'], pk)
        #print(sql_list)
        break
        #sql = make_gathering(i['pk'], i['fields'])
        count += 1

out_unit.close()
out_gathering.close()
out_field_number.close()
print(count)
