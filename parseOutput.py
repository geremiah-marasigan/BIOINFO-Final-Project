import json
import dbhelper

conn = dbhelper.init()

try:
	fp = open("../maf/out-marine-copepod-proteome.maf") #Change file name depending on the output files
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
						count = int(temp_protein[2])+1
						dbhelper.update_protein(conn, temp_protein[0], count)
						alignment = (temp_protein[0], query[1], value)
						dbhelper.create_alignment(conn, alignment)
					else: 
						protein_id = dbhelper.create_protein(conn, protein)
						alignment = (protein_id, query[1], value)
						dbhelper.create_alignment(conn, alignment)
		line = fp.readline()
finally:
	conn.commit()
	conn.close()
	print("Parsing Complete")

	fp.close()