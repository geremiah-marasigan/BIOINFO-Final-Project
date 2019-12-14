import json
import dbhelper

conn = dbhelper.init()

try:
	fp = open("../DATA/out-fruit-fly-proteome_100k_1.maf")
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
				protein = (ref[1], 1)

				if first:
					protein_id = dbhelper.create_protein(conn, protein)
					alignment = (protein_id, query[1], value)
					dbhelper.create_alignment(conn, alignment)
					first = False
				else:
					temp_protein = dbhelper.select_protein(conn, ref[1])
					if temp_protein is not None:
						dbhelper.update_protein(conn, temp_protein[0], temp_protein[1])
						alignment = (temp_protein[0], query[1], value)
						dbhelper.create_alignment(conn, alignment)
					else: 
						protein_id = dbhelper.create_protein(conn, protein)
						alignment = (protein_id, query[1], value)
						dbhelper.create_alignment(conn, alignment)
					cnt+=1
					if(cnt % 1000000 == 0):
						print('Why hello there',cnt)
		line = fp.readline()
	print("done")
finally:
	conn.commit()
	conn.close()
	print("oi")

	fp.close()