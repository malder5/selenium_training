
def main():
    with open('text', 'r', encoding='utf8')as f:
        for line in f:
            line = line.strip()
            if line[0]=='#':
                continue
            line = line.replace(' = None', '').replace(',', '')
            # print(line)
            print('self.app.page.text_field_fill(\'{}\', Users.{})'.format(line, line))



if __name__ == '__main__':
    main()