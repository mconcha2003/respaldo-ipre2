##IMPORTANDO Y CREANDO LOS ARBOLES##

import ROOT
import numpy as np
import array
import pandas as pd
from ROOT import gPad
g = ROOT.TFile("GamGam/MC/mc_343981.ggH125_gamgam.GamGam.root")
v = ROOT.TFile("GamGam/MC/mc_345041.VBFH125_gamgam.GamGam.root")
w = ROOT.TFile("GamGam/MC/mc_345318.WpH125J_Wincl_gamgam.GamGam.root")
z = ROOT.TFile("GamGam/MC/mc_345319.ZH125J_Zincl_gamgam.GamGam.root")
t = ROOT.TFile("GamGam/MC/mc_341081.ttH125_gamgam.GamGam.root")
a= ROOT.TFile("GamGam/Data/data_A.GamGam.root")
b= ROOT.TFile("GamGam/Data/data_B.GamGam.root")
c= ROOT.TFile("GamGam/Data/data_C.GamGam.root")
d= ROOT.TFile("GamGam/Data/data_D.GamGam.root")
arbol1=g.mini;1
arbol2=v.mini;1
arbol3=w.mini;1
arbol4=z.mini;1
arbol5=t.mini;1
arbolA=a.mini;1
arbolB=b.mini;1
arbolC=c.mini;1
arbolD=d.mini;1

## MC ##

energiafotones1 = ROOT.std.vector('float')() 
momentofotones1 = ROOT.std.vector('float')()
etafotones1 = ROOT.std.vector('float')()
phifotones1 = ROOT.std.vector('float')()
trigfotones1 = array.array('i',[0])
tightfotones1 = ROOT.std.vector('bool')()
ptconefotones1 = ROOT.std.vector('float')()
etconefotones1 = ROOT.std.vector('float')()
mc1 = array.array('f',[0.0])
spileup1 = array.array('f',[0.0])
sfoton1 = array.array('f',[0.0])
sfotontrigger1 = array.array('f',[0.0])
xsection1 = array.array('f',[0.0])

energiafotones2 = ROOT.std.vector('float')() 
momentofotones2 = ROOT.std.vector('float')()
etafotones2 = ROOT.std.vector('float')()
phifotones2 = ROOT.std.vector('float')()
trigfotones2 = array.array('i',[0])
tightfotones2 = ROOT.std.vector('bool')()
ptconefotones2 = ROOT.std.vector('float')()
etconefotones2 = ROOT.std.vector('float')()
mc2 = array.array('f',[0.0])
spileup2 = array.array('f',[0.0])
sfoton2 = array.array('f',[0.0])
sfotontrigger2 = array.array('f',[0.0])
xsection2 = array.array('f',[0.0])

energiafotones3 = ROOT.std.vector('float')() 
momentofotones3 = ROOT.std.vector('float')()
etafotones3 = ROOT.std.vector('float')()
phifotones3 = ROOT.std.vector('float')()
trigfotones3 = array.array('i',[0])
tightfotones3 = ROOT.std.vector('bool')()
ptconefotones3 = ROOT.std.vector('float')()
etconefotones3 = ROOT.std.vector('float')()
mc3 = array.array('f',[0.0])
spileup3 = array.array('f',[0.0])
sfoton3 = array.array('f',[0.0])
sfotontrigger3 = array.array('f',[0.0])
xsection3 = array.array('f',[0.0])

energiafotones4 = ROOT.std.vector('float')() 
momentofotones4 = ROOT.std.vector('float')()
etafotones4 = ROOT.std.vector('float')()
phifotones4 = ROOT.std.vector('float')()
trigfotones4 = array.array('i',[0])
tightfotones4 = ROOT.std.vector('bool')()
ptconefotones4 = ROOT.std.vector('float')()
etconefotones4 = ROOT.std.vector('float')()
mc4 = array.array('f',[0.0])
spileup4 = array.array('f',[0.0])
sfoton4 = array.array('f',[0.0])
sfotontrigger4 = array.array('f',[0.0])
xsection4 = array.array('f',[0.0])

energiafotones5 = ROOT.std.vector('float')() 
momentofotones5 = ROOT.std.vector('float')()
etafotones5 = ROOT.std.vector('float')()
phifotones5 = ROOT.std.vector('float')()
trigfotones5 = array.array('i',[0])
tightfotones5 = ROOT.std.vector('bool')()
ptconefotones5 = ROOT.std.vector('float')()
etconefotones5 = ROOT.std.vector('float')()
mc5 = array.array('f',[0.0])
spileup5 = array.array('f',[0.0])
sfoton5 = array.array('f',[0.0])
sfotontrigger5 = array.array('f',[0.0])
xsection5 = array.array('f',[0.0])

## DATA ##

energiafotonesA = ROOT.std.vector('float')() 
momentofotonesA = ROOT.std.vector('float')()
etafotonesA = ROOT.std.vector('float')()
phifotonesA = ROOT.std.vector('float')()
trigfotonesA = array.array('i',[0])
tightfotonesA = ROOT.std.vector('bool')()
ptconefotonesA = ROOT.std.vector('float')()
etconefotonesA = ROOT.std.vector('float')()
mcA = array.array('f',[0.0])
spileupA = array.array('f',[0.0])
sfotonA = array.array('f',[0.0])
sfotontriggerA = array.array('f',[0.0])
xsectionA = array.array('f',[0.0])

energiafotonesB = ROOT.std.vector('float')() 
momentofotonesB = ROOT.std.vector('float')()
etafotonesB = ROOT.std.vector('float')()
phifotonesB = ROOT.std.vector('float')()
trigfotonesB = array.array('i',[0])
tightfotonesB = ROOT.std.vector('bool')()
ptconefotonesB = ROOT.std.vector('float')()
etconefotonesB = ROOT.std.vector('float')()
mcB = array.array('f',[0.0])
spileupB = array.array('f',[0.0])
sfotonB = array.array('f',[0.0])
sfotontriggerB = array.array('f',[0.0])
xsectionB = array.array('f',[0.0])

energiafotonesC = ROOT.std.vector('float')() 
momentofotonesC = ROOT.std.vector('float')()
etafotonesC = ROOT.std.vector('float')()
phifotonesC = ROOT.std.vector('float')()
trigfotonesC = array.array('i',[0])
tightfotonesC = ROOT.std.vector('bool')()
ptconefotonesC = ROOT.std.vector('float')()
etconefotonesC = ROOT.std.vector('float')()
mcC = array.array('f',[0.0])
spileupC = array.array('f',[0.0])
sfotonC = array.array('f',[0.0])
sfotontriggerC = array.array('f',[0.0])
xsectionC = array.array('f',[0.0])

energiafotonesD = ROOT.std.vector('float')() 
momentofotonesD = ROOT.std.vector('float')()
etafotonesD = ROOT.std.vector('float')()
phifotonesD = ROOT.std.vector('float')()
trigfotonesD = array.array('i',[0])
tightfotonesD = ROOT.std.vector('bool')()
ptconefotonesD = ROOT.std.vector('float')()
etconefotonesD = ROOT.std.vector('float')()
mcD = array.array('f',[0.0])
spileupD = array.array('f',[0.0])
sfotonD = array.array('f',[0.0])
sfotontriggerD = array.array('f',[0.0])
xsectionD = array.array('f',[0.0])

M=[arbolA.GetEntries(),arbolB.GetEntries(),arbolC.GetEntries(),arbolD.GetEntries()] #M
n=1000
#0.045 max de r
r=0.045
mm=[round(M[0]*r),round(M[1]*r),round(M[2]*r),round(M[3]*r)]

## MC ##

arbol1.SetBranchAddress("photon_E", energiafotones1)
arbol1.SetBranchAddress("photon_pt", momentofotones1)
arbol1.SetBranchAddress("photon_eta", etafotones1)
arbol1.SetBranchAddress("photon_phi", phifotones1)
arbol1.SetBranchAddress("trigP",trigfotones1)
arbol1.SetBranchAddress("photon_isTightID",tightfotones1)
arbol1.SetBranchAddress("photon_ptcone30",ptconefotones1)
arbol1.SetBranchAddress("photon_etcone20",etconefotones1)
arbol1.SetBranchAddress("mcWeight", mc1)
arbol1.SetBranchAddress("scaleFactor_PILEUP",spileup1)
arbol1.SetBranchAddress("scaleFactor_PHOTON",sfoton1)
arbol1.SetBranchAddress("scaleFactor_PhotonTRIGGER",sfotontrigger1)
arbol1.SetBranchAddress("XSection",xsection1)

arbol2.SetBranchAddress("photon_E", energiafotones2)
arbol2.SetBranchAddress("photon_pt", momentofotones2)
arbol2.SetBranchAddress("photon_eta", etafotones2)
arbol2.SetBranchAddress("photon_phi", phifotones2)
arbol2.SetBranchAddress("trigP",trigfotones2)
arbol2.SetBranchAddress("photon_isTightID",tightfotones2)
arbol2.SetBranchAddress("photon_ptcone30",ptconefotones2)
arbol2.SetBranchAddress("photon_etcone20",etconefotones2)
arbol2.SetBranchAddress("mcWeight", mc2)
arbol2.SetBranchAddress("scaleFactor_PILEUP",spileup2)
arbol2.SetBranchAddress("scaleFactor_PHOTON",sfoton2)
arbol2.SetBranchAddress("scaleFactor_PhotonTRIGGER",sfotontrigger2)
arbol2.SetBranchAddress("XSection",xsection2)

arbol3.SetBranchAddress("photon_E", energiafotones3)
arbol3.SetBranchAddress("photon_pt", momentofotones3)
arbol3.SetBranchAddress("photon_eta", etafotones3)
arbol3.SetBranchAddress("photon_phi", phifotones3)
arbol3.SetBranchAddress("trigP",trigfotones3)
arbol3.SetBranchAddress("photon_isTightID",tightfotones3)
arbol3.SetBranchAddress("photon_ptcone30",ptconefotones3)
arbol3.SetBranchAddress("photon_etcone20",etconefotones3)
arbol3.SetBranchAddress("mcWeight", mc3)
arbol3.SetBranchAddress("scaleFactor_PILEUP",spileup3)
arbol3.SetBranchAddress("scaleFactor_PHOTON",sfoton3)
arbol3.SetBranchAddress("scaleFactor_PhotonTRIGGER",sfotontrigger3)
arbol3.SetBranchAddress("XSection",xsection3)

arbol4.SetBranchAddress("photon_E", energiafotones4)
arbol4.SetBranchAddress("photon_pt", momentofotones4)
arbol4.SetBranchAddress("photon_eta", etafotones4)
arbol4.SetBranchAddress("photon_phi", phifotones4)
arbol4.SetBranchAddress("trigP",trigfotones4)
arbol4.SetBranchAddress("photon_isTightID",tightfotones4)
arbol4.SetBranchAddress("photon_ptcone30",ptconefotones4)
arbol4.SetBranchAddress("photon_etcone20",etconefotones4)
arbol4.SetBranchAddress("mcWeight", mc4)
arbol4.SetBranchAddress("scaleFactor_PILEUP",spileup4)
arbol4.SetBranchAddress("scaleFactor_PHOTON",sfoton4)
arbol4.SetBranchAddress("scaleFactor_PhotonTRIGGER",sfotontrigger4)
arbol4.SetBranchAddress("XSection",xsection4)


arbol5.SetBranchAddress("photon_E", energiafotones5)
arbol5.SetBranchAddress("photon_pt", momentofotones5)
arbol5.SetBranchAddress("photon_eta", etafotones5)
arbol5.SetBranchAddress("photon_phi", phifotones5)
arbol5.SetBranchAddress("trigP",trigfotones5)
arbol5.SetBranchAddress("photon_isTightID",tightfotones5)
arbol5.SetBranchAddress("photon_ptcone30",ptconefotones5)
arbol5.SetBranchAddress("photon_etcone20",etconefotones5)
arbol5.SetBranchAddress("mcWeight", mc5)
arbol5.SetBranchAddress("scaleFactor_PILEUP",spileup5)
arbol5.SetBranchAddress("scaleFactor_PHOTON",sfoton5)
arbol5.SetBranchAddress("scaleFactor_PhotonTRIGGER",sfotontrigger5)
arbol5.SetBranchAddress("XSection",xsection5)

## DATA ##

arbolA.SetBranchAddress("photon_E", energiafotonesA)
arbolA.SetBranchAddress("photon_pt", momentofotonesA)
arbolA.SetBranchAddress("photon_eta", etafotonesA)
arbolA.SetBranchAddress("photon_phi", phifotonesA)
arbolA.SetBranchAddress("trigP", trigfotonesA)
arbolA.SetBranchAddress("photon_isTightID", tightfotonesA)
arbolA.SetBranchAddress("photon_ptcone30", ptconefotonesA)
arbolA.SetBranchAddress("photon_etcone20", etconefotonesA)
arbolA.SetBranchAddress("mcWeight", mcA)
arbolA.SetBranchAddress("scaleFactor_PILEUP", spileupA)
arbolA.SetBranchAddress("scaleFactor_PHOTON", sfotonA)
arbolA.SetBranchAddress("scaleFactor_PhotonTRIGGER", sfotontriggerA)
arbolA.SetBranchAddress("XSection", xsectionA)

arbolB.SetBranchAddress("photon_E", energiafotonesB)
arbolB.SetBranchAddress("photon_pt", momentofotonesB)
arbolB.SetBranchAddress("photon_eta", etafotonesB)
arbolB.SetBranchAddress("photon_phi", phifotonesB)
arbolB.SetBranchAddress("trigP", trigfotonesB)
arbolB.SetBranchAddress("photon_isTightID", tightfotonesB)
arbolB.SetBranchAddress("photon_ptcone30", ptconefotonesB)
arbolB.SetBranchAddress("photon_etcone20", etconefotonesB)
arbolB.SetBranchAddress("mcWeight", mcB)
arbolB.SetBranchAddress("scaleFactor_PILEUP", spileupB)
arbolB.SetBranchAddress("scaleFactor_PHOTON", sfotonB)
arbolB.SetBranchAddress("scaleFactor_PhotonTRIGGER", sfotontriggerB)
arbolB.SetBranchAddress("XSection", xsectionB)

