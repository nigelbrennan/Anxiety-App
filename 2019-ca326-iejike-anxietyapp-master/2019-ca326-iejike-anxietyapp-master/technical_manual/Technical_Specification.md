CA326 Year 3 Project
====================
Technical Specification for Anxiety Application
====================


![](/Markdown_images/appanxiety.PNG)


Nigel Brennan - 14716325
====================
Ikenna Festus – 14383451
====================












##Table of Contents
1. **Introduction**
	1. Overview**
	2.Business Context
	3. Glossary
2. **System Architecture**
	1. High level overview diagram
	2. Client
	3. Therapist
	4. Client user interface
	5.Therapist user interface
	6.Anxiety database
	7.Fitbit hardware and web api
	8.Firebase cloud/database
3. **High-Level Design**
	1. Class diagram
	2. Class skeleton
	3. Sequence Diagram
	4.Context diagram
	5.Data flow diagram
	6.Simple high level diagram
	7.Use case diagram
4. **Problems and Resolutions**
	1. Fitbit Api
	2. Research
	3. Method for identifying pattern in data
	4.Rules engine
5. **Installation Guide**
	1. Requirements
	2. Instructions
	3. Device Instructions
6.**References**

####1. Introduction 
#####1.1 Overview
We are developing a mobile phone app that works with a Fitbit to detect the physiological symptoms of anxiety attacks. We will use Fitbit to track the physiological effects of the stress response and use a rules engine to decipher when a user is experiencing an anxiety attack as opposed to mild stress or exercise etc, it will then:
1) Launch a graphic with helpful advice for the user. 
This advice will be time and location specific i.e. It will not suggest to have a cup of tea if the user is experiencing an anxiety attack at 2am.
2) The app will graph the anxiety attack and all the data around it, which will be shared with the users therapist. This will allow the user and the therapist to see over time the frequency of these attacks and see if the therapy is effective or not. It will also allow the user and therapist to identify triggers for the users anxiety attacks.
 
Need for the system.
In therapy for anxiety the treatments focus on the psychological approach. Psychologists are aware of the physiological effects of anxiety attacks but to date the information has remained unused. At most it’s used in diagnosing someone with an anxiety condition. What we aim to do with our app is to take the decades of research and knowledge about the physiological aspects of the disorder and use it to allow a more effective therapy treatment and allow the patient to maintain their mental health once they leave therapy.
We have met with psychologists and they have agreed that if the system works as planned then it would be a very beneficial tool for therapy.
 
Interaction with other systems:
The app will communicate with a Fitbit on the patients person. It will create an image of the patients experiences in real time and use those to decide whether the user is experiencing an anxiety attack.
 


#####1.2 - Business context.
There are many parties that would be interested in this app. Predominantly it would be sufferers of an anxiety disorder and therapists interested in more comprehensive ways of treating their patients. At the moment there is nothing like this available on the market and with the ever growing rise in diagnosis of anxiety disorders, technology like our app could become commonplace.
Anxiety disorders are the most common mental illness in the world today, affecting 40 million adults in the United States alone. Women have double the risk for anxiety disorders than men do. It can be a debilitating condition affecting all areas of a person's life. According to the NHS U.K, Anxiety is defined as a feeling of unease, such as worry or fear, that can be mild or severe. Everyone has feelings of anxiety at some point in their life – for example, you may feel worried and anxious about sitting an exam, or having a medical test or a job interview. During times like these, feeling anxious can be perfectly normal. However, some people find it hard to control their worries. Their feelings of anxiety are more constant and can often affect their daily lives. During an anxiety attack, people may feel fearful, apprehensive, may feel their heart racing or feel short of breath. It’s clear that some events, emotions, or experiences may cause symptoms of anxiety to begin or may make them worse. These elements are called triggers. Anxiety triggers can be different for each person. But for some people, anxiety attacks can be triggered for no reason at all.
 
#####1.3 - Glossary of terms
 
Firebase: Firebase is a database and cloud service provided to app developers by google.
Triggers: Anything that provokes a memory or impulse.
Sharding database: Sharding a database is the process of essentially turning one database into 2 sub-databases. We did this with for our app with our firebase database.


####2.System Arcitecture.
#####2.1 -High level overview diagram:
![](/Markdown_images/System_Architecture.png)


#####2.2 – Client
This is the user with anxiety who wears the Fitbit on their person.

#####2.3 – Therapist.
This is a licensed and practicing therapist that has the client as a patient as part of therapy.

