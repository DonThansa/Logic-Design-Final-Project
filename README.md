# Logic-Design-Final-Project:

# Logic-Controlled Board – Digital Systems Project

##	Overview
This project implements a logic-controlled board with dynamic LED behavior based on the last switch turned off. 
It showcases core digital design principles such as finite state machines (FSM), combinational and sequential logic, and 555 timer-based clock circuits.

##	Features
- 4 toggle switches and 4 LEDs (Red, Green, Blue, Yellow)
- Dynamic LED activation sequence based on last switch turned off
- Capless switch behavior (trick mode in Sequence 3)
- Reset logic triggered after timeout and switch-off condition
- Lock/unlock mechanism via switch configuration
- 7-Segment display for sequence indication (practice mode)
- 555 timer used for clock signal generation

##	Components Used
- 13x 74LS32 (OR gates)
- 20x 74LS08 (AND gates)
- 5x 74LS04 (NOT gates)
- 6x 74LS74 (D Flip-Flops)
- 2x LM555 Timers
- LEDs, switches, resistors, capacitors, wires
- 15 breadboards

##	Setup & Usage
1. Clone the repository to get all the files.
2. Open the Quartus_Files folder in *Altera Quartus II*.
3. Simulate the design.
4. Refer to 555_Timer_Circuit/ for clock wiring on breadboard.
5. Assemble the hardware according to Paper_Design/ schematics.

##	Demo Video
Watch the full functionality in action: [YouTube Demo](https://www.youtube.com/watch?v=JfVOs4ASpmE)

##	Key Highlights
- Practical implementation of FSM logic on physical hardware
- Combines logic theory with real-world switching systems
- Clean modular design makes it easy to troubleshoot and extend
- Capless trick feature adds an interactive challenge

##	Cost Optimization
The total estimated cost of components was ~$91.5, sourced from online retailers and bulk orders. 

##	Authors
- Anthony Abdallah
- Ricardo El Otayek
- Elie Hanna
- Ghadi Ammar

##	License
This project is for educational use only. For any reuse or distribution, please cite the authors.
