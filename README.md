# Welcome to TriForce's Wiki Page
_Members:_ Anh Pham, Brent Carey, Hieu Tran 

Mission: This page will be used to document our group's progress through the Robots course. It will follow the building and programming of our robot and give an overview of tasks we complete in class.

## System Installation and Documentation (17/3/2015)

On the first day of this class, we set up our Raspberry Pi and then had our very first experience with Python programming language. After setting up all the connection by plugging in the monitor, mouse, keyboard, Ethernet and power cables, we installed a fresh Operating System, which called Raspbian, into the Raspberry Pi. By holding shift key while turning on the Pi, we entered the OS installation screen. We can install a new one from there by following the instruction.

![Installing OS](https://farm1.staticflickr.com/737/22891869182_787c6a190c_b.jpg)

The installation is pretty easy and straightforward but it will take a while.

![Waiting time](https://farm1.staticflickr.com/565/22905305865_d9035ec067_b.jpg)

When the installation was done we logged in the Raspberry Pi with username "pi" and password "raspberry". You can enter graphical GUI of your Pi like you are Windows by command "startx" but we prefered using command lines GUI. It is recommended to update and upgrade your Pi. With the internet cable already plugged in, we can do that by entering "sudo apt-get update" and "sudo apt-get upgrade" into the Terminal. This process also took a while.

Going to make a Python file, we simply used "nano hello.py" to create and edit a new Python file named "hello". In this session, we wrote " print("Hello World!") " into the file then saved. In order to compile and run the file, we entered "sudo python3 hello.py" into Terminal and then it shown the line "Hello World!" on the screen. That is how we made our very first Python program.

## Python GPIO Exercise (19/3/2015)

Task: The main purpose of today's exercise was to get familiar with Raspberry Pi GPIO (general purpose input/output) pins. Our first step was to find a way to connect our laptop to the raspberrypi. While there are several ways to do this, we connected them through ethernet and then by using ssh in our terminal. We then passed our premade python programs to raspberrypi and prepared to run them. After we analysed the python programs (to see what the did how they functioned) we set up a basic LED circuit through the GPIO pins on the raspberrypi. Once the circuit was prepared we began experimenting with the program, making simple modifications like changing how often the LED blinked.

![GPIO](https://farm1.staticflickr.com/640/22916578821_cbbac538b7.jpg)

## Robot Assembly (19/03/2015)

![Robot Shape](https://farm1.staticflickr.com/693/22487091787_c63e7c263c.jpg)

We also started assembling the robot we will use and program later in the course. We connected the motors to the base-board and added two tires (to the motors) and one free-rotating wheel.

![Finished Assembly](https://farm6.staticflickr.com/5648/22905453125_0fb3b636c7.jpg)

## PWM - Pulse Width Modulation (24/03/2015)

PWM is a method of controlling our robot, or more specifically our robot's motor. PWM has many different applications, two of which we have already had the opportunity to explore in class. The first way we used PWM was the dimming and brightening of an LED giving it a breathing effect. Although this experiment didn't really benefit our robot, it introduced us to some of the key concepts of PWM of and how to use them in a python program. The second way we applied PWM was in the controlling of our robot's motors. By adjusting the duty cycle we were able to gradually speed up and slow down the rotation of our motor rather than having them full speed or off.

Below you can see the main idea of PWM. With a higher percent duty cycle the speed of the motor (or brightness of the LED) is greater. With a smaller percent value the motor rotates slower (and LED is dimmer). Using PWM is not only a great way to control power but is also very efficient with the way it is used.

![PWM](https://farm1.staticflickr.com/611/22717524920_d6e39a511c.jpg)

## Control the Robot wirelessly (26/03/2015)

![PiWifi](https://farm6.staticflickr.com/5658/22513366919_ee4a0ef721.jpg)

In this class we tried to connect to the robot wirelessly rather than always having the internet cable plugged into the robot. First, we need to set up a wifi connection between our laptop and the Raspberry Pi, it can be either from mobile phone or laptop. We chose hotspot from our phone as the wifi connection. The laptop can connect to this network without any problem but it was not that easy with the Raspberry Pi. We need to plug in the WiPi, which is a wifi adapter made for the Raspberry Pi. After that, we install wicd-curses, a software interface that list out all the wifi connections near you and help you connect to one of them, by using command "sudo apt-get install wicd-curses". To start the program, we entered "sudo wicd-curses" then the interface appeared on the screen.

By choosing the same network with the laptop we did before, these two systems were in the same local network. Then we can use ssh service to remotely control the Raspberry Pi from our laptop. From now on we can do not need to bother with monitor, keyboard, mouse or internet cable anymore. We can now try to make our robot run on the floor that we could not do it last session due to all the cable connected to the Pi.
Control Robot Manually

## Control Robot Manually
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

We read a lot from python documentation and conclude to use curses library in controlling robot manually. We read also from many people who had experienced in some kind like our robot and follow them a little bit.
Many functions in this library is helpful for us to work with to control inputs from users. 

Firstly, we successfully did it with curses but it did not smoothly as we expected. So, we changed the time sleep values to small like milliseconds, it worked. After that, we found a bug that the robot still doing actions even when we did not press the key down. We researched a lot and knew that the follow of input was being in a queue and still act until the last one done. Then we have to edit to the code and place one more function called refresh to make it as we want.

So after 2-3 days working with curses we have been able to control robot manually through keyboard. Those days was very stress with all the thing we need to figure out. But we was still united and worked hard. So proud of our team.

Also, at this time, we were trying to find out some way to fixed all the stuff on robot. I even took it home and tried to find some way. Hope that I will have a solution soon.

![Messy Stuff At Home](https://farm1.staticflickr.com/620/22513383749_10bb8d74ae.jpg)

To conclude, the materials we need is available here. We googled much and also do experiments much. Finally, we are done with curses. Moving into another more interesting adventure soon.

## Interrupter Sensor (21/04/2015)

Today we began working towards self automating our robot. In order to do this we need to create some sort of system that is able to track and determine our robot's movement without human interaction. This requires some form of sensor, which for our project will be an interrupter sensor. Using the interrupter sensor we plan to implement a way to track the rotation of the robot's wheels using the holes on the wheel's axle. From here we will be able to measure and determine the distance our robot travels.

![Interrupter Sensor](https://farm1.staticflickr.com/750/22892067882_cbef7bd4f4.jpg)
 
## Calibration (28/04/2015)

![Calibration](https://farm6.staticflickr.com/5627/22487140497_664c9bdaeb.jpg)

Once our sensors were installed we began the calibration process. We started with finding the wheel's turning ratio relative to each other, found by testing distances from a starting position after a set amount of wheel rotation time. We then adjusted the sleep time for each respective wheel be on that calculated ratio. After calibration tests were complete our robot was able to travel in a relatively straight line even with changing variables. To to increase our accuracy more you we increase the amount of sleep time, making our robot travel in short unnoticeable bursts. We also used this strategy when changing direction (or angle for turning).

 
## Self Navigation (06/05/2015)

For the self navigation aspect of the robot we implemented a file which our automation programs reads. This file contains the parameters for the intended journey of the robot. In the read file each action takes on three parameters. the first parameter tells whether the robot will be moving in a single direction (forward or reverse) or making a turn (left or right). The second parameter determines if the single direction motion is forward or backwards or is the action is a turn, clockwise or counter clockwise turn. The last parameter decides the amount of the action. For the turning aspect, it defines the angle of the turn and for the single direction motion, the distance the robot travels.

## 3D Printing (07/05/2015)

![Triforce_3D_Model](https://farm6.staticflickr.com/5742/22892077602_82edac1a20.jpg)

For the 3D printing our group decided to make a 3D Triforce, since our team name is Triforce. We used the 3D design program 3D Max to create the object and then proceeded to print it on one of Metropolia's 3D printers. Due because of the design we had to print the object in two separate pieces and hot-glue them together for the desired object.

## Course Conclusion and Competition (13/05/2015)

Today was the last day of the Robots Course. We started by presenting the posters we prepared to both the Finnish and the International groups. The poster was just a basic overview of our robot's design and functionality. It covered three main points, hardware, digital systems and software we used in the robot. After all the posters were presented the main event started.

We then started the robot competition. The different teams had about an hour to prepare their robot to navigate a give tack on its own (below you can see a crude map of the track where we made measurements to determine the movement parameters). I think our system of having a read file with parameter made the testing of the track very efficient and easy to do. Our team ended up coming in first place for the automated portion of the competition. After that there was manually controlled aspect of the competition. Our robot didn't do so well in this category, mostly because it was built for accuracy and not speed.

Overall the day went very well and our group felt very accomplished that all the hours of preparation paid off. We all learned so much along the way and feel that this course gave us knowledge and skills that we can use for the rest of our days at Metropolia.