arbolC.SetBranchAddress("photon_E", energiafotonesC)
arbolC.SetBranchAddress("photon_pt", momentofotonesC)
arbolC.SetBranchAddress("photon_eta", etafotonesC)
arbolC.SetBranchAddress("photon_phi", phifotonesC)
arbolC.SetBranchAddress("trigP", trigfotonesC)
arbolC.SetBranchAddress("photon_isTightID", tightfotonesC)
arbolC.SetBranchAddress("photon_ptcone30", ptconefotonesC)
arbolC.SetBranchAddress("photon_etcone20", etconefotonesC)
arbolC.SetBranchAddress("mcWeight", mcC)
arbolC.SetBranchAddress("scaleFactor_PILEUP", spileupC)
arbolC.SetBranchAddress("scaleFactor_PHOTON", sfotonC)
arbolC.SetBranchAddress("scaleFactor_PhotonTRIGGER", sfotontriggerC)
arbolC.SetBranchAddress("XSection", xsectionC)

arbolD.SetBranchAddress("photon_E", energiafotonesD)
arbolD.SetBranchAddress("photon_pt", momentofotonesD)
arbolD.SetBranchAddress("photon_eta", etafotonesD)
arbolD.SetBranchAddress("photon_phi", phifotonesD)
arbolD.SetBranchAddress("trigP", trigfotonesD)
arbolD.SetBranchAddress("photon_isTightID", tightfotonesD)
arbolD.SetBranchAddress("photon_ptcone30", ptconefotonesD)
arbolD.SetBranchAddress("photon_etcone20", etconefotonesD)
arbolD.SetBranchAddress("mcWeight", mcD)
arbolD.SetBranchAddress("scaleFactor_PILEUP", spileupD)
arbolD.SetBranchAddress("scaleFactor_PHOTON", sfotonD)
arbolD.SetBranchAddress("scaleFactor_PhotonTRIGGER", sfotontriggerD)
arbolD.SetBranchAddress("XSection", xsectionD)

##LLENANDO LAS CARACTERISTICAS DE LOS FOTONES##


listafoton1=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #e,pt,eta,phi,trig,tight,ptcone,etcone,etotal,p2,m,mc,pileup,scalefoton,sfotontrigger,xsection
listafoton2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafoton3=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafoton4=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafoton5=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafotonA = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafotonB = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafotonC = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafotonD = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]


listavectores1=[] #tlorentz fotones
listavectores2=[] 
listavectores3=[]
listavectores4=[] 
listavectores5=[]
listavectoresA = []
listavectoresB = []
listavectoresC = []
listavectoresD = []


listavectoreslistos1=[] #tlorentz con cortes
listavectoreslistos2=[]
listavectoreslistos3=[]
listavectoreslistos4=[]
listavectoreslistos5=[]
listavectoreslistosA = []
listavectoreslistosB = []
listavectoreslistosC = []
listavectoreslistosD = []


# MC #
for i in range(n):
    # Listas de fotones
    for j in range(8):
        listafoton1[j].append([])
        listafoton2[j].append([])
        listafoton3[j].append([])
        listafoton4[j].append([])
        listafoton5[j].append([])

    for j in range(11, 16):
        listafoton1[j].append([])
        listafoton2[j].append([])
        listafoton3[j].append([])
        listafoton4[j].append([])
        listafoton5[j].append([])

    # tlorentz fotones
    listavectores1.append([])
    listavectores2.append([])
    listavectores3.append([])
    listavectores4.append([])
    listavectores5.append([])


# DATA #
for i in range(mm[0]):
    # Listas de fotones
    for j in range(8):
        listafotonA[j].append([])

    for j in range(11, 16):
        listafotonA[j].append([])

    # tlorentz fotones
    listavectoresA.append([])

for i in range(mm[1]):
    # Listas de fotones
    for j in range(8):
        listafotonB[j].append([])

    for j in range(11, 16):
        listafotonB[j].append([])

    # tlorentz fotones
    listavectoresB.append([])

for i in range(mm[2]):
    # Listas de fotones
    for j in range(8):
        listafotonC[j].append([])

    for j in range(11, 16):
        listafotonC[j].append([])

    # tlorentz fotones
    listavectoresC.append([])

for i in range(mm[3]):
    # Listas de fotones
    for j in range(8):
        listafotonD[j].append([])

    for j in range(11, 16):
        listafotonD[j].append([])

    # tlorentz fotones
    listavectoresD.append([])

# MC #

for i in range(n):
    arbol1.GetEntry(i)
    for j in range(len(energiafotones1)):
        listafoton1[0][i].append([])
        listafoton1[0][i][j] = energiafotones1[j] / 1000
    for j in range(len(momentofotones1)):
        listafoton1[1][i].append([])
        listafoton1[1][i][j] = momentofotones1[j] / 1000
    for j in range(len(etafotones1)):
        listafoton1[2][i].append([])
        listafoton1[2][i][j] = np.abs(etafotones1[j])
    for j in range(len(phifotones1)):
        listafoton1[3][i].append([])
        listafoton1[3][i][j] = phifotones1[j]
    listafoton1[4][i] = trigfotones1[0]
    for j in range(len(tightfotones1)):
        listafoton1[5][i].append([])
        listafoton1[5][i][j] = tightfotones1[j]
    for j in range(len(ptconefotones1)):
        listafoton1[6][i].append([])
        listafoton1[6][i][j] = ptconefotones1[j]
    for j in range(len(etconefotones1)):
        listafoton1[7][i].append([])
        listafoton1[7][i][j] = etconefotones1[j]
    listafoton1[11][i] = mc1[0]
    listafoton1[12][i] = spileup1[0]
    listafoton1[13][i] = sfoton1[0]
    listafoton1[14][i] = sfotontrigger1[0]
    listafoton1[15][i] = xsection1[0]

for i in range(n):
    arbol2.GetEntry(i)
    for j in range(len(energiafotones2)):
        listafoton2[0][i].append([])
        listafoton2[0][i][j] = energiafotones2[j] / 1000
    for j in range(len(momentofotones2)):
        listafoton2[1][i].append([])
        listafoton2[1][i][j] = momentofotones2[j] / 1000
    for j in range(len(etafotones2)):
        listafoton2[2][i].append([])
        listafoton2[2][i][j] = np.abs(etafotones2[j])
    for j in range(len(phifotones2)):
        listafoton2[3][i].append([])
        listafoton2[3][i][j] = phifotones2[j]
    listafoton2[4][i] = trigfotones2[0]
    for j in range(len(tightfotones2)):
        listafoton2[5][i].append([])
        listafoton2[5][i][j] = tightfotones2[j]
    for j in range(len(ptconefotones2)):
        listafoton2[6][i].append([])
        listafoton2[6][i][j] = ptconefotones2[j]
    for j in range(len(etconefotones2)):
        listafoton2[7][i].append([])
        listafoton2[7][i][j] = etconefotones2[j]
    listafoton2[11][i] = mc2[0]
    listafoton2[12][i] = spileup2[0]
    listafoton2[13][i] = sfoton2[0]
    listafoton2[14][i] = sfotontrigger2[0]
    listafoton2[15][i] = xsection2[0]

for i in range(n):
    arbol3.GetEntry(i)
    for j in range(len(energiafotones3)):
        listafoton3[0][i].append([])
        listafoton3[0][i][j] = energiafotones3[j] / 1000
    for j in range(len(momentofotones3)):
        listafoton3[1][i].append([])
        listafoton3[1][i][j] = momentofotones3[j] / 1000
    for j in range(len(etafotones3)):
        listafoton3[2][i].append([])
        listafoton3[2][i][j] = np.abs(etafotones3[j])
    for j in range(len(phifotones3)):
        listafoton3[3][i].append([])
        listafoton3[3][i][j] = phifotones3[j]
    listafoton3[4][i] = trigfotones3[0]
    for j in range(len(tightfotones3)):
        listafoton3[5][i].append([])
        listafoton3[5][i][j] = tightfotones3[j]
    for j in range(len(ptconefotones3)):
        listafoton3[6][i].append([])
        listafoton3[6][i][j] = ptconefotones3[j]
    for j in range(len(etconefotones3)):
        listafoton3[7][i].append([])
        listafoton3[7][i][j] = etconefotones3[j]
    listafoton3[11][i] = mc3[0]
    listafoton3[12][i] = spileup3[0]
    listafoton3[13][i] = sfoton3[0]
    listafoton3[14][i] = sfotontrigger3[0]
    listafoton3[15][i] = xsection3[0]

for i in range(n):
    arbol4.GetEntry(i)
    for j in range(len(energiafotones4)):
        listafoton4[0][i].append([])
        listafoton4[0][i][j] = energiafotones4[j] / 1000
    for j in range(len(momentofotones4)):
        listafoton4[1][i].append([])
        listafoton4[1][i][j] = momentofotones4[j] / 1000
    for j in range(len(etafotones4)):
        listafoton4[2][i].append([])
        listafoton4[2][i][j] = np.abs(etafotones4[j])
    for j in range(len(phifotones4)):
        listafoton4[3][i].append([])
        listafoton4[3][i][j] = phifotones4[j]
    listafoton4[4][i] = trigfotones4[0]
    for j in range(len(tightfotones4)):
        listafoton4[5][i].append([])
        listafoton4[5][i][j] = tightfotones4[j]
    for j in range(len(ptconefotones4)):
        listafoton4[6][i].append([])
        listafoton4[6][i][j] = ptconefotones4[j]
    for j in range(len(etconefotones4)):
        listafoton4[7][i].append([])
        listafoton4[7][i][j] = etconefotones4[j]
    listafoton4[11][i] = mc4[0]
    listafoton4[12][i] = spileup4[0]
    listafoton4[13][i] = sfoton4[0]
    listafoton4[14][i] = sfotontrigger4[0]
    listafoton4[15][i] = xsection4[0]

for i in range(n):
    arbol5.GetEntry(i)
    for j in range(len(energiafotones5)):
        listafoton5[0][i].append([])
        listafoton5[0][i][j] = energiafotones5[j] / 1000
    for j in range(len(momentofotones5)):
        listafoton5[1][i].append([])
        listafoton5[1][i][j] = momentofotones5[j] / 1000
    for j in range(len(etafotones5)):
        listafoton5[2][i].append([])
        listafoton5[2][i][j] = np.abs(etafotones5[j])
    for j in range(len(phifotones5)):
        listafoton5[3][i].append([])
        listafoton5[3][i][j] = phifotones5[j]
    listafoton5[4][i] = trigfotones5[0]
    for j in range(len(tightfotones5)):
        listafoton5[5][i].append([])
        listafoton5[5][i][j] = tightfotones5[j]
    for j in range(len(ptconefotones5)):
        listafoton5[6][i].append([])
        listafoton5[6][i][j] = ptconefotones5[j]
    for j in range(len(etconefotones5)):
        listafoton5[7][i].append([])
        listafoton5[7][i][j] = etconefotones5[j]
    listafoton5[11][i] = mc5[0]
    listafoton5[12][i] = spileup5[0]
    listafoton5[13][i] = sfoton5[0]
    listafoton5[14][i] = sfotontrigger5[0]
    listafoton5[15][i] = xsection5[0]

# DATA #

for i in range(mm[0]):
    arbolA.GetEntry(i)
    for j in range(len(energiafotonesA)):
        listafotonA[0][i].append([])
        listafotonA[0][i][j] = energiafotonesA[j] / 1000
    for j in range(len(momentofotonesA)):
        listafotonA[1][i].append([])
        listafotonA[1][i][j] = momentofotonesA[j] / 1000
    for j in range(len(etafotonesA)):
        listafotonA[2][i].append([])
        listafotonA[2][i][j] = np.abs(etafotonesA[j])
    for j in range(len(phifotonesA)):
        listafotonA[3][i].append([])
        listafotonA[3][i][j] = phifotonesA[j]
    listafotonA[4][i] = trigfotonesA[0]
    for j in range(len(tightfotonesA)):
        listafotonA[5][i].append([])
        listafotonA[5][i][j] = tightfotonesA[j]
    for j in range(len(ptconefotonesA)):
        listafotonA[6][i].append([])
        listafotonA[6][i][j] = ptconefotonesA[j]
    for j in range(len(etconefotonesA)):
        listafotonA[7][i].append([])
        listafotonA[7][i][j] = etconefotonesA[j]
    listafotonA[11][i] = mcA[0]
    listafotonA[12][i] = spileupA[0]
    listafotonA[13][i] = sfotonA[0]
    listafotonA[14][i] = sfotontriggerA[0]
    listafotonA[15][i] = xsectionA[0]

for i in range(mm[1]):
    arbolB.GetEntry(i)
    for j in range(len(energiafotonesB)):
        listafotonB[0][i].append([])
        listafotonB[0][i][j] = energiafotonesB[j] / 1000
    for j in range(len(momentofotonesB)):
        listafotonB[1][i].append([])
        listafotonB[1][i][j] = momentofotonesB[j] / 1000
    for j in range(len(etafotonesB)):
        listafotonB[2][i].append([])
        listafotonB[2][i][j] = np.abs(etafotonesB[j])
    for j in range(len(phifotonesB)):
        listafotonB[3][i].append([])
        listafotonB[3][i][j] = phifotonesB[j]
    listafotonB[4][i] = trigfotonesB[0]
    for j in range(len(tightfotonesB)):
        listafotonB[5][i].append([])
        listafotonB[5][i][j] = tightfotonesB[j]
    for j in range(len(ptconefotonesB)):
        listafotonB[6][i].append([])
        listafotonB[6][i][j] = ptconefotonesB[j]
    for j in range(len(etconefotonesB)):
        listafotonB[7][i].append([])
        listafotonB[7][i][j] = etconefotonesB[j]
    listafotonB[11][i] = mcB[0]
    listafotonB[12][i] = spileupB[0]
    listafotonB[13][i] = sfotonB[0]
    listafotonB[14][i] = sfotontriggerB[0]
    listafotonB[15][i] = xsectionB[0]

