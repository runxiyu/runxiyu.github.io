pragmatics.txt: pragmatics.xml
	xml2rfc --text pragmatics.xml

pragmatics.xml: pragmatics.md
	mmark pragmatics.md > pragmatics.xml

update:
	git add .
	git commit
	git push
