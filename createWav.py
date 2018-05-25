import CreateRecord

for x in range(1,11):
	test = CreateRecord.Record()
	test.createRecord("./wav/tiep/%s.wav" %x)