for i in range(mm[2]):
    arbolC.GetEntry(i)
    for j in range(len(energiafotonesC)):
        listafotonC[0][i].append([])
        listafotonC[0][i][j] = energiafotonesC[j] / 1000
    for j in range(len(momentofotonesC)):
        listafotonC[1][i].append([])
        listafotonC[1][i][j] = momentofotonesC[j] / 1000
    for j in range(len(etafotonesC)):
        listafotonC[2][i].append([])
        listafotonC[2][i][j] = np.abs(etafotonesC[j])
    for j in range(len(phifotonesC)):
        listafotonC[3][i].append([])
        listafotonC[3][i][j] = phifotonesC[j]
    listafotonC[4][i] = trigfotonesC[0]
    for j in range(len(tightfotonesC)):
        listafotonC[5][i].append([])
        listafotonC[5][i][j] = tightfotonesC[j]
    for j in range(len(ptconefotonesC)):
        listafotonC[6][i].append([])
        listafotonC[6][i][j] = ptconefotonesC[j]
    for j in range(len(etconefotonesC)):
        listafotonC[7][i].append([])
        listafotonC[7][i][j] = etconefotonesC[j]
    listafotonC[11][i] = mcC[0]
    listafotonC[12][i] = spileupC[0]
    listafotonC[13][i] = sfotonC[0]
    listafotonC[14][i] = sfotontriggerC[0]
    listafotonC[15][i] = xsectionC[0]

for i in range(mm[3]):
    arbolD.GetEntry(i)
    for j in range(len(energiafotonesD)):
        listafotonD[0][i].append([])
        listafotonD[0][i][j] = energiafotonesD[j] / 1000
    for j in range(len(momentofotonesD)):
        listafotonD[1][i].append([])
        listafotonD[1][i][j] = momentofotonesD[j] / 1000
    for j in range(len(etafotonesD)):
        listafotonD[2][i].append([])
        listafotonD[2][i][j] = np.abs(etafotonesD[j])
    for j in range(len(phifotonesD)):
        listafotonD[3][i].append([])
        listafotonD[3][i][j] = phifotonesD[j]
    listafotonD[4][i] = trigfotonesD[0]
    for j in range(len(tightfotonesD)):
        listafotonD[5][i].append([])
        listafotonD[5][i][j] = tightfotonesD[j]
    for j in range(len(ptconefotonesD)):
        listafotonD[6][i].append([])
        listafotonD[6][i][j] = ptconefotonesD[j]
    for j in range(len(etconefotonesD)):
        listafotonD[7][i].append([])
        listafotonD[7][i][j] = etconefotonesD[j]
    listafotonD[11][i] = mcD[0]
    listafotonD[12][i] = spileupD[0]
    listafotonD[13][i] = sfotonD[0]
    listafotonD[14][i] = sfotontriggerD[0]
    listafotonD[15][i] = xsectionD[0]


##CREANDO LOS TLORENTZ VECTOR##

# MC #

for i in range(n):
    for j in range(len(listafoton1[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafoton1[1][i][j], listafoton1[2][i][j], listafoton1[3][i][j], listafoton1[0][i][j])
        listavectores1[i].append(vec)

for i in range(n):
    for j in range(len(listafoton2[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafoton2[1][i][j], listafoton2[2][i][j], listafoton2[3][i][j], listafoton2[0][i][j])
        listavectores2[i].append(vec)

for i in range(n):
    for j in range(len(listafoton3[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafoton3[1][i][j], listafoton3[2][i][j], listafoton3[3][i][j], listafoton3[0][i][j])
        listavectores3[i].append(vec)

for i in range(n):
    for j in range(len(listafoton4[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafoton4[1][i][j], listafoton4[2][i][j], listafoton4[3][i][j], listafoton4[0][i][j])
        listavectores4[i].append(vec)

for i in range(n):
    for j in range(len(listafoton5[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafoton5[1][i][j], listafoton5[2][i][j], listafoton5[3][i][j], listafoton5[0][i][j])
        listavectores5[i].append(vec)

# DATA #

for i in range(mm[0]):
    for j in range(len(listafotonA[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafotonA[1][i][j], listafotonA[2][i][j], listafotonA[3][i][j], listafotonA[0][i][j])
        listavectoresA[i].append(vec)

for i in range(mm[1]):
    for j in range(len(listafotonB[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafotonB[1][i][j], listafotonB[2][i][j], listafotonB[3][i][j], listafotonB[0][i][j])
        listavectoresB[i].append(vec)

for i in range(mm[2]):
    for j in range(len(listafotonC[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafotonC[1][i][j], listafotonC[2][i][j], listafotonC[3][i][j], listafotonC[0][i][j])
        listavectoresC[i].append(vec)

for i in range(mm[3]):
    for j in range(len(listafotonD[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafotonD[1][i][j], listafotonD[2][i][j], listafotonD[3][i][j], listafotonD[0][i][j])
        listavectoresD[i].append(vec)


##CREANDO LOS TLORENTZ VECTOR DE LOS HIGGS RECONSTRUIDOS##

listavec1 = [] # tlorentz Higgs para el conjunto 1
listavec2 = []
listavec3 = []
listavec4 = []
listavec5 = []
listavecA = []
listavecB = []
listavecC = []
listavecD = []


# MC #

for i in range(n):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafoton1[0][i])):
        vecsum += listavectores1[i][j]
    listavec1.append(vecsum)

for i in range(n):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafoton2[0][i])):
        vecsum += listavectores2[i][j]
    listavec2.append(vecsum)

for i in range(n):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafoton3[0][i])):
        vecsum += listavectores3[i][j]
    listavec3.append(vecsum)

for i in range(n):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafoton4[0][i])):
        vecsum += listavectores4[i][j]
    listavec4.append(vecsum)

for i in range(n):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafoton5[0][i])):
        vecsum += listavectores5[i][j]
    listavec5.append(vecsum)

# DATA #

for i in range(mm[0]):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafotonA[0][i])):
        vecsum += listavectoresA[i][j]
    listavecA.append(vecsum)

for i in range(mm[1]):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafotonB[0][i])):
        vecsum += listavectoresB[i][j]
    listavecB.append(vecsum)

for i in range(mm[2]):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafotonC[0][i])):
        vecsum += listavectoresC[i][j]
    listavecC.append(vecsum)

for i in range(mm[3]):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafotonD[0][i])):
        vecsum += listavectoresD[i][j]
    listavecD.append(vecsum)


##AGREGANDO LA NUEVA INFORMACION A LAS LISTAS DE LOS FOTONES##

# MC #

