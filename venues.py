"""
Venue data for the Distinguished Gentlemen dinner map.
Each venue has coordinates, type (bar/restaurant/club/other), and a list of events held there.
"""

VENUES = [
    # ── DG I — 12/14/22 ──
    {
        "name": "Greens Restaurant",
        "lat": 37.8063,
        "lng": -122.4325,
        "type": "restaurant",
        "events": [
            {"dinner": "DG I — FESTIVUS!", "date": "12/14/22", "role": "Pre-Dinner", "dg": "CPT Pritchett"}
        ],
    },
    {
        "name": "Maybeck's",
        "lat": 37.7995,
        "lng": -122.4382,
        "type": "bar",
        "events": [
            {"dinner": "DG I — FESTIVUS!", "date": "12/14/22", "role": "Post-Dinner", "dg": "CPT Pritchett"}
        ],
    },
    {
        "name": "Balboa Cafe",
        "lat": 37.7999,
        "lng": -122.4340,
        "type": "bar",
        "events": [
            {"dinner": "DG I — FESTIVUS!", "date": "12/14/22", "role": "Post-Dinner", "dg": "CPT Pritchett"},
            {"dinner": "DG V", "date": "4/21/23", "role": "Post-Dinner", "dg": "Mr. Molinari"},
            {"dinner": "DG VII", "date": "6/29/23", "role": "Pre-Dinner", "dg": "Mr. Clifford"},
            {"dinner": "DG XI — FESTIVUS II", "date": "12/19/23", "role": "Post-Dinner", "dg": "Mr. Molinari"},
        ],
    },
    # ── DG II — 1/24/23 ──
    {
        "name": "The Devil's Acre",
        "lat": 37.7975,
        "lng": -122.4035,
        "type": "bar",
        "events": [
            {"dinner": "DG II", "date": "1/24/23", "role": "Pre-Dinner", "dg": "Mr. Cook",
             "note": "The DG Charter was written this night"}
        ],
    },
    {
        "name": "Original Joe's",
        "lat": 37.7978,
        "lng": -122.4072,
        "type": "restaurant",
        "events": [
            {"dinner": "DG II", "date": "1/24/23", "role": "Dinner", "dg": "Mr. Cook"}
        ],
    },
    {
        "name": "Gino and Carlo",
        "lat": 37.7980,
        "lng": -122.4083,
        "type": "bar",
        "events": [
            {"dinner": "DG II", "date": "1/24/23", "role": "Post-Dinner", "dg": "Mr. Cook"}
        ],
    },
    # ── DG III — 2/21/23 ──
    {
        "name": "Harper and Rye",
        "lat": 37.7865,
        "lng": -122.4222,
        "type": "bar",
        "events": [
            {"dinner": "DG III", "date": "2/21/23", "role": "Pre-Dinner", "dg": "Dr. Cudahy"}
        ],
    },
    {
        "name": "Harris' Steakhouse",
        "lat": 37.7903,
        "lng": -122.4213,
        "type": "restaurant",
        "events": [
            {"dinner": "DG III", "date": "2/21/23", "role": "Dinner", "dg": "Dr. Cudahy",
             "note": "HOPR Failure — couldn't get into House of Prime Rib"}
        ],
    },
    {
        "name": "Tupelo",
        "lat": 37.7702,
        "lng": -122.4310,
        "type": "bar",
        "events": [
            {"dinner": "DG III", "date": "2/21/23", "role": "Post-Dinner", "dg": "Dr. Cudahy"},
            {"dinner": "DG IX", "date": "9/26/23", "role": "Post-Dinner", "dg": "Dr. Cudahy"},
        ],
    },
    # ── DG IV — 3/30/23 ──
    {
        "name": "Black Magic Voodoo Lounge",
        "lat": 37.7853,
        "lng": -122.4293,
        "type": "bar",
        "events": [
            {"dinner": "DG IV", "date": "3/30/23", "role": "Pre-Dinner", "dg": "ESQ Deming"}
        ],
    },
    {
        "name": "Bobo's Steakhouse",
        "lat": 37.7912,
        "lng": -122.4096,
        "type": "restaurant",
        "events": [
            {"dinner": "DG IV", "date": "3/30/23", "role": "Dinner", "dg": "ESQ Deming"}
        ],
    },
    {
        "name": "Silver Cloud",
        "lat": 37.7839,
        "lng": -122.4112,
        "type": "bar",
        "events": [
            {"dinner": "DG IV", "date": "3/30/23", "role": "Post-Dinner", "dg": "ESQ Deming"}
        ],
    },
    # ── DG V — 4/21/23 ──
    {
        "name": "Geelou",
        "lat": 37.8002,
        "lng": -122.4365,
        "type": "bar",
        "events": [
            {"dinner": "DG V", "date": "4/21/23", "role": "Pre-Dinner", "dg": "Mr. Molinari"}
        ],
    },
    {
        "name": "Izzy's Steaks",
        "lat": 37.8005,
        "lng": -122.4371,
        "type": "restaurant",
        "events": [
            {"dinner": "DG V", "date": "4/21/23", "role": "Dinner", "dg": "Mr. Molinari"}
        ],
    },
    # ── DG VI — 5/19/23 ──
    {
        "name": "Amado's",
        "lat": 37.7625,
        "lng": -122.4198,
        "type": "restaurant",
        "events": [
            {"dinner": "DG VI", "date": "5/19/23", "role": "Pre-Dinner", "dg": "Mr. Rothaug"}
        ],
    },
    {
        "name": "Lolinda",
        "lat": 37.7564,
        "lng": -122.4158,
        "type": "restaurant",
        "events": [
            {"dinner": "DG VI", "date": "5/19/23", "role": "Dinner", "dg": "Mr. Rothaug"}
        ],
    },
    {
        "name": "Emporium SF",
        "lat": 37.7700,
        "lng": -122.4215,
        "type": "bar",
        "events": [
            {"dinner": "DG VI", "date": "5/19/23", "role": "Post-Dinner", "dg": "Mr. Rothaug"}
        ],
    },
    # ── DG VII — 6/29/23 ──
    {
        "name": "Cote Ouest Bistro",
        "lat": 37.8001,
        "lng": -122.4355,
        "type": "restaurant",
        "events": [
            {"dinner": "DG VII", "date": "6/29/23", "role": "Dinner", "dg": "Mr. Clifford",
             "note": "Mr. Hewitt's first dinner"}
        ],
    },
    {
        "name": "Final Final",
        "lat": 37.7998,
        "lng": -122.4367,
        "type": "bar",
        "events": [
            {"dinner": "DG VII", "date": "6/29/23", "role": "Post-Dinner", "dg": "Mr. Clifford"},
            {"dinner": "DG VIII", "date": "8/22/23", "role": "Post-Dinner", "dg": "Mr. Cook"},
        ],
    },
    # ── DG VIII — 8/22/23 (Sausalito) ──
    {
        "name": "Bar Bocce",
        "lat": 37.8594,
        "lng": -122.4849,
        "type": "bar",
        "events": [
            {"dinner": "DG VIII", "date": "8/22/23", "role": "Pre-Dinner", "dg": "Mr. Cook"}
        ],
    },
    {
        "name": "Salito's Crab House",
        "lat": 37.8586,
        "lng": -122.4851,
        "type": "restaurant",
        "events": [
            {"dinner": "DG VIII", "date": "8/22/23", "role": "Dinner", "dg": "Mr. Cook"}
        ],
    },
    # ── DG IX — 9/26/23 ──
    {
        "name": "The Ramp",
        "lat": 37.7614,
        "lng": -122.3870,
        "type": "bar",
        "events": [
            {"dinner": "DG IX", "date": "9/26/23", "role": "Pre-Dinner", "dg": "Dr. Cudahy"}
        ],
    },
    {
        "name": "RH Rooftop (Palm Court)",
        "lat": 37.7711,
        "lng": -122.4032,
        "type": "restaurant",
        "events": [
            {"dinner": "DG IX", "date": "9/26/23", "role": "Dinner", "dg": "Dr. Cudahy"}
        ],
    },
    # ── DG X — 10/25/23 ──
    {
        "name": "Old Ship Saloon",
        "lat": 37.7968,
        "lng": -122.3980,
        "type": "bar",
        "events": [
            {"dinner": "DG X", "date": "10/25/23", "role": "Pre-Dinner", "dg": "ESQ Deming"}
        ],
    },
    {
        "name": "Pierside",
        "lat": 37.7957,
        "lng": -122.3935,
        "type": "restaurant",
        "events": [
            {"dinner": "DG X", "date": "10/25/23", "role": "Dinner", "dg": "ESQ Deming"}
        ],
    },
    {
        "name": "Northstar Cafe",
        "lat": 37.7974,
        "lng": -122.4062,
        "type": "bar",
        "events": [
            {"dinner": "DG X", "date": "10/25/23", "role": "Post-Dinner", "dg": "ESQ Deming"}
        ],
    },
    # ── DG Wedding — 11/4/23 ──
    {
        "name": "Perry's",
        "lat": 37.7993,
        "lng": -122.4327,
        "type": "bar",
        "events": [
            {"dinner": "DG WEDDING!", "date": "11/4/23", "role": "Pre-Wedding", "dg": "Mr. Clifford"}
        ],
    },
    {
        "name": "Mauna Loa",
        "lat": 37.7855,
        "lng": -122.4090,
        "type": "bar",
        "events": [
            {"dinner": "DG WEDDING!", "date": "11/4/23", "role": "Venue", "dg": "Mr. Clifford"}
        ],
    },
    {
        "name": "The Olympic Club",
        "lat": 37.7813,
        "lng": -122.4068,
        "type": "club",
        "events": [
            {"dinner": "DG WEDDING!", "date": "11/4/23", "role": "Reception", "dg": "Mr. Clifford"},
            {"dinner": "DG XIII", "date": "2/16/24", "role": "Dinner", "dg": "Mr. Clifford",
             "note": "Justin — Cancer Free!"},
            {"dinner": "DG XXI — Crab Feed II", "date": "2/13/25", "role": "Dinner", "dg": "Mr. Clifford"},
        ],
    },
    # ── DG XI — 12/19/23 ──
    {
        "name": "Elements Bar + Lounge",
        "lat": 37.7855,
        "lng": -122.4102,
        "type": "bar",
        "events": [
            {"dinner": "DG XI — FESTIVUS II", "date": "12/19/23", "role": "Pre-Dinner", "dg": "Mr. Molinari",
             "note": "DG Turns 1! Grievance of the Year awarded."}
        ],
    },
    {
        "name": "John's Grill",
        "lat": 37.7868,
        "lng": -122.4047,
        "type": "restaurant",
        "events": [
            {"dinner": "DG XI — FESTIVUS II", "date": "12/19/23", "role": "Dinner", "dg": "Mr. Molinari"}
        ],
    },
    # ── DG XIV — 3/22/24 ──
    {
        "name": "The Bungalow",
        "lat": 37.8735,
        "lng": -122.4567,
        "type": "bar",
        "events": [
            {"dinner": "DG XIV", "date": "3/22/24", "role": "Post-Dinner", "dg": "CPT Pritchett",
             "note": "Tiburon — 'Bungalow, the only place we go'"}
        ],
    },
    # ── DG XVI — 6/13/24 ──
    {
        "name": "House of Prime Rib",
        "lat": 37.7910,
        "lng": -122.4180,
        "type": "restaurant",
        "events": [
            {"dinner": "DG XVI — HOPR Night", "date": "6/13/24", "role": "Dinner", "dg": "Dr. Cudahy",
             "note": "The group FINALLY makes it to HOPR!"}
        ],
    },
    # ── DG XVIII — 9/26/24 ──
    {
        "name": "Starlight Room",
        "lat": 37.7870,
        "lng": -122.4110,
        "type": "bar",
        "events": [
            {"dinner": "DG XVIII", "date": "9/26/24", "role": "Pre-Dinner", "dg": "Unknown",
             "note": "THE GREAT FLOWER FIASCO. Anthony: HAVING A BABY!"}
        ],
    },
    {
        "name": "Dawn Club",
        "lat": 37.7900,
        "lng": -122.4000,
        "type": "bar",
        "events": [
            {"dinner": "DG XVIII", "date": "9/26/24", "role": "Post-Dinner", "dg": "Unknown"}
        ],
    },
    # ── DG XX — 12/19/24 ──
    {
        "name": "The Fairmont (Tonga Room)",
        "lat": 37.7921,
        "lng": -122.4073,
        "type": "bar",
        "events": [
            {"dinner": "DG XX — FESTIVUS III", "date": "12/19/24", "role": "Pre-Dinner", "dg": "CPT Pritchett",
             "note": "Mickey INDUCTED. Grievance of the Year: Dr. Cudahy."}
        ],
    },
    {
        "name": "Acquerello",
        "lat": 37.7910,
        "lng": -122.4195,
        "type": "restaurant",
        "events": [
            {"dinner": "DG XX — FESTIVUS III", "date": "12/19/24", "role": "Dinner", "dg": "CPT Pritchett",
             "note": "High-end Italian in Nob Hill. Charter Review."}
        ],
    },
    # ── DG XVI Trivia ──
    {
        "name": "83 Proof",
        "lat": 37.7810,
        "lng": -122.3985,
        "type": "bar",
        "events": [
            {"dinner": "DG XVI — Trivia Night", "date": "2024", "role": "Trivia", "dg": "Unknown",
             "note": "Trivia with Riddles"}
        ],
    },
    {
        "name": "Tadich Grill",
        "lat": 37.7919,
        "lng": -122.4003,
        "type": "restaurant",
        "events": [
            {"dinner": "DG XVI — Trivia Night", "date": "2024", "role": "Dinner", "dg": "Unknown",
             "note": "Mussels + Clams / Risotto"}
        ],
    },
    # ── Post-Dinner Drinks Spots ──
    {
        "name": "April Jean",
        "lat": 37.7970,
        "lng": -122.4075,
        "type": "bar",
        "events": [
            {"dinner": "DG X (cont.)", "date": "10/25/23", "role": "Post-Dinner", "dg": "ESQ Deming",
             "note": "North Beach late-night spot"}
        ],
    },
    # ── Festivus IX — 12/19/25 ──
    {
        "name": "Trick Dog",
        "lat": 37.7617,
        "lng": -122.4175,
        "type": "bar",
        "events": [
            {"dinner": "Festivus IX", "date": "12/19/25", "role": "Pre-Dinner", "dg": "Mr. Cook",
             "note": "White Elephant gift exchange"}
        ],
    },
    {
        "name": "Flour + Water",
        "lat": 37.7592,
        "lng": -122.4125,
        "type": "restaurant",
        "events": [
            {"dinner": "Festivus IX", "date": "12/19/25", "role": "Dinner", "dg": "Mr. Cook"}
        ],
    },
    {
        "name": "Benders",
        "lat": 37.7655,
        "lng": -122.4195,
        "type": "bar",
        "events": [
            {"dinner": "Festivus IX", "date": "12/19/25", "role": "Post-Dinner", "dg": "Mr. Cook",
             "note": "Dive bar in the Mission"}
        ],
    },
    # ── DG Dinner 06/25/25 ──
    {
        "name": "Harry's Bar",
        "lat": 37.7890,
        "lng": -122.4340,
        "type": "bar",
        "events": [
            {"dinner": "DG Dinner", "date": "6/25/25", "role": "Post-Dinner", "dg": "Unknown",
             "note": "Ryan won over/under 1.5 hot chicks bet"}
        ],
    },
    # ── Chotto Matte (DG IV extended notes) ──
    {
        "name": "Chotto Matte",
        "lat": 37.7870,
        "lng": -122.4065,
        "type": "restaurant",
        "events": [
            {"dinner": "DG IV (extended notes)", "date": "3/30/23", "role": "Dinner", "dg": "ESQ Deming",
             "note": "Nikkei restaurant in Union Square. 'Justin looks like Matt Damon.'"}
        ],
    },
]
