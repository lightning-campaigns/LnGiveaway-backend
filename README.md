# LnGiveaway-backend


## Start App
```
chmod -R 765 entrypoint.sh 
```
```
docker-compose up -d 
```

** Below endpoints will be exposed on port 6000
### Get Campaigns
```bash
curl --location 'http://127.0.0.1:6000/campaign'
```
### Create Campaigns
```bash
curl --location 'http://127.0.0.1:6000/campaign' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Test2"
}'
```