#Zero shot prompting 
asking AI to do a task without giving any examples
adv: good for simpler tasks
-less tokens used

#Few shot prompting 
giving AI few examples before asking the actual question
adv: better for consistency and formatting
-more tokens used

its like teaching the AI first how to execute the task you are going to assign to it 
like teaching: 
- what formats to use  
- how to interpret the task

#respond in only json format prompt:

Extract information from the text.

Respond ONLY in JSON with these fields:

{
  "name": "",
  "age": 0,
  "city": ""
}

Text:
John is 25 years old and lives in London.

output would be : 
{
  "name": "John",
  "age": 25,
  "city": "London"
}
