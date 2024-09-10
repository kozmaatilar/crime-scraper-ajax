from util import converter

def postData(startDate='',endDate='',locationData={'longitude':None, 'latitude':None}):
        data = converter(locationData['latitude'], locationData['longitude'])
        return {
    "buffer": {
        "enabled": False,
        "restrictArea": False,
        "value": []
    },
    "date": {
        "start": startDate,
        "end": endDate,
        "quick": ""
    },
    "agencies": [],
    "layers": {
        "selection": [
            None,
            None,
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            {
                "selected": False
            },
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            },
            {
                "selected": True
            }
        ]
    },
    "location": {
        "bounds": {
            "east": data['lngMax/east'],
            "north": data['latMax/north'],
            "south": data['latMin/south'],
            "west": data['lngMin/west']
        },
        "lat": locationData['latitude'],
        "lng": locationData['longitude'],
        "zoom": 13
    },
    "analyticLayers": {
        "density": {
            "selected": False,
            "transparency": 60
        }
    }
}