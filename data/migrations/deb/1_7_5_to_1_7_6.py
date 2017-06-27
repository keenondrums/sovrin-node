import shutil
with open('/home/sovrin/.sovrin/migration_proof', 'w') as f:
  f.write('1.5.6')

shutil.copytree('/home/sovrin/.sovrin', '/home/sovrin/.sovrin_test')
raise Exception('1.5.6test')