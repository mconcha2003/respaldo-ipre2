import ROOT

ROOT.gSystem.Load( "particle_CLASS_h" ) 
from ROOT import particle_CLASS

myParticle = particle_CLASS()

t = ROOT.TTree("t","tree1")
t.Branch("particle",myParticle)

myParticle.Set_position(1,2,3)
myParticle.Set_energy(10)
t.Fill()

myParticle.Set_position( 4, 5, 6 )
myParticle.Set_energy( 20 )
t.Fill()


myParticle.Set_position( 7, 8, 9 )
myParticle.Set_energy( 30 )
t.Fill()

#t.Show(0)

#t.Scan("particle.energy")

#t.Scan("particle.position[0]","","colsize=20")

#c=ROOT.TCanvas()
#t.Draw("particle.energy")

#c.Print("c.png")

for i in range( t.GetEntriesFast() ):
        
        t.GetEntry(i)

        # print t.particle.Get_energy() 
        print(f"eng = {t.particle.energy:7.2f}") 

        print(f"x={t.particle.position[0]:7.2f}\ty={t.particle.position[1]:7.2f}\tz={t.particle.position[2]:7.2f}\n")