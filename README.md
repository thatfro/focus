# home smart home
Started as a school project, this is going to be developed further.

## Idea
The idea is to create a system to control your home via a Raspberry Pi and a smartphone or tablet. The goal is to offer a cheap and easy to setup solution for everyone.
For now it's only possible to control a modified, fully automatic coffee machine directly hooked to the Raspi.

## Goals

I am now working on a transportation mechanism that allows the user to pour coffe into 5 cups standing on a 3D-printed, movable board.
The next step is to get away from the coffee machine and control something else (e.g. blinds, light, heating, ...), still being able to control the coffee machine as well.

## Structure
* Server (files for the Raspberry Pi)
  * control.py (running on Raspi)
  * templates (directory for rendering templates)
* Client (directory for the smarthpone)
  * coffee (cordova directory)
    * www (actual development directory)

## Achievements
* The project has been successfull as a school project and i want to go further.
* The project is accepted at *Schweizer Jugend forscht - nationaler Wettbewerb* (http://sjf.ch/nationaler-wettbewerb-2015/), a swiss competition for students with their (mostly school) projects and is going to be presented public at May 1st and May 2nd 2015 in Davos, Switzerland.