for i in range(n):
    E = listavec1[i].E()
    px = listavec1[i].Px()
    py = listavec1[i].Py()
    pz = listavec1[i].Pz()
    listafoton1[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafoton1[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafoton1[10].append(m)

for i in range(n):
    E = listavec2[i].E()
    px = listavec2[i].Px()
    py = listavec2[i].Py()
    pz = listavec2[i].Pz()
    listafoton2[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafoton2[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafoton2[10].append(m)

for i in range(n):
    E = listavec3[i].E()
    px = listavec3[i].Px()
    py = listavec3[i].Py()
    pz = listavec3[i].Pz()
    listafoton3[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafoton3[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafoton3[10].append(m)

for i in range(n):
    E = listavec4[i].E()
    px = listavec4[i].Px()
    py = listavec4[i].Py()
    pz = listavec4[i].Pz()
    listafoton4[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafoton4[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafoton4[10].append(m)

for i in range(n):
    E = listavec5[i].E()
    px = listavec5[i].Px()
    py = listavec5[i].Py()
    pz = listavec5[i].Pz()
    listafoton5[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafoton5[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafoton5[10].append(m)

# DATA #

for i in range(mm[0]):
    E = listavecA[i].E()
    px = listavecA[i].Px()
    py = listavecA[i].Py()
    pz = listavecA[i].Pz()
    listafotonA[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafotonA[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafotonA[10].append(m)

for i in range(mm[1]):
    E = listavecB[i].E()
    px = listavecB[i].Px()
    py = listavecB[i].Py()
    pz = listavecB[i].Pz()
    listafotonB[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafotonB[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafotonB[10].append(m)

for i in range(mm[2]):
    E = listavecC[i].E()
    px = listavecC[i].Px()
    py = listavecC[i].Py()
    pz = listavecC[i].Pz()
    listafotonC[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafotonC[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafotonC[10].append(m)

for i in range(mm[3]):
    E = listavecD[i].E()
    px = listavecD[i].Px()
    py = listavecD[i].Py()
    pz = listavecD[i].Pz()
    listafotonD[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafotonD[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafotonD[10].append(m)


##CORTES##


cortes = [
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes 1
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes 2
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes 3
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes 4
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes A
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes B
    [0, 0, 0, 0, 0, 0, 0, 0],  # cortes C
    [0, 0, 0, 0, 0, 0, 0, 0]   # cortes D
]


# Conteos para los conjuntos: cantidad de eventos de más de dos fotones y cantidad de eventos de más de 2 fotones que aún quedan luego de los primeros 4 cortes


n_values = [
    [0, 0],  # para 1: [n10, n1]
    [0, 0],  # para 2: [n20, n2]
    [0, 0],  # para 3: [n30, n3]
    [0, 0],  # para 4: [n40, n4]
    [0, 0],  # para 5: [n50, n5]
    [0, 0],  # para A: [nA0, nA]
    [0, 0],  # para B: [nB0, nB]
    [0, 0],  # para C: [nC0, nC]
    [0, 0]   # para D: [nD0, nD]
]


# Inicialización de listas para contar la cantidad de cortes que pasa cada grupo de fotones: lista con la cantidad de cortes que pasa cada grupo de fotones para el conjunto 1

C = [
    [0] * n,  # C1
    [0] * n,  # C2
    [0] * n,  # C3
    [0] * n,  # C4
    [0] * n,  # C5
    [0] * mm[0],  # CA
    [0] * mm[1],  # CB
    [0] * mm[2],  # CC
    [0] * mm[3]   # CD
]


for i in range(n):
    ## TRIGGER #
    if listafoton1[4][i] == 1:
        C[0][i] += 1
    if C[0][i] == 1:
        cortes[0][0] += 1

    if listafoton2[4][i] == 1:
        C[1][i] += 1
    if C[1][i] == 1:
        cortes[1][0] += 1

    if listafoton3[4][i] == 1:
        C[2][i] += 1
    if C[2][i] == 1:
        cortes[2][0] += 1

    if listafoton4[4][i] == 1:
        C[3][i] += 1
    if C[3][i] == 1:
        cortes[3][0] += 1

    if listafoton5[4][i] == 1:
        C[4][i] += 1
    if C[4][i] == 1:
        cortes[4][0] += 1

    # TIGHT ID #
    
    c11 = 0
    for j in range(len(listafoton1[5][i])):
        if listafoton1[5][i][j] == 1:
            c11 += 1
    if c11 == len(listafoton1[5][i]):
        C[0][i] += 1
    if C[0][i] == 2:
        cortes[0][1] += 1

    c21 = 0
    for j in range(len(listafoton2[5][i])):
        if listafoton2[5][i][j] == 1:
            c21 += 1
    if c21 == len(listafoton2[5][i]):
        C[1][i] += 1
    if C[1][i] == 2:
        cortes[1][1] += 1

    c31 = 0
    for j in range(len(listafoton3[5][i])):
        if listafoton3[5][i][j] == 1:
            c31 += 1
    if c31 == len(listafoton3[5][i]):
        C[2][i] += 1
    if C[2][i] == 2:
        cortes[2][1] += 1

    c41 = 0
    for j in range(len(listafoton4[5][i])):
        if listafoton4[5][i][j] == 1:
            c41 += 1
    if c41 == len(listafoton4[5][i]):
        C[3][i] += 1
    if C[3][i] == 2:
        cortes[3][1] += 1

    c51 = 0
    for j in range(len(listafoton5[5][i])):
        if listafoton5[5][i][j] == 1:
            c51 += 1
    if c51 == len(listafoton5[5][i]):
        C[4][i] += 1
    if C[4][i] == 2:
        cortes[4][1] += 1


    # pT #

    c12 = 0
    for j in range(len(listafoton1[1][i])):
        if listafoton1[1][i][j] > 25:
            c12 += 1
    if c12 == len(listafoton1[1][i]):
        C[0][i] += 1
    if C[0][i] == 3:
        cortes[0][2] += 1

    c22 = 0
    for j in range(len(listafoton2[1][i])):
        if listafoton2[1][i][j] > 25:
            c22 += 1
    if c22 == len(listafoton2[1][i]):
        C[1][i] += 1
    if C[1][i] == 3:
        cortes[1][2] += 1

    c32 = 0
    for j in range(len(listafoton3[1][i])):
        if listafoton3[1][i][j] > 25:
            c32 += 1
    if c32 == len(listafoton3[1][i]):
        C[2][i] += 1
    if C[2][i] == 3:
        cortes[2][2] += 1

    c42 = 0
    for j in range(len(listafoton4[1][i])):
        if listafoton4[1][i][j] > 25:
            c42 += 1
    if c42 == len(listafoton4[1][i]):
        C[3][i] += 1
    if C[3][i] == 3:
        cortes[3][2] += 1

    c52 = 0
    for j in range(len(listafoton5[1][i])):
        if listafoton5[1][i][j] > 25:
            c52 += 1
    if c52 == len(listafoton5[1][i]):
        C[4][i] += 1
    if C[4][i] == 3:
        cortes[4][2] += 1


    # ETA #

    c13 = 0
    for j in range(len(listafoton1[2][i])):
        if listafoton1[2][i][j] < 2.37 and (listafoton1[2][i][j] > 1.52 or listafoton1[2][i][j] < 1.37):
            c13 += 1
    if c13 == len(listafoton1[2][i]):
        C[0][i] += 1
    if C[0][i] == 4:
        cortes[0][3] += 1

    c23 = 0
    for j in range(len(listafoton2[2][i])):
        if listafoton2[2][i][j] < 2.37 and (listafoton2[2][i][j] > 1.52 or listafoton2[2][i][j] < 1.37):
            c23 += 1
    if c23 == len(listafoton2[2][i]):
        C[1][i] += 1
    if C[1][i] == 4:
        cortes[1][3] += 1

    c33 = 0
    for j in range(len(listafoton3[2][i])):
        if listafoton3[2][i][j] < 2.37 and (listafoton3[2][i][j] > 1.52 or listafoton3[2][i][j] < 1.37):
            c33 += 1
    if c33 == len(listafoton3[2][i]):
        C[2][i] += 1
    if C[2][i] == 4:
        cortes[2][3] += 1

    c43 = 0
    for j in range(len(listafoton4[2][i])):
        if listafoton4[2][i][j] < 2.37 and (listafoton4[2][i][j] > 1.52 or listafoton4[2][i][j] < 1.37):
            c43 += 1
    if c43 == len(listafoton4[2][i]):
        C[3][i] += 1
    if C[3][i] == 4:
        cortes[3][3] += 1

    c53 = 0
    for j in range(len(listafoton5[2][i])):
        if listafoton5[2][i][j] < 2.37 and (listafoton5[2][i][j] > 1.52 or listafoton5[2][i][j] < 1.37):
            c53 += 1
    if c53 == len(listafoton5[2][i]):
        C[4][i] += 1
    if C[4][i] == 4:
        cortes[4][3] += 1


    # CANTIDAD DE FOTONES POR HIGGS #

    if len(listafoton1[0][i]) > 2 and C[0][i] == 4:
        n_values[0][1] += 1
    if len(listafoton1[0][i]) > 2:
        n_values[0][0] += 1

    if len(listafoton2[0][i]) > 2 and C[1][i] == 4:
        n_values[1][1] += 1
    if len(listafoton2[0][i]) > 2:
        n_values[1][0] += 1

    if len(listafoton3[0][i]) > 2 and C[2][i] == 4:
        n_values[2][1] += 1
    if len(listafoton3[0][i]) > 2:
        n_values[2][0] += 1

    if len(listafoton4[0][i]) > 2 and C[3][i] == 4:
        n_values[3][1] += 1
    if len(listafoton4[0][i]) > 2:
        n_values[3][0] += 1

    if len(listafoton5[0][i]) > 2 and C[4][i] == 4:
        n_values[4][1] += 1
    if len(listafoton5[0][i]) > 2:
        n_values[4][0] += 1


    # PT CONE #

    c14 = 0
    for j in range(len(listafoton1[6][i])):
        if (listafoton1[6][i][j] / listafoton1[1][i][j]) < 0.065:
            c14 += 1
    if c14 == len(listafoton1[6][i]):
        C[0][i] += 1
    if C[0][i] == 5:
        cortes[0][4] += 1

    c24 = 0
    for j in range(len(listafoton2[6][i])):
        if (listafoton2[6][i][j] / listafoton2[1][i][j]) < 0.065:
            c24 += 1
    if c24 == len(listafoton2[6][i]):
        C[1][i] += 1
    if C[1][i] == 5:
        cortes[1][4] += 1

    c34 = 0
    for j in range(len(listafoton3[6][i])):
        if (listafoton3[6][i][j] / listafoton3[1][i][j]) < 0.065:
            c34 += 1
    if c34 == len(listafoton3[6][i]):
        C[2][i] += 1
    if C[2][i] == 5:
        cortes[2][4] += 1

    c44 = 0
    for j in range(len(listafoton4[6][i])):
        if (listafoton4[6][i][j] / listafoton4[1][i][j]) < 0.065:
            c44 += 1
    if c44 == len(listafoton4[6][i]):
        C[3][i] += 1
    if C[3][i] == 5:
        cortes[3][4] += 1

    c54 = 0
    for j in range(len(listafoton5[6][i])):
        if (listafoton5[6][i][j] / listafoton5[1][i][j]) < 0.065:
            c54 += 1
    if c54 == len(listafoton5[6][i]):
        C[4][i] += 1
    if C[4][i] == 5:
        cortes[4][4] += 1


    # ET CONE #

    c15 = 0
    for j in range(len(listafoton1[7][i])):
        if (listafoton1[7][i][j] / listafoton1[1][i][j]) < 0.065:
            c15 += 1
    if c15 == len(listafoton1[7][i]):
        C[0][i] += 1
    if C[0][i] == 6:
        cortes[0][5] += 1

    c25 = 0
    for j in range(len(listafoton2[7][i])):
        if (listafoton2[7][i][j] / listafoton2[1][i][j]) < 0.065:
            c25 += 1
    if c25 == len(listafoton2[7][i]):
        C[1][i] += 1
    if C[1][i] == 6:
        cortes[1][5] += 1

    c35 = 0
    for j in range(len(listafoton3[7][i])):
        if (listafoton3[7][i][j] / listafoton3[1][i][j]) < 0.065:
            c35 += 1
    if c35 == len(listafoton3[7][i]):
        C[2][i] += 1
    if C[2][i] == 6:
        cortes[2][5] += 1

    c45 = 0
    for j in range(len(listafoton4[7][i])):
        if (listafoton4[7][i][j] / listafoton4[1][i][j]) < 0.065:
            c45 += 1
    if c45 == len(listafoton4[7][i]):
        C[3][i] += 1
    if C[3][i] == 6:
        cortes[3][5] += 1

    c55 = 0
    for j in range(len(listafoton5[7][i])):
        if (listafoton5[7][i][j] / listafoton5[1][i][j]) < 0.065:
            c55 += 1
    if c55 == len(listafoton5[7][i]):
        C[4][i] += 1
    if C[4][i] == 6:
        cortes[4][5] += 1


    # PT/MASSgg #

    if (max(listafoton1[1][i]) / listafoton1[10][i]) > 0.35 and (min(listafoton1[1][i]) / listafoton1[10][i]) > 0.25 and len(listafoton1[1][i]) == 2:
        C[0][i] += 1
    if C[0][i] == 7:
        cortes[0][6] += 1

    if (max(listafoton2[1][i]) / listafoton2[10][i]) > 0.35 and (min(listafoton2[1][i]) / listafoton2[10][i]) > 0.25 and len(listafoton2[1][i]) == 2:
        C[1][i] += 1
    if C[1][i] == 7:
        cortes[1][6] += 1

    if (max(listafoton3[1][i]) / listafoton3[10][i]) > 0.35 and (min(listafoton3[1][i]) / listafoton3[10][i]) > 0.25 and len(listafoton3[1][i]) == 2:
        C[2][i] += 1
    if C[2][i] == 7:
        cortes[2][6] += 1

    if (max(listafoton4[1][i]) / listafoton4[10][i]) > 0.35 and (min(listafoton4[1][i]) / listafoton4[10][i]) > 0.25 and len(listafoton4[1][i]) == 2:
        C[3][i] += 1
    if C[3][i] == 7:
        cortes[3][6] += 1

    if (max(listafoton5[1][i]) / listafoton5[10][i]) > 0.35 and (min(listafoton5[1][i]) / listafoton5[10][i]) > 0.25 and len(listafoton5[1][i]) == 2:
        C[4][i] += 1
    if C[4][i] == 7:
        cortes[4][6] += 1


    # VENTANA DE MASAS #
    
    if listafoton1[10][i] > 105 and listafoton1[10][i] < 160:
        C[0][i] += 1
    if C[0][i] == 8:
        cortes[0][7] += 1

    if listafoton2[10][i] > 105 and listafoton2[10][i] < 160:
        C[1][i] += 1
    if C[1][i] == 8:
        cortes[1][7] += 1

    if listafoton3[10][i] > 105 and listafoton3[10][i] < 160:
        C[2][i] += 1
    if C[2][i] == 8:
        cortes[2][7] += 1

    if listafoton4[10][i] > 105 and listafoton4[10][i] < 160:
        C[3][i] += 1
    if C[3][i] == 8:
        cortes[3][7] += 1

    if listafoton5[10][i] > 105 and listafoton5[10][i] < 160:
        C[4][i] += 1
    if C[4][i] == 8:
        cortes[4][7] += 1


# DATA #

for i in range(mm[0]):
    ## TRIGGER #
    if listafotonA[4][i] == 1:
        C[5][i] += 1
    if C[5][i] == 1:
        cortes[5][0] += 1

    # TIGHT ID #
    cA1 = 0
    for j in range(len(listafotonA[5][i])):
        if listafotonA[5][i][j] == 1:
            cA1 += 1
    if cA1 == len(listafotonA[5][i]):
        C[5][i] += 1
    if C[5][i] == 2:
        cortes[5][1] += 1

    # pT #
    cA2 = 0
    for j in range(len(listafotonA[1][i])):
        if listafotonA[1][i][j] > 25:
            cA2 += 1
    if cA2 == len(listafotonA[1][i]):
        C[5][i] += 1
    if C[5][i] == 3:
        cortes[5][2] += 1

    # ETA #
    cA3 = 0
    for j in range(len(listafotonA[2][i])):
        if listafotonA[2][i][j] < 2.37 and (listafotonA[2][i][j] > 1.52 or listafotonA[2][i][j] < 1.37):
            cA3 += 1
    if cA3 == len(listafotonA[2][i]):
        C[5][i] += 1
    if C[5][i] == 4:
        cortes[5][3] += 1

    # CANTIDAD DE FOTONES POR HIGGS #
    if len(listafotonA[0][i]) > 2 and C[5][i] == 4:
        n_values[5][1] += 1
    if len(listafotonA[0][i]) > 2:
        n_values[5][0] += 1

    # PT CONE #
    cA4 = 0
    for j in range(len(listafotonA[6][i])):
        if (listafotonA[6][i][j] / listafotonA[1][i][j]) < 0.065:
            cA4 += 1
    if cA4 == len(listafotonA[6][i]):
        C[5][i] += 1
    if C[5][i] == 5:
        cortes[5][4] += 1

    # ET CONE #
    cA5 = 0
    for j in range(len(listafotonA[7][i])):
        if (listafotonA[7][i][j] / listafotonA[1][i][j]) < 0.065:
            cA5 += 1
    if cA5 == len(listafotonA[7][i]):
        C[5][i] += 1
    if C[5][i] == 6:
        cortes[5][5] += 1

    # PT/MASSgg #
    if (max(listafotonA[1][i]) / listafotonA[10][i]) > 0.35 and (min(listafotonA[1][i]) / listafotonA[10][i]) > 0.25 and len(listafotonA[1][i]) == 2:
        C[5][i] += 1
    if C[5][i] == 7:
        cortes[5][6] += 1

    # VENTANA DE MASAS #
    if listafotonA[10][i] > 105 and listafotonA[10][i] < 160:
        C[5][i] += 1
    if C[5][i] == 8:
        cortes[5][7] += 1

for i in range(mm[1]):
    ## TRIGGER #
    if listafotonB[4][i] == 1:
        C[6][i] += 1
    if C[6][i] == 1:
        cortes[6][0] += 1

    # TIGHT ID #
    cB1 = 0
    for j in range(len(listafotonB[5][i])):
        if listafotonB[5][i][j] == 1:
            cB1 += 1
    if cB1 == len(listafotonB[5][i]):
        C[6][i] += 1
    if C[6][i] == 2:
        cortes[6][1] += 1

    # pT #
    cB2 = 0
    for j in range(len(listafotonB[1][i])):
        if listafotonB[1][i][j] > 25:
            cB2 += 1
    if cB2 == len(listafotonB[1][i]):
        C[6][i] += 1
    if C[6][i] == 3:
        cortes[6][2] += 1

    # ETA #
    cB3 = 0
    for j in range(len(listafotonB[2][i])):
        if listafotonB[2][i][j] < 2.37 and (listafotonB[2][i][j] > 1.52 or listafotonB[2][i][j] < 1.37):
            cB3 += 1
    if cB3 == len(listafotonB[2][i]):
        C[6][i] += 1
    if C[6][i] == 4:
        cortes[6][3] += 1

    # CANTIDAD DE FOTONES POR HIGGS #
    if len(listafotonB[0][i]) > 2 and C[6][i] == 4:
        n_values[6][1] += 1
    if len(listafotonB[0][i]) > 2:
        n_values[6][0] += 1

    # PT CONE #
    cB4 = 0
    for j in range(len(listafotonB[6][i])):
        if (listafotonB[6][i][j] / listafotonB[1][i][j]) < 0.065:
            cB4 += 1
    if cB4 == len(listafotonB[6][i]):
        C[6][i] += 1
    if C[6][i] == 5:
        cortes[6][4] += 1

    # ET CONE #
    cB5 = 0
    for j in range(len(listafotonB[7][i])):
        if (listafotonB[7][i][j] / listafotonB[1][i][j]) < 0.065:
            cB5 += 1
    if cB5 == len(listafotonB[7][i]):
        C[6][i] += 1
    if C[6][i] == 6:
        cortes[6][5] += 1

    # PT/MASSgg #
    if (max(listafotonB[1][i]) / listafotonB[10][i]) > 0.35 and (min(listafotonB[1][i]) / listafotonB[10][i]) > 0.25 and len(listafotonB[1][i]) == 2:
        C[6][i] += 1
    if C[6][i] == 7:
        cortes[6][6] += 1

    # VENTANA DE MASAS #
    if listafotonB[10][i] > 105 and listafotonB[10][i] < 160:
        C[6][i] += 1
    if C[6][i] == 8:
        cortes[6][7] += 1


for i in range(mm[2]):
    ## TRIGGER #
    if listafotonC[4][i] == 1:
        C[7][i] += 1
    if C[7][i] == 1:
        cortes[7][0] += 1

    # TIGHT ID #
    cC1 = 0
    for j in range(len(listafotonC[5][i])):
        if listafotonC[5][i][j] == 1:
            cC1 += 1
    if cC1 == len(listafotonC[5][i]):
        C[7][i] += 1
    if C[7][i] == 2:
        cortes[7][1] += 1

    # pT #
    cC2 = 0
    for j in range(len(listafotonC[1][i])):
        if listafotonC[1][i][j] > 25:
            cC2 += 1
    if cC2 == len(listafotonC[1][i]):
        C[7][i] += 1
    if C[7][i] == 3:
        cortes[7][2] += 1

    # ETA #
    cC3 = 0
    for j in range(len(listafotonC[2][i])):
        if listafotonC[2][i][j] < 2.37 and (listafotonC[2][i][j] > 1.52 or listafotonC[2][i][j] < 1.37):
            cC3 += 1
    if cC3 == len(listafotonC[2][i]):
        C[7][i] += 1
    if C[7][i] == 4:
        cortes[7][3] += 1

    # CANTIDAD DE FOTONES POR HIGGS #
    if len(listafotonC[0][i]) > 2 and C[7][i] == 4:
        n_values[7][1] += 1
    if len(listafotonC[0][i]) > 2:
        n_values[7][0] += 1

    # PT CONE #
    cC4 = 0
    for j in range(len(listafotonC[6][i])):
        if (listafotonC[6][i][j] / listafotonC[1][i][j]) < 0.065:
            cC4 += 1
    if cC4 == len(listafotonC[6][i]):
        C[7][i] += 1
    if C[7][i] == 5:
        cortes[7][4] += 1

    # ET CONE #
    cC5 = 0
    for j in range(len(listafotonC[7][i])):
        if (listafotonC[7][i][j] / listafotonC[1][i][j]) < 0.065:
            cC5 += 1
    if cC5 == len(listafotonC[7][i]):
        C[7][i] += 1
    if C[7][i] == 6:
        cortes[7][5] += 1

    # PT/MASSgg #
    if (max(listafotonC[1][i]) / listafotonC[10][i]) > 0.35 and (min(listafotonC[1][i]) / listafotonC[10][i]) > 0.25 and len(listafotonC[1][i]) == 2:
        C[7][i] += 1
    if C[7][i] == 7:
        cortes[7][6] += 1

    # VENTANA DE MASAS #
    if listafotonC[10][i] > 105 and listafotonC[10][i] < 160:
        C[7][i] += 1
    if C[7][i] == 8:
        cortes[7][7] += 1


for i in range(mm[3]):
    ## TRIGGER #
    if listafotonD[4][i] == 1:
        C[8][i] += 1
    if C[8][i] == 1:
        cortes[8][0] += 1

    # TIGHT ID #
    cD1 = 0
    for j in range(len(listafotonD[5][i])):
        if listafotonD[5][i][j] == 1:
            cD1 += 1
    if cD1 == len(listafotonD[5][i]):
        C[8][i] += 1
    if C[8][i] == 2:
        cortes[8][1] += 1

    # pT #
    cD2 = 0
    for j in range(len(listafotonD[1][i])):
        if listafotonD[1][i][j] > 25:
            cD2 += 1
    if cD2 == len(listafotonD[1][i]):
        C[8][i] += 1
    if C[8][i] == 3:
        cortes[8][2] += 1

    # ETA #
    cD3 = 0
    for j in range(len(listafotonD[2][i])):
        if listafotonD[2][i][j] < 2.37 and (listafotonD[2][i][j] > 1.52 or listafotonD[2][i][j] < 1.37):
            cD3 += 1
    if cD3 == len(listafotonD[2][i]):
        C[8][i] += 1
    if C[8][i] == 4:
        cortes[8][3] += 1

    # CANTIDAD DE FOTONES POR HIGGS #
    if len(listafotonD[0][i]) > 2 and C[8][i] == 4:
        n_values[8][1] += 1
    if len(listafotonD[0][i]) > 2:
        n_values[8][0] += 1

    # PT CONE #
    cD4 = 0
    for j in range(len(listafotonD[6][i])):
        if (listafotonD[6][i][j] / listafotonD[1][i][j]) < 0.065:
            cD4 += 1
    if cD4 == len(listafotonD[6][i]):
        C[8][i] += 1
    if C[8][i] == 5:
        cortes[8][4] += 1

    # ET CONE #
    cD5 = 0
    for j in range(len(listafotonD[7][i])):
        if (listafotonD[7][i][j] / listafotonD[1][i][j]) < 0.065:
            cD5 += 1
    if cD5 == len(listafotonD[7][i]):
        C[8][i] += 1
    if C[8][i] == 6:
        cortes[8][5] += 1

    # PT/MASSgg #
    if (max(listafotonD[1][i]) / listafotonD[10][i]) > 0.35 and (min(listafotonD[1][i]) / listafotonD[10][i]) > 0.25 and len(listafotonD[1][i]) == 2:
        C[8][i] += 1
    if C[8][i] == 7:
        cortes[8][6] += 1

    # VENTANA DE MASAS #
    if listafotonD[10][i] > 105 and listafotonD[10][i] < 160:
        C[8][i] += 1
    if C[8][i] == 8:
        cortes[8][7] += 1


## INICIALIZANDO LOS CORTES ##

listafotonlisto1=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]#fotones con cortes
listafotonlisto2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlisto3=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlisto4=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlisto5=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
listafotonlistoA=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlistoB=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlistoC=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
listafotonlistoD=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 

         
for i in range(cortes[0][7]):
    listafotonlisto1[0].append([])
    listafotonlisto1[1].append([])
    listafotonlisto1[2].append([])
    listafotonlisto1[3].append([])
    listafotonlisto1[4].append([])
    listafotonlisto1[5].append([])
    listafotonlisto1[6].append([])
    listafotonlisto1[7].append([])
    listafotonlisto1[8].append([])
    listafotonlisto1[9].append([])
    listafotonlisto1[10].append([])
    listafotonlisto1[11].append([])
    listafotonlisto1[12].append([])
    listafotonlisto1[13].append([])
    listafotonlisto1[14].append([])
    listafotonlisto1[15].append([])
    listavectoreslistos1.append([])

for i in range(cortes[1][7]):
    listafotonlisto2[0].append([])
    listafotonlisto2[1].append([])
    listafotonlisto2[2].append([])
    listafotonlisto2[3].append([])
    listafotonlisto2[4].append([])
    listafotonlisto2[5].append([])
    listafotonlisto2[6].append([])
    listafotonlisto2[7].append([])
    listafotonlisto2[8].append([])
    listafotonlisto2[9].append([])
    listafotonlisto2[10].append([])
    listafotonlisto2[11].append([])
    listafotonlisto2[12].append([])
    listafotonlisto2[13].append([])
    listafotonlisto2[14].append([])
    listafotonlisto2[15].append([])
    listavectoreslistos2.append([])

for i in range(cortes[2][7]):
    listafotonlisto3[0].append([])
    listafotonlisto3[1].append([])
    listafotonlisto3[2].append([])
    listafotonlisto3[3].append([])
    listafotonlisto3[4].append([])
    listafotonlisto3[5].append([])
    listafotonlisto3[6].append([])
    listafotonlisto3[7].append([])
    listafotonlisto3[8].append([])
    listafotonlisto3[9].append([])
    listafotonlisto3[10].append([])
    listafotonlisto3[11].append([])
    listafotonlisto3[12].append([])
    listafotonlisto3[13].append([])
    listafotonlisto3[14].append([])
    listafotonlisto3[15].append([])
    listavectoreslistos3.append([])

for i in range(cortes[3][7]):
    listafotonlisto4[0].append([])
    listafotonlisto4[1].append([])
    listafotonlisto4[2].append([])
    listafotonlisto4[3].append([])
    listafotonlisto4[4].append([])
    listafotonlisto4[5].append([])
    listafotonlisto4[6].append([])
    listafotonlisto4[7].append([])
    listafotonlisto4[8].append([])
    listafotonlisto4[9].append([])
    listafotonlisto4[10].append([])
    listafotonlisto4[11].append([])
    listafotonlisto4[12].append([])
    listafotonlisto4[13].append([])
    listafotonlisto4[14].append([])
    listafotonlisto4[15].append([])
    listavectoreslistos4.append([])

for i in range(cortes[4][7]):
    listafotonlisto5[0].append([])
    listafotonlisto5[1].append([])
    listafotonlisto5[2].append([])
    listafotonlisto5[3].append([])
    listafotonlisto5[4].append([])
    listafotonlisto5[5].append([])
    listafotonlisto5[6].append([])
    listafotonlisto5[7].append([])
    listafotonlisto5[8].append([])
    listafotonlisto5[9].append([])
    listafotonlisto5[10].append([])
    listafotonlisto5[11].append([])
    listafotonlisto5[12].append([])
    listafotonlisto5[13].append([])
    listafotonlisto5[14].append([])
    listafotonlisto5[15].append([])
    listavectoreslistos5.append([])

for i in range(cortes[5][7]):
    listafotonlistoA[0].append([])
    listafotonlistoA[1].append([])
    listafotonlistoA[2].append([])
    listafotonlistoA[3].append([])
    listafotonlistoA[4].append([])
    listafotonlistoA[5].append([])
    listafotonlistoA[6].append([])
    listafotonlistoA[7].append([])
    listafotonlistoA[8].append([])
    listafotonlistoA[9].append([])
    listafotonlistoA[10].append([])
    listafotonlistoA[11].append([])
    listafotonlistoA[12].append([])
    listafotonlistoA[13].append([])
    listafotonlistoA[14].append([])
    listafotonlistoA[15].append([])
    listavectoreslistosA.append([])

for i in range(cortes[6][7]):
    listafotonlistoB[0].append([])
    listafotonlistoB[1].append([])
    listafotonlistoB[2].append([])
    listafotonlistoB[3].append([])
    listafotonlistoB[4].append([])
    listafotonlistoB[5].append([])
    listafotonlistoB[6].append([])
    listafotonlistoB[7].append([])
    listafotonlistoB[8].append([])
    listafotonlistoB[9].append([])
    listafotonlistoB[10].append([])
    listafotonlistoB[11].append([])
    listafotonlistoB[12].append([])
    listafotonlistoB[13].append([])
    listafotonlistoB[14].append([])
    listafotonlistoB[15].append([])
    listavectoreslistosB.append([])

for i in range(cortes[7][7]):
    listafotonlistoC[0].append([])
    listafotonlistoC[1].append([])
    listafotonlistoC[2].append([])
    listafotonlistoC[3].append([])
    listafotonlistoC[4].append([])
    listafotonlistoC[5].append([])
    listafotonlistoC[6].append([])
    listafotonlistoC[7].append([])
    listafotonlistoC[8].append([])
    listafotonlistoC[9].append([])
    listafotonlistoC[10].append([])
    listafotonlistoC[11].append([])
    listafotonlistoC[12].append([])
    listafotonlistoC[13].append([])
    listafotonlistoC[14].append([])
    listafotonlistoC[15].append([])
    listavectoreslistosC.append([])

for i in range(cortes[8][7]):
    listafotonlistoD[0].append([])
    listafotonlistoD[1].append([])
    listafotonlistoD[2].append([])
    listafotonlistoD[3].append([])
    listafotonlistoD[4].append([])
    listafotonlistoD[5].append([])
    listafotonlistoD[6].append([])
    listafotonlistoD[7].append([])
    listafotonlistoD[8].append([])
    listafotonlistoD[9].append([])
    listafotonlistoD[10].append([])
    listafotonlistoD[11].append([])
    listafotonlistoD[12].append([])
    listafotonlistoD[13].append([])
    listafotonlistoD[14].append([])
    listafotonlistoD[15].append([])
    listavectoreslistosD.append([])


# Para listafotonlisto1,2,...

j = 0
for i in range(n):
    if C[0][i] == 8:
        listafotonlisto1[0][j] = listafoton1[0][i]
        listafotonlisto1[1][j] = listafoton1[1][i]
        listafotonlisto1[2][j] = listafoton1[2][i]
        listafotonlisto1[3][j] = listafoton1[3][i]
        listafotonlisto1[4][j] = listafoton1[4][i]
        listafotonlisto1[5][j] = listafoton1[5][i]
        listafotonlisto1[6][j] = listafoton1[6][i]
        listafotonlisto1[7][j] = listafoton1[7][i]
        listafotonlisto1[8][j] = listafoton1[8][i]
        listafotonlisto1[9][j] = listafoton1[9][i]
        listafotonlisto1[10][j] = listafoton1[10][i]
        listafotonlisto1[11][j] = listafoton1[11][i]
        listafotonlisto1[12][j] = listafoton1[12][i]
        listafotonlisto1[13][j] = listafoton1[13][i]
        listafotonlisto1[14][j] = listafoton1[14][i]
        listafotonlisto1[15][j] = listafoton1[15][i]
        j += 1

j = 0
for i in range(n):
    if C[1][i] == 8:
        listafotonlisto2[0][j] = listafoton2[0][i]
        listafotonlisto2[1][j] = listafoton2[1][i]
        listafotonlisto2[2][j] = listafoton2[2][i]
        listafotonlisto2[3][j] = listafoton2[3][i]
        listafotonlisto2[4][j] = listafoton2[4][i]
        listafotonlisto2[5][j] = listafoton2[5][i]
        listafotonlisto2[6][j] = listafoton2[6][i]
        listafotonlisto2[7][j] = listafoton2[7][i]
        listafotonlisto2[8][j] = listafoton2[8][i]
        listafotonlisto2[9][j] = listafoton2[9][i]
        listafotonlisto2[10][j] = listafoton2[10][i]
        listafotonlisto2[11][j] = listafoton2[11][i]
        listafotonlisto2[12][j] = listafoton2[12][i]
        listafotonlisto2[13][j] = listafoton2[13][i]
        listafotonlisto2[14][j] = listafoton2[14][i]
        listafotonlisto2[15][j] = listafoton2[15][i]
        j += 1

j = 0
for i in range(n):
    if C[2][i] == 8:
        listafotonlisto3[0][j] = listafoton3[0][i]
        listafotonlisto3[1][j] = listafoton3[1][i]
        listafotonlisto3[2][j] = listafoton3[2][i]
        listafotonlisto3[3][j] = listafoton3[3][i]
        listafotonlisto3[4][j] = listafoton3[4][i]
        listafotonlisto3[5][j] = listafoton3[5][i]
        listafotonlisto3[6][j] = listafoton3[6][i]
        listafotonlisto3[7][j] = listafoton3[7][i]
        listafotonlisto3[8][j] = listafoton3[8][i]
        listafotonlisto3[9][j] = listafoton3[9][i]
        listafotonlisto3[10][j] = listafoton3[10][i]
        listafotonlisto3[11][j] = listafoton3[11][i]
        listafotonlisto3[12][j] = listafoton3[12][i]
        listafotonlisto3[13][j] = listafoton3[13][i]
        listafotonlisto3[14][j] = listafoton3[14][i]
        listafotonlisto3[15][j] = listafoton3[15][i]
        j += 1

j = 0
for i in range(n):
    if C[3][i] == 8:
        listafotonlisto4[0][j] = listafoton4[0][i]
        listafotonlisto4[1][j] = listafoton4[1][i]
        listafotonlisto4[2][j] = listafoton4[2][i]
        listafotonlisto4[3][j] = listafoton4[3][i]
        listafotonlisto4[4][j] = listafoton4[4][i]
        listafotonlisto4[5][j] = listafoton4[5][i]
        listafotonlisto4[6][j] = listafoton4[6][i]
        listafotonlisto4[7][j] = listafoton4[7][i]
        listafotonlisto4[8][j] = listafoton4[8][i]
        listafotonlisto4[9][j] = listafoton4[9][i]
        listafotonlisto4[10][j] = listafoton4[10][i]
        listafotonlisto4[11][j] = listafoton4[11][i]
        listafotonlisto4[12][j] = listafoton4[12][i]
        listafotonlisto4[13][j] = listafoton4[13][i]
        listafotonlisto4[14][j] = listafoton4[14][i]
        listafotonlisto4[15][j] = listafoton4[15][i]
        j += 1

j = 0
for i in range(n):
    if C[4][i] == 8:
        listafotonlisto5[0][j] = listafoton5[0][i]
        listafotonlisto5[1][j] = listafoton5[1][i]
        listafotonlisto5[2][j] = listafoton5[2][i]
        listafotonlisto5[3][j] = listafoton5[3][i]
        listafotonlisto5[4][j] = listafoton5[4][i]
        listafotonlisto5[5][j] = listafoton5[5][i]
        listafotonlisto5[6][j] = listafoton5[6][i]
        listafotonlisto5[7][j] = listafoton5[7][i]
        listafotonlisto5[8][j] = listafoton5[8][i]
        listafotonlisto5[9][j] = listafoton5[9][i]
        listafotonlisto5[10][j] = listafoton5[10][i]
        listafotonlisto5[11][j] = listafoton5[11][i]
        listafotonlisto5[12][j] = listafoton5[12][i]
        listafotonlisto5[13][j] = listafoton5[13][i]
        listafotonlisto5[14][j] = listafoton5[14][i]
        listafotonlisto5[15][j] = listafoton5[15][i]
        j += 1

j = 0
for i in range(mm[0]):
    if C[5][i] == 8:
        listafotonlistoA[0][j] = listafotonA[0][i]
        listafotonlistoA[1][j] = listafotonA[1][i]
        listafotonlistoA[2][j] = listafotonA[2][i]
        listafotonlistoA[3][j] = listafotonA[3][i]
        listafotonlistoA[4][j] = listafotonA[4][i]
        listafotonlistoA[5][j] = listafotonA[5][i]
        listafotonlistoA[6][j] = listafotonA[6][i]
        listafotonlistoA[7][j] = listafotonA[7][i]
        listafotonlistoA[8][j] = listafotonA[8][i]
        listafotonlistoA[9][j] = listafotonA[9][i]
        listafotonlistoA[10][j] = listafotonA[10][i]
        listafotonlistoA[11][j] = listafotonA[11][i]
        listafotonlistoA[12][j] = listafotonA[12][i]
        listafotonlistoA[13][j] = listafotonA[13][i]
        listafotonlistoA[14][j] = listafotonA[14][i]
        listafotonlistoA[15][j] = listafotonA[15][i]
        j += 1

j = 0
for i in range(mm[1]):
    if C[6][i] == 8:
        listafotonlistoB[0][j] = listafotonB[0][i]
        listafotonlistoB[1][j] = listafotonB[1][i]
        listafotonlistoB[2][j] = listafotonB[2][i]
        listafotonlistoB[3][j] = listafotonB[3][i]
        listafotonlistoB[4][j] = listafotonB[4][i]
        listafotonlistoB[5][j] = listafotonB[5][i]
        listafotonlistoB[6][j] = listafotonB[6][i]
        listafotonlistoB[7][j] = listafotonB[7][i]
        listafotonlistoB[8][j] = listafotonB[8][i]
        listafotonlistoB[9][j] = listafotonB[9][i]
        listafotonlistoB[10][j] = listafotonB[10][i]
        listafotonlistoB[11][j] = listafotonB[11][i]
        listafotonlistoB[12][j] = listafotonB[12][i]
        listafotonlistoB[13][j] = listafotonB[13][i]
        listafotonlistoB[14][j] = listafotonB[14][i]
        listafotonlistoB[15][j] = listafotonB[15][i]
        j += 1

j = 0
for i in range(mm[2]):
    if C[7][i] == 8:
        listafotonlistoC[0][j] = listafotonC[0][i]
        listafotonlistoC[1][j] = listafotonC[1][i]
        listafotonlistoC[2][j] = listafotonC[2][i]
        listafotonlistoC[3][j] = listafotonC[3][i]
        listafotonlistoC[4][j] = listafotonC[4][i]
        listafotonlistoC[5][j] = listafotonC[5][i]
        listafotonlistoC[6][j] = listafotonC[6][i]
        listafotonlistoC[7][j] = listafotonC[7][i]
        listafotonlistoC[8][j] = listafotonC[8][i]
        listafotonlistoC[9][j] = listafotonC[9][i]
        listafotonlistoC[10][j] = listafotonC[10][i]
        listafotonlistoC[11][j] = listafotonC[11][i]
        listafotonlistoC[12][j] = listafotonC[12][i]
        listafotonlistoC[13][j] = listafotonC[13][i]
        listafotonlistoC[14][j] = listafotonC[14][i]
        listafotonlistoC[15][j] = listafotonC[15][i]
        j += 1

j = 0
for i in range(mm[3]):
    if C[8][i] == 8:
        listafotonlistoD[0][j] = listafotonD[0][i]
        listafotonlistoD[1][j] = listafotonD[1][i]
        listafotonlistoD[2][j] = listafotonD[2][i]
        listafotonlistoD[3][j] = listafotonD[3][i]
        listafotonlistoD[4][j] = listafotonD[4][i]
        listafotonlistoD[5][j] = listafotonD[5][i]
        listafotonlistoD[6][j] = listafotonD[6][i]
        listafotonlistoD[7][j] = listafotonD[7][i]
        listafotonlistoD[8][j] = listafotonD[8][i]
        listafotonlistoD[9][j] = listafotonD[9][i]
        listafotonlistoD[10][j] = listafotonD[10][i]
        listafotonlistoD[11][j] = listafotonD[11][i]
        listafotonlistoD[12][j] = listafotonD[12][i]
        listafotonlistoD[13][j] = listafotonD[13][i]
        listafotonlistoD[14][j] = listafotonD[14][i]
        listafotonlistoD[15][j] = listafotonD[15][i]
        j += 1

     
##TABLA DE CORTES##

# MC #

#m: numero arbitrario de data que correré
#M: numero de data real
#eventos esperados = (Nexp=L*sigma)*m/M
data1 = {
    "Cantidad de eventos ggH": [
        n, 
        cortes[0][0], 
        cortes[0][1], 
        cortes[0][2], 
        cortes[0][3], 
        cortes[0][4], 
        cortes[0][5], 
        cortes[0][6], 
        cortes[0][7]
    ],
    "Cantidad de eventos esperados ggH": [
        10000 * listafoton1[15][0] * r, 
        10000 * listafoton1[15][0] * r * cortes[0][0] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][1] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][2] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][3] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][4] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][5] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][6] / n, 
        10000 * listafoton1[15][0] * r * cortes[0][7] / n
    ],
    "Último corte": [
        "Cantidad inicial", 
        "Trigger", 
        "Tight ID", 
        "pT", 
        "Eta", 
        "pT cone", 
        "ET cone", 
        "pT/mgg", 
        "Ventana de masas"
    ]
}

tabla1 = pd.DataFrame(data1)
print("\n")
print(tabla1)


data2 = {
    "Cantidad de eventos VBF": [
        n, 
        cortes[1][0], 
        cortes[1][1], 
        cortes[1][2], 
        cortes[1][3], 
        cortes[1][4], 
        cortes[1][5], 
        cortes[1][6], 
        cortes[1][7]
    ],
    "Cantidad de eventos esperados VBF": [
        10000 * listafoton2[15][0] * r , 
        10000 * listafoton2[15][0] * r * cortes[1][0] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][1] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][2] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][3] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][4] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][5] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][6] / n, 
        10000 * listafoton2[15][0] * r * cortes[1][7] / n
    ],
    "Último corte": [
        "Cantidad inicial", 
        "Trigger", 
        "Tight ID", 
        "pT", 
        "Eta", 
        "pT cone", 
        "ET cone", 
        "pT/mgg", 
        "Ventana de masas"
    ]
}

tabla2 = pd.DataFrame(data2)
print("\n")
print(tabla2)


data3 = {
    "Cantidad de eventos WpH": [
        n, 
        cortes[2][0], 
        cortes[2][1], 
        cortes[2][2], 
        cortes[2][3], 
        cortes[2][4], 
        cortes[2][5], 
        cortes[2][6], 
        cortes[2][7]
    ],
    "Cantidad de eventos esperados WpH": [
        10000 * listafoton3[15][0] * r, 
        10000 * listafoton3[15][0] * r * cortes[2][0] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][1] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][2] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][3] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][4] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][5] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][6] / n, 
        10000 * listafoton3[15][0] * r * cortes[2][7] / n
    ],
    "Último corte": [
        "Cantidad inicial", 
        "Trigger", 
        "Tight ID", 
        "pT", 
        "Eta", 
        "pT cone", 
        "ET cone", 
        "pT/mgg", 
        "Ventana de masas"
    ]
}

