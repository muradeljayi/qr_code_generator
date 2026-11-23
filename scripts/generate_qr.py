import os
import qrcode

os.makedirs("outputs/images", exist_ok=True)

nom = input("Nom du fichier : ")
texte = input("Texte ou URL : ")

img =  qrcode.make(texte)
img.save(f"outputs/images/{nom}.png")

print("QR code généré avec succés")