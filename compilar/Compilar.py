#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
def main(argv):
    NOMBREROM='mem'#escriba el nombre de la ROM dentro del cascaron, por defecto es mem
    codigo=open(argv[1],'r') #codigo a compilar
    SetIns=open(argv[2],'r') #codigo a compila
    Set=Separar(SetIns,3,':')
    Lin=codigo.read().splitlines()
    codigo.close()
    SetIns.close()
    print(Set)
    print(Lin)
    MEMROM=Compilar(Set, Lin)
    #nombre=str(input('Ingrese el nombre de la ROM en el cascaron: \n  si quiere que se mem ingrese un espacio\n'))
    #if(nombre==' 'or nombre=='  ' or nombre==''):
    Final=open('ROMbits.txt','w')
    CODROM=open('CodROM.txt','w')
    CODROM.write('initial begin\n\t//-----> Incio ROM <-----\n')
    print('-----> Incio ROM <-----')
    for li in range(len(MEMROM)):
        print(MEMROM[li])
        texto='\t'+NOMBREROM+'[6\'d'+str(li)+']='+MEMROM[li]+';\n'
        CODROM.write(texto)
        if(li==31):
            print('-----> Incio VARS <-----')
            CODROM.write('\t//-----> Incio VARS <-----\n')
        if(li==63):
            Final.write(MEMROM[li])
        else:
            Final.write(MEMROM[li]+'\n')
    CODROM.write('\t//-----> Fin de ROM <-----\n')
    CODROM.write('end\n')
    print('-----> Fin de ROM <-----')
    CODROM.close()
    Final.close()
    
def Compilar(Set,lineas):
    JJ=0
    var=[]
    for i in range(len(Set)):
        if(Set[i][1].lower()=="jump"):
            JJ=i
    bitstream=[]
    ROM=[]
    k=0
    if(lineas[k]!='INICIO:'):
        print('El codigo debe arrancar con la palabra INICIO:  NO con \"'+str(lineas[0])+'\"')
    else: #continuamos
        ROM = ['0000000000000000000000000'] * 64
        bitstream.append(lineas[0]+'\n0|00000|000000|000000|000000|0')
        agrega=0
        for k in range(1,len(lineas)):
            if(lineas[k].find('//')>=0):
                print('comentario linea= ' +str(k))
            else:
                ptocoma=lineas[k].find(";")
                if(ptocoma>=0):
                    lineas[k]=lineas[k][:ptocoma]
                if(lineas[k].find('FIN')>=0):
                    ROM[k] = '0111110000000000000000000'
                elif(lineas[k].find('if(')>=0 or lineas[k].find('while(')>=0 or lineas[k].find('for(')>=0 ):
                    print('estructura con jump ' + lineas[k])
                else:
                    if(ptocoma>=0):
                        VaOP=[lineas[k][0:lineas[k].find('=')],lineas[k][lineas[k].find('=')+1:]]
                        nvar=verVar(var,VaOP[0])
                        if(nvar==-1):
                            nvar=len(var)
                            var.append(VaOP[0])
                        binVAR='1'+CA2(5,nvar)
                        binOP=Operacion(VaOP[1],Set)
                        binVARRA='000000'
                        binVARRB='000000'
                        CR='0'
                        if(binOP[1]==-1001):
                            datoRA=VaOP[1]
                            nVarRA=verVar(var,str(datoRA))
                            if(nVarRA<=-1):
                                #print(bin(int(VaOP[1])))
                                entero=[]
                                try:
                                    entero=int(datoRA)
                                except:
                                    ptocoma=-3
                                    print('***************************************\n* Error la variable >> '+datoRA +' << No ha sido declarada\n* en linea -> ' +str(k)+' <- verifique\n***************************************')
                                else:
                                    binVARRA='111111'
                                    binVARRB=WarningNUM(entero,k)
                                    if(binVARRB=='bien'):
                                           binVARRB=CA2(6,entero)
                                    #print(binVARRB)
                                    CR='1'
                            else:
                                binVARRB='1'+CA2(5,nVarRA)
                                binVARRA='111111'
                                CR='0'
                                
                        else:
                            datoRA=[]
                            datoRAA=[]
                            if(binOP[1]<0 and binOP[1]>-1000):
                                auxa=VaOP[0];
                                VaOP=[auxa,VaOP[1][:-binOP[1]]+'?'+VaOP[1][(-binOP[1])+2:]]
                                binOP[1]=-binOP[1]
                                
                            datoRA=VaOP[1][:binOP[1]]
                            if(datoRA==''):
                                datoRA='0'
                                nVarRA=-1
                            else:
                                nVarRA=verVar(var,str(datoRA))
                            if(nVarRA<=-1):
                                entero=[]
                                try:
                                    entero=int(datoRA)
                                except:
                                    ptocoma=-3
                                    print('***************************************\n* Error la variable >> '+datoRA +' << No ha sido declarada\n* en linea -> ' +str(k)+' <- verifique\n***************************************')
                                else:
                                    binVARRB=WarningNUM(entero,k)
                                    if(binVARRB=='bien'):
                                        binVARRB=CA2(6,entero)
                                    CR='1'
                                    if(datoRA=='0'):
                                        binVARRA='111111'
                                        binVARRB=CA2(6,int(VaOP[1][(binOP[1]+1):]))
                                    else:
                                        datoRAA=VaOP[1][(binOP[1]+1):]
                                        nVarRAA=verVar(var,str(datoRAA))
                                        if(nVarRAA<=-1):
                                            try:
                                                entero=int(datoRAA)
                                            except:
                                                ptocoma=-3
                                                print('***************************************\n* Error la variable >> '+datoRAA +' << No ha sido declarada\n* en linea -> ' +str(k)+' <- verifique\n***************************************')
                                            else:
                                                binVARRB=WarningNUM(entero,k)
                                                if(binVARRB=='bien'):
                                                    binVARRB=CA2(6,entero)
                                                ROM[k]=ROM[k][0]+binOP[0]+binVAR+'111111'+binVARRB+'1'
                                                bitstream.append('0 [OP]'+str(entero)+';\n'+ROM[k][0]+'|'+ROM[k][1:6]+'|'+ROM[k][6:12]+'|'+ROM[k][12:18]+'|'+ROM[k][18:24]+'|'+ROM[k][24])
                                                agrega=agrega+1
                                                lineas[k]=lineas[k]+';'
                                                binVARRA=binVAR;
                                                entero=int(VaOP[1][:binOP[1]])
                                                binVARRB=WarningNUM(entero,k)
                                                if(binVARRB=='bien'):
                                                    binVARRB=CA2(6,entero)
                                                CR='1'
                                        else:
                                            binVARRA='1'+CA2(5,nVarRAA)
                            else:
                                binVARRA='1'+CA2(5,nVarRA)
                                datoRB=VaOP[1][binOP[1]+1:]
                                nVarRB=verVar(var,str(datoRB))
                                if(nVarRB<=-1):
                                    entero=[]
                                    try:
                                        entero=int(datoRB)
                                    except:
                                        ptocoma=-3
                                        print('***************************************\n* Error la variable >> '+datoRB +' << No ha sido declarada\n* en linea -> ' +str(k)+' <- verifique\n***************************************')
                                    else:
                                        binVARRB=WarningNUM(entero,k)
                                        if(binVARRB=='bien'):
                                            binVARRB=CA2(6,entero)
                                        CR='1'
                                else:
                                    binVARRB='1'+CA2(5,nVarRB)
                                    CR='0'
                        ROM[k]=ROM[k][0]+binOP[0]+binVAR+binVARRA+binVARRB+CR
                    else:
                        print('***************************************\n* Error cerca de la linea -> ' +str(k)+' <- verificar el ;\n***************************************')
                if(ptocoma>=0):
                    bitstream.append(lineas[k]+';\n'+ROM[k][0]+'|'+ROM[k][1:6]+'|'+ROM[k][6:12]+'|'+ROM[k][12:18]+'|'+ROM[k][18:24]+'|'+ROM[k][24])
                    #print(lineas[k]+';\t'+ROM[k][0]+'|'+ROM[k][1:6]+'|'+ROM[k][6:12]+'|'+ROM[k][12:18]+'|'+ROM[k][18:24]+'|'+ROM[k][24])
                else:
                    print(lineas[k])
                k=k+agrega
                #print(k)
        #print(var,len(var))
    for w in range(len(bitstream)):
        print(bitstream[w])
    return ROM
    
