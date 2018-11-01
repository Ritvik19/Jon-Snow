# imports
import re, wikipedia, time

print('Hello User!')
while True:
    query = input('What do you want to know about?\n')
    search_results = wikipedia.search(query)
    if len(search_results) == 0:
        print('Sorry i cant help you with that')
        cont = 0
    elif search_results[0].lower() == query.lower():
        cont = 1
    else:
        print('Do you mean')
        print(search_results[0], '? (yes/no)')
        if input().lower() == 'yes':
            cont = 1
        else:
            cont = 0

    if cont == 1:
        result = wikipedia.page(search_results[0])
        fetched_content = result.content
        cleaned = re.split(r"=+", fetched_content)
        summary = ' '.join(cleaned[0].split())
        print(summary)
        structured_result = []
        for c in cleaned[1:]:
            structured_result.append(' '.join(c.split()))
        time.sleep(3)
        while True:
            print('Do you want to know more about', query, '? (yes/no)')
            ask_new = input()
            if ask_new.lower() == 'yes':
                new_q = input('How may I help you?')
                i = 0
                flag = 0
                while i < len(structured_result):
                    if new_q.lower() in structured_result[i].lower():
                        j = 0
                        while len(structured_result[i+j].split()) < 10:
                            j += 1
                        print(structured_result[i+j])
                        flag = 1
                        break
                    else:
                        i += 1
                if flag == 0:
                    print('Sorry i cant help you with that')
            else:
                break
    if input('Can I help you with something else? (yes/no)').lower() == 'yes':
        query = input('What do you want to know about?\n')
    else:
        print('Nice to help you.. Thankyou')
        break
