# Neo4j_test

Get familiar with Neo4j and Cypher Query Language

This is a testing project for practicing Neo4j with Python

To run this project, please have these requiremnets installed
    - Neo4j: JDK 17.x and Neo4j 5.4.0 with APOC library
    - Python: Python 3.10 with py2neo 2021.2.3 and pandas


1. Start Neo4j server
    - For MacOS or Linux, use command line "neo4j start"
    - For Windows, use command line "neo4j.bat console"
    
    Open a browser with "http://localhost:7474", log in neo4j browser

2. Run test.py
    - It will create some nodes and simple relations between them
    - Now the database is ready for operations


Update on Nov 16th:
    - Py2neo has come to an end. This project may migrate to a new one with a new library "neomodel"