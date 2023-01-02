sitemap:
	find . -name '*.html' | sed 's/^\./https:\/\/www.andrewyu.org/' > sitemap.txt