#####2.4 – Client user interface
There are separate login/register/profile/home etc pages for the therapist and the client. This one uses a sharded database that stores client users(client database). 

#####2.5 – Therapist user interface.
There are separate login/register/profile/home etc pages for the therapist and the client. This one uses a sharded databse on firebase to store only the therapist users details (therapist database).

#####2.6 -Anxiety database.
This is the sharded database that we set up on firebase. It stores graph data that is uploaded to it from the anxiety app. The anxiety app also calls it to show the graph to the user in the view graph section of the app.

#####2.7 -Fitbit sensor and Fitbit web api.
The hardware used as part of this app is a Fitbit charge hr 2. It is wrist fitness tracker with sensors such as heart rate, altimeter, step counter etc.
We had to use the Fitbit web api for this app instead of the hardware api.

#####2.8 - Firebase/cloud/ database
Firebase essentially works as a development platform for the application. A specific console is created within Firebase. The console contains all the necessary data handling features required by the application, also allowing the developers to monitor and manage user activity. 

Firebase authentication deals with all the emails which were used to register an account. A unique user UID is created for each email as a reference. The date of when the email was registered and also last used to sign in to the application can be viewed here. 
The Firebase Real-time database creates a folder with a list of keys. 
For this app we had to shard the database as we have 2 distinct users , the client and the therapist. Sharding a database is the process of essentially turning one database into 2 sub-databases.


####3 .High level design:
Using Draw.io, we created the following diagrams to cover the system architecture and the initial design of the system before we started coding(class diagram, class skeleton and sequence diagram ), describing the relation between functions, modules and the database within the system:

#####3.1 – class diagram
The class diagram is a diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.
![](/Markdown_images/anxiety_app_class_diagram.png)



#####3.2 – class skeleton
A class skeleton is an outline of a class that is used in software engineering. It contains a description of the class's roles, and describes the purposes of the variables and methods, but does not implement them. The class is later implemented from the skeleton.The class skeleton is uploaded on gitlab and available to view. It was not included here because of its size.

#####3.3 Sequence Diagram 
The sequence diagram portrays the order of interactions that take place between the user and the subsystems within the overall system. The subsystems are square boxes, the dotted lines represent the timeline of events and arrows are the passing of information between subsystems. 
![](/Markdown_images/sequence_diagram.png)



#####3.4 -Context Diagram 
In this diagram the application is viewed as one big process. All external entities that interact with the application are included and can be seen as squares around the process. The arrows pointing to and from the circle are the inputs and outputs of data/instructions between the process and its external entities. 
![](/Markdown_images/Context_Diagram.png)










#####3.5 - Data Flow Diagram
This is a depiction of the flow of data through our intended software system. Creating this diagram helped to provide an overview of the data and functionality within the system. External entities are rectangle boxes, processes can be seen as ellipses, data stores are the rectangles with missing sides and data flow is conveyed through arrows. 

![](/Markdown_images/DFD.png)









#####3.6  -Simple high level diagram:
The simple high level diagram Shows the path of the user through the high level design.


![](/Markdown_images/HighLevelDiagram.png)






#####3.7 -Use case diagram:
The use case diagram is a representation of a user's interaction with the system that shows the relationship between the user and the different use cases in which the user is involved.

![](/Markdown_images/UseCaseDiagram.png)







####4 – problems and resolution.

#####4.1 -Fitbit api
Using the Fitbit apis directly with our app is restricted by Fitbit. The company only allows direct use of apis for software installed on the Fitbit device. Newer versions of Fitbit like there smart watches have opened up the apis to use companion apis but we are using a Fitbit charge hr 2.
This meant that we could not get the heart rate data in real time like we would have liked. Instead we get it in 5 minute intervals from the Fitbit web api. This impacted the usefulness of the notification feature but only slightly.

#####4.2 – Research
This was a difficult project to do solid scientific research for as the specific details of anxiety physiological symptoms are largely seen as unimportant. The physiological effects are widely known such as an increased heart rate or hyperventilation but specific measurements were difficult to come across such as the heart rate range and the time span an anxiety attack takes to send a resting heart rate into this heart rate range.
We were planning to use other sensors to give a more robust representation of the users experience to accurately detect if a user is experiencing an anxiety attack, we had researched other physiological symptoms of anxiety and the science behind them to use them to detect an anxiety attack. We were advised my our supervisor Mark Roantree to scale the app back to just the Fitbit as this was becoming too ambitious for a third year project given the time frame that we had.
Research references:
 
