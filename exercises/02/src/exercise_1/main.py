import sys
import BTE.BodyTextExtractor

in_file_name = sys.argv[1]

html = open(in_file_name).read()
p = BTE.BodyTextExtractor.HtmlBodyTextExtractor()
p.feed(html)
p.close()

body = p.body_text()

body_file = open(in_file_name + ".content", "w")
body_file.write(body)
body_file.close()


counts = p.counts()
count_file = open(in_file_name + ".counts", "w")

for i in range(0, len(counts)):
  count_file.write(str(i) + " " + str(counts[i]) + "\n")

count_file.close()
