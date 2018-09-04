def compute_final (marks):
    '''(str) ->float
    extracts the marks and the corresponding weight from a string and computes the final mark.
    >>> compute_final ("[100, 5], [80, 10], [70 , 5], [60 , 30], [70, 20], [0, 10], [60, 20]")
    60.5
    >>> compute_final("[90, 5], [100, 10], [50 , 5], [60 , 30], [70, 20], [50, 10], [70, 20]")
    68.0
    '''
    # remove [] from the string
    marks = marks.replace('[', "")
    marks = marks.replace(']', "")
    #convert the string into a list 
    marks_list = marks.split(sep = ',')
    #compute the final mark
    final = 0
    for index in range (0, len(marks_list), 2):
        final += float(marks_list[index])* float(marks_list[index+1]) /100
    return final

def read_a_file(name):
    ''' (text)-> list
    reads the file into a list.
    REQ: name is the name of an existing file in the same path as the program
    >>> read_a_file("grades.txt")
    [['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]]

    '''
# open the file for reading
    input_file_handle = open(name, "r")
    # read a line at a time from the file
    transcript = []
    for line in input_file_handle:
        if (not line.startswith("-")):
            # create a list of student info
            student_info = line.split(sep=', ', maxsplit=4)  
            # compute the final mark for each course
            student_info [4] = compute_final(student_info[4])
            # keep this student info in another list
            transcript.append(student_info)

   # close the file
    input_file_handle.close()
    return transcript

def make_transcript (mark_list, name):
    ''' (list, str) -> None
    creates a transcript for each student and write it to a file with the given name. 
    REQ: None of the inputs are null
    >>> make_transcript ([['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]], "transcript_1.txt")
    '''
    while (mark_list !=[]):      
        # get one student
        studentID = mark_list[0][0]
        # make a list of all the marks for this studentID
        info = get_all_marks(mark_list, studentID)
        # write it to the file
        write_to_file(name, info)
        #remove it from the original list
        mark_list = remove_marks(mark_list, studentID)
        

 
def get_all_marks (marks_list, studentID):
    '''(list, str) ->list
    finds all marks for the given studentID
    REQ: mark_list, studentID are not empty
    >>> get_all_marks ([['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]], '100')
    [['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]]

    >>> get_all_marks ([['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]], '200')
    [['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8]]
    '''
    # create an empty list to keep student information
    info = []
    # search the list for a data corresponding to studentID
    for index in range(0, len(marks_list)):
        # if data was found
        if (marks_list[index][0] == studentID):
            # add it to the info list
            info.append(marks_list[index])
    # return the list containing student information
    return info

def write_to_file(name, info):
    '''(str, list) -> None
    writes the given info to a file with the given name
    REQ: None of the inputs are null
    '''
    # open a file for writing
    output_file_handle = open(name, "w")  
    # write student name and ID and draw a line underneath
    output_file_handle.write("StudentName: " + info[0][1] + "\t" + "Student No: " + info[0][0]+"\n")
    # draw a line of length 60
    output_file_handle.write("-" * 60 +"\n")
    marks_total = 0
    marks_no = 0
    # write all the other marks, if any, for the student.
    for index in range(0, len(info)):
        output_file_handle.write(info[index][2] + "\t" + info[index][3]+"\t" + str(info[index][4])+ "\n")
        # keep track of the total of the marks for computing an average
        marks_total += info[index][4]
        # keep track of the number of marks for computing an average        
        marks_no += 1         
    # draw a line of length 60
    output_file_handle.write("-" * 60 +"\n")  
    # write the average
    output_file_handle.write("Average = " + str(marks_total/marks_no)+"\n\n\n")  
    # close the file
    output_file_handle.close()

def remove_marks(mark_list, studentID):
    '''(list, str)->list
    removes all the data about the student with student no = studentID
    REQ: None of the inputs are null
    >>> remove_marks([['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0]], '100')
    [['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8]]
 
    >>> remove_marks([['100', 'John', 'CSCA08', 'Introduction to Computer Science I', 60.5], ['100', 'John', 'CSCA48', 'Introduction to Computer Science II', 72.0], ['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8]], '100')
    [['200', 'Jane', 'CSCA08', 'Introduction to Computer Science I', 69.8]]
    '''    
    # check each item in the list
    for items in mark_list:
        # to find the item related to the given studentID
        if(items[0] == studentID):
            # remove the found item
            mark_list.remove(items)
    return mark_list


if (__name__ == "__main__"):
    # read the file
    mark_list = read_a_file("grades_0.txt")
    # prepare the transcript
    make_transcript(mark_list, "transcript_1.txt")
