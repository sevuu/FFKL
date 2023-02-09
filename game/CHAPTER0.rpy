# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label ch0_main:
scene szkola
stop music fadeout 1.0
stop sound fadeout 1.0
"O kurde, nie mogę się doczekać pójścia do nowej szkoły!"
"Mam nadzieję, że poznam wiele fajnych osób!"
"No i że nic zajebanego z innych popierdolonych nowelek sie nie stanie..."
"No cóż, nic mi nie zostało, tylko wejść do klasy!"
play sound "audio/dzwonekszkolny.mp3"
scene klasa
with dissolve
play music "audio/beautifuldays.mp3"
ncz "Witam wszystkich uczniów w nowym roku szkolnym!"
ncz "W tym roku zawitała do nas jedna nowa osoba."
ncz "Prawdopodobnie zdążyliście już to zauważyć."
ncz "Czy mógłbyś się przedstawić?"
"Cześć."
"*Kurwa, nie wiem w jaki sposób się przedstawić*"
menu:
     "W jaki sposób powinienem się przedstawić?"

     "Przedstaw się normalnie":
         "Cześć, jestem Filip Ha-Hardyn i lubię palić wedd d-_-b"

     "Miej wyjebane będzie ci dane d-___-b":

         ncz "No dalej, przedstaw się"
         "*Ehh...*"
         "Cześć, jestem Filip Ha-Hardyn i lubię palić wedd d-_-b"

show wojtek zorder 2 at t22
idk "Wydaje się być kurwa głupi"
hide wojtek
with dissolve
"*Już widzę jak będzie wyglądał ten rok szkolny...*"
"*Czy mi się wydaje, czy zegarek przestał działać?*"
play sound "audio/dzwonekdg.mp3"
stop music fadeout 2.0
show kuba zorder 2 at t41
idk "EJ LUDZIE"
idk "ZNALAZŁEM CIAŁO PACIEJA W SKŁADZIKU!"
stop sound fadeout 1.0
hide kuba
with dissolve
scene r1
with dissolve

play sound "audio/1z7.mp3"
