import io, re
p = r"C:\Users\sy911\AccioWork\2026-09-15-10-01-24-209-f9963c3e\mahjongbest-repo\index.html"
with io.open(p, "r", encoding="utf-8", newline="") as f:
    t = f.read()

before = t
# CSS: remove leading space on the two new rules
t = t.replace("\n .footer-col .contact-value", "\n.footer-col .contact-value")
t = t.replace("\n .footer-col a:hover .contact-value", "\n.footer-col a:hover .contact-value")
# HTMl: normalize indentation to 10 spaces
t = re.sub(r"(?m)^\s+<li><a href=\"https://wa\.me/8618669693290\" target=\"_blank\" rel=\"noopener\">",
           "          <li><a href=\"https://wa.me/8618669693290\" target=\"_blank\" rel=\"noopener\">", t)
t = re.sub(r"(?m)^\s+<li><a href=\"mailto:yale@mahjongbest\.com\">",
           "          <li><a href=\"mailto:yale@mahjongbest.com\">", t)

with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(t)

print("changed:", before != t)
for line in t.split("\n"):
    if "contact-value" in line or "wa.me/8618669693290\" target" in line or "mailto:yale@" in line:
        print(repr(line[:140]))
