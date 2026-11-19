import io, re, html.parser
p = r"C:\Users\sy911\AccioWork\2026-09-15-10-01-24-209-f9963c3e\mahjongbest-repo\index.html"
t = io.open(p, encoding="utf-8").read()

class P(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.stack=[]; self.errs=[]
    def handle_starttag(self, tag, attrs):
        if tag not in ("br","img","input","meta","link","hr","path","circle","rect","source"):
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1]==tag: self.stack.pop()
        else:
            if tag in self.stack:
                self.errs.append("mismatch at %s (open=%s)" % (tag, self.stack[-3:]))
                while self.stack and self.stack.pop()!=tag: pass
            else:
                self.errs.append("stray </%s>" % tag)
pr=P(); pr.feed(t)
print("unclosed:", pr.stack)
print("errors:", pr.errs[:5])

# footer connect block
m = re.search(r'<h4>Connect</h4>.*?</ul>', t, re.S)
print(m.group(0))
print("contact-value count:", t.count("contact-value"))
print("wa.me count:", t.count("wa.me/8618669693290"))
print("mailto count:", t.count("mailto:yale@mahjongbest.com"))
print("email_click script present:", 'email_click' in t)
print("price tokens count:", t.count("$"))
