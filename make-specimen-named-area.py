import json


a = open('specimen.json')
m = a.read()
data = json.loads(m)

out = open('out-named-area.sql', 'w')
out2 = open('out-area-class.sql', 'w')

x = []
y = []
def make_named_area(data):
    #print (data)
    sql = ''
    name = data['name']
    name_en = data['name_other']
    name_en = name_en.replace("'", "''")
    area_class = data['area_class']
    sql = f"INSERT INTO named_area (name, name_en, area_class_id) VALUES ('{name}', '{name_en}', {area_class});\n"
    return sql

def make_area_class(data):
    #print (data)
    name = data['name']
    label = data['label']
    sql = f"INSERT INTO area_class (name, label) VALUES ('{name}', '{label}');\n"
    return sql

count = 0
for i in data:
    if i['model'] == 'specimen.namedarea':
        count += 1
        sql = make_named_area(i['fields'])
        out.write(sql);

    if i['model'] == 'specimen.areaclass':
        sql = make_area_class(i['fields'])
        out2.write(sql)

    if i['model'] not in x:
        x.append(i['model'])


#print (count)
out.close()
out2.close()
print (x)
