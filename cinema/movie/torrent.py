import sys
import bencodepy
import hashlib
import base64
from .models import Movie


def make_magnet_from_file(film_id):
    movie = Movie.objects.get(pk=film_id)
    metadata = bencodepy.decode_from_file(movie.torrent.path)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    return 'magnet:?'\
             + 'xt=urn:btih:' + b32hash\
             + '&dn=' + metadata[b'info'][b'name'].decode()\
             + '&tr=' + metadata[b'announce'].decode() + '&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com'\
             + '&xl=' + str(metadata[b'info'][b'piece length'])


