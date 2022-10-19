# Do not edit this file
import Location
import Print

# Start of main execution -------------------------------------------------------

# Load in test data
ipswich = Location.Location("Ipswich")
norwich = Location.Location("Norwich")
lowerstoft = Location.Location("Lowerstoft")
rendlesham = Location.Location("Rendlesham")
wickhammarket = Location.Location("Wickham Market")

woodbridge = Location.Location("Woodbridge", {rendlesham, wickhammarket})

suffolk = Location.Location("Suffolk", {ipswich, lowerstoft, woodbridge})
norfolk = Location.Location("Norfolk", {norwich})

england = Location.Location("England", {suffolk, norfolk})

uk = Location.Location("UK", {england})

# Call to print
Print.Print.printTree(uk)