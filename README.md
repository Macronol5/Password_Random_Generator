# Random_Password_Generator
This Program is a flask which will generator a Password based on user need like alpha, number or special symbol etc. It has a Docker which will create a image in all which can be Deployed in hub

1.Create a app.py file and template/index.html
2.Run the command to make Docker Image 


docker build -t password-generator .
docker run -p 5000:5000 password-generator

3.This will create a Docker image 
You can see by $Docker images

4.Now open in localhost:5000 
5.Select type of Password to be Generated

Thank you