tabla3 = pd.DataFrame(data3)
print("\n")
print(tabla3)


data4 = {
    "Cantidad de eventos ZH": [
        n, 
        cortes[3][0], 
        cortes[3][1], 
        cortes[3][2], 
        cortes[3][3], 
        cortes[3][4], 
        cortes[3][5], 
        cortes[3][6], 
        cortes[3][7]
    ],
    "Cantidad de eventos esperados ZH": [
        10000 * listafoton4[15][0] * r, 
        10000 * listafoton4[15][0] * r * cortes[3][0] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][1] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][2] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][3] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][4] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][5] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][6] / n, 
        10000 * listafoton4[15][0] * r * cortes[3][7] / n
    ],
    "Último corte": [
        "Cantidad inicial", 
        "Trigger", 
        "Tight ID", 
        "pT", 
        "Eta", 
        "pT cone", 
        "ET cone", 
        "pT/mgg", 
        "Ventana de masas"
    ]
}

tabla4 = pd.DataFrame(data4)
print("\n")
print(tabla4)


data5 = {
    "Cantidad de eventos ttH": [
        n, 
        cortes[4][0], 
        cortes[4][1], 
        cortes[4][2], 
        cortes[4][3], 
        cortes[4][4], 
        cortes[4][5], 
        cortes[4][6], 
        cortes[4][7]
    ],
    "Cantidad de eventos esperados ttH": [
        10000 * listafoton5[15][0] * r, 
        10000 * listafoton5[15][0] * r * cortes[4][0] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][1] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][2] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][3] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][4] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][5] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][6] / n, 
        10000 * listafoton5[15][0] * r * cortes[4][7] / n
    ],
    "Último corte": [
        "Cantidad inicial", 
        "Trigger", 
        "Tight ID", 
        "pT", 
        "Eta", 
        "pT cone", 
        "ET cone", 
        "pT/mgg", 
        "Ventana de masas"
    ]
}

