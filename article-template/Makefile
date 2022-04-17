update: leah.txt leah.7 leah.html
	git add .
	git commit
	git push

leah.7: leah.md
	mmark --man leah.md > leah.7
leah.txt leah.html: leah.xml
	xml2rfc --text --html leah.xml
	sed -i -e '/\f/{n;s/^.\{5\}/RFD 1/}' leah.txt
	ed leah.txt < Edfile
leah.xml: leah.md
	sed '0,/title =/{s/ ."$$/"/}' leah.md | mmark > leah.xml
