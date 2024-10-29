# Para el MC crearé una gaussiena aleatoria. Para los datos usaré solo la data D

import ROOT
import numpy as np
import array
import pandas as pd
from ROOT import gPad
d= ROOT.TFile("GamGam/Data/data_D.GamGam.root")
arbolD=d.mini;1

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

M=[0,0,0,arbolD.GetEntries()]
r=0.005
mm=[0,0,0,round(M[3]*r)]
n=int(mm[3]*0.03)

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

listafotonlistoD = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #e,pt,eta,phi,trig,tight,ptcone,etcone,etotal,p2,m,mc,pileup,scalefoton,sfotontrigger,xsection
listavectoreslistosD = [] #tlorentz fotones

for i in range(mm[3]):
    # Listas de fotones
    for j in range(8):
        listafotonlistoD[j].append([])

    for j in range(11, 16):
        listafotonlistoD[j].append([])

    # tlorentz fotones
    listavectoreslistosD.append([])


for i in range(mm[3]):
    arbolD.GetEntry(i)
    for j in range(len(energiafotonesD)):
        listafotonlistoD[0][i].append([])
        listafotonlistoD[0][i][j] = energiafotonesD[j] / 1000
    for j in range(len(momentofotonesD)):
        listafotonlistoD[1][i].append([])
        listafotonlistoD[1][i][j] = momentofotonesD[j] / 1000
    for j in range(len(etafotonesD)):
        listafotonlistoD[2][i].append([])
        listafotonlistoD[2][i][j] = np.abs(etafotonesD[j])
    for j in range(len(phifotonesD)):
        listafotonlistoD[3][i].append([])
        listafotonlistoD[3][i][j] = phifotonesD[j]
    listafotonlistoD[4][i] = trigfotonesD[0]
    for j in range(len(tightfotonesD)):
        listafotonlistoD[5][i].append([])
        listafotonlistoD[5][i][j] = tightfotonesD[j]
    for j in range(len(ptconefotonesD)):
        listafotonlistoD[6][i].append([])
        listafotonlistoD[6][i][j] = ptconefotonesD[j]
    for j in range(len(etconefotonesD)):
        listafotonlistoD[7][i].append([])
        listafotonlistoD[7][i][j] = etconefotonesD[j]
    listafotonlistoD[11][i] = mcD[0]
    listafotonlistoD[12][i] = spileupD[0]
    listafotonlistoD[13][i] = sfotonD[0]
    listafotonlistoD[14][i] = sfotontriggerD[0]
    listafotonlistoD[15][i] = xsectionD[0]


##CREANDO LOS TLORENTZ VECTOR##

for i in range(mm[3]):
    for j in range(len(listafotonlistoD[0][i])):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiE(listafotonlistoD[1][i][j], listafotonlistoD[2][i][j], listafotonlistoD[3][i][j], listafotonlistoD[0][i][j])
        listavectoreslistosD[i].append(vec)

##CREANDO LOS TLORENTZ VECTOR DE LOS HIGGS RECONSTRUIDOS##

listavecD = [] # tlorentz Higgs

for i in range(mm[3]):
    vecsum = ROOT.TLorentzVector()
    for j in range(len(listafotonlistoD[0][i])):
        vecsum += listavectoreslistosD[i][j]
    listavecD.append(vecsum)

##AGREGANDO LA NUEVA INFORMACION A LAS LISTAS DE LOS FOTONES##

for i in range(mm[3]):
    E = listavecD[i].E()
    px = listavecD[i].Px()
    py = listavecD[i].Py()
    pz = listavecD[i].Pz()
    listafotonlistoD[8].append(E)
    p2 = (px * px) + (py * py) + (pz * pz)
    listafotonlistoD[9].append(p2)
    m = np.sqrt((E * E) - p2)
    listafotonlistoD[10].append(m)

## HISTOGRAMAS ##

# MC #

# Parámetros de la gaussiana
mu = 125        # Media
sigma = 1     # Desviación estándar

hist = ROOT.TH1F("hist MC", "Distribucion Gaussiana", 100, mu - 5*sigma, mu + 5*sigma)

for _ in range(n):
    hist.Fill(ROOT.gRandom.Gaus(mu, sigma))


# DATA #


histD = ROOT.TH1F("hist data","Bck vs MC Example", 20, 105, 145)
histD.SetLineColor(ROOT.kRed)

for i in listafotonlistoD[10]:
    histD.Fill(i)

# CANVAS #

hist.SetLineColor(ROOT.kRed)
histD.SetLineColor(ROOT.kBlue)
canvasbkgej = ROOT.TCanvas("canvasbckej", "Bck vs MC Example", 800, 600)
hist.SetStats(0)
histD.SetStats(0)
hist.Draw()
histD.Draw("SAME") #SAME          
hist.GetYaxis().SetRangeUser(0, 50000*r)             
histD.GetYaxis().SetRangeUser(0, 50000*r)  
legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legend.AddEntry(hist, "Signal", "l")
legend.AddEntry(histD, "Data D", "l")
legend.Draw("HIST")
canvasbkgej.SaveAs("backgroundexample.png")

# AJUSTE CURVAS #

# AJUSTE POLINOMIO #

# Definir la variable observable
m = ROOT.RooRealVar("m", "Masa", 0, 300)

# Definir los parámetros del polinomio de tercer orden (background)
a0 = ROOT.RooRealVar("a0", "Constant", 0, -1000, 1000)
a1 = ROOT.RooRealVar("a1", "Linear term", 0, -1000, 1000)
a2 = ROOT.RooRealVar("a2", "Quadratic term", 0, -1000, 1000)
a3 = ROOT.RooRealVar("a3", "Cubic term", 0, -1000, 1000)

# Definir el polinomio de tercer orden (fondo)
background = ROOT.RooPolynomial("background", "Background Polynomial", m, ROOT.RooArgList(a0, a1, a2, a3))

# Crear un conjunto de datos a partir de la lista
data = ROOT.RooDataSet("data", "Dataset from list", ROOT.RooArgSet(m))

# Llenar el RooDataSet con los datos de la lista
for value in listafotonlistoD[10]:
    m.setVal(value)  # Establecer el valor de la variable observable
    data.add(ROOT.RooArgSet(m))  # Agregar el valor al conjunto de datos

# Ajustar el modelo de polinomio a los datos
background.fitTo(data)

# Crear un marco para la variable y graficar los datos
xframe = m.frame()
data.plotOn(xframe)            # Graficar los datos
background.plotOn(xframe)      # Graficar el ajuste del polinomio

# Dibujar el gráfico
canvasajuste = ROOT.TCanvas("canvasajuste")
xframe.Draw()
canvasajuste.SaveAs("polynomial_fit.png")  # Guardar el resultado como imagen
canvasajuste.Draw()


## INFORMACIÓN IMPORTANTE ##


