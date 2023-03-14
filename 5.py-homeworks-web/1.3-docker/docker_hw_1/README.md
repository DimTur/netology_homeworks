Сборка образа

docker build . --tag=hw_nginx

Запуск контейнера

docker run -d -p 7998:6060 hw_nginx