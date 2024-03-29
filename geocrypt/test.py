# -*- coding: utf-8 -*-
# =================================================================
#
# Copyright (C) 2021 Spatial Current, Inc. - All Rights Reserved
# Released as open source under the MIT License.  See LICENSE file.
#
# =================================================================
import unittest

test_cases = {
    "point": {
        "input": [
            {
                "type": "lonlat",
                "value": [-77.03338623046875, 38.933241401288399]
            },
            {
                 "type": "Point",
                 "coordinates": [-77.03338623046875, 38.933241401288399]
            },
            {
                "type": "Feature",
                "geometry": {
                     "type": "Point",
                     "coordinates": [-77.03338623046875, 38.933241401288399]
                }
            },
            {
                "type": "Feature",
                "geometry":
                {
                    "type": "GeometryCollection",
                    "geometries": [{
                        "type": "Point",
                        "coordinates": [-77.03338623046875, 38.933241401288399]
                    }]
                }
            }
        ],
        "output": "a49b25eda343f0dd88e93dca71d0c5a0"
    },
    "polygon": {
        "input": [
            {
                "id": 1,
                "type": "Feature",
                "properties":
                {
                    "addr:street": "18th Street Northwest"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-77.0416259765625, 38.90065217853344],
                            [-77.0416259765625, 38.92202385126893],
                            [-77.04299926757812, 38.92309226598178],
                            [-77.04299926757812, 38.9070643560226],
                            [-77.0416259765625, 38.90065217853344]
                        ]
                    ]
                }
            },
            {
                "id": 1,
                "type": "Feature",
                "properties":
                {
                    "addr:street": "18th Street Northwest"
                },
                "geometry": {
                    "type": "GeometryCollection",
                    "geometries": [
                        {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [-77.0416259765625, 38.90065217853344],
                                    [-77.0416259765625, 38.92202385126893],
                                    [-77.04299926757812, 38.92309226598178],
                                    [-77.04299926757812, 38.9070643560226],
                                    [-77.0416259765625, 38.90065217853344]
                                ]
                            ]
                        }
                    ]
                }
            },
            {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-77.0416259765625, 38.90065217853344],
                        [-77.0416259765625, 38.92202385126893],
                        [-77.04299926757812, 38.92309226598178],
                        [-77.04299926757812, 38.9070643560226],
                        [-77.0416259765625, 38.90065217853344]
                    ]
                ]
            }
        ],
        "output": "ca9f61e80989882e6876f69aef90a899"
    }
}


class TestGeocrypt(unittest.TestCase):
    """
    TestGeocrypt is used for testing geocrypt
    """

    def test_point(self):
        import geocrypt

        for x in test_cases["point"]["input"]:
            try:
                self.assertEqual(geocrypt.hash(x), test_cases["point"]["output"])
            except Exception as err:
                print("Input Object:", x)
                print("Calculated Hash:", geocrypt.hash(x))
                print("Valid Hash:", test_cases["point"]["output"])
                raise err

    def test_polygon(self):
        import geocrypt

        for x in test_cases["polygon"]["input"]:
            try:
                self.assertEqual(geocrypt.hash(x), test_cases["polygon"]["output"])
            except Exception as err:
                print("Input Object:", x)
                print("Calculated Hash:", geocrypt.hash(x))
                print("Valid Hash:", test_cases["polygon"]["output"])
                raise err


if __name__ == '__main__':
    unittest.main()
