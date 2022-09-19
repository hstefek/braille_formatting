# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 12:13:31 2013

@author: amestrovic
"""
import re
#algoritam kako je opisan u radu, gleda početke riječi - do vokala

vokali = u'aeiouEIR'
samoglasnici = u'aeiouREI'
svi = u'sptkfhczbgdcGCDSZvmrjlnLNKrxywq'


popisIJE = open("rijeci_jat.txt", 'r')
korijeniIJE = [line.rstrip() for line in open('rijeci_jat.txt')]

#provjerava je li slovo na poziciji i u riječi 'riječ' u funkciji slogotvornog r
def slogotvornoR(rijec, i):
    if(len(rijec)>1):
        if (i==0 and rijec[0]=='r' and rijec[1] in svi and rijec[1]!='j'):               
            return True
        elif (i+1<len(rijec) and rijec[i]=='r' and rijec[i-1] in svi and rijec[i+1] in svi and rijec[i+1]!='j'):            
            return True
        elif (i==len(rijec)-1 and rijec[i]=='r' and rijec[i-1] in svi): #iznimka za riječi tipa masakr
            return True
        else:
            return False
    else:
        return False

def konvertiraj(rijec):
    niz_iznimki_nj = ['konjun', 'konjug','injek', 'injic']
    niz_iznimki_dz = ['nadZiv', 'odZiv','podZanr','podZeCi','podZeg','podZig','podZiz','podZeZ','podZupan']
    iznimka_nj = False
    iznimka_dz = False    
    tmp_rijec = rijec
    tmp_rijec = re.sub('Č','č', tmp_rijec)               
    tmp_rijec = re.sub('Ć','ć',tmp_rijec)              
    tmp_rijec = re.sub('Š','š',tmp_rijec)               
    tmp_rijec = re.sub('Đ','đ',tmp_rijec)               
    tmp_rijec = re.sub('Ž','ž',tmp_rijec)                       
    tmp_rijec = tmp_rijec.lower()
    tmp_rijec = re.sub('č','G', tmp_rijec)               
    tmp_rijec = re.sub('ć','C',tmp_rijec)              
    tmp_rijec = re.sub('š','S',tmp_rijec)               
    tmp_rijec = re.sub('đ','D',tmp_rijec)               
    tmp_rijec = re.sub('ž','Z',tmp_rijec)                   
    tmp_rijec = re.sub('lj','L',tmp_rijec)
    for i in niz_iznimki_nj:
        if(i in tmp_rijec):
            iznimka_nj = True
    if(not iznimka_nj):        
        tmp_rijec = re.sub('nj','N',tmp_rijec)        
    for j in niz_iznimki_dz:
        if(j in tmp_rijec):
            iznimka_dz = True
    if(not iznimka_dz):
        tmp_rijec = re.sub('dZ','K',tmp_rijec)               
    tmp_rijec = re.sub('[^A-Za-z\.]','',tmp_rijec)      
    if tmp_rijec in korijeniIJE:        
        tmp_rijec = re.sub('ije','I', tmp_rijec)          
    tmp_rijec = re.sub('naest',u'nEst', tmp_rijec)       
    return  tmp_rijec
    
def dekonvertiraj(rijec):
    tmpL = rijec    
    tmpL = tmpL.replace('G','č')               
    tmpL = tmpL.replace('C','ć')               
    tmpL = tmpL.replace('S','š')                
    tmpL = tmpL.replace('D','đ')               
    tmpL = tmpL.replace('Z','ž')               
    tmpL = tmpL.replace('L', 'lj')
    tmpL = tmpL.replace('N', 'nj')   
    tmpL = tmpL.replace('K', 'dž')  
    tmpL = tmpL.replace('I', 'ije')
    tmpL = tmpL.replace('E', 'ae')
    return tmpL
    

#provjerava ako je slovo silabem
def silabem(rijec,i):
    return slogotvornoR(rijec,i) or rijec[i] in vokali

#otvara datoteku u kojoj se nalazi popis nizova s kojima riječ može početi  
popisPoc = open("skupInit.txt", 'r')
lx = popisPoc.readlines()
listaPocetaka = [x.rstrip() for x in lx] 
  

#funkcija koja rastavlja riječ na slogove  
def rastavinaslogove(rijec1):   
    rijec = konvertiraj(rijec1)      
    u'''Rastavi riječ slogove. Riječ mora biti pisana malim slovima.'''     
    pozPoc=0
    slogovi=[]
    i = 0   
    while i < len(rijec):
        if silabem(rijec,i):
            try: 
                #rastavljanje za oblike VCV
                if (i+2 < len(rijec) and not silabem(rijec,i+1) and silabem(rijec,i+2)):
                    slogovi.append(rijec[pozPoc:i + 1])                            
                    pozPoc = i + 1
                    
                #rastavljanje za oblike VCCV                 
                elif (i+3 < len(rijec) and not silabem(rijec,i+1) and not silabem(rijec,i+2) and silabem(rijec,i+3)):                       
                    if(not(slogotvornoR(rijec, i+3))):                                                                              
                        if(''.join([rijec[i+1], rijec[i+2]]) not in listaPocetaka):
                            slogovi.append(rijec[pozPoc:i+2])
                            pozPoc = i + 2                                                    
                        else:                        
                            slogovi.append(rijec[pozPoc:i + 1])                            
                            pozPoc = i + 1                       
                    else:                            
                        if(''.join([rijec[i+1], rijec[i+2],rijec[i+3]]) not in listaPocetaka):
                            slogovi.append(rijec[pozPoc:i+2])
                            pozPoc = i + 2                                                    
                        else:                        
                            slogovi.append(rijec[pozPoc:i + 1])                            
                            pozPoc = i + 1 
                            
                #rastavljanje za oblike VCCCV
                elif (i+4 < len(rijec) and not silabem(rijec,i+1) and not silabem(rijec,i+2) and not silabem(rijec,i+3) and silabem(rijec,i+4)):                                           
                    if (''.join([rijec[i+1], rijec[i+2], rijec[i+3]]) in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+1])
                        pozPoc = i + 1                                  
                    elif (''.join([rijec[i+2], rijec[i+3]]) not in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+3])                            
                        pozPoc = i + 3                             
                    else:
                        slogovi.append(rijec[pozPoc:i+2])                            
                        pozPoc = i + 2                         
                        
                #rastavljanje za oblike VCCCCV  
                elif (i+5 < len(rijec) and not silabem(rijec,i+1) and not silabem(rijec,i+2) and not silabem(rijec,i+3) 
                    and not silabem(rijec,i+4) and silabem(rijec,i+5)):    
                    #print '3'
                    if(''.join([rijec[i+2], rijec[i+3], rijec[i+4]]) in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+2])
                        pozPoc = i + 2                        
                    elif (''.join([rijec[i+3], rijec[i+4]]) not in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+4])                            
                        pozPoc = i + 4   
                                                    
                    else:
                        slogovi.append(rijec[pozPoc:i+3])                            
                        pozPoc = i + 3
                       
                #rastavljanje za oblike VCCCCCV  
                elif (i+6 < len(rijec) and not silabem(rijec,i+1) and not silabem(rijec,i+2) and not silabem(rijec,i+3) 
                    and not silabem(rijec,i+4) and not silabem(rijec,i+5) and silabem(rijec,i+6)):                                                          
                    if(''.join([rijec[i+3], rijec[i+4], rijec[i+5]]) in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+3])
                        pozPoc = i + 3
                    elif (''.join([rijec[i+4], rijec[i+5]]) not in listaPocetaka):
                        slogovi.append(rijec[pozPoc:i+5])                            
                        pozPoc = i + 5                                
                    else:
                        slogovi.append(rijec[pozPoc:i+4])                            
                        pozPoc = i + 4                           
                else:                 
                    slogovi.append(rijec[pozPoc:i + 1])
                    pozPoc = i + 1
            except Exception:
                slogovi.append(rijec[pozPoc:i + 1])
                pozPoc = i + 1
                print ('exeption')
                                
        i += 1
   
    if len(slogovi) > 0:        
        last = slogovi.pop()
        last = last + rijec[pozPoc:]
        slogovi.append(last)
    else:
        slogovi = rijec
    slogovi1 = []
    for x in slogovi:               
        x = dekonvertiraj(x)
        slogovi1.append(x)

    return slogovi1
    


popisIJE.close()

