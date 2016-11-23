users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}
c=1
d=1
print 'Students'
for n in users['Students']:
    print c,'-',n['first_name'], n['last_name'], len(n['first_name']+ n['last_name'])
    c+=1
print 'Instructors'
for m in users['Instructors']:
    print d,'-',m['first_name'], m['last_name'], len(m['first_name']+ m['last_name'])
    d+=1
