def allsorted(alllist,form,to):
    if to<=1:
        return
    if form==to:
        print(alllist)
    else:
        for i in range(form,to+1):
            alllist[i],alllist[form]=alllist[form],alllist[i]
            allsorted(alllist,form+1,to)
            alllist[i],alllist[form]=alllist[form],alllist[i]

if __name__ == '__main__':
    alllist=['a','b','c','d','e','f']
    allsorted(alllist,0,len(alllist)-1)