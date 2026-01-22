from flask import Flask, render_template

app = Flask(__name__)

treks = [
    {
        "title": "Rajgad Fort",
        "slug": "rajgad-fort",
        "difficulty": "Moderate",
        "distance": "15 km",
        "image": "rajgad_uppercard.webp",
        "duration": "1 Day",
        "description": "Historic Maratha capital with royal palaces, watchtowers, and stunning Sahyadri views from the King of Forts.",
        "group_size": "5-20"
    },
    {
        "title": "Kalsubai Peak",
        "slug": "kalsubai-peak",
        "difficulty": "Moderate",
        "distance": "12 km",
        "image": "kalsubai peak.jpg",
        "duration": "1 Day",
        "description": "Maharashtra's highest peak at 1,646 meters offering breathtaking sunrise views and panoramic Sahyadri mountain ranges.",
        "group_size": "8-15"
    },
    {
        "title": "Harishchandragad",
        "slug": "harishchandragad",
        "difficulty": "Difficult",
        "distance": "18 km",
        "image": "harishchandra_ghad.webp",
        "duration": "2 Days",
        "description": "Ancient fort famous for Konkan Kada cliff, Saptatirtha lakes, and mystical Kedareshwar cave temple with floating pillar.",
        "group_size": "6-15"
    },
    {
        "title": "Sinhagad Fort",
        "slug": "sinhagad-fort",
        "difficulty": "Easy",
        "distance": "6 km",
        "image": "sinhaghad.jpg",
        "duration": "Half Day",
        "description": "Popular fort near Pune with rich Maratha history, famous for Tanaji Malusare's bravery and delicious local cuisine.",
        "group_size": "4-20"
    },
    {
        "title": "Torna Fort",
        "slug": "torna-fort",
        "difficulty": "Moderate",
        "distance": "10 km",
        "image": "torna-fort.jpg",
        "duration": "1 Day",
        "description": "First fort captured by Shivaji Maharaj at age 16, featuring Menghai Devi temple and spectacular valley views.",
        "group_size": "5-15"
    },
    {
        "title": "Lohagad Fort",
        "slug": "lohagad-fort",
        "difficulty": "Easy",
        "distance": "5 km",
        "image": "lohagad-fort.webp",
        "duration": "Half Day",
        "description": "Iron fort with monsoon beauty, Vinchu Kata scorpion tail ridge, and historic connections to Shivaji and Peshwas.",
        "group_size": "4-20"
    },
    {
        "title": "Kalavantin Durg",
        "slug": "kalavantin-durg",
        "difficulty": "Difficult",
        "distance": "11 km",
        "image": "kalavantin_durg.jpg",
        "duration": "1 Day",
        "description": "Thrilling pinnacle climb with near-vertical rock-cut steps offering adrenaline rush and stunning coastal Konkan views.",
        "group_size": "4-10"
    },
    {
        "title": "Raigad Fort",
        "slug": "raigad-fort",
        "difficulty": "Moderate",
        "distance": "8 km",
        "image": "Raigad-Fort.jpg",
        "duration": "1 Day",
        "description": "Maratha Empire capital where Shivaji was crowned, featuring royal ruins, Maha Darwaja gate, and accessible ropeway.",
        "group_size": "5-20"
    },
    {
        "title": "Visapur Fort",
        "slug": "visapur-fort",
        "difficulty": "Easy",
        "distance": "7 km",
        "image": "visapur-fort.avif",
        "duration": "1 Day",
        "description": "Twin fort of Lohagad with ancient caves, water cisterns, and perfect monsoon trekking through lush greenery great sea views.",
        "group_size": "4-15"
    },
    {
        "title": "Prabalgad Fort",
        "slug": "prabalgad-fort",
        "difficulty": "Moderate",
        "distance": "9 km",
        "image": "prabalghad.jpg",
        "duration": "1 Day",
        "description": "Muranjan fort with impressive doorways, ancient bastions, and magnificent views of Matheran, Panvel, and Kalavantin Durg.",
        "group_size": "5-12"
    },
    {
        "title": "Bhimashankar Trek",
        "slug": "bhimashankar-trek",
        "difficulty": "Moderate",
        "distance": "16 km",
        "image": "bhimshankar.jpg",
        "duration": "1 Day",
        "description": "Sacred Jyotirlinga temple trek through dense forests, home to endangered Malabar giant squirrels and scenic waterfalls.",
        "group_size": "6-15"
    },
    {
        "title": "Bhairavgad Fort",
        "slug": "bhairavgad-fort",
        "difficulty": "Difficult",
        "distance": "14 km",
        "image": "Bhairavgad.jpg",
        "duration": "1 Day",
        "description": "Challenging climb with rock patches and steep slopes, rewarding with Bhairavnath temple and spectacular Sahyadri panoramic views.",
        "group_size": "4-10"
    }
]

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/treks')
def treks_page():
    return render_template('treks.html', treks=treks)


if __name__ == '__main__':
    app.run(debug=True)