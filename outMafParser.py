import json

try:

	data = {}
	data['RNA-Seq'] =[]

	fp = open("../DATA/out-fruit-fly-proteome.maf")
	line = fp.readline()
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

				data['RNA-Seq'].append({
					'id': ref[1],
					'aligned': {'rna': query[1], 'score': value}
				})

				#print(cnt, ": ", ref[1], " is aligned with ", query[1], " and has a score of ", value)
				cnt += 1
		line = fp.readline()
finally:

	with open('Alignment-Results.json', 'w') as outfile:
		json.dump(data, outfile);

	fp.close()