tabla5 = pd.DataFrame(data5)
print("\n")
print(tabla5)

# DATA #

dataA = {
    "Cantidad de eventos data A": [
        mm[0], 
        cortes[5][0], 
        cortes[5][1], 
        cortes[5][2], 
        cortes[5][3], 
        cortes[5][4], 
        cortes[5][5], 
        cortes[5][6], 
        cortes[5][7]
    ]
}

tablaA = pd.DataFrame(dataA)
print("\n")
print(tablaA)


dataB = {
    "Cantidad de eventos data B": [
        mm[1], 
        cortes[6][0], 
        cortes[6][1], 
        cortes[6][2], 
        cortes[6][3], 
        cortes[6][4], 
        cortes[6][5], 
        cortes[6][6], 
        cortes[6][7]
    ]
}

tablaB = pd.DataFrame(dataB)
print("\n")
print(tablaB)


dataC = {
    "Cantidad de eventos data C": [
        mm[2], 
        cortes[7][0], 
        cortes[7][1], 
        cortes[7][2], 
        cortes[7][3], 
        cortes[7][4], 
        cortes[7][5], 
        cortes[7][6], 
        cortes[7][7]
    ]
}

tablaC = pd.DataFrame(dataC)
print("\n")
print(tablaC)


dataD = {
    "Cantidad de eventos data D": [
        mm[3], 
        cortes[8][0], 
        cortes[8][1], 
        cortes[8][2], 
        cortes[8][3], 
        cortes[8][4], 
        cortes[8][5], 
        cortes[8][6], 
        cortes[8][7]
    ]
}

tablaD = pd.DataFrame(dataD)
print("\n")
print(tablaD)


## TABLA DE EVENTOS CON DOS FOTONES ##

# MC #

