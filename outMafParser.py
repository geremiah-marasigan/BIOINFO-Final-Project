import json

try:

	data = {}
	data['Results'] =[]

	fp = open("../DATA/out-fruit-fly-proteome_500k_1.maf")
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

				if first:
					data['Results'].append({
						'id': ref[1],
						'aligned': {'rna': query[1], 'score': value}
					})
					first = False
				else:
					for key in data['Results']:
						if key['id'] == ref[1]: #if one of the proteins already in Results has the same name of the read protein
							#print(key['aligned'])
							#for value in key['aligned'].values():
								#if cnt % 2 == 1:
									#print(cnt, value)
							if(cnt % 1000000 == 0):
								print('count', cnt)	
							cnt += 1
							
						else:
							data['Results'].append({
								'id': ref[1],
								'aligned': {'rna': query[1], 'score': value}
							})
							#print(key['id'], " matches with ", ref[1])
				
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

	with open('Alignment-Results.json', 'w') as outfile:
		json.dump(data, outfile)

	fp.close()