import ROOT
f = ROOT.TFile("GamGam/MC/mc_345319.ZH125J_Zincl_gamgam.GamGam.root")
arbol=f.mini;1
#arbol.Show(0) #0 es el evento 0, son Ntuple



# Define una variable para almacenar los datos de la branch
#energiafotones = ROOT.std.vector('float')() 

# Conéctala a la branch que quieres leer
#arbol.SetBranchAddress("photon_E", energiafotones)

# Recorre los eventos (entradas) en el TTree
#nEntries = arbol.GetEntries()
#for i in range(100):
    #arbol.GetEntry(i)
    # Ahora "energiafoton" contiene el valor de la branch en el evento "i"
    #valores_formateados = ', '.join([f'{float(v):.2f} MeV' for v in energiafotones])
    #print(f"Valor en evento {i}: {{ {valores_formateados} }}")

#MANERA MEJOR!

#arbol.Scan("photon_E", "", "colsize=20")

canvas = ROOT.TCanvas("canvas", "Canvas Example", 800, 600)
histor = ROOT.TH1F("histo", "histogram", 30, 0, 30)
arbol.Draw("photon_E>>histor","","goff")

canvas.SaveAs("fotones.png")

#dibujemos branch

#ROOT.gSystem.Load( "particle_CLASS_h" ) 
#from ROOT import particle_CLASS
#myParticle = particle_CLASS()

#arbol.Branch("prueba",myParticle)


#myParticle.Set_position( 4, 5, 6 )
#myParticle.Set_energy( 20 )
#arbol.Fill()

#arbol.Scan("prueba.energy","","colsize=20")
