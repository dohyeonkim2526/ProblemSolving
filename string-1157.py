word=input().upper()
alphabet=list(set(word))
cnt=[]

for a in alphabet:
    c=word.count(a)
    cnt.append(c)

m=max(cnt) #가장 많은 알파벳 개수
m_cnt=cnt.count(m) #알파벳 개수가 중복되는 지 확인
print(alphabet[cnt.index(m)] if m_cnt==1 else '?')