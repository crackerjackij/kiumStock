# 키움증권 거래내역을 카카오톡에서 내려받은 뒤
# 보기쉬운 문자열 형식으로 파싱
# 카카오톡 > 메뉴버튼 > 대화내용 > 대화내용 내보내기
# 출력 결과를 엑셀로 붙여넣기한다음 텍스트마법사를 사용해서 구분기호로 분리하면 보기 좋아짐
# 아래 파일 위치만 변경필요
# ex) 2022년3월8일|금호석유|매도|6주|32000

import re

# 파일 열기
f = open('C:/project/kiumStock.txt', 'r', encoding='utf-8')

# 문자열 처리
text = ''
fullText = ''
days = ''
nowTarget = 0
for txt in f:
    if "--------------- " in txt:
        year = re.search('[0-9]{4}년', txt)
        month = re.search('[0-9]{1,2}월', txt)
        day = re.search('[0-9]{1,2}일', txt)
        text = year.group()+month.group()+day.group()
        days = year.group()+month.group()+day.group()
    elif "체결통보" in txt:
        if text == '':
            nowTarget = 2
        else:
            nowTarget = 1
    elif nowTarget > 0:
        if nowTarget == 2:
            text = days
        text = text + "|" + txt.rstrip("\n")
        nowTarget = 0
    elif "매수" in txt or "매도" in txt:
        text = text + "|" + txt[:2] + "|" + txt[2:10].rstrip("\n")
    elif "평균단가" in txt:
        text = text + "|" + txt.replace("평균단가","").replace("원","").rstrip("\n")
        fullText += text + "\n"
        text = ''


print(fullText)

# 파일 닫기
f.close()