import json
#from app.models import Person

#from app.database import session

a = open('specimen.json')
m = a.read()
data = json.loads(m)

out = open('out.sql', 'w')

def make_person(data):
    full_name = data.get('name', '')
    abbreviated_name = ''
    is_collector = data['is_collector']
    is_identifier = data['is_identifier']
    organization = ''
    source_data = '{}'

    atom_name = {}
    if sd := data['source_data']:
        source_data = json.dumps(sd)
        source_data = source_data.replace("'", "''")
        organization = sd['organAbbr']
        if abbr := sd['nameAbbr']:
            abbreviated_name = abbr
        if not full_name: # 外國人
            name_list = []
            if first_name := sd['firstName']:
                name_list.append(first_name)
            if last_name := sd['lastName']:
                name_list.append(last_name)
            full_name = ' '.join(name_list)
        atom_name = {
            'en': {
                'given_name': sd['firstName'],
                'inherited_name': sd['lastName'],
            }
        }
        if name_other := sd['nameOther']:
            atom_name['other'] = name_other

        #print (full_name, abbreviated_name, atom_name, organization, sd)

        # check updated filst/last name
        '''
        if data['first_name'] != sd['firstName']:
            print('first_name', data['first_name'], ' | ', sd['firstName'])
        if data['last_name'] != sd['lastName']:
            print ('last_name', data['last_name'], ' | ',sd['lastName'])
        '''
    else:
        #print(data)
        pass

    #if data['first_name'] or data['last_name']:
    #    print
    full_name = full_name.replace("'", "''")
    atomized_name = json.dumps(atom_name)
    atomized_name = atomized_name.replace("'", "''")
    organization = organization.replace("'", "''")
    sql = f"INSERT INTO person (full_name, abbreviated_name, atomized_name, is_collector, is_identifier, source_data, organization) VALUES ('{full_name}', '{abbreviated_name}', '{atomized_name}', {is_collector}, {is_identifier}, '{source_data}', '{organization}');"
    #print (sql)
    return sql

count = 0
for i in data:
    if i['model'] == 'specimen.person':
        count += 1
        sql = make_person(i['fields'])
        out.write(sql+'\n')
out.close()
print(count)

