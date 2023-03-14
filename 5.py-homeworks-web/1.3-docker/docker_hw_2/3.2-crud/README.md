Сборка образа

docker build . --tag=image_3.2_crud

Запуск контейнера

docker run -d -p  7998:6060 --name=container_3.2_crud image_3.2_crud