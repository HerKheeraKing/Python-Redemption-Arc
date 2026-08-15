
# HEADER: Learning dictionaries & list "nested structure"
# when?: the time i would use a nested structure could be to hold a log that needs 
# ?:to be searchable by the log name and reveal it's contents.


contacts = {
    'number': 4, 
    'students':
        [
            {'name': 'Sarah Holderness', 'email':'sarah@example.com'}, 
            {'name': 'harry Potter', 'email':'harry@example.com'}, 
            {'name': 'Hermione Granger', 'email':'hermione@example.com'},
            {'name': 'Ron Weasley', 'email':'ron@example.com'}
        ]
}

print("Student emails:")
for student in contacts['students']: 
    print(student['email'])

