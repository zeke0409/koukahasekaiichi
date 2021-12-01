#coding : utf_8
import sys
import re
command_dict = {
    "→": '>',
    "←": '<',
    "工": '+',
    "化": '-',
    "レポート提出": '.',
    "課題爆誕": ',',
    "福井": '[',
    "謙一": ']',
}


def decode_to_bf(cmd):
    head = 0
    bf_code = ""
    while(head < len(cmd)):
        s_flag = 1
        for kouka_cmd, bf_cmd in command_dict.items():
            if(cmd[head:head+len(kouka_cmd)] == kouka_cmd):
                bf_code += bf_cmd
                s_flag = 0
                head = head+len(kouka_cmd)
                break
        if(s_flag):
            print("invalid syntax")
            exit()
    return bf_code


def exe(bf_code):
    code_head = 0
    mem_size = 30000
    mem = [0 for i in range(mem_size)]
    mem_head = 0
    for i in bf_code:
        print(i, end='')
    print()
    while(code_head < len(bf_code)):
        #print(bf_code[code_head])
        if(bf_code[code_head] == '+'):
            mem[mem_head] += 1
            code_head += 1
        elif(bf_code[code_head] == '-'):
            mem[mem_head] -= 1
            code_head += 1
        elif(bf_code[code_head] == '<'):
            mem_head -= 1
            if(mem_head < 0):
                print("runtime error")
                exit()
            code_head += 1
        elif(bf_code[code_head] == '>'):
            mem_head += 1
            if(mem_head >= mem_size):
                print("memory leak")
                exit()
            code_head += 1
        elif(bf_code[code_head] == '.'):
            print(chr(mem[mem_head]), end='')
            code_head += 1
        elif(bf_code[code_head] == ','):
            input = sys.stdin.buffer.read(1)
            input = int(input)
            mem[mem_head] = input
            code_head += 1
        elif(bf_code[code_head] == '['):
            if(mem[mem_head] == 0):
                cnt = 0
                while(1):
                    if(bf_code[code_head] == '['):
                        cnt += 1
                    if(bf_code[code_head] == ']'):
                        cnt -= 1
                        if(cnt == 0):
                            break
                    code_head += 1
                    if(code_head == len(bf_code)):
                        print("runtime error")
                        exit()

            code_head += 1
        elif(bf_code[code_head] == ']'):
            cnt = 0
            while(1):

                if(bf_code[code_head] == ']'):
                    cnt += 1
                if(bf_code[code_head] == '['):
                    cnt -= 1
                    if(cnt == 0):
                        break
                code_head -= 1
                if(code_head == -1):
                    print("runtime error")
                    exit()


if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    with open(path, encoding="utf-8") as f:
        print("decode")
        kouka_code = f.read()
        kouka_code = kouka_code.replace(' ', '')
        kouka_code = kouka_code.replace('\n', '')
        bf_code = decode_to_bf(kouka_code)
        #bf_code = kouka_code
        bf_code = bf_code.replace(' ', '')
        bf_code = bf_code.replace('\n', '')
        exe(bf_code)
