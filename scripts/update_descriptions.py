from pymongo import MongoClient

# ---------- DB CONNECTION ----------
client = MongoClient("mongodb://localhost:27017/")
db = client["trek_maharashtra"]

treks_collection = db["treks"]
waterfalls_collection = db["waterfalls"]

# ---------- TREK DESCRIPTIONS ----------
TREK_DESCRIPTIONS = {
    "Kalavantin Durg": """Perched at an elevation of <strong>2,250 feet</strong> in the Western Ghats near Panvel, Kalavantin Durg is one of Maharashtra's most <strong>thrilling and vertigo-inducing treks</strong>. Known for its <strong>near-vertical rock-cut steps</strong> carved at a jaw-dropping <strong>40-degree incline</strong>, this ancient fort offers an adrenaline-pumping adventure that separates the brave from the faint-hearted. The reward? <strong>360-degree panoramic views</strong> of the Matheran plateau, Prabalgad fort, and the endless Sahyadri ranges that will leave you absolutely speechless.

<h2 class="text-2xl font-bold mt-6 mb-4">History & Heritage</h2>

Here's the fascinating part - Kalavantin Durg isn't just another fort. Dating back to the <strong>3rd century BC</strong>, it belongs to the <strong>Buddhist era</strong>, making it over <strong>2,300 years old</strong>! The fort is named after <strong>Queen Kalavantin</strong>, a Buddhist queen who was so mesmerized by the views that she chose this rocky pinnacle as her <strong>personal meditation retreat</strong>. Imagine a queen climbing these treacherous steps daily for inner peace!<br><br>

Unlike typical military forts, Kalavantin Durg served as a <strong>strategic watchtower and observation post</strong>. Its location was perfect for monitoring the bustling <strong>trade routes between the Konkan coast and the Deccan plateau</strong>. Guards stationed here could spot approaching armies or traders from miles away. Today, only the <strong>rock-cut steps and scattered stone structures</strong> remain, but they whisper tales of an era when this was a thriving lookout point.

<h2 class="text-2xl font-bold mt-6 mb-4">The Trail Experience</h2>

The adventure begins at <strong>Thakurwadi village</strong>, at the base of Prabalgad fort. The initial trail through dense forests is moderate, but here's where it gets wild - the <strong>infamous rock-cut steps</strong>! Picture this: <strong>hand-carved stairs</strong> etched directly into vertical cliff faces, with <strong>sheer drops on both sides</strong> and no railings. You'll literally need to use <strong>all fours</strong> in some sections, gripping rocks while your heart races.<br><br>

<strong>Trek Duration:</strong> 2-3 hours (but feels like an eternity when you're clinging to those steps!)<br>
<strong>Best Time:</strong> June to February (monsoon brings dramatic mist; winter offers crystal-clear views)<br>
<strong>Difficulty:</strong> Moderate to challenging - not for acrophobics!<br><br>

<strong>Pro tip:</strong> The final 10 minutes is a near-vertical climb that'll test every ounce of your courage. But trust us, standing atop that pinnacle with clouds beneath your feet is pure magic!

<h2 class="text-2xl font-bold mt-6 mb-4">How to Reach</h2>

<div class="bg-gray-50 p-4 rounded-lg">
<p class="font-semibold text-lg mb-3">🚉 Nearest Railway Station</p>
<p class="mb-4">Panvel Railway Station (approximately 25 km away)</p>

<p class="font-semibold text-lg mb-3">🚗 From Station</p>
<p class="mb-4">Take a local bus or private vehicle to <strong>Thakurwadi village</strong> (base village). The journey takes approximately 1-1.5 hours from Panvel. You can also hire a taxi directly from Mumbai (approximately 2.5 hours).</p>

<p class="font-semibold text-lg mb-3">📍 Base Village (Starting Point)</p>
<p class="mb-4">Thakurwadi Village - This is where your trek begins</p>

<p class="font-semibold text-lg mb-3">🚌 Transport Options:</p>
<ul class="list-disc ml-6 space-y-2 mb-4">
<li><strong>State Transport Bus:</strong> Panvel to Prabalgad base village, then local transport to Thakurwadi</li>
<li><strong>Private Taxi from Panvel:</strong> ₹800-1200 (negotiate beforehand to avoid overcharging)</li>
<li><strong>Shared Jeep:</strong> Available from Panvel ST stand on weekends (₹150-200 per person)</li>
<li><strong>Private Vehicle:</strong> Best option for groups - parking available at Thakurwadi village</li>
</ul>

<p class="font-semibold text-yellow-700">💡 Traveler Tip:</p>
<p>Locals may quote higher prices (₹1500-2000) for taxi rides - the fair price is ₹800-1200. Always negotiate and fix the price before starting your journey. On weekends, shared jeeps are the most economical option!</p>
</div>

<h2 class="text-2xl font-bold mt-6 mb-4">🤔 Did You Know?</h2>

<ul class="list-disc ml-6 space-y-2">
<li><strong>Kalavantin Durg has approximately 350-400 rock-cut steps</strong> carved directly into the mountain face - each one a testament to ancient engineering!</li>
<li>On <strong>crystal-clear winter mornings</strong>, you can actually spot the <strong>Arabian Sea shimmering in the distance</strong> from the summit - that's over 40 km away!</li>
<li>The steps are so steep that you're actually climbing at a <strong>70-80 degree angle</strong> in some sections - almost like climbing a ladder on a cliff!</li>
<li><strong>Kalavantin Durg is often called the "sister fort" of Prabalgad</strong>, and both can be trekked in a single day by experienced trekkers</li>
<li>During the <strong>monsoon, clouds literally pass below you</strong> while you're standing at the top - it's like being in an airplane!</li>
<li>The trek is also known as <strong>"Kalvantin Pinnacle"</strong> and is considered one of the most <strong>dangerous treks in Maharashtra</strong> due to its exposure</li>
</ul>

<h2 class="text-2xl font-bold mt-6 mb-4">📸 Photo Gallery Callouts</h2>

<ul class="list-disc ml-6 space-y-2">
<li><strong>📍 The Stairway to Heaven Shot:</strong> Capture the near-vertical rock-cut steps disappearing into the clouds (best during monsoon mornings with mist)</li>
<li><strong>📍 Summit 360° Panorama:</strong> The flat summit offers breathtaking views of Matheran, Prabalgad, and the entire Sahyadri range - perfect for sunrise shots</li>
<li><strong>📍 The Courage Shot:</strong> Looking down from the top of the steps with the valley thousands of feet below - only for the brave!</li>
<li><strong>📍 Cloud Cover Magic:</strong> Monsoon afternoons when clouds roll in below you, creating a surreal "above the clouds" experience</li>
<li><strong>📍 The Pinnacle Silhouette:</strong> Capture the dramatic rocky pinnacle against the setting sun from Prabalgad fort across the valley</li>
<li><strong>📍 Ancient Steps Close-up:</strong> Detail shots of the weathered rock-cut steps showing centuries of erosion and history</li>
</ul>"""
}

