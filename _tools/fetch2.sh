#!/bin/bash
fetch() { d=$1; base=$2; mkdir -p agentcore-docs/$d; curl -s $base/llms.txt > agentcore-docs/$d/llms.txt
  grep -o "$base/[^)]*\.md" agentcore-docs/$d/llms.txt | sort -u > .urls_$d
  echo "$d: $(wc -l < .urls_$d) pages"
  xargs -P 12 -I{} bash -c 'u="{}"; f="agentcore-docs/'$d'/$(basename "$u")"; curl -sf --retry 3 "$u" -o "$f" || echo "FAIL $u"' < .urls_$d
  curl -s $base/toc-contents.json | grep -oE '"href" *: *"[^"]+"' | sed -E 's/.*"([^"]+)"$/\1/;s/\.html.*//;s/#.*//' | sort -u > toc_$d.txt
  ls agentcore-docs/$d/*.md | xargs -n1 basename | sed 's/\.md$//' | sort -u > have_$d.txt
  echo "  toc $(wc -l < toc_$d.txt), have $(wc -l < have_$d.txt), missing: $(comm -23 toc_$d.txt have_$d.txt | tr '\n' ' ')"; }
fetch agent-registry-api-control-plane https://docs.aws.amazon.com/agent-registry-control/latest/APIReference
fetch agent-registry-api-data-plane https://docs.aws.amazon.com/agent-registry/latest/APIReference
