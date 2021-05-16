## разворачиваем стенд

vagrant ssh ansible

```bash
sudo apt-get install sshpass -y
ansible-galaxy install sleighzy.zookeeper sleighzy.kafka
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i otus.inv kafka.yml
```

---

## Изучаем стенды

vagrant ssh kafka1
cd /opt/kafka_2.13-2.8.0/bin
ls -l
more /etc/zookeeper/zoo.cfg
ls -l /etc/kafka/

---

## check config 

./kafka-configs.sh --bootstrap-server localhost:9092 --describe --all --entity-type brokers
./kafka-configs.sh --bootstrap-server localhost:9092 --describe --all --broker 1 

---

## Create topic

- ./kafka-topics.sh
    - Create, delete, describe, or change a topic.

```bash
./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3 --topic otus
./kafka-topics.sh --list --bootstrap-server localhost:9092
./kafka-configs.sh --bootstrap-server localhost:9092 --describe --all --entity-type topics
./kafka-configs.sh --bootstrap-server localhost:9092 --describe --all --topic otus
./kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic otus

```

---
## Запишем и прочитаем данные из топика

```bash
./kafka-console-producer.sh --topic otus --bootstrap-server localhost:9092
./kafka-console-consumer.sh --topic otus --from-beginning --bootstrap-server localhost:9092
./kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics \
--entity-name otus --add-config delete.retention.ms=1000
```

---

## Меняем настройки топика

```bash
./kafka-configs.sh --bootstrap-server localhost:9092 --describe --all --topic otus | grep retention
./kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics \
--entity-name otus --add-config retention.ms=1000
./kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics \
--entity-name otus --delete-config retention.ms
./kafka-topics.sh --topic otus --bootstrap-server localhost:9092 --alter --partitions 5
```

---

## Проведем нагрузочное тестирование

```bash
./kafka-producer-perf-test.sh --topic otus --num-records 1000 --record-size 1000 \
--throughput -1 --producer.config ../config/producer.properties --print-metrics
```

---

## Самостоятельная работа

- создайте топик mytopic (2 реплики, 2 партиции)
- добавьте в топик несколько сообщений 
- измените retention на удаление
- проверьте что записи исчезают
- измените кол-во партиций на 3
- сделать describe топиков
- результат скопируйте в чат

---

## коtнсольная утилита kafkacat 

vagrant ssh ansible

sudo apt-get install kafkacat
export kafka=192.168.50.12:9092

kafkacat -P -l -b $kafka -t otus 
kafkacat -L -b  $kafka
kafkacat -b $kafka -C -t otus -o beginning 
kafkacat -C -b $kafka -t otus -o -3 -e -p 0
kafkacat -b $kafka -t otus -X list


---