

def count_ids():
    """
    practice how to use the split function
    """
    
    members = ['id321', 'id3', 'id123']
    messages = ['@id321,id3 wow good job.  I liked how you solved it id3', 'no comment lol', 'id321 you are great', '@id3 good job better than id123']

    message_id_count = {}
    
    for message in messages:
        
        split_message = message.split(' ')
        
        print(split_message)
        for string in split_message:
            if len(string) > 1 and string[0] == '@':
                unique_ids = string[1::].split(',')
                for _id in unique_ids:
                    message_id_count[_id] = 1 + message_id_count.get(_id, 0)
        print(message_id_count)
            
            
def print_each_string_except_i():
    """
    practice string splitting
    """
    
    string = 'michael'
    
    for i in range(len(string)):        
        new_string = string[0:i:] + string[i+1:]   #ichael, mchael, mihael, micael, michel, michal, michae
        print('\n' +new_string)
        print('removed ' + string[i])



    
# count_ids()
print_each_string_except_i()