def inheritance(Descriptions):
    answer=[]
    for i in Descriptions:
        if i[:3] == 'DEC':
            a = i.split()
            deceased = a[1]
            amount = a[2]
    return inheritance1(Descriptions,answer,deceased,amount)


def inheritance1(Descriptions,answer,deceased,amount):
    
    
    def soyuvarmi(person):
        children=childfinder(person)
        for child in children:
            if not isdead(child) or soyuvarmi(child):
                return True
            
                
        return False

    def childfinder(parent):
        children = []
        for i in Descriptions:
            
            if i[:3] == 'CHI':
                a = i.split()
                parent1 = a[1]
                parent2 = a[2]
                
                
                if (parent1 == parent) or (parent2 == parent):
                    for j in a[3:]:
                        children.append(j)
        return children
                
    def isdead(person):
        deadlist = []
        for i in Descriptions:
            if i[:3] == 'DEP' or i[:3] == 'DEC':
                a=i.split()
                dead=a[1]
                deadlist.append(dead)
        if person in deadlist: return True
        else: return False
    
    def esbulucu(person):
        for i in Descriptions:
            if i[:3] == 'MAR':
                a=i.split()
                if person in a:
                    if person == a[1]:
                        es = a[2]
                    else:
                        es = a[1]
                    return es
        return 'sap'

    def esindexbulucu(person):
        a=-1
        for i in Descriptions:
            if i[:3] == 'MAR':
                b=i.split()
                if b[1]==person or b[2]==person:
                    a=Descriptions.index(i)
        return a
    
    def parentfinder(person) -> list:
        for i in Descriptions:
            if i[:3] == 'CHI':
                a = i.split()
                parent1 = a[1]
                parent2 = a[2]
                for j in a[3:]:
                    if j == person:
                        return [parent1,parent2]
        return []

    def parentsoy(person):
        parents=parentfinder(person)
        a=[]
        if parents!=[]:
            for i in parents:
                a.append(soyuvarmi(i))
                a.append(not isdead(i))
        if True in a:
            return True
        return False
    
    def grandparentsoy(person):
        grandparents=[]
        parents=parentfinder(person)
        a=[]
        if parents!=[]:
            for i in parents:
                grandparents.extend(parentfinder(i))
            for i in grandparents:
                a.append(soyuvarmi(i))
                a.append(not isdead(i))
        if True in a:
            return True
        return False

    def grandparentfinder(person):
        grandparents=[]
        parents=parentfinder(person)
        for i in parents:
            grandparents.extend(parentfinder(i))
        return grandparents
    

    if soyuvarmi(deceased):
        es=esbulucu(deceased)
        if es != 'sap' and not isdead(es):
            answer.append((es,float(amount)/4))
            amount=float(amount)*3/4

        cocuklar=childfinder(deceased)
        soylu=[]
        for i in cocuklar:
            if soyuvarmi(i) or not isdead(i):
                soylu.append(i)

        for i in soylu:
            if not(isdead(i)):
                answer.append((i,float(amount)/len(soylu)))
                
            else:
                esindexbulucu(i)
                Desc=Descriptions
                Desc[esindexbulucu(i)]=[]

                inheritance1(Desc,answer,i,float(amount)/len(soylu))
    
    elif parentsoy(deceased):
        parali=[]
        parents=parentfinder(deceased)
        es=esbulucu(deceased)
        if es != 'sap' and not isdead(es):
            answer.append((es,float(amount)/2))
            amount=float(amount)/2

            
        for i in parents:
            if not soyuvarmi(i) and isdead(i):
                continue
            else:
                parali.append(i)
        div=len(parali)
        
        for i in parali:
            if not isdead(i):
                answer.append((i,float(amount)/div))
            else:
                
                Desc=Descriptions
                if esindexbulucu!=-1:
                    Desc[esindexbulucu(i)]=[]
                inheritance1(Desc,answer,i,float(amount)/div) 

    elif grandparentsoy(deceased):

        parali=[]
        grandparents=grandparentfinder(deceased)
        es=esbulucu(deceased)
        if es != 'sap' and not isdead(es):
            answer.append((es,float(amount)*3/4))
            amount=float(amount)/4

            
        for i in grandparents:
            if not soyuvarmi(i) and isdead(i):
                continue
            else:
                parali.append(i)

        for i in parali:
            if not isdead(i):
                answer.append((i,float(amount)/len(parali)))
            else:
                
                Desc=Descriptions
                Desc[esindexbulucu(i)]=[]
                inheritance1(Desc,answer,i,float(amount)/len(parali)) 

    else:
        es=esbulucu(deceased)
        if es != 'sap' and not isdead(es):
            answer.append((es,float(amount)))
            
        


    result = {}

    for person, money in answer:
        if person in result:
            result[person] += money
        else:
            result[person] = money

    answer = list(result.items())
    return answer



