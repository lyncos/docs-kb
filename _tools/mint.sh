#!/bin/bash
# $1=outdir $2=host $3=llms.txt url
out=$1; host=$2; mkdir -p $out; curl -s $3 > $out/llms.txt
grep -oE '\]\((https://'$host')?/[^) ]+' $out/llms.txt | sed -E 's/^\]\(//; s#^/#https://'$host'/#; s/#.*//' | sed -E 's/\.md$//' | sort -u > $out/.urls
echo "$out: $(wc -l < $out/.urls) urls"
while read u; do p=${u#https://$host/}; f="$out/${p}.md"; mkdir -p "$(dirname "$f")"
  echo "$u|$f"; done < $out/.urls | xargs -P 10 -I{} bash -c 'IFS="|" read u f <<< "{}"; code=$(curl -sL --retry 3 -o "$f" -w "%{http_code}" "$u.md"); [ "$code" = 200 ] || { echo "FAIL $code $u"; rm -f "$f"; }'
