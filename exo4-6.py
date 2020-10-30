# _*_ coding:Utf8 _*_

# nbr de secondes
ns = 12345678912

# nombres de secondes par journée:
nsJour = 3600 * 24

# nbr de secondes dans une années:
nsAn = nsJour * 365

# nbr de secondes dans un mois:
nsMois = nsAn / 12          # nsMois = nsJour * 30

# nbr année
nAnnee = ns // nsAn         # division entière
nsRestante = ns % nsAn  # nbr de secondes restante

# nbr mois
nMois = nsRestante // nsMois
nsRestante = nsRestante % nsMois

# nbr jour
nJour = nsRestante // nsJour
nsRestante = nsRestante % nsJour

# nbr heure
nHeure = nsRestante // 3600
nsRestante = nsRestante % 3600

# nbr minutes
nMinutes = nsRestante // 60
nsRestante = nsRestante % 60

print('Nombre de seondes a convertir: ', ns)
print('année: ', nAnnee, ', mois: ', nMois, ', jour: ', nJour, ', heures: ',
      nHeure, ', minutes: ', nMinutes, ', secondes: ', nsRestante)
