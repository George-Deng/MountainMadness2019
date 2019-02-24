import modifier


##stats
stats = [0,0,0,0] ##RandStats.CharStats()
wis = stats[0] + ##racial
strt = stats[1] + ##racial
dex = stats[2] + ##racial
con = stats[3] + ##racial

##modifiers
wismod = modifier.mod(wis)
##print (wismod)
strtmod = modifier.mod(strt)
##print (strtmod)
dexmod = modifier.mod(dex)
##print (dexmod)
conmod = modifier.mod(con)
##print (conmod)


hitdie = 12 ##<-- default
temphitdie = 12 ##<-- default

race = "monster"

name = "real monster"

ac = 0
