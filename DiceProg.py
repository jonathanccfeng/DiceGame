import cgi
import random
form = cgi.FieldStorage()
dieUser = random.randint(1,6)
dieComp = random.randint(1,6)
name = form.getvalue("name")
bet = int(form.getvalue("bet"))
print "Content-type: text/html"
print
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
print "<html>"
print "<head>"
print "<title>Dice Game</title>"
print "</head>"
print "<body>"
print "<h1> Hello " + name + "!</h1>"
if dieUser == 1:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-1.png" alt="2" width="107" height="107" /></p>'
if dieComp == 1:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-1.png" alt="2" width="107" height="107" /></p>'
if dieUser == 2:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-2.png" alt="2" width="107" height="107" /></p>'
if dieComp == 2:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-2.png" alt="2" width="107" height="107" /></p>'
if dieUser == 3:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-3.png" alt="2" width="107" height="107" /></p>'
if dieComp == 3:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-3.png" alt="2" width="107" height="107" /></p>'
if dieUser == 4:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-4.png" alt="2" width="107" height="107" /></p>'
if dieComp == 4:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-4.png" alt="2" width="107" height="107" /></p>'
if dieUser == 5:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-5.png" alt="2" width="107" height="107" /></p>'
if dieComp == 5:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-5.png" alt="2" width="107" height="107" /></p>'
if dieUser == 6:
	print "<p> You rolled a " + str(dieUser) + ".</p>"
	print '<p><img src="dice-6.png" alt="2" width="107" height="107" /></p>'
if dieComp == 6:
	print "<p> Your opponent rolled a " + str(dieComp) + " </b>.</p>"
	print '<p><img src="dice-6.png" alt="2" width="107" height="107" /></p>'
if dieUser > dieComp:
	print "<p> you won $" + str(bet) + "!</p>"
if dieUser < dieComp:
	print "<p> You lost $" + str(bet) + "!</p>"
if dieUser == dieComp:
	print "<p> You won $" + str(bet*2) + "!</p>"
