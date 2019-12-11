try:
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
				print(cnt, ": ", ref[1], " is aligned with ", query[1], " and has a ", score[1])
				cnt += 1
		line = fp.readline()
finally:
	fp.close()