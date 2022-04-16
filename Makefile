update: pragmatics.txt pragmatics.man
	git add .
	git commit
	git push

pragmatics.man: pragmatics.7
	groff -man -Tascii pragmatics.7 > pragmatics.man
pragmatics.7: pragmatics.md
	mmark --man pragmatics.md > pragmatics.7
pragmatics.txt: pragmatics.xml
	xml2rfc --text --html pragmatics.xml
pragmatics.xml: pragmatics.md
	mmark pragmatics.md > pragmatics.xml

