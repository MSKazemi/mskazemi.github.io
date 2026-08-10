#!/usr/bin/env bash
# Push mskazemi.com URLs to the IndexNow network (Bing, Yandex, Seznam, Naver, Yep)
# so a new or changed page is crawled in hours instead of weeks.
#
# Run this immediately after a deploy. Google does NOT participate in IndexNow —
# for Google, resubmit the sitemap in Search Console.
#
#   ./tools/indexnow-submit.sh              # submit every URL in sitemap.xml
#   ./tools/indexnow-submit.sh /about/ /hire/   # submit only these paths
#
# The key file must stay reachable at https://mskazemi.com/<key>.txt — it is the
# only proof of ownership IndexNow uses.

set -euo pipefail

HOST="mskazemi.com"
KEY="934a8206b4840756ba9fcb16d64fff7b"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
ENDPOINT="https://api.indexnow.org/IndexNow"

cd "$(dirname "$0")/.."

if [[ $# -gt 0 ]]; then
  urls=()
  for p in "$@"; do urls+=("https://${HOST}${p}"); done
else
  mapfile -t urls < <(grep -oE '<loc>[^<]+</loc>' sitemap.xml | sed -e 's|<loc>||' -e 's|</loc>||')
fi

if [[ ${#urls[@]} -eq 0 ]]; then
  echo "No URLs to submit." >&2
  exit 1
fi

echo "Verifying the key file is live before submitting…"
if ! curl -fsS --max-time 15 "$KEY_LOCATION" | grep -qx "$KEY"; then
  echo "ERROR: $KEY_LOCATION does not serve the expected key. IndexNow will reject the batch." >&2
  exit 1
fi

payload=$(python3 -c '
import json, sys
host, key, loc = sys.argv[1], sys.argv[2], sys.argv[3]
print(json.dumps({"host": host, "key": key, "keyLocation": loc, "urlList": sys.argv[4:]}))
' "$HOST" "$KEY" "$KEY_LOCATION" "${urls[@]}")

echo "Submitting ${#urls[@]} URL(s) to IndexNow:"
printf '  %s\n' "${urls[@]}"

code=$(curl -sS -o /tmp/indexnow-response.txt -w '%{http_code}' \
  -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data "$payload")

case "$code" in
  200|202) echo "OK ($code) — accepted. Crawl usually follows within hours." ;;
  400) echo "FAILED ($code) — malformed request."; cat /tmp/indexnow-response.txt; exit 1 ;;
  403) echo "FAILED ($code) — key not valid for this host. Check $KEY_LOCATION."; exit 1 ;;
  422) echo "FAILED ($code) — a URL does not belong to $HOST."; cat /tmp/indexnow-response.txt; exit 1 ;;
  429) echo "FAILED ($code) — rate limited. Wait and retry."; exit 1 ;;
  *)   echo "Unexpected response $code"; cat /tmp/indexnow-response.txt; exit 1 ;;
esac

echo
echo "Reminder: Google ignores IndexNow. Resubmit https://${HOST}/sitemap.xml in"
echo "Google Search Console, and use URL Inspection → Request Indexing for /about/ and /hire/."
