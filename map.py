import math
import requests
from io import BytesIO
from PIL import Image
from db.tiles import MapTile
from db.db_session import create_session


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)


class Map:
    def __init__(self):
        self.smurl = r"http://a.tile.openstreetmap.org/{}/{}/{}.png"

    def downloadTile(self, x, y, zoom):
        imgurl = self.smurl.format(zoom, x, y)
        try:
            req = requests.get(imgurl, timeout=5)
            img = req.content
            if not img or req.status_code != 200:
                print(imgurl)
                raise Exception
        except Exception:
            return None
        tile = MapTile(x=x, y=y, zoom=zoom, img=img)
        with create_session() as session:
            session.add(tile)
            session.commit()
            session.refresh(tile)
        return tile

    def getFromDB(self, x, y, zoom):
        with create_session() as session:
            req = session.query(MapTile).filter(MapTile.x == x).filter(MapTile.y == y).filter(MapTile.zoom == zoom)
            if req.count() < 1:
                return None
            return req.first()

    # def getImageCluster(self, lat_deg, lon_deg, delta_lat, delta_long, zoom, x_size, y_size):
    def getImageCluster(self, xmin, ymin, zoom, x_size, y_size):
        # delta_lat = 0.02
        # delta_long = 0.05
        # xmin, ymax = deg2num(lat_deg, lon_deg, zoom)
        # xmax, ymin = deg2num(lat_deg + delta_lat, lon_deg + delta_long, zoom)
        # Cluster = Image.new('RGB', ((xmax - xmin + 1) * 256 - 1, (ymax - ymin + 1) * 256 - 1))
        xmax = xmin + math.ceil(x_size / 256)
        ymax = ymin + math.ceil(y_size / 256)
        Cluster = Image.new('RGB', (x_size, y_size))
        for xtile in range(xmin, xmax + 1):
            for ytile in range(ymin, ymax + 1):
                maptile = self.getFromDB(xtile, ytile, zoom)
                if not maptile:
                    maptile = self.downloadTile(xtile, ytile, zoom)
                if not maptile:
                    # No tile
                    tile = Image.new("RGB", (256, 256), (179, 179, 179))
                else:
                    tile = Image.open(BytesIO(maptile.img))
                Cluster.paste(tile, box=((xtile - xmin) * 256, (ytile - ymin) * 255))
        return Cluster