Medical Research papers prove that anxiety can be measured by sensors. The most effective way is through a combination of respiration and heart rate monitoring.
“A combination of heart rate monitoring and respiration is apparently the best
proven way to monitor stress. anxieties 2 biggest physical symptoms are
increased heart rate and hyperventilation so these are solid metric for anxiety detection but there are others.
''Standard deviations (SDs) of these  measurements, as  well  as 
other  measurements  of  their  variability,  have been  frequently  used  to characterize respiratory
variability, which seems to be negatively correlated to anxiety''
 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4631393/?fbclid=IwAR0TOvWjGB_7wsy3fUumqtMlPF3qG8YiVoNdkdT4kEqM4dTBCXvNjNTtudg


#####4.3 – Method for identifying pattern in data

We ran into a few problems with this stage of the app.
First of all we were thinking of data mining and predictive algorithm that would allow us to get an algorithm that would be able to identify the pattern we were looking for in the data based on other data and measures we set. Our supervisor Mark Roantree pointed out that the feasibility of this was unrealistic because we hadn’t done data mining module yet and the amount of data required would need to be very large.
Then we went to our python/java lecturer Charles Daly on advice of what technique we should use to identify the specific pattern in the data we were getting from the Fitbit web api. We went to Charlie because our supervisor Mark Roantree was gone for 3 weeks on work I believe and we needed to speak to someone to figure this out. Charlie recommended the fourier transform and explained to us that it’s a mathematical process to find frequencies in data. I researched and looked up code examples of a fourier transform to see how we can incorporate it into our project. The closest I got to finding an implementation similar to what we needed was the use of a fast fourier transform which is used in ppg sensors like the one the Fitbit charge hr 2 uses to find a persons resting heart rate.I met with Charlie a second time(during an exam consultation) to ask again if the fourier transform would work, he said it would but that I could also use a neural network but that would be more work. I emailed my supervisor Mark Roantree to update him on our progress and I let him know that we were going to use the fourier transform to find the pattern in the heart rate data. he emailed me back to say that the fourier transform would not work because it only works on waves. Mark then advised us to create a rule engine to identify the pattern we were looking for.


#####4.4 – The rule engine.
Researching the rule engine it seemed to be perfect for what we needed. We could program in specific rules such as ‘’if the heart rate value from the fitbit is over 115 then fire rule 2’’. 
The rule engine required facts as well, each data object we passed in such as heart rate was a fact.
And the algorithm in the rule engine , usually a rete algorithm but some use a variation on this or there own algorithm, would take the facts and combine them with the rules to create a new object that is then combined with other rules to see if it should fire any actions.
There are rule action libraries you can download and run in an ide such as drools or rulebook. We ran into a problem that none of these libraries could be imported to android studios. Most only worked with eclipse. So we couldn’t get any libraries already available so we tried to create our own rule engine. There is very little instructions of how to do this online but we tried to create one with generics. It had a rule engine core that combined classes of rules that used a rules interface with facts and used java.util.stream to perform functional style operations on elements. Unfortunately we couldn’t get this rules engine to work for our app and we didn’t have the time to debug and make it work so in the end we created a system of methods that data is passed through to simulate a rules engine.





####5. Installation Guide 

#####5.1 Requirements
●	Android Studio 3.3
●	Java 1.8
●	Android Device (5.0.1 or Higher)
●	Internet Connection
●	Fitbit device with heart rate sensor and a Fitbit account details to sign into to give permission to the app to use the data.

The app is only available to be downloaded from Gitlab using a git repository.

#####5.2 Instructions
●	Have a cloned git repository and change to your desired directory.
●	Run the below git command.
●	Git clone https://gitlab.computing.dcu.ie/ejikei2/2019-ca326-iejike-anxietyapp
●	Go to android studio and choose import project .
●	Once the project has finished the build you can connect a physical android phone through a usb and run the app or you can run on the android virtual machine.


#####5.3 Device Instructions 
To run on android virtual machine:
●	Go to tools and select AVD manager.
●	If there is no usable device create a new one.
●	Choose Pie for System Image, 
●	Android 9.0 is the Target.
●	Select portrait for the orientation and then Finish.
●	You have now created a new device. Select the “Run App” option at the top of the platform under “Run” or the green arrow to the right of it and select your new device.
●	Make sure you have an internet connection.

Physical android phone instructions:
●	Go into settings on device and select “About phone” and go to “Developer options” and enable USB debugging.
●	Always allow access on this device to the computer you are using.
●	Select the “Run App” option on android studio and subsequently select “Run” and then choose user running device.
●	Select your device.


####6. References



