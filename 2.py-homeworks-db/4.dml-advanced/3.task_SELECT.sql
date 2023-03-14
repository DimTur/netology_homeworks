--количество исполнителей в каждом жанре;
SELECT name_genre, COUNT(nickname) FROM artists a
JOIN genre_artist ga ON a.id = ga.artist_id
JOIN genres g ON ga.genre_id = g.id
GROUP BY name_genre;

--количество треков, вошедших в альбомы 1970-1972 годов;
 SELECT year_realease, COUNT(name_song) FROM albums a
 JOIN songs s  ON a.id = s.album_id 
 WHERE a.year_realease >= 1970 AND a.year_realease <= 1972
 GROUP BY year_realease;

--средняя продолжительность треков по каждому альбому;
 SELECT title, AVG(duration) FROM albums a 
 JOIN songs s ON a.id = s.album_id 
 GROUP BY title;
 
--все исполнители, которые не выпустили альбомы в 1970 году;
 SELECT nickname, year_realease FROM albums a 
 JOIN artist_albums aa ON a.id = aa.album_id
 JOIN artists a2 ON aa.artist_id = a2.id 
 WHERE a.year_realease != 1970;
 
--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
SELECT name_collection FROM collections c
JOIN collection_song cs ON c.id = cs.collection_id 
JOIN songs s ON cs.song_id = s.id
JOIN albums a ON s.album_id = a.id
JOIN artist_albums aa ON a.id = aa.album_id 
JOIN artists a2 ON aa.artist_id = a2.id 
WHERE a2.nickname LIKE 'The Doors';

--название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT title FROM albums a 
JOIN artist_albums aa ON a.id = aa.album_id
JOIN artists a2 ON aa.artist_id = a2.id 
JOIN genre_artist ga ON a2.id = ga.artist_id 
GROUP BY a2.nickname, a.title 
HAVING count(ga.genre_id) > 1;

--наименование треков, которые не входят в сборники;
SELECT name_song FROM songs s 
LEFT JOIN collection_song cs ON s.id = cs.song_id 
WHERE cs.song_id IS NULL;

--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
SELECT nickname, duration FROM artists a
JOIN artist_albums aa ON a.id = aa.artist_id 
JOIN albums a2 ON aa.album_id = a2.id 
JOIN songs s ON	a2.id = s.album_id 
WHERE s.duration IN (SELECT min(duration) FROM songs);

--название альбомов, содержащих наименьшее количество треков.
SELECT a.title, count_song FROM (SELECT s2.album_id, count(s2.album_id) count_song FROM songs s2 GROUP BY s2.album_id) cs
JOIN albums a ON a.id = cs.album_id
GROUP BY a.title, cs.count_song
HAVING count_song = (SELECT min(mycount) FROM (SELECT album_id, count(album_id) mycount FROM songs GROUP BY album_id) AS MYMIN); 
