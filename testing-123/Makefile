update: testing-123.txt testing-123.7 testing-123.html
	git add .
	git commit
	git push

testing-123.7: testing-123.md
	mmark --man testing-123.md > testing-123.7
testing-123.txt testing-123.html: testing-123.xml
	xml2rfc --text --html testing-123.xml
	sed -i -e '/\f/{n;s/^.\{5\}/RFD 1/}' testing-123.txt
	ed testing-123.txt < Edfile
testing-123.xml: testing-123.md
	sed '0,/title =/{s/ ."$$/"/}' testing-123.md | mmark > testing-123.xml
