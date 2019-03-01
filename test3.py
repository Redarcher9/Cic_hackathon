from wn_1 import wordnet
doc1=wordnet("Marijuana is legal in some countries. It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.","Marijuana is legal in some countries. It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.")
wordnet_results=doc1.compute_wn_resullts()
lis =[]
for e in wordnet_results:
    lis.append(str(e))
mylist=map(lambda each:each.strip("Sysnet()"),lis)
mylist=list(map(lambda each:each.strip("')"),mylist))
print(mylist)
