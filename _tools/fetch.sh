#!/bin/bash
fetch() { d=$1; base=$2; mkdir -p agentcore-docs/$d; curl -s $base/llms.txt > agentcore-docs/$d/llms.txt
  grep -o "$base/[^)]*\.md" agentcore-docs/$d/llms.txt | sort -u > agentcore-docs/$d/.urls
  echo "$d: $(wc -l < agentcore-docs/$d/.urls) pages"
  xargs -P 12 -I{} bash -c 'u="{}"; f="agentcore-docs/'$d'/$(basename "$u")"; curl -sf --retry 3 "$u" -o "$f" || echo "FAIL $u"' < agentcore-docs/$d/.urls; }
fetch developer-guide https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide
fetch api-control-plane https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference
fetch api-data-plane https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference
