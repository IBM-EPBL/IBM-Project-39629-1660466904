### Final Deliverables - Code Ready to Deploy

- Build a News Tracker application using Flask and IBM Cloud products (DB2,Watson,Object Storage,Container Registry,Kubernetes)
- The Goal of the Project is to provide customized News Feed per User as per their perferences.
- app.py prepare the app folder as a whole application
- Important files - views.py, request.py and base.html which organize the flow of the application and make various API calls and dynamically contruct the webpages as per the feed
- The Whole Project made Platform independent to deploy as a Microservice application
- with help of Docker the Application is converted to ImageFile (done by DockerFile)
- Container Registry of IBM helps to host the Image Globally
- IBM Kubernetes cloud services helps to implement worker and client nodes to organizes request as mircoservices
- IBM Watson give 30 words of news content of prefer genre.
- IBM Object Storage gives a space and convenient way of organizing bigger files.
- IBM DB2 stores the User Login credentials and User Preferences. 