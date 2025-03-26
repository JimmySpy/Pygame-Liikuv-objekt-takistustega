##Pygame Liikuvad kujundid koos mängijaga
#Alguses tegin ekraani seaded ning vaatasin video kuidas teha Main Menus kasutasin pilte ning font-i file:
“folder assets on pildid ja font”
Vaatasin ka selle jaoks video
Pea menu:
Play button
Option button
Quit button

#Pidin tegema Peamised funktsioonid:

Mängija kiirus
Kus mängija alustab
Takistused (Saab lisada juurde takistusi)

#Vaatasin video kuidas panna takistused liikuma ja kuidas panna mängija nuppudega liikuma: 

#Noole nuppudega saad liikuda
Kasutasin seda koodi:
# Mängija liikumine nooleklahvide abil
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
   player_x -= player_speed
if keys[pygame.K_RIGHT]:
   player_x += player_speed
if keys[pygame.K_UP]:
   player_y -= player_speed
if keys[pygame.K_DOWN]:
   player_y += player_speed




##Tegin skoori ka (videoga)
Kasutasin fonti ja video koode.
Kasutasin ka tekst file selle jaoks et see automaatselt paneks kõige suurema skoori kirja.







##Allikad mida kasutasin:

https://www.youtube.com/watch?v=y9VG3Pztok8
https://www.youtube.com/watch?v=81qOMZ-nkaQ
https://www.youtube.com/watch?v=GMBqjxcKogA
https://www.youtube.com/watch?v=6zRqd-gyO4c
https://www.youtube.com/watch?v=atoGQ9o0ooI

Mida leidsin ka youtube descriptionist:
https://github.com/baraltech/Menu-System-PyGame
https://github.com/thatKevinSmall/SpaceDodger 

#Github = https://github.com/JimmySpy/Pygame-Liikuv-objekt-takistustega


