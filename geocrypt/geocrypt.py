import json
import hashlib


def hash(value, value_type=None, algorithm="md5"):

    if value is None:
        raise Exception("value missing")

    if not isinstance(value, dict):
        raise Exception("value is not a dict")

    if value_type is None:
        value_type = value.get("type")

    if value_type is None:
        raise Exception("value_type is missing and not given by value.")

    if algorithm is None:
        raise Exception("algorithm is missing")

    text = None

    value_type_lc = value_type.lower()

    if value_type_lc == "lonlat":

        coords = value.get("value") or value.get("coords")

        if coords is None or len(coords) == 0:
            raise Exception("missing coordinates")

        if len(coords) != 2:
            raise Exception("Invalid number of coordinates")

        text = json.dumps([{"coordinates": coords, "type": "Point"}], ensure_ascii=False)

    elif value_type_lc == "featurecollection":

        features = value.get("features")

        if features is None or len(features) == 0:
            raise Exception("missing features")

        geometries = [f.get("geometry") for f in features]

        text = json.dumps(geometries, ensure_ascii=False)

    elif value_type_lc == "feature":

        geom = value.get("geometry")

        if geom is None:
            raise Exception("missing geometry")

        text = json.dumps([geom], ensure_ascii=False)

    else:
        raise Exception("Unknown value type "+value_type_lc+".")

    digest = None

    if algorithm == "md5":
        digest = hashlib.md5(text).hexdigest()
    elif algorithm == "sha1":
        digest = hashlib.sha1(text).hexdigest()
    elif algorithm == "sha256":
        digest = hashlib.sha256(text).hexdigest()
    elif algorithm == "sha512":
        digest = hashlib.sha512(text).hexdigest()
    else:
        raise("Unknown hash function "+algorithm+".")

    return digest