def verVar(var,VaOP):
    nvar=-1
    for aux in range(len(var)):
        if(var[aux]==VaOP):
             nvar=aux
    return nvar

def WarningNUM(entero,k):
    cambio=0
    num='bien'
    if(entero>=32 or entero<=-33):
        num=CA2(5,entero)
        if (len(num)>5):
            num=num[-(5-len(a)):]
        if(entero>0):
            num='0'+num
        else:
            num='1'+num
            print('***************************************\n* Warning el entero >> '+entero +' <<  es muy grande para 6 bits en CA2\n* en linea -> ' +str(k)+' <- los datos seran recortados a: '+num+'\n***************************************')
    return num

def Operacion(l,Set):
    k=-2
    pos=-2
    igual=-1
    doble=-1
    for j in range(len(Set)-1):
        p=l.find(Set[j][1])
        if(p>=0):
            pos=p
            k=j
        if(Set[j][1]=='='):
            igual=j
        if(Set[j][1]=='=='):
            doble=j
    if(k!=-2 and k!=doble):
        return [Set[k][0],pos]
    elif(igual!=-1 and k!=doble):
        return [Set[igual][0],-1001]
    elif(k==doble):
        return [Set[doble][0],-pos]
    else:
        return ['-NO',-1000]


def CA2(bits, valor):
    if valor < 0:
        valor = ( 1<<bits ) + valor
    formatstring = '{:0%ib}' % bits
    return formatstring.format(valor)

def Separar(archivo,k,ch):
    # separa texto archivo con minimo k caracteres
    texto=archivo.read().splitlines()
    separado=[]
    n=0
    for i in range(len(texto)):#obtenemos la matriz del texto
        if(len(texto[i])>k):
            n=n+1
            a=texto[i].split(ch)
            if(ch==';'):
                separado.append(a[0])
            else:
                separado.append(a)
    return separado

def printROM(ROM):
    for i in range(len(ROM)):
        print(ROM[i])
    

if __name__== "__main__":
    main(sys.argv)
    