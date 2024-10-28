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

n1 = arbol1.GetEntries()
for i in range(10000):
    arbol1.GetEntry(i)
    for j in range(len(energiafotones1)):
        listaenergia1.append(energiafotones1[j]/1000)
    for j in range(len(momentofotones1)):
        listapt1.append(momentofotones1[j]/1000)
    for j in range(len(etafotones1)):
        listaeta1.append(etafotones1[j])
    for j in range(len(phifotones1)):
        listaphi1.append(phifotones1[j])

n2 = arbol2.GetEntries()
for i in range(10000):
    arbol2.GetEntry(i)
    for j in range(len(energiafotones2)):
        listaenergia2.append(energiafotones2[j]/1000)
    for j in range(len(momentofotones2)):
        listapt2.append(momentofotones2[j]/1000)
    for j in range(len(etafotones2)):
        listaeta2.append(etafotones2[j])
    for j in range(len(phifotones2)):
        listaphi2.append(phifotones2[j])


maxe1=700
maxp1=280
maxeta1=max(listaeta1)

maxe2=700
maxp2=280
maxeta2=max(listaeta2)

histe1 = ROOT.TH1F("Histogram","Photon energy histogram;E_{#gamma} [GeV];Events / bin", 100, 0, maxe1)
histp1 = ROOT.TH1F("Histogram","Photon transversal momentum histogram;pt_{#gamma} [GeV/c];Events / bin", 100, 0, maxp1)
histeta1 = ROOT.TH1F("Histogram", "Photon #eta histogram;#eta_{#gamma};Events / bin", 100, -maxeta1, maxeta1)
histphi1 = ROOT.TH1F("Histogram","Photon #phi histogram;#phi_{#gamma} [rad];Events / bin", 100, -np.pi, np.pi)

histe1.SetLineColor(ROOT.kRed)
histp1.SetLineColor(ROOT.kRed)
histeta1.SetLineColor(ROOT.kRed)
histphi1.SetLineColor(ROOT.kRed)

histe2 = ROOT.TH1F("Histogram","Photon energy histogram;E_{#gamma} [GeV];Events / bin", 100, 0, maxe2)
histp2 = ROOT.TH1F("Histogram","Photon transversal momentum histogram;pt_{#gamma} [GeV/c];Events / bin", 100, 0, maxp2)
histeta2 = ROOT.TH1F("Histogram", "Photon #eta histogram;#eta_{#gamma};Events / bin", 100, -maxeta2, maxeta2)
histphi2 = ROOT.TH1F("Histogram","Photon #phi histogram;#phi_{#gamma} [rad];Events / bin", 100, -np.pi, np.pi)

histe2.SetLineColor(ROOT.kBlue)
histp2.SetLineColor(ROOT.kBlue)
histeta2.SetLineColor(ROOT.kBlue)
histphi2.SetLineColor(ROOT.kBlue)

for i in listaenergia1:
    histe1.Fill(i)
for i in listaenergia2:
    histe2.Fill(i)

canvase = ROOT.TCanvas("canvase", "Photon energy histogram", 800, 600)
histe1.Draw()
histe2.Draw("SAME")
legende = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legende.AddEntry(histe1, "ggF", "l")
legende.AddEntry(histe2, "VBF", "l")
legende.Draw()
canvase.SaveAs("branche.png")

for i in listapt1:
    histp1.Fill(i)
for i in listapt2:
    histp2.Fill(i)

canvasp = ROOT.TCanvas("canvasp", "Photon transversal momentum histogram", 800, 600)
histp1.Draw()
histp2.Draw("SAME")
legendp = ROOT.TLegend(0.7, 0.6, 0.9, 0.7)
legendp.AddEntry(histp1, "ggF", "l")
legendp.AddEntry(histp2, "VBF", "l")
legendp.Draw()
canvasp.SaveAs("branchp.png")

for i in listaeta1:
    histeta1.Fill(i)
for i in listaeta2:
    histeta2.Fill(i)

canvaseta = ROOT.TCanvas("canvaseta", "Photon eta histogram", 800, 600)
histeta1.Draw()
histeta2.Draw("SAME")
legendeta = ROOT.TLegend(0.8, 0.5, 1, 0.6)
legendeta.AddEntry(histeta1, "ggF", "l")
legendeta.AddEntry(histeta2, "VBF", "l")
legendeta.Draw()
canvaseta.SaveAs("brancheta.png")

for i in listaphi1:
    histphi1.Fill(i)
for i in listaphi2:
    histphi2.Fill(i)

canvasphi = ROOT.TCanvas("canvasphi", "Photon #phi histogram", 800, 600)
histphi1.Draw()
histphi2.Draw("SAME")
legendphi = ROOT.TLegend(0.2, 0.8, 0.4, 0.9)
legendphi.AddEntry(histphi1, "ggF", "l")
legendphi.AddEntry(histphi2, "VBF", "l")
histphi1.GetYaxis().SetRangeUser(100, 350)
histphi2.GetYaxis().SetRangeUser(100, 350)
legendphi.Draw()
canvasphi.SaveAs("branchphi.png")

