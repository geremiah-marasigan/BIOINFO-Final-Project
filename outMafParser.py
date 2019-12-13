import json
import dbhelper

dbhelper.init()
print('JIA')
print(dbhelper.connection)

try:
	fp = open("../DATA/out-fruit-fly-proteome_500k_1.maf")
	print('WEI')
	line = fp.readline()
	first = True
	cnt = 1
	while line:
		if "#" not in line:
			score = line.split()
			if len(score) == 4:
				ref = fp.readline()
				ref = ref.split()
				query = fp.readline()
				query = query.split()
				value = score[1].split('=')[1]
				protein = (ref[1], '')

				if first:
					# data['Results'].append({
					# 	'id': ref[1],
					# 	'aligned': {'rna': query[1], 'score': value}
					# })
					protein_id = dbhelper.create_protein(dbhelper.connection, protein)
					alignment = (protein_id, query[1], value)
					dbhelper.create_alignment(dbhelper.connection, alignment)
					first = False
				else:
					temp_protein = dbhelper.select_protein(dbhelper.connection, ref[1])
					if temp_protein is not None:
						alignment = (temp_protein[0], query[1], value)
						dbhelper.create_alignment(dbhelper.connection, alignment)
					else:
						protein_id = dbhelper.create_protein(dbhelper.connection, protein)
						alignment = (protein_id, query[1], value)
						dbhelper.create_alignment(dbhelper.connection, alignment)
					# for key in data['Results']:
					# 	if key['id'] == ref[1]: #if one of the proteins already in Results has the same name of the read protein
					# 		#print(key['aligned'])
					# 		#for value in key['aligned'].values():
					# 			#if cnt % 2 == 1:
					# 				#print(cnt, value)
					# 		if(cnt % 1000000 == 0):
					# 			print('count', cnt)	
					# 		cnt += 1 #match = protein 
							
					# 	else:
					# 		data['Results'].append({
					# 			'id': ref[1],
					# 			'aligned': {'rna': query[1], 'score': value}
					# 		})
					# 		#print(key['id'], " matches with ", ref[1])
				
				#print(data['Results'][0]['aligned']['score'])
				#print(data['Results'][0]['id'])
				#print(cnt, ": ", ref[1], " is aligned with ", query[1], " and has a score of ", value)
				#cnt += 1
		line = fp.readline()
	print("done")
finally:

	print("oi")
	#for key in data['Results']:
	#	print(key)

	# with open('Alignment-Results.json', 'w') as outfile:
	# 	json.dump(data, outfile)

	fp.close()