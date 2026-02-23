from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from sqlalchemy import false, true

from validators.trek_validator import validate_trek
from validators.waterfall_validator import validate_waterfall

# ---------- DB CONNECTION ----------
client = MongoClient("mongodb://localhost:27017/")
db = client["trek_maharashtra"]

treks_collection = db["treks"]
waterfalls_collection = db["waterfalls"]

# ---------- DATA ----------
TREKS = [
    {
    "name": "Bhimashankar",
    "slug": "bhimashankar-trek",
    "description": """Bhimashankar is where spirituality meets the raw, untamed wilderness of the Western Ghats. It is home to one of the twelve Jyotirlingas of Lord Shiva, making it a major pilgrimage site, but for trekkers, it is the ultimate "Jungle Trek." Located in the heart of the Bhimashankar Wildlife Sanctuary, the trail takes you through dense, evergreen forests that are among the most biodiverse in Maharashtra. This is the land of the "Shekru" (Malabar Giant Squirrel) and ancient trees covered in moss and orchids. Whether you take the challenging Shidi Ghat (Ladder Route) or the scenic Ganesh Ghat, the journey is an immersive experience in nature. Reaching the temple complex, with its stunning Nagara-style architecture and the sound of bells echoing through the misty valley, feels like a transition from the wild into the divine.

<h2 class="text-2xl font-bold mt-6 mb-4">History & Heritage</h2>

The heritage of Bhimashankar is ancient and deeply spiritual. The Bhimashankar Temple dates back to the 13th century, though the current structure reflects the 18th-century Nagara style of architecture, famously renovated by Nana Phadnavis. The temple is built over a site where, according to the Puranas, Lord Shiva took the form of 'Bhima' to defeat the demon Tripurasura. The sweat from his brow after the battle is said to have formed the Bhima River, which originates right here. 



Architecturally, the temple is a masterpiece. The shikhara (spire) is intricately carved with figures of gods and celestial beings. A standout feature is the massive Portuguese bell hanging outside the temple. This bell was captured by Chimaji Appa (brother of Peshwa Bajirao I) from the Portuguese during the Battle of Vasai in 1739 and offered to the temple as a trophy. Culturally, the region is also home to the Gupt Bhimashankar, a hidden spot in the forest where the river first emerges. The surrounding forest has been protected for centuries as a "Devrai" (Sacred Grove), where the local tribal communities believe the spirits of the forest reside, ensuring the jungle remains untouched by human greed.

<h2 class="text-2xl font-bold mt-6 mb-4">The Trail Experience</h2>

There are two primary ways to reach the top from the base village of Khandas. The Ganesh Ghat is the more popular and scenic route, passing by a small Ganesh temple and winding through lush meadows and thick forests. It is a long but gradual climb. The Shidi Ghat (Ladder Route) is for the adrenaline junkies. It involves climbing three massive iron ladders installed on vertical rock faces and navigating narrow, rocky ridges. During the monsoon, this route becomes a thrilling challenge as you climb through waterfalls. The forest section, known as the "Rainforest of Maharashtra," is notoriously humid and filled with leeches during the rains, but the sight of rare bioluminescent fungi glowing on the trees at night makes it worth the effort.



<strong>Pro tip:</strong> If you are taking the Shidi Ghat, ensure you have a good pair of waterproof trekking shoes. The ladders can be slippery. Also, keep your eyes on the high canopy—the Malabar Giant Squirrel is shy, but its loud, rattling call often gives away its location among the silver-grey bark trees.

<h2 class="text-2xl font-bold mt-6 mb-4">How to Reach</h2>

<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-500">
<p class="font-semibold text-lg mb-3">🚉 Nearest Railway Station</p>
<p class="mb-4"><strong>Karjat Railway Station</strong> (for the trek from the base) or <strong>Pune Station</strong> (for those driving directly to the temple).</p>

<p class="font-semibold text-lg mb-3">🚗 From Station to Base Village (Khandas)</p>
<p class="mb-4">From Karjat station, you can hire a private or shared rickshaw to reach the base village of Khandas. The journey takes about 1 hour. If you aren't trekking, you can drive all the way to the temple from Pune (approx 110 km) or Manchar.</p>

<p class="font-semibold text-lg mb-3">🚌 Transport Options & Pricing:</p>
<ul class="list-disc ml-6 space-y-2 mb-4">
<li><strong>Shared Rickshaw (Karjat to Khandas):</strong> ₹100–₹150 per seat.</li>
<li><strong>Private Rickshaw (Full):</strong> ₹800–₹1,000 (Fix the return time with the driver).</li>
<li><strong>ST Bus (Pune to Bhimashankar):</strong> ₹150–₹200 (For the direct road route).</li>
<li><strong>Parking at Khandas/Temple:</strong> ₹50 (Bikes) / ₹150 (Cars).</li>
</ul>

<p class="font-semibold text-yellow-700">💡 Traveler Tip:</p>
<p>Bhimashankar is a popular pilgrimage site, so it gets extremely crowded on Mondays and during Mahashivratri. If you are a trekker seeking peace, plan your visit for a <strong>Tuesday or Wednesday</strong>. The queue for the temple can take 4-6 hours on weekends!</p>
</div>

<h2 class="text-2xl font-bold mt-6 mb-4">🤔 Did You Know?</h2>

<ul class="list-disc ml-6 space-y-2">
<li>Bhimashankar is one of the very few places in the world where you can find the Malabar Giant Squirrel (Shekru)—they are nearly 3 feet long from nose to tail!</li>
<li>The forest here is a Bioluminescent Zone; during the first few rains of the monsoon, the decaying wood on the forest floor glows in the dark due to a rare fungus.</li>
<li>The Portuguese Bell at the temple weighs over 500 kg and was transported through the rugged mountains without any modern machinery.</li>
<li>The Bhima River, which is a major tributary of the Krishna River, begins as a tiny trickle inside the Gupt Bhimashankar forest.</li>
<li>The region is an Important Bird Area (IBA), home to the rare Malabar Whistling Thrush, whose song sounds exactly like a human whistling.</li>
<li>The Nagphani Point (Cobra's Hood) is the highest point in the region, offering a view of the Konkan region that looks like a vast green sea.</li>
<li>There are ancient Buddhist caves located in the hills nearby, suggesting the area has been a spiritual center for over 2,000 years.</li>
<li>Local legends say that the water from the temple's pond never dries up, even in the most severe droughts, because it is fed by an underground celestial stream.</li>
</ul>

<h2 class="text-2xl font-bold mt-6 mb-4">📸 Photo Gallery Callouts</h2>

<ul class="list-disc ml-6 space-y-2">
<li><strong>📍 The Nagara Spire:</strong> A low-angle shot of the temple's intricately carved spire against the morning mist.</li>
<li><strong>📍 The Giant Squirrel:</strong> Patience is key! Capture the "Shekru" in its vibrant maroon and beige coat jumping through the canopy.</li>
<li><strong>📍 Shidi Ghat Ladders:</strong> A dramatic shot of trekkers ascending the vertical iron ladders with the valley in the background.</li>
<li><strong>📍 The Portuguese Bell:</strong> Detail shots of the Latin inscriptions and the cross on the ancient bell.</li>
<li><strong>📍 Gupt Bhimashankar:</strong> A peaceful shot of the small Shiva Linga located under a natural waterfall in the deep forest.</li>
<li><strong>📍 Forest Macro:</strong> Close-up shots of the unique Sahyadri orchids and ferns that cover the trees during the monsoon.</li>
</ul>""",
    "difficulty": "Moderate",
    "duration_hours": 7,
    "distance_km": 12.0,
    "height": 1033,
    "best_season": ["Monsoon", "Winter"],
    "group_size": 15,
    "image": "images/treks/bhimashankar.webp",
    "location": { "district": "Pune", "region": "Sahyadri (Western Ghats)", "state": "Maharashtra" },
    "created_at": { "$date": "2026-02-20T00:00:00Z" },
    "highlights": [
      { "name": "Shidi Ghat", "type": "adventure", "description": "The ladder route for experienced trekkers." },
      { "name": "Gupt Bhimashankar", "type": "culture", "description": "A hidden lingam in the riverbed." },
      { "name": "Shekru Sightings", "type": "nature", "description": "Home to the Giant Indian Squirrel." }
    ],
    "is_active": True, "is_featured": False, "featured_rank": 0
  }
]

