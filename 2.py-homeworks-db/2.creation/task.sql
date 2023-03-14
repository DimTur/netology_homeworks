create table if not exists artists (
	id serial primary key,
	nickname text
);

create table if not exists albums (
	id serial primary key,	
	title text,
	year_realease integer
);

create table if not exists songs ( 
	id serial primary key,
	name_song text,
	duration numeric,
	album_id integer references albums(id)
);

create table if not exists genres (
	id serial primary key,
	name_genre text
);

create table if not exists collections (
	id serial primary key,
	name_collection text,
	year_realease integer
);

create table if not exists genre_artist (
	id serial primary key,
	genre_id integer references genres(id),
	artist_id integer references artists(id)
);

create table if not exists artist_albums (
	id serial primary key,
	artist_id integer references artists(id),
	album_id integer references albums(id)
);

create table if not exists collection_song (
	id serial primary key,
	collection_id integer references collections(id),
	song_id integer references songs(id)
);
