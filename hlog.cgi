#!/bin/sh

printf 'Content-Type: text/html\r\n\r\n'

cat << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Runxi Yu's Hyperlog</title>
    <link rel="stylesheet" href="./style.css" />
    <link rel="icon" href="./favicon.ico" sizes="any" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
    <meta name="theme-color" content="#241504" />
    <meta name="color-scheme" content="light dark">
</head>
<body>
<header>
    <h1>Runxi Yu's Hyperlog</h1>
    <p style="font-style:italic;position:absolute;right:var(--margin-width);">
EOF

TZ='Asia/Shanghai' date -r /srv/hlog/runxiyu.hlog '+%Y-%m-%d %H:%M:%S %Z'


cat << EOF
    </p>
</header>
<article>
<pre style="margin-top: 3rem;">
EOF
sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g' /srv/hlog/runxiyu.hlog
cat << EOF
</pre>
</article>
<footer>
    <ul role="list">
        <li><a href="./">Home</a></li>
        <li>Runxi Yu</li>
        <li><a rel="license" href="./pubdom.html">Public Domain</a></li>
    </ul>
</footer>
</body>
</html>
EOF
