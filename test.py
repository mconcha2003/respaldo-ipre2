import ROOT
import numpy as np


h = ROOT.TH1D(name="h", title="My histo", nbinsx=1000, xlow=-5, xup=5)
h.FillRandom("gaus", ntimes=5000)

c = ROOT.TCanvas()
h.SetLineColor(ROOT.kBlue)
h.SetFillColor(ROOT.kBlue)
h.GetXaxis().SetTitle("value")
h.GetYaxis().SetTitle("count")
h.SetTitle("My histo with latex: p_{t}, #eta, #phi")
h.Draw() # draw the histogram on the canvas
c.Draw() # draw the canvas on the screen

c.Print("test.pdf")

