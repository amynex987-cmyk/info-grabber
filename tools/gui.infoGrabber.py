try:
    from customtkinter import *
    import requests
    import cloudscraper
    import socket
    from bs4 import BeautifulSoup as bs

except Exception:
    input('some required libraries are missing. would you like install them now? (y/n)\n').strip().lower()
    Q = input('').strip().lower()
    
    if Q == 'y':
        try:
                    try:
                        import os
                        os.system('pip install requests rich cloudscraper beautifulsoup4 pyfiglet')
                    except Exception:
                        print('error.')
                    
        except Exception:
            import os
            os.system('python -m pip install requests rich cloudscraper beautifulsoup4 pyfiglet')
    elif Q == 'n':
        print('ok')
        exit()
    
    else:
        print('Syntax Error.')

root = CTk()
root.geometry('685x480')
set_appearance_mode('dark')
root.title('Info Grabber GUI V1.6')
root.resizable(False,False)
lb = CTkLabel(root, text='Info Grabber', text_color='purple', font=('arial', 16, 'bold'))
lb.pack()

frame = CTkFrame(root, width=685)

txtbx = CTkTextbox(root, width=560, height=360, corner_radius=50, border_color='purple', fg_color='black', border_width=5)
txtbx.place(x=20 , y=90)
def options1(choice):
    if choice == 'light':
        set_appearance_mode('light')
    elif choice == 'dark':
        set_appearance_mode('dark')
    elif choice == 'system':
        set_appearance_mode('system')

def scan():
    url = er.get()

    if ' ' in url:
        url = url.replace(' ', '')

    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    clude = cloudscraper.create_scraper()
    try:
        qrl = clude.get(url)
        soup = bs(qrl.text, 'html.parser')
        txtbx.delete('1.0', 'end')

        title = txtbx.insert('end', f'Title : {soup.title.text}\n')
        status = txtbx.insert('end', f'status : {qrl.status_code}\n')
        server = txtbx.insert('end', f'server : {qrl.headers.get("Server", "not found")}\n')
        srsd = txtbx.insert('end', f'server speed : {qrl.elapsed.total_seconds()}\n')
        ltue = txtbx.insert('end', f'latest update : {qrl.headers.get('Last-Modified', 'not found')}\n')
        ft = txtbx.insert('end', f'file type : {qrl.headers.get('Content-Type', '[yellow]not found')}\n')
        if not url.endswith('/'):
              url = url + '/robots.txt'
              qrl2 = clude.get(url)
              if qrl2.status_code > 299:
                    txtbx.insert('end', 'robots.txt : False\n')
              if qrl2.status_code < 300:
                    txtbx.insert('end', 'robots.txt : True\n')
        elif url.endswith('/'):
              url = url + 'robots.txt'
              qrl2 = clude.get(url)
              if qrl2.status_code > 299:
                    txtbx.insert('end','robots.txt : False\n')
              if qrl2.status_code < 300:
                    txtbx.insert('end', 'robots.txt : Ture\n')
        else:
              txtbx.insert('end','error')
        url = url.replace('http://', '').replace('https://', '')
        url = url.split('/')[0]
        IP = txtbx.insert('end', f'IP : {socket.gethostbyname(url)} (The IP  might belong to the server, not website itself)')
    #t7t al ttwer
    except Exception:
         txtbx.insert('end', 'error')

def abt(choice2):
     if choice2 == 'about tool':
          new = CTkToplevel(root)
          new.geometry('300x180')
          new.resizable(False, False)
          new.title('about tool')
          new.attributes('-topmost', True) 
          abtnew = CTkTextbox(new, width=300, height=180, fg_color='black', bg_color='purple',border_color='purple', border_width=4)
          abtnew.place(x=1, y=1)
          abtnew.insert('end', 'A lightweight OSINT and Web Scraping utility featuring a modern Graphical User Interface (GUI). This tool is designed to safely bypass security challenges like Cloudflare to extract and analyze essential website infrastructure data, including server details, response latency, robots.txt status, and active server IP resolution.')
     elif choice2 == 'about doveloper':
          new2 = CTkToplevel(root)
          new2.geometry('270x150')
          new2.resizable(False, False)
          new2.title('about doveloper')
          new2.attributes('-topmost', True) 
          abtnew2 = CTkTextbox(new2, width=270, height=150, fg_color='black',border_color='purple', border_width=4)
          abtnew2.place(x=1, y=1)
          abtnew2.insert('end', '\t    developer users:\n\nuser tiktok : @amynex..dev\nuser instagram : @amynex.dev\nuser github : amynex987-cmyk\nuser discord : amynex_56023\nuser telegram : EJ_SP')

def HELP():
     HelP = CTkToplevel(root)
     HelP.geometry('300x300')
     HelP.resizable(False, False)
     HelP.title('info grabber, help')
     HelP.attributes('-topmost', True)
     helpH = CTkTextbox(HelP, width=300, height=300, border_color='purple', border_width=4)
     helpH.place(x=1, y=1)
     helpH.insert('end', 'Input: Inside the application window, click the search bar labeled "Enter URL :" and type the website address (e.g., google.com). The script automatically fixes spaces and adds http:// if missing.\n\nRun: Click the Scan button. The tool will bypass security layers like Cloudflare, scrape the site, and display technical infrastructure details inside the main black text box.\n\nWhat Every UI Element and Button Does:\n\nEnter URL : Bar: The input field where you type the target website address\nScan Button: Triggers the scraper to gather and print the following data:\nTitle: The HTML title tag of the webpage\nStatus: The HTTP status code (e.g., 200 for OK, 404 for Not Found)\nServer: The software operating the web server (e.g., Nginx, Apache, Cloudflare)\nServer Speed: The response latency time in seconds\nLatest Update: The Last-Modified header showing when the page was last updated.\nFile Type: The format of the content (e.g., text/html)\nRobots.txt: Displays True if a robots.txt file exists on the target, or False if it does not.\nIP: Resolves and displays the hosting server\'s direct  IP address')
er = CTkEntry(root, width=560, height=30, corner_radius=20, border_color='purple', border_width=4, placeholder_text='Enter URL :', placeholder_text_color='purple', fg_color='black')
er.place(x=20, y=45)

op = CTkOptionMenu(root,values=['dark', 'light', 'system'], width=50, height=18, fg_color='black', text_color='purple', button_color='purple', command=(options1), corner_radius=10, dropdown_fg_color='black', dropdown_text_color='purple', dropdown_font=('arial', 14, 'bold') , button_hover_color='gray')
op.place(x=10, y=10)

op2 = CTkOptionMenu(root, values=['about tool', 'about doveloper'], command=abt, width=45 , height=18, fg_color='black', text_color='purple', button_color='purple', corner_radius=10)
op2.place(x=560,y=10)

ent = CTkButton(root, width=80, height=30, fg_color='black', border_color='purple', text='scan', text_color='purple', corner_radius=10, border_width=3, hover_color='gray', command=scan)
ent.place(x=588, y=45)

Help = CTkButton(root, width=80, height=30, fg_color='black', border_color='purple', text='help', text_color='purple', corner_radius=10, border_width=3, hover_color='gray', command=HELP)
Help.place(x=588, y=90)



root.mainloop()