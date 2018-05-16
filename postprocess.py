data = []
para = ''
with open('tobechecked.md') as file:
    for line in file:
        if line.startswith('>'):
            para += line
            para = para.replace('>', '')
            para = para.replace('\n', '')
            if line.strip().endswith('^p'):
                para = para.replace('^p', '')
                para = para + '\n\n'
                data.append(para)
                para = ''

print(data)
with open('target.md', 'w') as file:
    file.writelines(data)
