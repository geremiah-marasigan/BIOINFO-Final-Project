try:
	fp = open("../DATA/sample_1million.fastq")
	line = fp.readline()
	cnt = 1
	while line:
		if "@" in line:
			print(cnt, ": ", line)
			cnt += 1
		line = fp.readline()
finally:
	fp.close()