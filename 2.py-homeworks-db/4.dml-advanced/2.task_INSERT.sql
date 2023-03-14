insert into artists
values 
	(1, 'Guns N Roses'),
	(2, 'AC/DC'),
	(3, 'Led Zeppelin'),
	(4, 'The Doors'),
	(5, 'David Bowie'),
	(6, 'Black Sabbath'),
	(7, 'Kiss'),
	(8, 'Metallica');

insert into genres
values 
	(1, 'psychedelic rock'),
	(2, 'glam rock'),
	(3, 'hard rock'),
	(4, 'folk rock'),
	(5, 'heavy metal');

insert into albums
values 
	(1, 'Appetite for Destruction', 1987),
	(2, 'Back in Black', 1980),
	(3, 'Led Zeppelin III', 1970),
	(4, 'The Doors', 1967),
	(5, 'The Rise and Fall of Ziggy Stardust and the Spiders from Mars', 1972),
	(6, 'Paranoid', 1970),
	(7, 'Destroyer', 1976),
	(8, 'Metallica', 1991);

insert into songs
values
	(1, 'Welcome To The Jungle', '4.31', 1),
	(2, 'Paradise City', '6.46', 1),
  	(3, 'Back in Black', '3.51', 2),
  	(4, 'Highway to Hell', '3.27', 2),
  	(5, 'Immigrant Song', '2.27', 3),
  	(6, 'Since Ive Been Loving You', '7.24', 3),
  	(7, 'Break on Through (To the Other Side)', '2.29', 4),
  	(8, 'Light My Fire', '7.10', 4),
  	(9, 'Starman', '4.14', 5),
  	(10, 'Ziggy Stardust', '3.13', 5),
  	(11, 'War Pigs', '7.57', 6),
  	(12, 'Paranoid', '2.52', 6),
  	(13, 'Detroit Rock City', '5.15', 7),
  	(14, 'God Of Thunder', '4.16', 7),
  	(15, 'Enter Sandman', '5.31', 8),
  	(16, 'Sad But True', '5.24', 8);
  
  INSERT INTO songs 
  VALUES (17, 'Nothing Else Matters', '6.28', 8);
  

insert into collections
values 
	(1, 'Classic Rock', 2020),
	(2, 'Old School Of Rock', 2021),
	(3, 'Romantic', 2016),
	(4, 'Energetic', 2018),
	(5, 'True Metall', 2019),
	(6, 'No War', 2022),
	(7, 'Peace', 2022),
	(8, 'My Generation', 1993);

insert into genre_artist(genre_id, artist_id)
values
	(1, 4),
	(1, 5),
	(1, 6),
	(2, 1),
	(3, 1),
	(3, 6),
	(3, 7),
	(3, 8),
	(4, 3),
	(5, 2),
	(5, 6),
	(5, 7),
	(5, 8);

insert into artist_albums(artist_id, album_id)
values
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8);

insert into	collection_song(collection_id, song_id)
values
	(1, 5),
	(1, 6),
	(1, 7),
	(1, 8),
	(1, 9),
	(1, 10),
	(2, 1),
	(2, 2),
	(2, 3),
	(2, 4),
	(2, 5),
	(2, 6),
	(2, 7),
	(2, 8),
	(2, 9),
	(2, 10),
	(2, 11),
	(2, 12),
	(2, 13),
	(2, 14),
	(2, 15),
	(2, 16),
	(3, 6),
	(4, 1),
	(4, 4),
	(4, 15),
	(4, 16),
	(5, 15),
	(5, 16),
	(6, 11),
	(7, 9),
	(8, 5);
