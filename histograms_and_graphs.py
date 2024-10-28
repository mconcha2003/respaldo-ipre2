
import ROOT
import numpy as np

# Set up the random number generator
rng = np.random.default_rng(seed=42)

# Generate random data (e.g., 1000 numbers from a normal distribution)
data = rng.normal(loc=0, scale=1, size=1000)

# Create a ROOT histogram
hist = ROOT.TH1F("hist", "Histogram Example;X-axis;Y-axis", 50, -3, 3)

# Fill the histogram with data
for value in data:
    hist.Fill(value)

# Create a canvas to draw the histogram
canvas = ROOT.TCanvas("canvas", "Canvas Example", 800, 600)
hist.Draw()

# Save the canvas as a .png image
canvas.SaveAs("histogram.png")

# Keep the window open
input("Press Enter to exit...")


#/home/mconcha/prueba/histograms_and_graphs.py