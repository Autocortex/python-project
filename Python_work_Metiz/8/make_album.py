def make_album(artist_name, description_album, music_tracks = ''):
	"""Получает информацию и преобразовывает ее в словарь."""
	if music_tracks:
		album_info = {'artist': artist_name,
		              'description': description_album,
                      'mus_tracks': music_tracks,
		             }
	else:
		album_info = {'artist': artist_name, 'description': description_album}
	return album_info

while True:
	print("\nTell me about your album:")
	print("\n(enter 'q' for exit)")

	ar_name = input("Artist name: ")
	if ar_name == 'q':
		break

	desc_album = input("Description album: ")
	if desc_album == 'q':
		break

	mus_track = input("Music tracks: ")
	if mus_track == 'q':
		break

	album = make_album(ar_name, desc_album, mus_track)
	print(album)