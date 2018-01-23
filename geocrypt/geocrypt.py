import json
import hashlib


def hash(value, value_type=None, decimals=None, algorithm="md5"):

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

        coords = value.get("value") or value.get("coords") or value.get("coordinates")

        if coords is None or len(coords) == 0:
            raise Exception("missing coordinates")

        if len(coords) != 2:
            raise Exception("Invalid number of coordinates")

        if decimals is not None:

            if decimals < 0:
                raise Exception("Invalid number of decimals")

            coords = [round(i, decimals) for i in coords]

        geometries = [{"coordinates": coords, "type": "Point"}]
        text = json.dumps(geometries, ensure_ascii=False)

    elif value_type_lc == "featurecollection":

        features = value.get("features")

        if features is None or len(features) == 0:
            raise Exception("missing features")

        geometries = []
        for f in features:
            geometries = geometries + normalize_as_list_of_geometries(f.get("geometry"))

        if decimals is not None:

            if decimals < 0:
                raise Exception("Invalid number of decimals")

            geometries = [round_geometry(g, decimals) for g in geometries]

        geometries = sorted(geometries, cmp=geometry_comparator)

        text = json.dumps(geometries, ensure_ascii=False)

    elif value_type_lc == "feature":

        geom = value.get("geometry")

        if geom is None:
            raise Exception("missing geometry")

        geometries = normalize_as_list_of_geometries(geom)

        if decimals is not None:

            if decimals < 0:
                raise Exception("Invalid number of decimals")

            geometries = [round_geometry(g, decimals) for g in geometries]

        geometries = sorted(geometries, cmp=geometry_comparator)

        text = json.dumps(geometries, ensure_ascii=False)

    elif value_type_lc == "point":
        geometries = [value]

        if decimals is not None:

            if decimals < 0:
                raise Exception("Invalid number of decimals")

            geometries = [round_geometry(g, decimals) for g in geometries]

        geometries = sorted(geometries, cmp=geometry_comparator)

        text = json.dumps(geometries, ensure_ascii=False)

    elif value_type_lc == "polygon":

        geometries = [value]

        if decimals is not None:

            if decimals < 0:
                raise Exception("Invalid number of decimals")

            geometries = [round_geometry(g, decimals) for g in geometries]

        geometries = sorted(geometries, cmp=geometry_comparator)

        text = json.dumps(geometries, ensure_ascii=False)

    else:
        raise Exception("Unknown value type "+value_type_lc+".")

    digest = None

    if algorithm == "md5":
        digest = hashlib.md5(text).hexdigest()
    elif algorithm == "sha1":
        digest = hashlib.sha1(text).hexdigest()
    elif algorithm == "sha224":
        digest = hashlib.sha224(text).hexdigest()
    elif algorithm == "sha256":
        digest = hashlib.sha256(text).hexdigest()
    elif algorithm == "sha384":
        digest = hashlib.sha384(text).hexdigest()
    elif algorithm == "sha512":
        digest = hashlib.sha512(text).hexdigest()
    else:
        raise Exception("Unknown hash function "+algorithm+".")

    return digest


def normalize_as_list_of_geometries(geom):
    if geom is None:
        raise Exception("geometry missing")

    if not isinstance(geom, dict):
        raise Exception("geometry is not a dict")

    geom_type = geom.get("type")
    if geom_type is None or len(geom_type) == 0:
        raise Exception("geometry type is missing")

    geom_type_lc = geom.get("type").lower()

    if geom_type_lc == "geometrycollection":

        geometries = geom.get("geometries")

        if geometries is None or len(geometries) == 0:
            raise Exception("missing geometries")

        return geometries

    else:
        return [geom]


def geometry_comparator(a, b):
    if a is None:
        raise Exception("a is missing")

    if b is None:
        raise Exception("b is missing")

    if not isinstance(a, dict):
        raise Exception("a is not a dict")

    if not isinstance(b, dict):
        raise Exception("b is not a dict")

    a_type = a.get("type")
    if a_type is None or len(a_type) == 0:
        raise Exception("A's geometry type is missing")

    a_type_lc = a_type.lower()

    b_type = b.get("type")
    if b_type is None or len(b_type) == 0:
        raise Exception("B's geometry type is missing")

    b_type_lc = b_type.lower()

    geometry_type_order = ["point", "polygon", "geometrycollection"]

    if a_type_lc != b_type_lc:
        return geometry_type_order.index(a_type_lc) - geometry_type_order.index(b_type_lc)
    else:

        a_coords = a.get("value") or a.get("coords") or a.get("coordinates")

        if a_coords is None or len(a_coords) == 0:
            raise Exception("missing coordinates")

        b_coords = b.get("value") or b.get("coords") or b.get("coordinates")

        if b_coords is None or len(b_coords) == 0:
            raise Exception("missing coordinates")

        if a_type_lc == "point":

            if len(a_coords) != 2:
                raise Exception("Invalid number of coordinates")

            if len(b_coords) != 2:
                raise Exception("Invalid number of coordinates")

            if a_coords[0] != a_coords[0]:
                return b_coords[0] - a_coords[0]
            else:
                return b_coords[1] - a_coords[1]

        elif a_type_lc == "polygon":

            if len(a_coords) != len(b_coords):  # test number of rings
                return len(b_coords) - len(a_coords)  # give precedence to larger number of rings
            else:
                for i in range(len(a_coords)):  # test each ring
                    if len(a_coords[i]) != len(b_coords[i]):  # test length of ring from each
                        return len(b_coords[i]) - len(a_coords[i])  # give precedence to longer ring
                    else:
                        for j in range(len(a_coords[i])):
                            if a_coords[i][j][0] != a_coords[i][j][0]:
                                return b_coords[i][j][0] - a_coords[i][j][0]
                            else:
                                return b_coords[i][j][1] - a_coords[i][j][1]

        elif a_type_lc == "geometrycollection":
            raise NotImplementedError("Ordering a geometry collection is not implemented yet.")


def round_geometry(geom, decimals):

    if geom is None:
        raise Exception("geometry missing")

    if not isinstance(geom, dict):
        raise Exception("geometry is not a dict")

    geom_type = geom.get("type")
    if geom_type is None or len(geom_type) == 0:
        raise Exception("geometry type is missing")

    geom_type_lc = geom.get("type").lower()

    if geom_type_lc == "point":

        coords = geom.get("coordinates") or geom.get("coords")

        if coords is None or len(coords) == 0:
            raise Exception("missing coordinates")

        if len(coords) != 2:
            raise Exception("Invalid number of coordinates")

        geom = {
            "type": "Point",
            "coordinates": [round(i, decimals) for i in coords]
        }

    elif geom_type_lc == "polygon":

        coords = geom.get("coordinates") or geom.get("coords")

        if coords is None or len(coords) == 0:
            raise Exception("missing coordinates")

        geom = {
            "type": "Polygon",
            "coordinates": round_rings(coords, decimals)
        }

    else:
        raise Exception("Unknown geometry type")

    return geom


def round_rings(rings, decimals):
    return [[[round(k, decimals) for k in j] for j in i] for i in rings]


def round_coordinates(coords, decimals):
    return [[round(j, decimals) for j in i] for i in coords]
