docker stop $(docker ps -a -q) 
docker rm $(docker ps -a -q)
cd /home/ec2-user/
docker-compose pull  # Pull the latest images on EC2
docker-compose up -d  # Run the containers on EC2