devise =input ("Devise : ")
montant = int (input ("Montant : ")
# 1 euro = 1.27 $
facteur_euro_dollar =0.99
if devise == 'E' :
print ("%f $" % (montant * facteur_euro_dollar))
elif devise == '$' :
print ("%f Euros" % (montant / facteur_euro_dollar))
else :
print ("Je n'ai rien compris") # affichage d'un message d'erreur
