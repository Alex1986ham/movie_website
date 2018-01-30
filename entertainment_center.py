import media
import fresh_tomatoes

# List of movies
despicable_me = media.movie("Despicable Me 3", "The discovery of Gru's twin brother Dru pushes the \
Minions to the margins in an amusing but over-stuffed sequel to Illumination's hit franchise.",
"http://www.insidevancouver.ca/wp-content/uploads/2017/05/minions-550x532.jpg", "https://youtu.be/6DBi41reeF0")

minions = media.movie("Minions", "Ever since the dawn of time, the Minions have lived to serve the most \
despicable of masters. From the T-Rex to Napoleon, the easily distracted tribe has helped the biggest and \
the baddest of villains. Now, join protective leader Kevin, teenage rebel Stuart, and lovable little Bob \
on a global road trip. They'll earn a shot to work for a new boss, the world's first female supervillain, \
and try to save all of Minionkind from annihilation.",
"https://images-na.ssl-images-amazon.com/images/I/71-Wt11rDvL._SL1500_.jpg", "https://youtu.be/ywOaCn2fwQU")

cars_3 = media.movie("Cars 3", "Lightning McQueen sets out to prove to a new generation of racers that \
he's still the best race car in the world.",
"http://t1.gstatic.com/images?q=tbn:ANd9GcQ-yoSL_4rKu1OYr1bOFeSmTCzqTfcZgD8jd6FRuC8e4JpCvGFZ",
"https://youtu.be/E4K7JgPJ8-s")

wall_e = media.movie("WALL E", "In the distant future, a small waste-collecting robot inadvertently \
embarks on a space journey that will ultimately decide the fate of mankind. In the distant future, a small waste-collecting robot inadvertently \
embarks on a space journey that will ultimately decide the fate of mankind.",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYZwiuoNMUjmgkAwbTgrhwtsU-c55MN4-Q243ZcNHSzjj6sCod",
"https://youtu.be/ahPI8IAb7co")

shrek = media.movie("Shrek", "When a green ogre named Shrek discovers his swamp has been 'swamped' \
with all sorts of fairytale creatures by the scheming Lord Farquaad, Shrek sets out with a very loud \
donkey by his side to 'persuade' Farquaad to give Shrek his swamp back. Instead, a deal is made. \
Farquaad, who wants to become the King, sends Shrek to rescue Princess Fiona, who is awaiting her \
true love in a tower guarded by a fire-breathing dragon. But once they head back with Fiona, \
it starts to become apparent that not only does Shrek, an ugly ogre, begin to fall in love with \
the lovely princess, but Fiona is also hiding a huge secret.",
"https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg", "https://youtu.be/ooJJX3R42WM")

finding_dory = media.movie("Finding Dory", "Dory is a wide-eyed, blue tang fish who suffers \
from memory loss every 10 seconds or so. The one thing she can remember is that she somehow \
became separated from her parents as a child. With help from her friends Nemo and Marlin, \
Dory embarks on an epic adventure to find them. Her journey brings her to the Marine Life \
Institute, a conservatory that houses diverse ocean species.",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
"https://youtu.be/3JNLwlcPBPI")

movies = [despicable_me, minions, cars_3, wall_e, shrek, finding_dory]

# Opnening the trailer page
fresh_tomatoes.open_movies_page(movies)
