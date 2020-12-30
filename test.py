import pyodbc


server = 'ispj-database.database.windows.net'
database = 'ISPJ Database'
username = 'Peter'
password = 'p@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

# account_status = 'Active'
# firstname = 'Darren'
# lastname = 'Kang'
# email = 'darrenkang@gmail.com'
# password = '987654321'
# isadmin = 'False'
# profile_image = '../static/images/profile.jpg'
# previous_passwords = "['123456789']"
# cursor.execute('INSERT INTO user_accounts VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?);', account_status, firstname, lastname, email, password, isadmin, profile_image, previous_passwords)
# conn.commit()
#

prod_quantity = 100
prod_name = "Rocket League"
prod_price = 15.00
prod_desc = "Rocket League is a high-powered hybrid of arcade-style soccer and vehicular mayhem with easy-to-understand controls and fluid, physics-driven competition. Rocket League includes casual and competitive Online Matches, a fully-featured offline Season Mode, special “Mutators” that let you change the rules entirely, hockey and basketball-inspired Extra Modes, and more than 500 trillion possible cosmetic customization combinations. Winner or nominee of more than 150 “Game of the Year” awards, Rocket League is one of the most critically-acclaimed sports games of all time. Boasting a community of more than 57 million players, Rocket League features ongoing free and paid updates, including new DLCs, content packs, features, modes and arenas."
prod_img = None
genre = "Action"
game_list = [(100,"Terraria",10.50,"Dig, Fight, Explore, Build: The very world is at your fingertips as you fight for survival, fortune, and glory. Will you delve deep into cavernous expanses in search of treasure and raw materials with which to craft ever-evolving gear, machinery, and aesthetics? Perhaps you will choose instead to seek out ever-greater foes to test your mettle in combat? Maybe you will decide to construct your own city to house the host of mysterious allies you may encounter along your travels? In the World of Terraria, the choice is yours! Blending elements of classic action games with the freedom of sandbox-style creativity, Terraria is a unique gaming experience where both the journey and the destination are completely in the player’s control. The Terraria adventure is truly as unique as the players themselves!","Action"),
             (100,"Dead by Daylight",20.00,"Death Is Not an Escape. Dead by Daylight is a multiplayer (4vs1) horror game where one player takes on the role of the savage Killer, and the other four players play as Survivors, trying to escape the Killer and avoid being caught, tortured and killed. Survivors play in third-person and have the advantage of better situational awareness. The Killer plays in first-person and is more focused on their prey. The Survivors' goal in each encounter is to escape the Killing Ground without getting caught by the Killer - something that sounds easier than it is, especially when the environment changes every time you play. More information about the game is available at http://www.deadbydaylight.com Key Features • Survive Together… Or Not - Survivors can either cooperate with the others or be selfish. Your chance of survival will vary depending on whether you work together as a team or if you go at it alone. Will you be able to outwit the Killer and escape their Killing Ground? • Where Am I? - Each level is procedurally generated, so you’ll never know what to expect. Random spawn points mean you will never feel safe as the world and its danger change every time you play. • A Feast for Killers - Dead by Daylight draws from all corners of the horror world. As a Killer you can play as anything from a powerful Slasher to terrifying paranormal entities. Familiarize yourself with your Killing Grounds and master each Killer’s unique power to be able to hunt, catch and sacrifice your victims. • Deeper and Deeper - Each Killer and Survivor has their own deep progression system and plenty of unlockables that can be customized to fit your own personal strategy. Experience, skills and understanding of the environment are key to being able to hunt or outwit the Killer. • Real People, Real Fear - The procedural levels and real human reactions to pure horror makes each game session an unexpected scenario. You will never be able to tell how it’s going to turn out. Ambience, music, and chilling environments combine into a terrifying experience. With enough time, you might even discover what’s hiding in the fog.","Horror"),
]

# for i in game_list:
# #     # conn.execute("""INSERT INTO dbo.products(prod_quantity,prod_name,prod_price,prod_desc,genre) VALUES (?,?,?,?,?)""",prod_quantity,prod_name,prod_price,prod_desc,genre)
#     conn.execute(f"""INSERT INTO dbo.products(prod_quantity,prod_name,prod_price,prod_desc,genre) VALUES (?,?,?,?,?)""",i)
# conn.commit()
# cursor.execute("""Select * from dbo.products""")
# for row in cursor:
#     print(row)
