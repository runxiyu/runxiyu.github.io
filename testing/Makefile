update: leahrowe-test.txt leahrowe-test.7 leahrowe-test.html
	git add .
	git commit
	git push

leahrowe-test.7: leahrowe-test.md
	mmark --man leahrowe-test.md > leahrowe-test.7
leahrowe-test.txt leahrowe-test.html: leahrowe-test.xml
	xml2rfc --text --html leahrowe-test.xml
	sed -i -e '/\f/{n;s/^......../RFD RFDN/}' leahrowe-test.txt
	ed leahrowe-test.txt < Edfile
leahrowe-test.xml: leahrowe-test.md
	sed '0,/title =/{s/ ."$$/"/}' leahrowe-test.md | mmark > leahrowe-test.xml
