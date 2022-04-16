update: pragmatics.txt pragmatics.man pragmatics.html
	git add .
	git commit
	git push

pragmatics.man: pragmatics.7
	groff -man -Tascii pragmatics.7 > pragmatics.man
pragmatics.7: pragmatics.md
	mmark --man pragmatics.md > pragmatics.7
pragmatics.txt pragmatics.html: pragmatics.xml
	xml2rfc --text --html pragmatics.xml
pragmatics.xml: pragmatics.md
	sed '0,/title =/{s/ ."$$/"/}' pragmatics.md | mmark > pragmatics.xml

