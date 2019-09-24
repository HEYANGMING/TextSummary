from textsummary import TextSummary

text = open("./static/testdata/rujia1", encoding="utf-8").read()
title = "如家道歉遇袭事件称努力改正 当事人曾就职浙江某媒体"
textsummary = TextSummary()
textsummary.SetText(title, text)
summary = textsummary.CalcSummary()
print(summary)