data = {
    "Eventos RAW con más de dos fotones ggH": [n_values[0][0]],
    "Luego de cuatro cortes": [n_values[0][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")


data = {
    "Eventos RAW con más de dos fotones VBF": [n_values[1][0]],
    "Luego de cuatro cortes": [n_values[1][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones WpH": [n_values[2][0]],
    "Luego de cuatro cortes": [n_values[2][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones ZH": [n_values[3][0]],
    "Luego de cuatro cortes": [n_values[3][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones ttH": [n_values[4][0]],
    "Luego de cuatro cortes": [n_values[4][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

# DATA #

data = {
    "Eventos RAW con más de dos fotones data A": [n_values[5][0]],
    "Luego de cuatro cortes": [n_values[5][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones data B": [n_values[6][0]],
    "Luego de cuatro cortes": [n_values[6][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones data C": [n_values[7][0]],
    "Luego de cuatro cortes": [n_values[7][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")

data = {
    "Eventos RAW con más de dos fotones data D": [n_values[8][0]],
    "Luego de cuatro cortes": [n_values[8][1]]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")
print("### DATOS FINALES ###")


# MC #

a0 = (listafoton1[15][0] + listafoton2[15][0] + listafoton3[15][0] + listafoton4[15][0] + listafoton5[15][0])
a1 = (listafoton1[15][0] * cortes[0][0] + listafoton2[15][0] * cortes[1][0] + listafoton3[15][0] * cortes[2][0] + listafoton4[15][0] * cortes[3][0] + listafoton5[15][0] * cortes[4][0])
a2 = (listafoton1[15][0] * cortes[0][1] + listafoton2[15][0] * cortes[1][1] + listafoton3[15][0] * cortes[2][1] + listafoton4[15][0] * cortes[3][1] + listafoton5[15][0] * cortes[4][1])
a3 = (listafoton1[15][0] * cortes[0][2] + listafoton2[15][0] * cortes[1][2] + listafoton3[15][0] * cortes[2][2] + listafoton4[15][0] * cortes[3][2] + listafoton5[15][0] * cortes[4][2])
a4 = (listafoton1[15][0] * cortes[0][3] + listafoton2[15][0] * cortes[1][3] + listafoton3[15][0] * cortes[2][3] + listafoton4[15][0] * cortes[3][3] + listafoton5[15][0] * cortes[4][3])
a5 = (listafoton1[15][0] * cortes[0][4] + listafoton2[15][0] * cortes[1][4] + listafoton3[15][0] * cortes[2][4] + listafoton4[15][0] * cortes[3][4] + listafoton5[15][0] * cortes[4][4])
a6 = (listafoton1[15][0] * cortes[0][5] + listafoton2[15][0] * cortes[1][5] + listafoton3[15][0] * cortes[2][5] + listafoton4[15][0] * cortes[3][5] + listafoton5[15][0] * cortes[4][5])
a7 = (listafoton1[15][0] * cortes[0][6] + listafoton2[15][0] * cortes[1][6] + listafoton3[15][0] * cortes[2][6] + listafoton4[15][0] * cortes[3][6] + listafoton5[15][0] * cortes[4][6])
a8 = (listafoton1[15][0] * cortes[0][7] + listafoton2[15][0] * cortes[1][7] + listafoton3[15][0] * cortes[2][7] + listafoton4[15][0] * cortes[3][7] + listafoton5[15][0] * cortes[4][7])


ac1 =(cortes[5][0] + cortes[6][0] + cortes[7][0] + cortes[8][0])
ac2 =(cortes[5][1] + cortes[6][1] + cortes[7][1] + cortes[8][1])
ac3 =(cortes[5][2] + cortes[6][2] + cortes[7][2] + cortes[8][2])
ac4 =(cortes[5][3] + cortes[6][3] + cortes[7][3] + cortes[8][3])
ac5 =(cortes[5][4] + cortes[6][4] + cortes[7][4] + cortes[8][4])
ac6 =(cortes[5][5] + cortes[6][5] + cortes[7][5] + cortes[8][5])
ac7 =(cortes[5][6] + cortes[6][6] + cortes[7][6] + cortes[8][6])
ac8 =(cortes[5][7] + cortes[6][7] + cortes[7][7] + cortes[8][7])

# esp= L*sigma*r
data = {
    "Cantidad de eventos esperados MC": [10000*a0*r,10000*a1*r/n,10000*a2*r/n,10000*a3*r/n,10000*a4*r/n,10000*a5*r/n,10000*a6*r/n,10000*a7*r/n,10000*a8*r/n], 
    "Último corte": ["Cantidad inicial","Trigger","Tight ID","pT","Eta","pT cone","ET cone","pT/mgg","Ventana de masas"]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")


#event: sum(m[i])
summ=mm[0]+mm[1]+mm[2]+mm[3]
data = {
    "Cantidad de eventos Data": [summ,ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8], 
    "Último corte": ["Cantidad inicial","Trigger","Tight ID","pT","Eta","pT cone","ET cone","pT/mgg","Ventana de masas"]
}

tabla = pd.DataFrame(data)
print("\n")
print(tabla)
print("\n")


## HISTOGRAMAS ##

# MC #

#sum*alpha=L*sigma*r
hist1 = ROOT.TH1F("RAW Histogram"," ggH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist12 = ROOT.TH1F("CUTs Histogram"," ggH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist1.SetLineColor(ROOT.kRed)
hist12.SetLineColor(ROOT.kBlue)

totalweight1=0
for j in range(len(listafoton1[0])):
   totalweight1+=listafoton1[11][j]*listafoton1[12][j]*listafoton1[13][j]*listafoton1[14][j]

a=0
for i in listafoton1[10]:
    hist1.Fill(i,listafoton1[11][a]*listafoton1[12][a]*listafoton1[13][a]*listafoton1[14][a]*listafoton1[15][a]*10000*r/totalweight1)
    a+=1

# El 10.000 incluye la luminosidad y la conversión de unidades de medida. 

a=0
for i in listafotonlisto1[10]:
    hist12.Fill(i,listafotonlisto1[11][a]*listafotonlisto1[12][a]*listafotonlisto1[13][a]*listafotonlisto1[14][a]*listafoton1[15][a]*10000*r/totalweight1)
    a+=1


hist2 = ROOT.TH1F("RAW Histogram"," VBF Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist22 = ROOT.TH1F("CUTs Histogram"," VBF Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist2.SetLineColor(ROOT.kRed)
hist22.SetLineColor(ROOT.kBlue)

totalweight2=0
for j in range(len(listafoton2[0])):
   totalweight2+=listafoton2[11][j]*listafoton2[12][j]*listafoton2[13][j]*listafoton2[14][j]

a=0
for i in listafoton2[10]:
    hist2.Fill(i,listafoton2[11][a]*listafoton2[12][a]*listafoton2[13][a]*listafoton2[14][a]*listafoton2[15][a]*10000*r/totalweight2)
    a+=1

a=0
for i in listafotonlisto2[10]:
    hist22.Fill(i,listafotonlisto2[11][a]*listafotonlisto2[12][a]*listafotonlisto2[13][a]*listafotonlisto2[14][a]*listafotonlisto2[15][a]*10000*r/totalweight2)
    a+=1


hist3 = ROOT.TH1F("RAW Histogram"," WpH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist32 = ROOT.TH1F("CUTs Histogram"," WpH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist3.SetLineColor(ROOT.kRed)
hist32.SetLineColor(ROOT.kBlue)

totalweight3=0
for j in range(len(listafoton3[0])):
   totalweight3+=listafoton3[11][j]*listafoton3[12][j]*listafoton3[13][j]*listafoton3[14][j]

a=0
for i in listafoton3[10]:
    hist3.Fill(i,listafoton3[11][a]*listafoton3[12][a]*listafoton3[13][a]*listafoton3[14][a]*listafoton3[15][a]*10000*r/totalweight3)
    a+=1

a=0
for i in listafotonlisto3[10]:
    hist32.Fill(i,listafotonlisto3[11][a]*listafotonlisto3[12][a]*listafotonlisto3[13][a]*listafotonlisto3[14][a]*listafoton3[15][a]*10000*r/totalweight3)
    a+=1


hist4 = ROOT.TH1F("RAW Histogram"," ZH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist42 = ROOT.TH1F("CUTs Histogram"," ZH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist4.SetLineColor(ROOT.kRed)
hist42.SetLineColor(ROOT.kBlue)

totalweight4=0
for j in range(len(listafoton4[0])):
   totalweight4+=listafoton4[11][j]*listafoton4[12][j]*listafoton4[13][j]*listafoton4[14][j]

a=0
for i in listafoton4[10]:
    hist4.Fill(i,listafoton4[11][a]*listafoton4[12][a]*listafoton4[13][a]*listafoton4[14][a]*listafoton4[15][a]*10000*r/totalweight4)
    a+=1

a=0
for i in listafotonlisto4[10]:
    hist42.Fill(i,listafotonlisto4[11][a]*listafotonlisto4[12][a]*listafotonlisto4[13][a]*listafotonlisto4[14][a]*listafoton4[15][a]*10000*r/totalweight4)
    a+=1


hist5 = ROOT.TH1F("RAW Histogram"," ttH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist52 = ROOT.TH1F("CUTs Histogram"," ttH Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
hist5.SetLineColor(ROOT.kRed)
hist52.SetLineColor(ROOT.kBlue)

totalweight5=0
for j in range(len(listafoton5[0])):
   totalweight5+=listafoton5[11][j]*listafoton5[12][j]*listafoton5[13][j]*listafoton5[14][j]

a=0
for i in listafoton5[10]:
    hist5.Fill(i,listafoton5[11][a]*listafoton5[12][a]*listafoton5[13][a]*listafoton5[14][a]*listafoton5[15][a]*10000*r/totalweight5)
    a+=1

a=0
for i in listafotonlisto5[10]:
    hist52.Fill(i,listafotonlisto5[11][a]*listafotonlisto5[12][a]*listafotonlisto5[13][a]*listafotonlisto5[14][a]*listafoton5[15][a]*10000*r/totalweight5)
    a+=1


histfinalMC = ROOT.TH1F("RAW Histogram"," MC Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
histfinalMC2 = ROOT.TH1F("CUTs Histogram"," MC Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 40, 105, 145)
histfinalMC.SetLineColor(ROOT.kRed)
histfinalMC2.SetLineColor(ROOT.kBlue)

a=0
for i in listafoton1[10]:
    histfinalMC.Fill(i,listafoton1[11][a]*listafoton1[12][a]*listafoton1[13][a]*listafoton1[14][a]*listafoton1[15][a]*10000*r/totalweight1)
    a+=1
a=0
for i in listafoton2[10]:
    histfinalMC.Fill(i,listafoton2[11][a]*listafoton2[12][a]*listafoton2[13][a]*listafoton2[14][a]*listafoton2[15][a]*10000*r/totalweight2)
    a+=1
a=0
for i in listafoton3[10]:
    histfinalMC.Fill(i,listafoton3[11][a]*listafoton3[12][a]*listafoton3[13][a]*listafoton3[14][a]*listafoton3[15][a]*10000*r/totalweight3)
    a+=1
a=0
for i in listafoton4[10]:
    histfinalMC.Fill(i,listafoton4[11][a]*listafoton4[12][a]*listafoton4[13][a]*listafoton4[14][a]*listafoton4[15][a]*10000*r/totalweight4)
    a+=1
a=0
for i in listafoton5[10]:
    histfinalMC.Fill(i,listafoton5[11][a]*listafoton5[12][a]*listafoton5[13][a]*listafoton5[14][a]*listafoton5[15][a]*10000*r/totalweight5)
    a+=1

a=0
for i in listafotonlisto1[10]:
    histfinalMC2.Fill(i,listafotonlisto1[11][a]*listafotonlisto1[12][a]*listafotonlisto1[13][a]*listafotonlisto1[14][a]*listafotonlisto1[15][a]*10000*r/totalweight1)
    a+=1
a=0
for i in listafotonlisto2[10]:
    histfinalMC2.Fill(i,listafotonlisto2[11][a]*listafotonlisto2[12][a]*listafotonlisto2[13][a]*listafotonlisto2[14][a]*listafotonlisto2[15][a]*10000*r/totalweight2)
    a+=1
a=0
for i in listafotonlisto3[10]:
    histfinalMC2.Fill(i,listafotonlisto3[11][a]*listafotonlisto3[12][a]*listafotonlisto3[13][a]*listafotonlisto3[14][a]*listafotonlisto3[15][a]*10000*r/totalweight3)
    a+=1
a=0
for i in listafotonlisto4[10]:
    histfinalMC2.Fill(i,listafotonlisto4[11][a]*listafotonlisto4[12][a]*listafotonlisto4[13][a]*listafotonlisto4[14][a]*listafotonlisto4[15][a]*10000*r/totalweight4)
    a+=1
a=0
for i in listafotonlisto5[10]:
    histfinalMC2.Fill(i,listafotonlisto5[11][a]*listafotonlisto5[12][a]*listafotonlisto5[13][a]*listafotonlisto5[14][a]*listafotonlisto5[15][a]*10000*r/totalweight5)
    a+=1


# DATA #

histA = ROOT.TH1F("RAW Histogram"," Data A Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histA2 = ROOT.TH1F("CUTs Histogram"," Data A Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histA.SetLineColor(ROOT.kRed)
histA2.SetLineColor(ROOT.kBlue)

for i in listafotonA[10]:
    histA.Fill(i)

for i in listafotonlistoA[10]:
    histA2.Fill(i)


histB = ROOT.TH1F("RAW Histogram"," Data B Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histB2 = ROOT.TH1F("CUTs Histogram"," Data B Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histB.SetLineColor(ROOT.kRed)
histB2.SetLineColor(ROOT.kBlue)

for i in listafotonB[10]:
    histB.Fill(i)

for i in listafotonlistoB[10]:
    histB2.Fill(i)


histC = ROOT.TH1F("RAW Histogram"," Data C Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histC2 = ROOT.TH1F("CUTs Histogram"," Data C Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histC.SetLineColor(ROOT.kRed)
histC2.SetLineColor(ROOT.kBlue)

for i in listafotonC[10]:
    histC.Fill(i)

for i in listafotonlistoC[10]:
    histC2.Fill(i)


histD = ROOT.TH1F("RAW Histogram"," Data D Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histD2 = ROOT.TH1F("CUTs Histogram"," Data D Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histD.SetLineColor(ROOT.kRed)
histD2.SetLineColor(ROOT.kBlue)

for i in listafotonD[10]:
    histD.Fill(i)

for i in listafotonlistoD[10]:
    histD2.Fill(i)


histfinaldata = ROOT.TH1F("RAW Histogram"," Data Avg Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histfinaldata2 = ROOT.TH1F("CUTs Histogram"," Data Avg Higgs Boson's mass histogram;m_{#gamma#gamma} [GeV];Events / bin", 20, 105, 145)
histfinaldata.SetLineColor(ROOT.kRed)
histfinaldata2.SetLineColor(ROOT.kBlue)

for i in listafotonA[10]:
    histfinaldata.Fill(i,0.25)
for i in listafotonB[10]:
    histfinaldata.Fill(i,0.25)
for i in listafotonC[10]:
    histfinaldata.Fill(i,0.25)
for i in listafotonD[10]:
    histfinaldata.Fill(i,0.25)

for i in listafotonlistoA[10]:
    histfinaldata2.Fill(i,0.25)
for i in listafotonlistoB[10]:
    histfinaldata2.Fill(i,0.25)
for i in listafotonlistoC[10]:
    histfinaldata2.Fill(i,0.25)
for i in listafotonlistoD[10]:
    histfinaldata2.Fill(i,0.25)

# CANVAS #
# MC #

canvasm1 = ROOT.TCanvas("canvasm1", " ggH Higgs Boson's mass histogram", 800, 600)
hist1.SetStats(0)
hist12.SetStats(0)
hist1.Draw("HIST")
hist12.Draw("SAME HIST") 
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist1, "RAW", "l")
legend.AddEntry(hist12, "CUTS", "l")
legend.Draw("HIST")
canvasm1.SaveAs("higgsmassggH.png")


canvasm2 = ROOT.TCanvas("canvasm2", " VBF Higgs Boson's mass histogram", 800, 600)
hist2.SetStats(0)
hist22.SetStats(0)
hist2.Draw("HIST")
hist22.Draw("SAME HIST")
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist1, "RAW", "l")
legend.AddEntry(hist22, "CUTS", "l")
legend.Draw("HIST")
canvasm2.SaveAs("higgsmassVBF.png")

canvasm3 = ROOT.TCanvas("canvasm3", " WpH Higgs Boson's mass histogram", 800, 600)
hist3.SetStats(0)
hist32.SetStats(0)
hist3.Draw("HIST")
hist32.Draw("SAME HIST")
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist3, "RAW", "l")
legend.AddEntry(hist32, "CUTS", "l")
legend.Draw("HIST")
canvasm3.SaveAs("higgsmassWpH.png")

canvasm4 = ROOT.TCanvas("canvasm4", " ZH Higgs Boson's mass histogram", 800, 600)
hist4.SetStats(0)
hist42.SetStats(0)
hist4.Draw("HIST")
hist42.Draw("SAME HIST")  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist4, "RAW", "l")
legend.AddEntry(hist42, "CUTS", "l")
legend.Draw("HIST")
canvasm4.SaveAs("higgsmassZH.png")

canvasm5 = ROOT.TCanvas("canvasm5", " ttH Higgs Boson's mass histogram", 800, 600)
hist5.SetStats(0)
hist52.SetStats(0)
hist5.Draw("HIST")
hist52.Draw("SAME HIST") 
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist5, "RAW", "l")
legend.AddEntry(hist52, "CUTS", "l")
legend.Draw("HIST")
canvasm5.SaveAs("higgsmassttH.png")


canvasmfinalMC = ROOT.TCanvas("canvasmfinalMC", " MC Higgs Boson's mass histogram", 800, 600)
histfinalMC.SetStats(0)
histfinalMC2.SetStats(0)
histfinalMC.Draw("HIST")
histfinalMC2.Draw("SAME HIST") 
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC, "RAW", "l")
legend.AddEntry(histfinalMC2, "CUTS", "l")
legend.Draw("HIST")
canvasmfinalMC.SaveAs("higgsmassMC.png")


# DATA #

canvasmA = ROOT.TCanvas("canvasmA", " Data A Higgs Boson's mass histogram", 800, 600)
histA.SetStats(0)
histA2.SetStats(0)
histA2.Draw("HIST")
histA.Draw("SAME HIST")
histA.GetYaxis().SetRangeUser(0, 7250*r)             
histA2.GetYaxis().SetRangeUser(0, 7250*r) 
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histA, "RAW", "l")
legend.AddEntry(histA2, "CUTS", "l")
legend.Draw("HIST")
canvasmA.SaveAs("higgsmassdataA.png")

canvasmB = ROOT.TCanvas("canvasmB", " Data B Higgs Boson's mass histogram", 800, 600)
histB.SetStats(0)
histB2.SetStats(0)
histB2.Draw("HIST") 
histB.Draw("SAME HIST")
histB.GetYaxis().SetRangeUser(0, 26600*r)             
histB2.GetYaxis().SetRangeUser(0, 26600*r) 
legendB = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legendB.AddEntry(histB, "RAW", "l")
legendB.AddEntry(histB2, "CUTS", "l")
legendB.Draw("HIST")
canvasmB.SaveAs("higgsmassdataB.png")

canvasmC = ROOT.TCanvas("canvasmC", " Data C Higgs Boson's mass histogram", 800, 600)
histC.SetStats(0)
histC2.SetStats(0)
histC2.Draw("HIST") 
histC.Draw("SAME HIST")
histC.GetYaxis().SetRangeUser(0, 37500*r)             
histC2.GetYaxis().SetRangeUser(0, 37500*r) 
legendC = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legendC.AddEntry(histC, "RAW", "l")
legendC.AddEntry(histC2, "CUTS", "l")
legendC.Draw("HIST")
canvasmC.SaveAs("higgsmassdataC.png")

canvasmD = ROOT.TCanvas("canvasmD", " Data D Higgs Boson's mass histogram", 800, 600)
histD.SetStats(0)
histD2.SetStats(0)
histD2.Draw("HIST") 
histD.Draw("SAME HIST")
histD.GetYaxis().SetRangeUser(0, 63000*r)             
histD2.GetYaxis().SetRangeUser(0, 63000*r) 
legendD = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legendD.AddEntry(histD, "RAW", "l")
legendD.AddEntry(histD2, "CUTS", "l")
legendD.Draw("HIST")
canvasmD.SaveAs("higgsmassdataD.png")

canvasmfinaldata = ROOT.TCanvas("canvasmfinaldata", " Data Avg Higgs Boson's mass histogram", 800, 600)
histfinaldata.SetStats(0)
histfinaldata2.SetStats(0)
histfinaldata2.Draw("HIST") 
histfinaldata.Draw("SAME HIST")
histfinaldata.GetYaxis().SetRangeUser(0, 34000*r)             
histfinaldata2.GetYaxis().SetRangeUser(0, 34000*r)
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinaldata, "RAW", "l")
legend.AddEntry(histfinaldata2, "CUTS", "l")
legend.Draw("HIST")
canvasmfinaldata.SaveAs("higgsmassDataAvg.png")


# DATA VS SEÑAL #


histfinalMC2.SetTitle(" Higgs Boson's mass Data A vs Signal histogram ")
histA2.SetTitle(" Higgs Boson's mass Data A vs Signal histogram ")
histfinalMC2.SetLineColor(ROOT.kRed)
histA2.SetLineColor(ROOT.kBlue)
canvasmdataAseñal = ROOT.TCanvas("canvasmdataAseñal", " Higgs Boson's mass Data A vs Señal histogram", 800, 600)
histfinalMC2.SetStats(0)
histA2.SetStats(0)
histA2.Draw("HIST")  
histfinalMC2.Draw("SAME HIST")
histfinalMC2.GetYaxis().SetRangeUser(0, 80*r)             
histA2.GetYaxis().SetRangeUser(0, 80*r)   
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC2, "Signal", "l")
legend.AddEntry(histA2, "Data A", "l")
legend.Draw("HIST")
canvasmdataAseñal.SaveAs("higgsmassSeñalvsDataA.png")

histfinalMC2.SetTitle(" Higgs Boson's mass Data B vs Signal histogram ")
histB2.SetTitle(" Higgs Boson's mass Data B vs Signal histogram ")
histB2.SetLineColor(ROOT.kBlue)
canvasmdataBseñal = ROOT.TCanvas("canvasmdataBseñal", " Higgs Boson's mass Data B vs Señal histogram", 800, 600)
histfinalMC2.SetStats(0)
histB2.SetStats(0)
histB2.Draw("HIST")  
histfinalMC2.Draw("SAME HIST")
histfinalMC2.GetYaxis().SetRangeUser(0, 230*r)             
histB2.GetYaxis().SetRangeUser(0, 230*r)  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC2, "Signal", "l")
legend.AddEntry(histB2, "Data B", "l")
legend.Draw("HIST")
canvasmdataBseñal.SaveAs("higgsmassSeñalvsDataB.png")

histfinalMC2.SetTitle(" Higgs Boson's mass Data C vs Signal histogram ")
histC2.SetTitle(" Higgs Boson's mass Data C vs Signal histogram ")
histfinalMC2.SetLineColor(ROOT.kRed)
histC2.SetLineColor(ROOT.kBlue)
canvasmdataCseñal = ROOT.TCanvas("canvasmdataCseñal", " Higgs Boson's mass Data C vs Señal histogram", 800, 600)
histfinalMC2.SetStats(0)
histC2.SetStats(0)
histfinalMC2.Draw("HIST") 
histC2.Draw("SAME HIST")         
histfinalMC2.GetYaxis().SetRangeUser(0, 350*r)             
histC2.GetYaxis().SetRangeUser(0, 350*r)  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC2, "Signal", "l")
legend.AddEntry(histC2, "Data C", "l")
legend.Draw("HIST")
canvasmdataCseñal.SaveAs("higgsmassSeñalvsDataC.png")

histfinalMC2.SetTitle(" Higgs Boson's mass Data D vs Signal histogram ")
histD2.SetTitle(" Higgs Boson's mass Data D vs Signal histogram ")
histfinalMC2.SetLineColor(ROOT.kRed)
histD2.SetLineColor(ROOT.kBlue)
canvasmdataDseñal = ROOT.TCanvas("canvasmdataDseñal", " Higgs Boson's mass Data D vs Señal histogram", 800, 600)
histfinalMC2.SetStats(0)
histD2.SetStats(0)
histfinalMC2.Draw("HIST")
histD2.Draw("SAME HIST")           
histfinalMC2.GetYaxis().SetRangeUser(0, 370*r)             
histD2.GetYaxis().SetRangeUser(0, 370*r)  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC2, "Signal", "l")
legend.AddEntry(histD2, "Data D", "l")
legend.Draw("HIST")
canvasmdataDseñal.SaveAs("higgsmassSeñalvsDataD.png")

histfinalMC2.SetTitle(" Higgs Boson's mass Data Avg vs Signal histogram ")
histfinaldata2.SetTitle(" Higgs Boson's mass Data Avg vs Signal histogram ")
histfinalMC2.SetLineColor(ROOT.kRed)
histfinaldata2.SetLineColor(ROOT.kBlue)
canvasmdataseñal = ROOT.TCanvas("canvasmdataseñal", " Higgs Boson's mass Data Avg vs Señal histogram", 800, 600)
histfinalMC2.SetStats(0)
histfinaldata2.SetStats(0)
histfinalMC2.Draw("HIST")
histfinaldata2.Draw("SAME HIST")         
histfinalMC2.GetYaxis().SetRangeUser(0, 240*r)             
histfinaldata2.GetYaxis().SetRangeUser(0, 240*r)  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(histfinalMC2, "Signal", "l")
legend.AddEntry(histD2, "Data Avg", "l")
legend.Draw("HIST")
canvasmdataseñal.SaveAs("higgsmassSeñalvsDataAvg.png")

## INFORMACIÓN IMPORTANTE ##

# a continuacion ejemplo de chat gpt para hacer bkg

###
#import ROOT

# Definir la variable observable
#x = ROOT.RooRealVar("x", "Observable", 0, 10)

# Definir los parámetros del polinomio de tercer orden (background)
#a0 = ROOT.RooRealVar("a0", "Constant", 0, -1, 1)
#a1 = ROOT.RooRealVar("a1", "Linear term", 0, -1, 1)
#a2 = ROOT.RooRealVar("a2", "Quadratic term", 0, -1, 1)
#a3 = ROOT.RooRealVar("a3", "Cubic term", 0, -1, 1)

# Definir el polinomio de tercer orden (fondo)
#background = ROOT.RooPolynomial("background", "Background Polynomial", x, ROOT.RooArgList(a0, a1, a2, a3))

# Cargar tus datos (en este ejemplo, asumo que tienes un histograma ROOT o un TTree con datos)
# Si tus datos están en un TTree:
#tree = ROOT.TChain("tree_name")  # Reemplaza "tree_name" con el nombre de tu TTree
#tree.Add("data_file.root")       # Reemplaza con la ruta a tu archivo ROOT

# Crear un conjunto de datos a partir del TTree
#data = ROOT.RooDataSet("data", "Dataset from TTree", tree, ROOT.RooArgSet(x))

# Ajustar el modelo de polinomio a los datos
#background.fitTo(data)

# Crear un marco para la variable x y graficar los datos
#xframe = x.frame()
#data.plotOn(xframe)            # Graficar los datos
#background.plotOn(xframe)      # Graficar el ajuste del polinomio

# Dibujar el gráfico
#canvas = ROOT.TCanvas("canvas")
#xframe.Draw()
#canvas.SaveAs("polynomial_fit.png")  # Guardar el resultado como imagen
#canvas.Draw()

