import ROOT
import numpy as np
f = ROOT.TFile("GamGam/MC/mc_343981.ggH125_gamgam.GamGam.root")
g = ROOT.TFile("GamGam/MC/mc_345041.VBFH125_gamgam.GamGam.root")
arbol1=f.mini;1
arbol2=g.mini;1


energiafotones1 = ROOT.std.vector('float')() 
momentofotones1 = ROOT.std.vector('float')()
etafotones1 = ROOT.std.vector('float')()
phifotones1 = ROOT.std.vector('float')()

energiafotones2 = ROOT.std.vector('float')() 
momentofotones2 = ROOT.std.vector('float')()
etafotones2 = ROOT.std.vector('float')()
phifotones2 = ROOT.std.vector('float')()

arbol1.SetBranchAddress("photon_E", energiafotones1)
arbol1.SetBranchAddress("photon_pt", momentofotones1)
arbol1.SetBranchAddress("photon_eta", etafotones1)
arbol1.SetBranchAddress("photon_phi", phifotones1)

arbol2.SetBranchAddress("photon_E", energiafotones2)
arbol2.SetBranchAddress("photon_pt", momentofotones2)
arbol2.SetBranchAddress("photon_eta", etafotones2)
arbol2.SetBranchAddress("photon_phi", phifotones2)


listaenergia1=[]
listapt1=[]
listaeta1=[]
listaphi1=[]

listaenergia2=[]
listapt2=[]
listaeta2=[]
listaphi2=[]

listavectores1=[]
listavectores2=[]

for i in range(10):
      listaenergia1.append([])
      listapt1.append([])
      listaeta1.append([])
      listaphi1.append([])
      listaenergia2.append([])
      listapt2.append([])
      listaeta2.append([])
      listaphi2.append([])
      listavectores1.append([])
      listavectores2.append([])

for i in range(10):
    arbol1.GetEntry(i)
    for j in range(len(energiafotones1)):
      listaenergia1[i].append([])
      listaenergia1[i][j]=energiafotones1[j]/1000 
    for j in range(len(momentofotones1)):
      listapt1[i].append([])
      listapt1[i][j]=momentofotones1[j]/1000
    for j in range(len(etafotones1)):
            listaeta1[i].append([])
            listaeta1[i][j]=etafotones1[j]
    for j in range(len(phifotones1)):
      listaphi1[i].append([])
      listaphi1[i][j]=phifotones1[j]


for i in range(10):
    arbol2.GetEntry(i)
    for j in range(len(energiafotones2)):
      listaenergia2[i].append([])
      listaenergia2[i][j]=energiafotones2[j]/1000 
    for j in range(len(momentofotones2)):
      listapt2[i].append([])
      listapt2[i][j]=momentofotones2[j]/1000
    for j in range(len(etafotones2)):
            listaeta2[i].append([])
            listaeta2[i][j]=etafotones2[j]
    for j in range(len(phifotones2)):
      listaphi2[i].append([])
      listaphi2[i][j]=phifotones2[j]


listavec1=[]
listavec2=[]



for i in range(10):
    for j in range(len(listaenergia1[i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listapt1[i][j], listaeta1[i][j], listaphi1[i][j], listaenergia1[i][j])
        listavectores1[i].append(vec)

for i in range(10):
    for j in range(len(listaenergia2[i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listapt2[i][j], listaeta2[i][j], listaphi2[i][j], listaenergia2[i][j])
        listavectores2[i].append(vec)


for i in range(10):
    vecsum=ROOT.TLorentzVector()
    for j in range(len(listaenergia1[i])):
      vecsum+=listavectores1[i][j]
    listavec1.append(vecsum)

for i in range(10):
    vecsum=ROOT.TLorentzVector()
    for j in range(len(listaenergia2[i])):
      vecsum+=listavectores2[i][j]
    listavec2.append(vecsum)


cvhiggs1=[[],[],[]] #E, p2, m
cvhiggs2=[[],[],[]]

for i in range(10):
    E=listavec1[i].E()
    px=listavec1[i].Px()
    py=listavec1[i].Py()
    pz=listavec1[i].Pz()
    cvhiggs1[0].append(E)
    p2=(px*px)+(py*py)+(pz*pz)
    cvhiggs1[1].append(p2)
    m=np.sqrt((E*E)-p2)
    cvhiggs1[2].append(m)

for i in range(10):
    E=listavec2[i].E()
    px=listavec2[i].Px()
    py=listavec2[i].Py()
    pz=listavec2[i].Pz()
    cvhiggs2[0].append(E)
    p2=(px*px)+(py*py)+(pz*pz)
    cvhiggs2[1].append(p2)
    m=np.sqrt((E*E)-p2)
    cvhiggs2[2].append(m)

for i in range(10):
    print(f"La masa de este bosón de Higgs es: {cvhiggs1[2][i]} GeV")

for i in range(10):
    print(f"La masa de este bosón de Higgs es: {cvhiggs2[2][i]} GeV")
