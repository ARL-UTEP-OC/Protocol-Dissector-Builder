from jinja2 import Environment, FileSystemLoader

class Dissector_Generator():
   
    dissector = {}
  
    



    def __init__(self):
      
        self.file_loader = FileSystemLoader('src/main/python/Backend/Dissector/templates')
        self.env = Environment(loader=self.file_loader)
        self.template = self.env.get_template('dissector.lua')
       
    
    def parse_json(self,JSON):
        self.dissector['name'] = JSON['name']
        self.dissector['description'] = JSON['description']
        self.dissector['subtree_name'] = JSON['change_protocol']
        self.dissector['port_type'] = JSON['protocol'] #NEED TO ADD THIS FIELD
        self.dissector['port_number'] = JSON['src_port']
        self.dissector['fields'] = []

        value = JSON['fields']['start_field']['next_field']
        print(value)

        while value is not 'end_field':
            temp = {}
            temp['name'] = JSON['fields'][value]['name']
            temp['type'] = JSON['fields'][value]['type']
            temp['filter'] = JSON['fields'][value]['filter']
            temp['label'] = JSON['fields'][value]['label']
            temp['size'] = JSON['fields'][value]['size']
            temp['display_type'] = JSON['fields'][value]['display_type']
            self.dissector['fields'].append(temp)
            value = JSON['fields'][value]['next_field']
        
    def mock_run(self,workspace):
        message_length = {}
        message_length['name'] = "message_length"
        message_length['type'] = "int32"
        message_length['filter'] = "mess"
        message_length['label'] = "length"
        message_length['size'] = 4
        message_length['display_type'] = "DEC"
        message_length['next_field'] = 'request'

        request = {}
        request['name'] = "request_id"
        request['type'] = "int32"
        request['filter'] = "request_id"
        request['label'] = "reqID"
        request['size'] = 4
        request['display_type'] = "DEC"
        request['next_field'] = 'end_field'

        JSON = {}
        JSON['name'] = "MyDNS"
        JSON['description'] = "MyDNS"
        JSON['protocol'] = "UDP"
        JSON['change_protocol'] = "MyDNS"
        JSON['src_port'] = "74400"
        JSON['fields'] ={}
        JSON['fields']['start_field']= {}
        JSON['fields']['start_field']['next_field'] = 'message_length'
        JSON['fields']['message_length'] = message_length
        JSON['fields']['request'] = request


        self.parse_json(JSON)
        self.export_lua(workspace)
            

    def export_lua(self,workspace):

        output = self.template.render(dis = self.dissector)
        print(output)
        if workspace is None:
            f = open("{}.lua".format(self.dissector['name']) ,"w+")
        else:
            f = open("{}/Lua/{}.lua".format(workspace,self.dissector['name']) ,"w+")
        f.write(output)
        f.close()

if __name__ == "__main__":

    message_length = {}
    message_length['name'] = "message_length"
    message_length['type'] = "int32"
    message_length['filter'] = "mess"
    message_length['label'] = "length"
    message_length['size'] = 4
    message_length['display_type'] = "DEC"
    message_length['next_field'] = 'request'

    request = {}
    request['name'] = "request_id"
    request['type'] = "int32"
    request['filter'] = "request_id"
    request['label'] = "reqID"
    request['size'] = 4
    request['display_type'] = "DEC"
    request['next_field'] = 'end_field'

    JSON = {}
    JSON['name'] = "ddd"
    JSON['description'] = "TST"
    JSON['protocol'] = "TCP"
    JSON['change_protocol'] = "TEST"
    JSON['src_port'] = "800"
    JSON['fields'] ={}
    JSON['fields']['start_field']= {}
    JSON['fields']['start_field']['next_field'] = 'message_length'
    JSON['fields']['message_length'] = message_length
    JSON['fields']['request'] = request

   


   
    c.parse_json(JSON)
    c.export_lua(None)