# ---------- WATERFALL DESCRIPTIONS ----------
WATERFALL_DESCRIPTIONS = {
    "Kalmadvi Waterfall": """Hidden in the pristine forests of the Konkan region near Khed, Kalmandavi Waterfall is nature's <strong>monsoon masterpiece</strong> - a <strong>150-foot thundering cascade</strong> that transforms from a gentle trickle to a roaring beast during the rains. This isn't just another waterfall; it's an <strong>untouched paradise</strong> where you can witness raw nature at its most powerful and beautiful.

<h2 class="text-2xl font-bold mt-6 mb-4">Origin of the Name</h2>

The name "Kalmandavi" has a mysterious origin that locals love sharing. <strong>"Kal"</strong> means <strong>black</strong> and <strong>"Mandavi"</strong> refers to the <strong>dark basalt rocks</strong> that create a dramatic black canvas behind the white cascade - especially stunning when the rocks glisten wet during monsoon!<br><br>

But here's the local legend: villagers believe the waterfall was named after a <strong>forgotten deity</strong> worshipped here centuries ago. Some elders claim that on foggy mornings, you can still see the <strong>silhouette of the deity in the mist</strong> rising from the falls. Spooky or spiritual? You decide!

<h2 class="text-2xl font-bold mt-6 mb-4">Natural Features & Seasons</h2>

Kalmandavi is a <strong>seasonal phenomenon</strong> - alive and roaring from <strong>June to September</strong>, with <strong>peak flow in July-August</strong> when it's at its most dramatic. The waterfall originates from <strong>plateau streams</strong> in the Western Ghats that converge and plunge dramatically over the cliff edge, creating a <strong>misty curtain</strong> that can drench you from 20 feet away!<br><br>

<strong>Best Time to Visit:</strong><br>
🌧️ <strong>Monsoon (July-August):</strong> Full force, deafening roar, misty spray<br>
🍃 <strong>Post-monsoon (Oct-Nov):</strong> Moderate flow, perfect for photography, lush green surroundings<br><br>

The surrounding <strong>dense sal and teak forests</strong> are home to <strong>exotic bird species, colorful butterflies</strong>, and if you're lucky, you might spot <strong>barking deer or jungle cats</strong> near the water pools below.

<h2 class="text-2xl font-bold mt-6 mb-4">Importance to the Region</h2>

Kalmandavi isn't just beautiful - it's a <strong>lifeline for the region</strong>. The waterfall feeds into streams that <strong>irrigate thousands of acres</strong> of agricultural land downstream, supporting <strong>rice paddies and vegetable farms</strong> that feed local communities year-round.<br><br>

During dry months, the <strong>catchment area becomes a crucial watering hole</strong> for wildlife, creating a mini-ecosystem where animals gather at dusk. For local villagers, this waterfall is <strong>sacred</strong> - they perform an annual <strong>monsoon festival</strong> here, thanking nature for its bounty.<br><br>

<strong>Eco-Tourism Impact:</strong> The waterfall has transformed the local economy, providing <strong>seasonal income through homestays, trekking guides, and local food stalls</strong>. It's a perfect example of <strong>sustainable tourism</strong> where nature and community thrive together.<br><br>

<strong>Hidden Gem Alert:</strong> Below the main fall, there's a <strong>natural pool</strong> perfect for a refreshing dip (monsoon swimmers beware - the current is strong!). The area also has <strong>ancient rock formations</strong> with natural caves that locals say were used by shepherds centuries ago.

<h2 class="text-2xl font-bold mt-6 mb-4">How to Reach</h2>

<div class="bg-gray-50 p-4 rounded-lg">
<p class="font-semibold text-lg mb-3">🚉 Nearest Railway Station</p>
<p class="mb-4">Khed Railway Station (approximately 15 km away)</p>

<p class="font-semibold text-lg mb-3">🚗 From Station</p>
<p class="mb-4">Take a local bus or private vehicle to the waterfall base point. The journey takes approximately 30-45 minutes from Khed station. From Pune, it's a scenic 3-hour drive through the Western Ghats.</p>

<p class="font-semibold text-lg mb-3">📍 Base Village (Starting Point)</p>
<p class="mb-4">Kalmandavi Village - A short 15-20 minute trek from the village leads to the waterfall</p>

<p class="font-semibold text-lg mb-3">🚌 Transport Options:</p>
<ul class="list-disc ml-6 space-y-2 mb-4">
<li><strong>State Transport Bus:</strong> Khed to Kalmandavi village (₹30-50 per person)</li>
<li><strong>Private Taxi from Khed:</strong> ₹500-700 (fair price - locals may quote ₹1000-1200)</li>
<li><strong>Shared Auto:</strong> Available from Khed on weekends (₹80-100 per person)</li>
<li><strong>Private Vehicle from Pune:</strong> Best for groups - parking available near the village</li>
</ul>

<p class="font-semibold text-yellow-700">💡 Traveler Tip:</p>
<p>During monsoon, local guides may offer their services for ₹500-800. While the trail is straightforward, a guide can be helpful for first-timers and provides insights into local flora and fauna. Always negotiate the price beforehand and avoid paying more than ₹800 for guide services!</p>
</div>

<h2 class="text-2xl font-bold mt-6 mb-4">🤔 Did You Know?</h2>

<ul class="list-disc ml-6 space-y-2">
<li>During <strong>peak monsoon, the water volume increases by more than 15 times</strong> - transforming from a gentle stream to a thundering cascade of over <strong>2,000 liters per second</strong>!</li>
<li>The <strong>mist from the waterfall can be felt from over 50 meters away</strong> during monsoon, creating a natural air-conditioning effect in the entire area</li>
<li>Local legends say that <strong>medicinal herbs grow around the waterfall</strong> that are used in traditional Ayurvedic treatments by village healers</li>
<li>The <strong>black basalt rocks behind the falls are over 65 million years old</strong> - formed during the Deccan Volcanic eruptions!</li>
<li>In the early morning sunlight, you can often spot <strong>rainbow formations in the waterfall's mist</strong> - a photographer's dream!</li>
<li>The waterfall is home to <strong>unique frog species</strong> that only breed during the monsoon season, creating a symphony of croaks at night</li>
</ul>

<h2 class="text-2xl font-bold mt-6 mb-4">📸 Photo Gallery Callouts</h2>

<ul class="list-disc ml-6 space-y-2">
<li><strong>📍 The Full Cascade Shot:</strong> Capture the entire 150-foot drop from the viewpoint opposite - best during peak monsoon for maximum drama</li>
<li><strong>📍 Rainbow in the Mist:</strong> Early morning (7-9 AM) when sunlight hits the mist, creating spectacular rainbow displays</li>
<li><strong>📍 The Natural Pool:</strong> Crystal-clear natural pool at the base during post-monsoon - perfect for that "waterfall swim" Instagram shot</li>
<li><strong>📍 Black Rock Contrast:</strong> Close-up of white water against the dark basalt rocks - stunning monochrome photography opportunity</li>
<li><strong>📍 Forest Trail Leading to Falls:</strong> The lush green approach through sal forests creates a mystical pathway shot</li>
<li><strong>📍 Monsoon Fury:</strong> Wide-angle shot during July-August showing the sheer power and volume of water - use a fast shutter speed!</li>
<li><strong>📍 Sunset Glow:</strong> Golden hour shots when the setting sun illuminates the mist, creating an ethereal golden glow around the falls</li>
</ul>""",

}

