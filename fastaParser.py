try:
	fp = open("../DATA/mud-crab-virus.fasta")
	line = fp.readline()
	cnt = 1
	while line:
		if ">" in line:
			print(cnt, ": ", line)
		line = fp.readline()
		cnt += 1
finally:
	fp.close()