from django.shortcuts import render ,  HttpResponse , redirect

def block(request):

    try:
        number_input = int(request.POST.get('number_input'))
               
        number_input2 = number_input * 2
        context = {
         'context': range(1, number_input2+1),  
         'positions': range(1, number_input+1),
         'total':number_input,
    }
        return render(request, 'alom.html' , context)
  
    except:
        return render(request, 'alom.html')

 
def re(request):
    if request.method == 'POST':
        input_list = request.POST.getlist('checkbox')
        
        filtered_output = []
     
        last_was_O = False
        for element in input_list:
             
            if element == 'O':
               filtered_output.append(element)
                
               last_was_O = True
              
            elif element == 'X' and last_was_O:
              
               last_was_O = False
               
            else:
              filtered_output.append(element)

        output_list = format_input(filtered_output)
        
        
        
        formatted_content = '\n'.join(output_list)
        
             
        total_count = len(output_list)
        
        formatted_content = f'{total_count}\n{formatted_content}'
        
        response = HttpResponse(formatted_content, content_type='text/plain')

        
        response['Content-Disposition'] = 'attachment; filename="formatted_content.txt"'

        return response
    else:
        return HttpResponse('Method not allowed')
   

def format_input(input_list):
    output_list = []
    if input_list:
        count = 1
        for i in range(0, len(input_list), 2):  # Iterate over input_list with step size 2
            if i + 1 < len(input_list):  # Ensure there are two elements available
                sequence = ''.join(input_list[i:i+2])  # Concatenate two elements
                output_list.append(f'{count}-{sequence}')
                count += 1
    return output_list


def alom(request):
    input_alom = request.POST.get('input_alom')
    int_value = int(input_alom)
    con = {"cont": range(1, int_value + 1)}
    return render(request, 'alom_2.html', con)

def alom_html(request):
    return render(request, 'alom_2.html')