# ---------- UPDATE FUNCTIONS ----------

def update_trek_descriptions():
    """Update ONLY the description field for treks"""
    print("\n🔄 Updating Trek Descriptions...")
    updated_count = 0
    not_found_count = 0
    
    for trek_name, description in TREK_DESCRIPTIONS.items():
        result = treks_collection.update_one(
            {"name": trek_name},  # Find by name
            {"$set": {"description": description}}  # Update ONLY description
        )
        
        if result.matched_count > 0:
            print(f"✅ Updated: {trek_name}")
            updated_count += 1
        else:
            print(f"⚠️ Not found: {trek_name}")
            not_found_count += 1
    
    print(f"\n📊 Trek Summary: {updated_count} updated, {not_found_count} not found")

# def update_waterfall_descriptions():
#     """Update ONLY the description field for waterfalls"""
#     print("\n🔄 Updating Waterfall Descriptions...")
#     updated_count = 0
#     not_found_count = 0
    
#     for waterfall_name, description in WATERFALL_DESCRIPTIONS.items():
#         result = waterfalls_collection.update_one(
#             {"name": waterfall_name},  # Find by name
#             {"$set": {"description": description}}  # Update ONLY description
#         )
        
#         if result.matched_count > 0:
#             print(f"✅ Updated: {waterfall_name}")
#             updated_count += 1
#         else:
#             print(f"⚠️ Not found: {waterfall_name}")
#             not_found_count += 1
    
#     print(f"\n📊 Waterfall Summary: {updated_count} updated, {not_found_count} not found")

# ---------- RUN ----------
if __name__ == "__main__":
    print("🚀 Starting description updates...\n")
    print("=" * 50)
    
    update_trek_descriptions()
    # update_waterfall_descriptions()
    
    print("=" * 50)
    print("\n✅ All descriptions updated successfully!")
    print("\n💡 Tip: Check your website to see the new descriptions in action!")


    # run this command at the erminal

    # python scripts/update_descriptions.py