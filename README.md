# Python_Implementation-for-7_Intelligent_agents
Intelligent Agents Simulation

Course: Artificial Intelligence
Level: 3rd Year Computer Science
Language: Python

This project implements and simulates different types of Intelligent Agents in a simple vacuum cleaner environment. The purpose is to demonstrate how various AI agents perceive their environment, make decisions, and perform actions to achieve goals or maximize performance.

Project Overview

In Artificial Intelligence, an agent is an entity that perceives its environment through sensors and acts upon that environment using actuators.

This project simulates a vacuum cleaner world, where rooms may be Clean or Dirty, and an agent must decide how to act based on different AI strategies.

The program allows the user to select different agent types, observe their behavior, and see how they interact with the environment.

 Implemented Agent Types
1. Simple Reflex Agent

A Simple Reflex Agent makes decisions based only on the current percept.

Rules example:

If the current room is Dirty → SUCK

If the room is Clean → MOVE

It does not remember previous states.

2. Agent and Environment Simulation

This simulation demonstrates how an agent interacts with the environment step by step.

Process:

Agent observes the environment

Agent performs an action

Environment updates

The process repeats

3. Rational Agent

A Rational Agent chooses actions that maximize performance.

Performance rules used:

Cleaning a room → +10 points

Moving between rooms → −1 point

The objective is to achieve the highest performance score.

4. Model-Based Agent

A Model-Based Agent maintains an internal memory (model) of the environment.

This allows the agent to:

Remember previously visited rooms

Avoid unnecessary actions

Make better decisions

5. Goal-Based Agent

A Goal-Based Agent acts to achieve a specific goal.

Goal in this simulation:

Ensure that all rooms become clean

The agent continues acting until the goal state is reached.

6. Utility-Based Agent

A Utility-Based Agent selects actions based on utility values.

Example utilities:

Cleaning a room → +10 utility

Moving between rooms → −2 utility

The agent selects actions that maximize total utility.

7. Learning Agent

A Learning Agent improves its decisions over time by recording past experiences.

The agent:

Stores previous actions

Evaluates performance

Improves behavior in future decisions
