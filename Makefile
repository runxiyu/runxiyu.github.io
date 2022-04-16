update: pragmatics.txt
	git add .
	git commit
	git push

pragmatics.txt: pragmatics.xml
	xml2rfc --text --html pragmatics.xml

pragmatics.xml: pragmatics.md
	mmark pragmatics.md > pragmatics.xml

