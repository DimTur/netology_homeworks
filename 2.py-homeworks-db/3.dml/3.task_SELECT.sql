--название и год выхода альбомов, вышедших в 1970 году;
select title, year_realease from albums
where year_realease = 1970;

--название и продолжительность самого длительного трека;
select name_song, duration from songs
where duration = (select max(duration) from songs);

--название треков, продолжительность которых не менее 3,5 минуты;
select name_song from songs
where duration >= '3:30';

--названия сборников, вышедших в период с 2018 по 2020 год включительно;
select name_collection from collections
where year_realease between  2018 and 2020

--исполнители, чье имя состоит из 1 слова;
select nickname from artists
where nickname not like '%% %%';

--название треков, которые содержат слово "мой"/"my".
select name_song from songs
where name_song like '%My%';