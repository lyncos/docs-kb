#!/bin/bash
# Redeploy the download mirror at https://kb.stephaneboisvert.com (Cloudflare Worker, static assets).
# Rebuilds the zip from ~/kb (without .git) and uploads index.html + zip + sha256.
set -euo pipefail
D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
mkdir -p "$D/public"
cp "$(dirname "$0")/wrangler.jsonc" "$D/"
cp "$(dirname "$0")"/{index.html,_headers} "$D/public/"
(cd ~ && zip -qr "$D/public/docs-kb.zip" kb -x 'kb/.git/*')
(cd "$D/public" && sha256sum docs-kb.zip > docs-kb.zip.sha256)
H=$(cut -d' ' -f1 "$D/public/docs-kb.zip.sha256")
python3 - "$D/public/index.html" "$H" <<'PY'
import re,sys; p,h=sys.argv[1:]; s=open(p).read()
s=re.sub(r"<code>[0-9a-f]{64}</code>",f"<code>{h}</code>",s); s=re.sub(r"must equal [0-9A-F]{64}",f"must equal {h.upper()}",s)
open(p,"w").write(s)
PY
cd "$D" && CLOUDFLARE_ACCOUNT_ID=324478f6c3ebf480bbc10bc217908644 npx --yes wrangler@latest deploy
