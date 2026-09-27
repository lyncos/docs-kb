#!/bin/bash
# Whole reference sets cited by the AgentCore docs: Markdown from official repos + AWS CLI command references.
# Usage: fetch_ref_sets.sh <workdir> <out_dir>   (out_dir = staging for ~/kb/agentcore/references)
set -u
W=$1; OUT=$2; mkdir -p "$W" "$OUT"
clone_md() { # repo subdir-filter out_name
  local repo=$1 filt=$2 name=$3; local d="$W/$name"
  rm -rf "$d"; git clone -q --depth 1 --filter=blob:none --no-checkout "https://github.com/$repo" "$d" || { echo "FAIL clone $repo"; return; }
  git -C "$d" sparse-checkout set --no-cone "$filt" && git -C "$d" checkout -q
  local sha; sha=$(git -C "$d" rev-parse --short HEAD)
  (cd "$d" && find . -type f \( -name '*.md' -o -name '*.mdx' \) -not -path './.git/*' -not -path '*/node_modules/*' -not -iname 'CHANGELOG*' ) | while read -r f; do
    mkdir -p "$OUT/repos/$name/$(dirname "$f")"; cp "$d/$f" "$OUT/repos/$name/$f"; done
  echo "$repo@$sha" > "$OUT/repos/$name/.source"
  echo "$name: $(find "$OUT/repos/$name" -name '*.md*' | wc -l) md @ $sha"
}
clone_md aws/agentcore-cli '*.md' agentcore-cli
clone_md aws/bedrock-agentcore-sdk-python '*.md' bedrock-agentcore-sdk-python
clone_md aws/bedrock-agentcore-sdk-typescript '*.md' bedrock-agentcore-sdk-typescript
clone_md aws/bedrock-agentcore-starter-toolkit '*.md' bedrock-agentcore-starter-toolkit
clone_md aws/agent-toolkit-for-aws '*.md' agent-toolkit-for-aws
clone_md aws/mcp-proxy-for-aws '*.md' mcp-proxy-for-aws
clone_md awslabs/mcp '/src/amazon-bedrock-agentcore-mcp-server/**/*.md' awslabs-mcp-agentcore-server
clone_md awslabs/agentcore-samples '*.md' agentcore-samples

# AWS CLI v2 command references (HTML only) -> pandoc
for svc in bedrock-agentcore-control bedrock-agentcore agent-registry-control agent-registry; do
  base="https://docs.aws.amazon.com/cli/latest/reference/$svc"
  idx=$(curl -sL "$base/index.html"); [ -z "$idx" ] && { echo "FAIL cli $svc"; continue; }
  mkdir -p "$OUT/aws-cli/$svc"
  cmds=$(printf '%s' "$idx" | grep -oE 'href="[a-z0-9-]+\.html"' | sed -E 's/href="//;s/"$//' | grep -v '^index.html$' | sort -u)
  printf '%s\n' index.html $cmds | xargs -P 8 -I{} bash -c '
    u="'"$base"'/{}"; f="'"$OUT/aws-cli/$svc"'/$(basename {} .html).md"
    h=$(curl -sL "$u"); body=$(printf "%s" "$h" | python3 -c "import re,sys;t=sys.stdin.read();m=re.search(r\"<div[^>]*(?:role=\\\"main\\\"|id=\\\"main-content\\\"|class=\\\"body\\\")[^>]*>(.*)\",t,re.S);print(m.group(1) if m else t)")
    printf "%s" "$body" | pandoc -f html -t gfm-raw_html --wrap=none 2>/dev/null | sed "/^\[Previous\]/,\$d" > "$f.tmp"
    { printf -- "---\ntitle: \"aws %s %s\"\nproduct: Amazon Bedrock AgentCore\nsection: References / AWS CLI\nsource_url: %s\nfetched: 2026-09-26\ntags: [agentcore, reference, aws-cli, core]\n---\n\n" "'"$svc"'" "$(basename {} .html)" "$u"; cat "$f.tmp"; } > "$f"; rm -f "$f.tmp"'
  echo "aws-cli/$svc: $(ls "$OUT/aws-cli/$svc" | wc -l) pages"
done
