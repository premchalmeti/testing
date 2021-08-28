# What is CLISH (Command Line Interface SHell)?
* A modular framework for implementing a CISCO-like CLI on a *NIX system.
* Arbitary command menus and actions can be defined using XML files.
* This software handles the user interaction, and forks the appropriate system commands to perform any actions.

## Background
The CISCO-like CLI has become a de-facto standard in the domain of network devices. It is a much more restricted interface than traditional *NIX shells, hence is simpler to use and inherently more secure. 

As more devices move to using an embedded *NIX operating systems, a simple, scalable means of producing such a CLI becomes valuable.


>MORE: http://clish.sourceforge.net/

>ROUTER commands: https://www.geeksforgeeks.org/cisco-router-basic-commands/


## About this repo

The `clish_testkit` framework provides suite of utilities to implement any arbitary test case for CLISH modules and CLISH commands
