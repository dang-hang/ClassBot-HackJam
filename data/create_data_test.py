import json

with open('data.json') as f:
    data = json.load(f)
data_list = []
data = {'course':'CEN 4020',
        "title": "Assignment 1",
        'description': 'Assignment 1 for CEN class, a written Feasibility Study and Plan (group assignment) and Survey 1 (individual assignment)',
        'content': "The deliverables for Assignment 1 are:\
A written Feasibility Study and Plan (group assignment)\
Survey 1 (individual assignment)\
Feasibility Report\
The exact form of the feasibility study is up to you. The length of the report is likely to be between five and ten pages. It should include the following:\
The client for whom the work will be done.\
List of team members and email addresses.\
A statement of the task to be undertaken. A preliminary requirements analysis.\
Suggested deliverables.\
Process to be followed, e.g., modified waterfall model, iterative refinement, incremental development, phased development, etc.\
Outline plan, showing principal activities and milestones.\
Visibility plan.  How will you keep in contact with the client and report progress?  How will you communicate among your team?\
Discussion of business considerations (see the Projects pages on the Web site). \
Risk analysis. What can go wrong? What is your fallback plan?\
Probable technical requirements"}
data_list.append(data)
data = {
    "course": "CEN 4020",
    "title": "Syllabus",
    "description": "Complete guide and syllabus for the CEN 4020 course, outlining the course structure, topics covered, grading scheme, and important dates.",
    "content": "Welcome to CEN 4020 - Software Engineering. This course aims to provide a comprehensive understanding of software development processes, methodologies, and tools. The syllabus includes course objectives, weekly breakdown of topics, assessment methods, grading policy, office hours, and contact information for the instructor. Students are expected to actively participate in class discussions, complete all assignments on time, and engage with the course materials to ensure a successful learning experience."
}
data_list.append(data)
data = {
    "course": "CEN 4020",
    "title": "Assignment 2 - Design Patterns",
    "description": "Second assignment focusing on the application of software design patterns.",
    "content": "Choose three design patterns from the course materials and provide a detailed analysis of each, including their usage scenarios, advantages, and disadvantages. For one of the chosen patterns, create a small code example demonstrating its application. Your submission should be clear, well-written, and not exceed 6 pages."
}
data_list.append(data)
data = {
    "course": "CEN 4020",
    "title": "Assignment 3 - Testing and Quality Assurance",
    "description": "Third assignment focusing on software testing methodologies and quality assurance practices.",
    "content": "Discuss various software testing methodologies and quality assurance practices. Provide examples of how these methodologies and practices can be applied in software development to ensure a high-quality product. Highlight any challenges and potential solutions. The report should be comprehensive, well-referenced, and between 8-10 pages."
}
data_list.append(data)
data = {
    "course": "CEN 4020",
    "title": "Assignment 4 - Group Project Proposal",
    "description": "Fourth assignment requiring groups to submit a proposal for their final project.",
    "content": "In groups of 4-5, choose a software project that you will develop as your final project. Submit a proposal outlining the problem statement, objectives, scope, potential challenges, and a preliminary list of tasks and responsibilities. The proposal should be detailed, well-organized, and not exceed 5 pages."
}
data_list.append(data)
data = {
    "course": "CEN 4020",
    "title": "Assignment 5 - Code Review and Maintenance",
    "description": "Fifth assignment focusing on the practices of code review and software maintenance.",
    "content": "Select an open-source software project, and conduct a code review of a particular module or component. Discuss the quality of the code, any potential improvements, and maintenance strategies. Provide specific examples and recommendations. Your report should be clear, concise, and between 7-9 pages."
}
data_list.append(data)
for data in data_list:
    metadata = {}
    metadata['course'] = data['course']
    metadata['title'] = data['title']
    metadata['description'] = data['description']
    del data['course']
    del data['title']
    del data['description']
    data['metadata'] = metadata


with open('data.json', 'w') as f:
    json.dump(data_list, f, indent=4)
