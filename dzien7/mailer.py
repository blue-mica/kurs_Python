import smtplib
import dzien7.secrets

adresat = dzien7.secrets.login
nadawca = dzien7.secrets.login
haslo = dzien7.secrets.haslo

# tworze silnik mailera
mailer = smtplib.SMTP("smtp.gmail.com", 587)
# witam sie z serwerem / lacze sie
mailer.ehlo()
# szyfruje polaczenie
mailer.starttls()
# loguje sie
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Szymon\n"
wiadomosc = "To jest moja widmosc :)"
tresc = temat + wiadomosc
# wysylam
mailer.sendmail(nadawca, adresat, tresc)
print("wyslalem :)")

mailer.close()