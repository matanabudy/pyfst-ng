import sys

import yaml

def generate_from_template(buffer,types):
    generateds = []
    for t in types['types']:
        buffer_t = buffer
        for k in t:
           buffer_t = buffer_t.replace('{{'+k+'}}', t[k])
        generateds.append(buffer_t)
    return generateds

if __name__ == '__main__':
    tpl_path = sys.argv[1]
    yml_path = sys.argv[2]
    out_path = sys.argv[3]
    stream = open(yml_path, 'r')
    types = yaml.load(stream)
    buffer = ''
    is_in_template = False
    with open(out_path,'w') as out_f:
        with open(tpl_path,'r') as tpl:
            for l in tpl.readlines():
                if l.strip() == '{{#types}}':
                    is_in_template = True
                    buffer = ''
                elif l.strip() == '{{/types}}':  
                    generateds = generate_from_template(buffer,types)
                    for g in generateds:
                        out_f.write(g)
                    is_in_template = False
                elif is_in_template == True:
                    buffer = buffer + l
                else:
                    out_f.write(l)
