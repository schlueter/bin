#!/bin/bash
fail() {
	echo >&2 "$@"
	exit 1
}

[ "$#" == 1 -a "${1#-}" = "$1" ] || fail "usage: `basename $0` app"
app=$1
desktop=$app.desktop
mimeapps=$HOME/.local/share/applications/mimeapps.list

mozprefs=`echo "$HOME"/.mozilla/firefox/*.default/prefs.js`
[ -e "$mozprefs" ] || fail "file not found: $mozprefs"
pidof >/dev/null firefox firefox-bin iceweasel iceweasel-bin && fail "firefox is running, kill it first"
echo 'user_pref("network.protocol-handler.expose.magnet", true);' >>"$mozprefs" || fail "write failed: $mozprefs"
echo "updated ok: $mozprefs"

locate >/dev/null "$desktop" || echo >&2 "warning: locate failed: $desktop"
[ -s "$mimeapps" ] && echo >>"$mimeapps"
echo >>"$mimeapps" "[Default Applications]
x-scheme-handler/magnet=$desktop"

echo "updated ok: $mimeapps"

xdg_open="$HOME/xdg-open"
cp /usr/bin/xdg-open "$xdg_open" || fail "cp failed: /usr/bin/xdg-open $xdg_open"
patch "$xdg_open" <<'End' || fail "patch failed: $xdg_open"
--- /usr/bin/xdg-open  2010-09-15 14:08:29.000000000 +0300
+++ bin/xdg-open  2012-01-24 22:05:03.935338593 +0200
@@ -437,6 +437,11 @@
                 exit_success
             fi
         fi
+    elif (echo "$1" | grep -q '^magnet:'); then
+        $app "$1" 
+        if [ $? -eq 0 ]; then
+            exit_success
+        fi
     fi
 
     sensible-browser "$1"
End
echo "To install patched xdg-open:"
echo "sudo cp $HOME/xdg-open /usr/local/bin/xdg-open"
