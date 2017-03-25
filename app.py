from flask import Flask, render_template

app = Flask(__name__)


class student():
	def __init__(self, avatar, name, age, description, quotes, images, x):
		self.avatar = avatar
		self.name = name
		self.age = age
		self.description = description
		self.quotes = quotes
		self.images = images
		self.x = x

Carlotta = student("CarlottaWalls", "Carlotta Walls LaNier",
"Sophomore", "She was the youngest member of the Little Rock Nine, and was a sophomore when she enrolled in Central High School. After 'The Lost Year' she returned to Central High School (as a senior) and graduated in 1960. After High School, she earned a Bachelor of Science degree from Colorado State University (Currently the University of Northern Colorado).",
 ["'I had to have that sheet of paper (referring to the Diploma). It was an achievement. I helped change the educational system' - Carlotta Walls LaNier"],
  ["C1", "C2", "C3"], 1)

Elizabeth = student("ElizabethEckford", "Elizabeth Eckford", "Junior",
"On the first day at Central High School, the location where these students were supposed to enter was changed. Eckford's family didn't own a phone, and Daisy Bates (The woman in charge of the integration) wasn't able to make it to the Eckford home on time. This resulted in Elizbeth ending up in the wrong spot surrounded by a white mob, which also brought about one of the most iconic images during the integration of Elizabeth being yelled at by angry students. After the first year, Elizabeth had to take night courses (because of 'The Lost Year'), and she later earned enough credits to receive her diploma. Later she attended Central State University, in Ohio, where she earned her Bachelor of Arts degree in History. She also served in the U.S. army for 5 years.",
["'The crowd moved in closer and then began to follow me, calling me names. I still wasn't afraid. Just a little bit nervous. Then my knees started to shake all of a sudden and I wondered whether I could make it to the center entrance a block away. It was the longest block I ever walked in my whole life' (Eckford The First Day: Little Rock, 1957)",
 "'They moved closer and closer. Somebody started yelling, 'Lynch her! Lynch her!'' (Eckford The First Day: Little Rock, 1957)",
 "'Just then a white man sat down beside me, put his arm around me and patted my shoulder. He raised my chin and said, 'Dont let them see you cry' '(Eckford The First Day: Little Rock, 1957)"],
["E1", "E2", "E3"], 1)
Ernest = student("ErnestGreen", "Ernest Green", "Senior", "Ernest was the oldest of the Little Rock Nine, and he was the only Senior. Before going to Central High, he was at the all-black school, Horace Mann. He was the first black graduate from Little Rock Central High School, and Martin Luther King Junior (although not yet nationally famous) was present at his graduation.",
["'When I first told my mother I was considering transferring to Central, she was supportive...she saw that the old way was something we had to be willing to change for the future' - Ernest Green",
"'Name-calling, harassment, abuse, breaking into lockers, wet towels and broken glass in the gym...telephone calls in the middle of the night, death threats' - Ernest Green, on the problems during the first year"],
["ER1", "ER2", "ER3"], 1)
Gloria = student("GloriaRayKarlmark", "Gloria Ray Karlmark", "Junior",
"Gloria decided to register to integrate Central High when she was a Junior. After all the schools had closed down (for 'The Lost Year'), she finished her education in Kansas, City, Missouri. She later went to the Illinois Institute of Technology and received a Bachelor of Science degree in Chemistry and Mathematics",
["'It would put me in doubt about my very existence...Some things are worth dying for. I stopped being me. I became what was a very important principle, every day in school' - Gloria Ray Karlmark"],
 ["G1", "G2", "G3"], 1)
Jefferson = student("JeffersonThomas", "Jefferson Thomas", "Unknown",
"Before he decided to integrate Little Rock Central High School, he was a track athlete at Horace Mann High school (an all-black high school). After integration he attended Los Angeles State College (now known as California State University). Jefferson served as an infantry squad leader in the U.S. army during the Vietnam war.",
["'I had no reason to think that the quiet, peaceful place where I grew up could change so drastically' - Jefferson Thomas"],
 ["J1", "J2", "J3"], 1)

Melba = student("MelbaPattillo", "Melba Pattillo Beals", "Unknown",
 "One of the more well-known members of the Little Rock Nine, partially because she was the first to write a book on her experiences during this first year at Central High, her novel Warriors Don't Cry was published in 1994. After Central High was integrated she went on to earn her Masters degree from the Columbia University Graduate School of Journalism.",
["'I sometimes wish I could change myself into a psychiatrist to determine what makes me such a hated member of this schoo. Can they really be treating me this way because I am brown?' - Melba Pattillo Beals"],
 ["M1", "M2", "M3"], 1)
Terrance = student("TerranceRoberts", "Terrance Roberts", "Sophomore",
 "Before joining with the other 8, Terrance was a Sophomore at Horace Mann High School. After the first year, Terrance moved to Los Angeles and graduated in 1959. Terrance later attended California State Universiy and earned a Masters degree in sociology and a Ph.D in psychology.",
["'In Little Rock, every possible decision had a racial component: where you could live, where you could go to school, whether you could go to school, whether you could work or not, whether you could get a bank loan...who you could marry. This made no sense to me, especially as I discovered there is no such thing as race' - Terrance Roberts"],
["T1", "T2"], 1)
Minni = student("MinnijeanBrown", "Minnijean Brown Trickey", "Unknown",
"While Minnijean attended Little Rock Central High School, she was constantly ridiculed. During one of these torments she decided to retaliate, she threw a bowl of chili on a white boy who was harrassing her. She was later suspended, and then expelled.",
["'Race relations are alright as long as we are giving our lives to the war or working hard, but when the time comes for equalization, we are turned down' - Minnijean Brown Trickey"],
["MJ1", "MJ2", "MJ3"], 1)
Thelma = student("ThelmaMothershed", "Thelma Mothershed", "Junior",
"Thelma Mothershed decided to enroll in Central High during her Junior year, and during 'The Lost Year' she continued her education through summer school in St. Louis, Missouri. Her diploma was sent via mail from Central High. After Highschool, Thelma Mothershed graduated from Southern Illinois University in 1964 with a Bachelors degree in home economics, and later she returned and earned a Master of Science degree in Guidance and Counseling.",
["'I was determinded to treat my kids equally...I taught home economics. I taught kids and helped them and graded them fairly' - Thelma Mothershed"],
["TH1", "TH2", "TH3"], 0)
users = [Carlotta, Elizabeth, Ernest, Gloria, Jefferson, Melba, Terrance, Minni, Thelma]
@app.route("/")
def index():
	names = []
	for prof in users:
		names.append([prof.name, prof.avatar])
	#names = ["CarlottaWalls", "ElizabethEckford", "ErnestGreen", "GloriaRayKarlmark","JeffersonThomas", "MelbaPattillo","TerranceRoberts", "MinnijeanBrown", "ThelmaMothershed"]
	return render_template("index.html", names=names)

@app.route("/<user>")
def info(user):
	profile = " "
	for person in users:
		if user in person.name:
			profile = person
			break
	return render_template("info.html", user=profile)

if __name__ == "__main__":
	app.run(host="tomcasavant.com", port=1234, debug=True)