WATERFALLS = [
  {
    "name": "Vajrai Waterfall",
    "slug": "vajrai-waterfall",
    "description": """Vajrai Waterfall is a spectacular three-tiered plunge that holds the title of the tallest waterfall in Maharashtra and the second tallest in India. Falling from a staggering height of 1,840 feet (560 meters), it originates from the Urmodi River and creates a thunderous roar as it crashes into the deep Sahyadri valley near Satara. This is not just a waterfall; it is a giant of nature that commands the landscape. Surrounded by the lush greenery of the Sahyadri Tiger Reserve, the falls are often shrouded in thick mist, with the white water appearing like a silver thread draped over the mountainside. Reaching the viewpoint after a pleasant trek through the Kaas region provides a sense of scale and power that few other natural wonders in India can match.

<h2 class="text-2xl font-bold mt-6 mb-4">Origin of the Name</h2>

The name "Vajrai" has deep spiritual roots in the Satara region. Locally, it is believed to be the abode of the Goddess Vajrai, a powerful protector deity of the Western Ghats. According to folklore, the waterfall was created when the Goddess struck the mountain with her divine weapon (Vajra) to create a perennial source of water for the drought-prone regions below. 



Culturally, the waterfall is considered sacred by the villagers of Bhambavli. They believe that the purity of the water is a gift from the heavens, and once a year, they perform a special 'Pooja' at the base to thank the Goddess for the prosperity the Urmodi River brings to their farms. The area around the falls is also home to ancient shrines tucked away in the forest, where sages are said to have meditated for centuries, drawn by the intense energy of the falling water.

<h2 class="text-2xl font-bold mt-6 mb-4">Natural Features & Seasons</h2>

Vajrai is a three-step perennial waterfall, though its "Beast Mode" is strictly during the monsoon.

Monsoon (July–Sept): The volume is so immense that the spray can be felt from hundreds of meters away. The entire cliff face turns into a vertical garden of rare Sahyadri wildflowers.

Post-Monsoon (Oct–Nov): The flow becomes more graceful and the sky clears, offering the best visibility for photography.

The Crater: The water falls into a massive natural basin that is nearly 500 feet deep. The sheer force of the water has carved out unique rock formations over millions of years.

<h2 class="text-2xl font-bold mt-6 mb-4">Importance to the Region</h2>

Vajrai is the lifeblood of the Urmodi Dam. The water that plunges here eventually feeds the reservoir, which provides drinking water and irrigation to over 100 villages in the Satara district. Economically, it has transformed the nearby Bhambavli Flower Plateau into a premier eco-tourism destination. The local community has formed a 'Vikas Samiti' to manage the tourism, ensuring that the revenue from entry fees goes directly into village schools and forest conservation. It is a shining example of how a natural wonder can sustain both an ecosystem and a community.

<h2 class="text-2xl font-bold mt-6 mb-4">How to Reach</h2>

<div class="bg-gray-50 p-4 rounded-lg border-l-4 border-blue-500">
<p class="font-semibold text-lg mb-3">🚉 Nearest Railway Station</p>
<p class="mb-4"><strong>Satara Railway Station</strong> (approximately 35 km away).</p>

<p class="font-semibold text-lg mb-3">🚗 From Station</p>
<p class="mb-4">Take a local ST bus or private vehicle from Satara city towards the Kaas Plateau. From Kaas, a diversion leads to Bhambavli village. The road is scenic but narrow with several hairpin bends.</p>

<p class="font-semibold text-lg mb-3">🚌 Transport Options:</p>
<ul class="list-disc ml-6 space-y-2 mb-4">
<li><strong>State Transport Bus:</strong> Satara to Kaas/Bhambavli (₹50–₹70).</li>
<li><strong>Private Taxi from Satara:</strong> ₹1,800–₹2,500 (Fair price for a round trip; avoid paying more than ₹3,000).</li>
<li><strong>Shared Jeep:</strong> Available from Satara ST stand during peak weekends (₹100–₹150 per seat).</li>
<li><strong>Private Vehicle:</strong> Best for groups; parking is available at the Bhambavli village base.</li>
</ul>

<p class="font-semibold text-yellow-700">💡 Traveler Tip:</p>
<p>There is a small entry fee (approx ₹30) collected by the Bhambavli Flower Plateau committee. Avoid trying to trek to the very mouth of the falls during heavy rains, as the river current is deceptively strong and flash floods are common.</p>
</div>

<h2 class="text-2xl font-bold mt-6 mb-4">🤔 Did You Know?</h2>

<ul class="list-disc ml-6 space-y-2">
<li>Vajrai is nearly three times the height of the Statue of Unity, making it one of the most imposing natural structures in India.</li>
<li>The water never dries up completely, even in May, because it is fed by a high-altitude underground aquifer.</li>
<li>The forest around the falls is part of the Sahyadri Tiger Reserve, and lucky visitors have spotted leopards and barking deer near the streams.</li>
<li>During the monsoon, the wind is so strong that the falling water is often blown upwards, creating a spectacular "Reverse Waterfall" effect.</li>
<li>The nearby Bhambavli Plateau is often compared to the Kaas Plateau for its variety of rare orchids and the 'Karvy' flower that blooms once in 8 years.</li>
<li>The sound of the waterfall is estimated to reach 90 decibels at the base—roughly the same as a shouting crowd!</li>
</ul>

<h2 class="text-2xl font-bold mt-6 mb-4">📸 Photo Gallery Callouts</h2>

<ul class="list-disc ml-6 space-y-2">
<li><strong>📍 The Three-Tier Frame:</strong> A wide-angle shot from the Bhambavli viewpoint showing all three stages of the fall against the green cliffs.</li>
<li><strong>📍 Mist and Rainbows:</strong> Morning shots (9 AM–11 AM) when the sunlight hits the spray to create vibrant rainbows at the base.</li>
<li><strong>📍 Reverse Waterfall Video:</strong> Capture the water being blown back into the sky during high-wind monsoon days.</li>
<li><strong>📍 The Flower Carpet:</strong> A macro shot of the wildflowers in the foreground with the blurry white waterfall in the background.</li>
<li><strong>📍 The Urmodi Reservoir View:</strong> A panoramic shot showing where the waterfall meets the calm waters of the dam below.</li>
</ul>""",
    "difficulty": "Moderate",
    "duration_hours": 3,
    "distance_km": 4.0,
    "height": 1840,
    "best_season": ["Monsoon"],
    "group_size": 20,
    "image": "images/waterfalls/vajrai.webp",
    "location": { "district": "Satara", "region": "Sahyadri (Western Ghats)", "state": "Maharashtra" },
    "created_at": { "$date": "2026-02-20T00:00:00Z" },
    "highlights": [
      { "name": "Three-tier Cascade", "type": "nature", "description": "The water drops in three distinct stages from a straight cliff." },
      { "name": "Kaas Plateau", "type": "nature", "description": "Located just 5km from the UNESCO World Heritage flower valley." },
      { "name": "Urmodi River Origin", "type": "history", "description": "The sacred starting point of the Urmodi river." }
    ],
    "is_active": True, "is_featured": True, "featured_rank": 1
  }
]

# ---------- INSERT HELPERS ----------
def seed_treks():
    for trek in TREKS:
        try:
            validate_trek(trek)
            treks_collection.insert_one(trek)
            print(f"✅ Trek inserted: {trek['name']}")
        except DuplicateKeyError:
            print(f"⚠️ Trek already exists: {trek['slug']}")
        except Exception as e:
            print(f"❌ Trek failed: {e}")

def seed_waterfalls():
    for wf in WATERFALLS:
        try:
            validate_waterfall(wf)
            waterfalls_collection.insert_one(wf)
            print(f"✅ Waterfall inserted: {wf['name']}")
        except DuplicateKeyError:
            print(f"⚠️ Waterfall already exists: {wf['slug']}")
        except Exception as e:
            print(f"❌ Waterfall failed: {e}")

# ---------- RUN ----------
if __name__ == "__main__":
    print("🌱 Seeding database...")
    seed_treks()
    seed_waterfalls()
    print("✅ Seeding complete")
